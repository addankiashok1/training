from db_connect import *

def creat_table(conn):
    # Creating tabale in database
    print("Inside create_table")
    cur = conn.cursor()
    query = """CREATE TABLE employee (id INT NOT NULL, first_name VARCHAR(255),
    last_name VARCHAR(100), email VARCHAR(150),
    gender VARCHAR(50), salary VARCHAR(100), PRIMARY KEY (id))"""
    try:
        cur.execute(query)
        print("Query executed and table got created")
        conn.commit()
        conn.close()
    except (Exception, Error) as error:
        print(error)
    finally:
        if conn is not None:
            cur.close()
            conn.close()
            print("DB Connection is closed")
            
if __name__=='__main__':
    creat_table(db_connection())


