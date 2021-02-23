CREATE DATABASE company_b_db;

--\c company_b_db (I use the psql Shell)


CREATE TABLE company_a_data (id BIGSERIAL NOT NULL PRIMARY KEY,
                            class_target INT NOT NULL, 
                            ordinal_var VARCHAR(6) NOT NULL, 
                            amount MONEY NOT NULL);


--***I ran ingest.py twice***

SELECT * FROM company_a_data -- db updated with the 200 rows

--Some transaction operators I tested with the data:

BEGIN; 

DELETE  FROM company_a_data WHERE ID>100; 

--***at this point I ran ingest.py again to see if the open 
--transaction block allows it***

SELECT * FROM company_a_data -- 100 rows with new indexes added

ROLLBACK; --old rows restored and indexes remain the same 



BEGIN;
DELETE FROM company_a_data;
COMMIT; 

ROLLBACK; -- Doesn't work, as expected 