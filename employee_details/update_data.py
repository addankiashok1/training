from db_connect import *

def update_data(conn):
    cur = conn.cursor()
    query = "UPDATE employee SET salary=%s where id=%s"
    try:
        print("Trying to update an emp data")
        cur.execute(query,('200000',2))
        conn.commit()
        print("Record got updated")
        conn.close()

    except (Exception, Error) as error:
        print(error)

if __name__=='__main__':
    update_data(db_connection())
