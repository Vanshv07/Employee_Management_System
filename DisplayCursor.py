"""Program to displaycursor in MySQL database"""
import pymysql as sql
try:
    conn=sql.connect(host="localhost",user="root",password="1234",port=3306,database="company",cursorclass=sql.cursors.DictCursor)
    smt=conn.cursor()
    smt.execute("select * from employees")
    rows=smt.fetchall()
    for row in rows:
        print(row['employeeid'],row['employeename'],row['dob'],row['gender'],row['city'],row['salary'],row['department'])

    conn.close()
except sql.err.OperationalError as err:
    print(err)