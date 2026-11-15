
CREATE OR REPLACE PROCEDURE upsert_contact(
    p_name VARCHAR,
    p_phone VARCHAR
)
LANGUAGE plpgsql
AS $$
BEGIN
    IF EXISTS (
        SELECT 1 FROM contacts WHERE name = p_name
    ) THEN
        UPDATE contacts
        SET phone = p_phone
        WHERE name = p_name;
    ELSE
        INSERT INTO contacts(name, phone)
        VALUES(p_name, p_phone);
    END IF;
END;
$$;


CREATE OR REPLACE PROCEDURE insert_many_contacts(
    p_names VARCHAR[],
    p_phones VARCHAR[],
    INOUT p_invalid TEXT
)
LANGUAGE plpgsql
AS $$
DECLARE
    i INT;
BEGIN
    p_invalid := '';

    IF array_length(p_names, 1) IS NULL THEN
        p_invalid := 'Empty list';
        RETURN;
    END IF;

    FOR i IN 1..array_length(p_names, 1)
    LOOP
        IF p_phones[i] ~ '^[0-9]{11}$' THEN

            IF EXISTS (
                SELECT 1 FROM contacts
                WHERE name = p_names[i]
            ) THEN
                UPDATE contacts
                SET phone = p_phones[i]
                WHERE name = p_names[i];
            ELSE
                INSERT INTO contacts(name, phone)
                VALUES(p_names[i], p_phones[i]);
            END IF;

        ELSE
            p_invalid := p_invalid ||
                'Name: ' || COALESCE(p_names[i], 'Unknown') ||
                ', Phone: ' || COALESCE(p_phones[i], 'NULL') ||
                E'\n';
        END IF;
    END LOOP;

    IF p_invalid = '' THEN
        p_invalid := 'All phone numbers are correct';
    END IF;
END;
$$;


CREATE OR REPLACE PROCEDURE delete_contact(
    p_name VARCHAR DEFAULT NULL,
    p_phone VARCHAR DEFAULT NULL
)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM contacts
    WHERE (p_name IS NOT NULL AND name = p_name)
       OR (p_phone IS NOT NULL AND phone = p_phone);
END;
$$;


CREATE OR REPLACE PROCEDURE add_phone(
    p_contact_name VARCHAR,
    p_phone VARCHAR,
    p_type VARCHAR
)
LANGUAGE plpgsql
AS $$
DECLARE
    v_contact_id INT;
BEGIN
    SELECT id INTO v_contact_id
    FROM contacts
    WHERE name = p_contact_name
    LIMIT 1;

    IF v_contact_id IS NULL THEN
        RAISE EXCEPTION 'Contact not found';
    END IF;

    INSERT INTO phones(contact_id, phone, type)
    VALUES(v_contact_id, p_phone, p_type);
END;
$$;


CREATE OR REPLACE PROCEDURE move_to_group(
    p_contact_name VARCHAR,
    p_group_name VARCHAR
)
LANGUAGE plpgsql
AS $$
DECLARE
    v_group_id INT;
BEGIN
    INSERT INTO groups(name)
    VALUES(p_group_name)
    ON CONFLICT(name) DO NOTHING;

    SELECT id INTO v_group_id
    FROM groups
    WHERE name = p_group_name;

    UPDATE contacts
    SET group_id = v_group_id
    WHERE name = p_contact_name;

    IF NOT FOUND THEN
        RAISE EXCEPTION 'Contact not found';
    END IF;
END;
$$;


DROP FUNCTION IF EXISTS search_contacts(VARCHAR);

CREATE OR REPLACE FUNCTION search_contacts(p_query TEXT)
RETURNS TABLE(
    contact_id INT,
    name VARCHAR,
    email VARCHAR,
    birthday DATE,
    group_name VARCHAR,
    phone VARCHAR,
    phone_type VARCHAR
)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT
        c.id,
        c.name,
        c.email,
        c.birthday,
        g.name,
        p.phone,
        p.type
    FROM contacts c
    LEFT JOIN groups g ON c.group_id = g.id
    LEFT JOIN phones p ON c.id = p.contact_id
    WHERE
        c.name ILIKE '%' || p_query || '%'
        OR c.email ILIKE '%' || p_query || '%'
        OR p.phone ILIKE '%' || p_query || '%'
    ORDER BY c.name;
END;
$$;




CREATE OR REPLACE FUNCTION get_contacts(
    p_limit INT,
    p_offset INT
)
RETURNS TABLE(
    id INT,
    name VARCHAR,
    phone VARCHAR
)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT
        c.id,
        c.name,
        COALESCE(STRING_AGG(p.phone, ', ' ORDER BY p.id), '')::VARCHAR
    FROM contacts c
    LEFT JOIN phones p ON c.id = p.contact_id
    GROUP BY c.id, c.name
    ORDER BY c.id
    LIMIT p_limit
    OFFSET p_offset;
END;
$$;
