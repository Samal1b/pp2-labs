from config import make_connection
from contacts import (
    create_table_contacts,
    read_contacts,
    insert_contacts,
    delete_contact,
    update_contact,
    select_contact_by_name
)
from utils import get_contacts_from_csv


options = {
    "0": "Exit",
    "1": "Insert contact",
    "2": "Insert contacts",
    "3": "Read contacts",
    "4": "Delete contacts",
    "5": "Update contact by name",
    "6": "Select contact by name",
    "7": "Insert contacts from csv"
}

def process_input(user_input, conn):

    if options[user_input] == "Exit":
        raise Exception("Stop execution")
    elif options[user_input] == "Read contacts":
        print("All contacts:")
        for contact in read_contacts(conn):
            print(f"{contact}")
    elif options[user_input] == "Insert contact":
        contact_info = tuple(input().split(" "))
        insert_contacts(conn, [contact_info])
        name, phone = contact_info
        print(f"Inserted contact: {name} - {phone}")
    elif options[user_input] == "Insert contacts":
            print("How many records?")
            contacts_number = int(input("Number of contacts: "))

            contacts = []

            for _ in range(contacts_number):
                contact_info = tuple(input().split(" "))
                
                contacts.append(contact_info)
                
            insert_contacts(conn, contacts)

            for contact in contacts:
                name, phone = contact
                print(f"Inserted contact: {name} - {phone}")
    elif options[user_input] == "Delete contacts":
        number = input("Number = ")
        try:
            delete_contact(conn, number)
            print(f"Deleted contact with number: {number}")
        except Exception as e:
            print(e)
    elif options[user_input] == "Update contact by name":
        name = input("Name = ").strip()
        new_phone = input("New phone number = ").strip()
        try:
            update_contact(conn, name, new_phone)
            print(f"Contact with name {name} was updated")
            print(f"New phone number = {new_phone}")
        except Exception as e:
            print(e)
    elif options[user_input] == "Select contact by name":
        name = input("name=").strip()
        print(select_contact_by_name(conn, name))
    elif options[user_input] == "Insert contacts from csv":
        path = input("path=").strip()
        insert_contacts(
            conn,
            get_contacts_from_csv(path)
        )
        print("Contacts from csv file were inserted")

def main():
    with make_connection() as conn:
        create_table_contacts(conn)

        while True:
            for key, value in options.items():
                print(f"{key}. {value}")

            user_input = input()

            try:
                process_input(user_input, conn)
            except Exception as e:
                print(e)
                break

if __name__ == "__main__":
    main()