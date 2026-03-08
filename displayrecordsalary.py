import pymysql as sql
try:
 conn=sql.connect(host="localhost",user="root",password="1234",port=3306,database="lic",cursorclass=sql.cursors.DictCursor)
 smt=conn.cursor()
 min=input("enter Minimum Salary:")
 max=input("Enter Maximum Salary:")
 q=f"select * from employee where salary between {min} and {max}"
 print(q)
 smt.execute(q)
 rows=smt.fetchall()
 for row in rows:
   print(row['employeeid'],row['employeename'],row['dob'],row['gender'])
 conn.close()
except sql.err.OperationalError as err:
  print(err)