from db_connect import *
import pandas as pd

def get_data(conn):
    cur = conn.cursor()
    query = "SELECT * FROM employee;"
    try:
        print("Trying to get emp data from the table")
        cur.execute(query)
        emp_data = cur.fetchall()
        data = pd.DataFrame(emp_data, columns=['EmpId','EmpFirstName','EmpLastName','EmpEmail','EmpGender','EmpSal'])
        print(data)
        # for record in emp_data:
        #     print(record)
    except (Exception, Error) as error:
        print(error)

        
if __name__=='__main__':
    get_data(db_connection())
