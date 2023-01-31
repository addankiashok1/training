from db_connect import *

def insert_data(conn):
    cur = conn.cursor()
    query = '''
        INSERT INTO employee(id, first_name, last_name, email, gender, salary) 
        VALUES (%s,%s,%s,%s,%s,%s);
        '''
    try:
        print("Trying to insert emp data into the table")
        emp_data = [(1,'Ashok','A','ashokaddanki@outlook.com','Male','25000'),
                    (2, 'Naveen','B','naveen@gmail.com','Male','45000'),
                    (3, 'Subbu', 'S','subbu@hotmail.com','Male','75000')]
        for record in emp_data:
            cur.execute(query,record)
        print("record records inserted")
        conn.commit()
        conn.close()
    except (Exception,Error) as error:
        print(error)

if __name__=='__main__':
    insert_data(db_connection())
