from db_connect import *

def delate_data(conn):
    cur = conn.cursor()
    query = "DELETE FROM employee where id = %s"
   
    try:
        print("Trying to delete a record")
        data = cur.execute(query,'2')
        conn.commit()
        print("Record got deleted")
        conn.close()

    except (Exception, Error) as error:
        print(error)

if __name__ =='__main__':
    delate_data(db_connection())
