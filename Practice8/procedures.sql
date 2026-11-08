
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

