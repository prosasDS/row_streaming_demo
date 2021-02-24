# row_streaming_demo


Hello Marcin, Ezequiel & team. 

After our talk this morning I investigated a bit about the TRAN operators and decided to make this project to apply them and also take this chance to show you what could I come up with for a data pipeline using the Stream functionality from Requests. 

Task: Company B needs a data pipeline that takes data from company A's database (for which I made a mock API that outputs random data) and after applying some simple transformations on some columns, save it to company B's database. 

Database prep: I created company B's database with psql Shell beforhand (database_prerp.sql has a transcript of what I did in the shell). 

Solution: A flask app (ingest.py) that draws data row by row from the mock API (so mock_api.py needs to be running for it to work) and saves the transformed rows to the previously created  database and table. 

To test it you must create the database and table in your server using the code from database_prep.sql, run mock_api.py and then ingest.py. 100 rows of transformed data should be added to the table. 
