"""Program to displayallrecord  in MySQL database"""
import pymysql as sql
try:
    conn=sql.connect(host="localhost",user="root",password="1234",port=3306,database="company")
    smt=conn.cursor()
    smt.execute("select * from employees")
    rows=smt.fetchall()
#print(rows)
    print("Id\t\tName\t\tDob\t\t\tGender\t\tCity\t\tSalary")
    print("--------------------------------------------------------------------")
    for row in rows:
        for col in row:
            print(col,end="\t\t")
    print()

    conn.close()
except sql.err.OperationalError as err:
    print(err)
except sql.err.InterfaceError as err:
    print(err)  