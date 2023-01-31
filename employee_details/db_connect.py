import psycopg2
from psycopg2 import Error
from readconfig import read_db_params

def db_connection():
    try:
        params = read_db_params()
        # Connect to Database
        # Read the database details from the config object
        conn = psycopg2.connect(
            user = params.get('DB','username'),
            password = params.get('DB','password'),
            host = params.get('DB','host'),
            port = params.get('DB','port'),
            database = params.get('DB', 'database')
        )
        return conn
    except (Exception, Error) as error:
        print(error)

def print_db_version(connection):
    cur = connection.cursor()
    try:
        cur.execute("SELECT version();")
        record = cur.fetchone()
        print("Postgresql version is:", record)
    except (Exception, Error) as error:
        print(error)
    
    finally:
        if connection is not None:
            cur.close()
            connection.close()
            print("Database connection closed")
# con = db_connection()
# print_db_version(con)
if __name__=='__main__':
    db_connection()