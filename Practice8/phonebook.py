
from connect import make_connection


def main():
    conn = make_connection()
    cur = conn.cursor()

    with open("functions.sql", "r") as file:
        cur.execute(file.read())

    with open("procedures.sql", "r") as file:
        cur.execute(file.read())

    conn.commit()

    while True:
        print("\n1. Search contacts")
        print("2. Add or update contact")
        print("3. Add many contacts")
        print("4. Show contacts")
        print("5. Delete contact")
        print("0. Exit")

        choice = input("Choose: ")

        if choice == "1":
            pattern = input("Enter name or phone: ")
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
            limit = int(input("How many contacts: "))
            offset = int(input("How many contacts to skip: "))

            cur.execute(
                "SELECT * FROM get_contacts(%s, %s)",
                (limit, offset)
            )
            print(cur.fetchall())

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

            conn.commit()
            print("Delete completed")

        elif choice == "0":
            break

    cur.close()
    conn.close()


if __name__ == "__main__":
    main()


  
