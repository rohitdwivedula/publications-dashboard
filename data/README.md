This directory contains:

1. `scrape_data.py` - Python3 script to scrape Google Scholar profiles of researchers whose email is a particular domain, and store it in a MongoDB Atlas instance.
2. `download_json_from_mongo.py` - download JSON dump of the MongoDB database populated in Step 1.
3. `json_to_csv.py`  and `json_to_sql.py` are used to convert the data from JSON format to CSV/SQL respectively. 
4. `raw_data` contains the raw JSON file created after Step 1, and the SQL database dump created after Step 3.
5. `sql_database_setup.sql` is the SQL database definition of the database - this script needs to be run before running `json_to_sql.py`.