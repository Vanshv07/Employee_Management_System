"""Display employee record by id from MySQL database"""
import pymysql as sql
try:
    conn=sql.connect(host="localhost",user="root",password="1234",port=3306,database="company",cursorclass=sql.cursors.DictCursor)
    smt=conn.cursor()
    emp_id=input("Enter Employee ID u want to Display ?")
    smt.execute(f"select * from employees where employeeid={emp_id}")
    row=smt.fetchone()
    if row:
        print(row['employeeid'],row['employeename'],row['salary'],row['city'],row['dob'],row['gender'],row['department'])
    else:
        print("Record not Fonund")
    conn.close()
except sql.err.OperationalError as err:
    print(err)
    