"""Program to Insertrecord in MySQL database"""
import pymysql as sql
try:
    conn=sql.connect(host="localhost",user="root",password="1234",port=3306,database="company")
    smt=conn.cursor()
    while True:
        eid=input("Enter Employee Id:")
        en=input("Enter Employee Name:")
        es=input("Enter Employee Salary:")
        ec=input("Enter Employee City:")
        ed=input("Enter Employee DOB:")
        eg=input("Enter Employee Gender:")
        ede=input("Enter Employee Department:")
        q="insert into employees values({0},'{1}',{2},'{3}','{4}','{5}','{6}')".format(eid,en,es,ec,ed,eg,ede)
        print(q)
        smt.execute(q)
        conn.commit()
        print("Employee Submitted Successfully...")
        ch=input("Add More Record:(yes/no)?")
        if(ch=='n' or ch=='N'):
            break

    conn.close()

except sql.err.ProgrammingError as err:
    print(err)
except sql.err.IntegrityError as err:
    print(err)    
