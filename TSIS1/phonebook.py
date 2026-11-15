
from connect import make_connection
import json
import csv


def main():
    conn = make_connection()
    cur = conn.cursor()

    with open("procedures.sql", "r") as file:
        cur.execute(file.read())

    conn.commit()

    while True:
        print("\n1. Search contacts")
        print("2. Add or update contact")
        print("3. Add many contacts")
        print("4. Show contacts")
        print("5. Delete contact")
        print("6. Add phone number")
        print("7. Move contact to group")
        print("8. Filter by group")
        print("9. Search by email")
        print("10. Sort contacts")
        print("11. Export contacts to JSON")
        print("12. Import contacts from JSON")
        print("13. Import contacts from CSV")
        print("0. Exit")

        choice = input("Choose: ")

        if choice == "1":
            pattern = input("Enter name, email or phone: ")

            cur.execute(
                "SELECT * FROM search_contacts(%s)",
                (pattern,)
            )

            print(cur.fetchall())

        elif choice == "2":
            name = input("Enter name: ")
            phone = input("Enter phone: ")

            cur.execute(
                "CALL upsert_contact(%s, %s)",
                (name, phone)
            )

            conn.commit()
            print("Contact saved")

        elif choice == "3":
            names = input("Enter names separated by comma: ").split(",")
            phones = input("Enter phones separated by comma: ").split(",")

            if len(names) != len(phones):
                print("Names and phones must have the same number")
                continue

            names = [name.strip() for name in names]
            phones = [phone.strip() for phone in phones]

            cur.execute(
                "CALL insert_many_contacts(%s, %s, %s)",
                (names, phones, None)
            )

            result = cur.fetchone()
            conn.commit()

            print("Incorrect data:")
            print(result[0])

        elif choice == "4":
            limit = int(input("How many contacts per page: "))

            if limit <= 0:
                print("Enter a positive number")
                continue

            page = 0

            while True:
                offset = page * limit

                cur.execute(
                    "SELECT * FROM get_contacts(%s, %s)",
                    (limit, offset)
                )

                contacts = cur.fetchall()

                if not contacts:
                    print("No more contacts")

                    if page > 0:
                        page -= 1

                    break

                print(f"\nPage {page + 1}")

                for contact in contacts:
                    print(contact)

                print("\nnext - next page")
                print("prev - previous page")
                print("quit - back to menu")

                command = input("Choose: ").lower()

                if command == "next":
                    cur.execute("SELECT COUNT(*) FROM contacts")
                    total = cur.fetchone()[0]

                    if (page + 1) * limit < total:
                        page += 1
                    else:
                        print("This is the last page")

                elif command == "prev":
                    if page > 0:
                        page -= 1
                    else:
                        print("This is the first page")

                elif command == "quit":
                    break

                else:
                    print("Invalid command")

        elif choice == "5":
            print("1. Delete by name")
            print("2. Delete by phone")

            delete_choice = input("Choose: ")

            if delete_choice == "1":
                name = input("Enter name: ")

                cur.execute(
                    "CALL delete_contact(%s, %s)",
                    (name, None)
                )

            elif delete_choice == "2":
                phone = input("Enter phone: ")

                cur.execute(
                    "CALL delete_contact(%s, %s)",
                    (None, phone)
                )

            else:
                print("Invalid choice")
                continue

            conn.commit()
            print("Delete completed")

        elif choice == "6":
            name = input("Enter contact name: ")
            phone = input("Enter phone number: ")
            phone_type = input("Enter type (home/work/mobile): ")

            cur.execute(
                "CALL add_phone(%s, %s, %s)",
                (name, phone, phone_type)
            )

            conn.commit()
            print("Phone added")

        elif choice == "7":
            name = input("Enter contact name: ")
            group = input("Enter group name: ")

            cur.execute(
                "CALL move_to_group(%s, %s)",
                (name, group)
            )

            conn.commit()
            print("Contact moved to group")

        elif choice == "8":
            group = input("Enter group name: ")

            cur.execute("""
                SELECT c.name, c.email, p.phone, p.type
                FROM contacts c
                LEFT JOIN groups g ON c.group_id = g.id
                LEFT JOIN phones p ON c.id = p.contact_id
                WHERE g.name ILIKE %s
                ORDER BY c.name
            """, (group,))

            for contact in cur.fetchall():
                print(contact)

        elif choice == "9":
            email = input("Enter email or part of email: ")

            cur.execute("""
                SELECT name, email
                FROM contacts
                WHERE email ILIKE %s
            """, ('%' + email + '%',))

            for contact in cur.fetchall():
                print(contact)

        elif choice == "10":
            print("1. Sort by name")
            print("2. Sort by birthday")
            print("3. Sort by date added")

            sort_choice = input("Choose: ")

            if sort_choice == "1":
                column = "name"
            elif sort_choice == "2":
                column = "birthday"
            elif sort_choice == "3":
                column = "date_added"
            else:
                print("Invalid choice")
                continue

            cur.execute(f"""
                SELECT name, email, birthday, date_added
                FROM contacts
                ORDER BY {column} NULLS LAST
            """)

            for contact in cur.fetchall():
                print(contact)

        elif choice == "11":
            cur.execute("""
                SELECT c.name, c.email, c.birthday, g.name,
                       p.phone, p.type
                FROM contacts c
                LEFT JOIN groups g ON c.group_id = g.id
                LEFT JOIN phones p ON c.id = p.contact_id
                ORDER BY c.name
            """)

            rows = cur.fetchall()
            contacts = []

            for row in rows:
                contacts.append({
                    "name": row[0],
                    "email": row[1],
                    "birthday": str(row[2]) if row[2] else None,
                    "group": row[3],
                    "phone": row[4],
                    "phone_type": row[5]
                })

            with open("contacts.json", "w") as file:
                json.dump(contacts, file, indent=4)

            print("Export completed")

        elif choice == "12":
            with open("contacts.json", "r") as file:
                contacts = json.load(file)

            for contact in contacts:
                cur.execute(
                    "SELECT id FROM contacts WHERE name = %s",
                    (contact["name"],)
                )

                existing = cur.fetchone()

                if existing:
                    action = input(
                        contact["name"] + " exists. skip or overwrite? "
                    ).lower()

                    if action == "skip":
                        continue

                    elif action == "overwrite":
                        contact_id = existing[0]

                        cur.execute("""
                            UPDATE contacts
                            SET email = %s, birthday = %s
                            WHERE id = %s
                        """, (
                            contact["email"],
                            contact["birthday"],
                            contact_id
                        ))

                        cur.execute(
                            "DELETE FROM phones WHERE contact_id = %s",
                            (contact_id,)
                        )

                    else:
                        continue

                else:
                    cur.execute("""
                        INSERT INTO contacts(name, email, birthday)
                        VALUES (%s, %s, %s)
                        RETURNING id
                    """, (
                        contact["name"],
                        contact["email"],
                        contact["birthday"]
                    ))

                    contact_id = cur.fetchone()[0]

                if contact["group"]:
                    cur.execute("""
                        INSERT INTO groups(name)
                        VALUES (%s)
                        ON CONFLICT (name) DO NOTHING
                    """, (contact["group"],))

                    cur.execute(
                        "SELECT id FROM groups WHERE name = %s",
                        (contact["group"],)
                    )

                    group_id = cur.fetchone()[0]

                    cur.execute("""
                        UPDATE contacts
                        SET group_id = %s
                        WHERE id = %s
                    """, (group_id, contact_id))

                if contact["phone"]:
                    cur.execute("""
                        INSERT INTO phones(contact_id, phone, type)
                        VALUES (%s, %s, %s)
                    """, (
                        contact_id,
                        contact["phone"],
                        contact["phone_type"]
                    ))

            conn.commit()
            print("Import completed")

        elif choice == "13":
            with open("contacts.csv", "r") as file:
                reader = csv.reader(file)

                for row in reader:
                    name = row[0].strip()
                    phone = row[1].strip()
                    phone_type = row[2].strip()
                    email = row[3].strip()
                    birthday = row[4].strip()
                    group = row[5].strip()

                    cur.execute("""
                        INSERT INTO contacts(name, phone, email, birthday)
                        VALUES (%s, %s, %s, %s)
                        RETURNING id
                    """, (name, phone, email, birthday))

                    contact_id = cur.fetchone()[0]

                    cur.execute("""
                        INSERT INTO phones(contact_id, phone, type)
                        VALUES (%s, %s, %s)
                    """, (contact_id, phone, phone_type))

                    if group:
                        cur.execute("""
                            INSERT INTO groups(name)
                            VALUES (%s)
                            ON CONFLICT (name) DO NOTHING
                        """, (group,))

                        cur.execute(
                            "SELECT id FROM groups WHERE name = %s",
                            (group,)
                        )

                        group_id = cur.fetchone()[0]

                        cur.execute("""
                            UPDATE contacts
                            SET group_id = %s
                            WHERE id = %s
                        """, (group_id, contact_id))

            conn.commit()
            print("CSV import completed")

        elif choice == "0":
            break

        else:
            print("Invalid choice")

    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
