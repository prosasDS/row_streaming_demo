import requests
import psycopg2 
import numpy as np

with requests.get("http://127.0.0.1:5000/data_request/100", stream = True) as r:

    conn = psycopg2.connect(dbname='company_b_db',
                            user='postgres',
                            password='equinomuteki')

    cur = conn.cursor()
    sql = "INSERT INTO company_a_data (class_target, ordinal_var, amount) VALUES (%s, %s, %s)"

    buffer = ""
    ordinal_var = 0

    for chunk in r.iter_content(chunk_size = 1):
        if chunk.endswith(b'\n'):
            t = eval(buffer)
            
            #some transformation examples

            if t[1] == 'Large':
                ordinal_var = 3
            elif t[1] == 'Medium':
                ordinal_var = 2
            else:
                ordinal_var = 1

            log_amount = np.log(t[2])

            cur.execute(sql, (t[0], ordinal_var, log_amount))
            conn.commit()
            buffer = ""

        else:
            buffer += chunk.decode()