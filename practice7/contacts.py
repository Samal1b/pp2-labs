CREATE_TABLE_CONTACTS = """CREATE TABLE IF NOT EXISTS contacts (
id SERIAL PRIMARY KEY, 
name VARCHAR(50),
phone VARCHAR(11)
);"""

SELECT_CONTACTS = """SELECT * FROM contacts;"""

INSERT_CONTACTS = """INSERT INTO contacts (name, phone) VALUES
(%s, %s)"""

DELETE_CONTACT = """DELETE FROM contacts 
WHERE phone = %s"""

UPDATE_CONTACT = """UPDATE contacts
SET phone = %s
WHERE name = %s"""

SELECT_CONTACT_BY_NAME = """SELECT * FROM contacts
WHERE name = %s """

def create_table_contacts(conn):
    with conn.cursor() as cur:
        cur.execute(CREATE_TABLE_CONTACTS)
    conn.commit()

def read_contacts(conn):
    with conn.cursor() as cur:
        cur.execute(SELECT_CONTACTS)
        result = cur.fetchall()
        return result

def insert_contacts(conn, contacts):
    with conn.cursor() as cur:
        for contact in contacts:
            name, phone = contact
            cur.execute(INSERT_CONTACTS, (name, phone))
    conn.commit()

def delete_contact(conn, number):
    with conn.cursor() as cur:        
        cur.execute(DELETE_CONTACT, (number,))
    conn.commit()

def update_contact(conn, name, new_phone):
    with conn.cursor() as cur:
        cur.execute(UPDATE_CONTACT, (new_phone, name))
    conn.commit()

def select_contact_by_name(conn, name):
    with conn.cursor() as cur:
        cur.execute(SELECT_CONTACT_BY_NAME, (name,))
        result = cur.fetchall()
        return result
