"""This program to find employee by city name."""
import pymysql as sql
try:
    conn=sql.connect(host="localhost",user="root",password="1234",port=3306,database="company",cursorclass=sql.cursors.DictCursor)
    smt=conn.cursor()
    pat=input("Enter Cities:")
    pat = ","+pat.replace(",",",")+","
    
    q=f"select * from employees where city in ({pat})'"
    print(q)
    smt.execute(q)
    rows=smt.fetchall()
    if(len(rows)>0):
  
        for row in rows:
            print(row['employeeid'],row['employeename'],row['dob'],row['gender'])
    else:
        print("Record not found...")  
    conn.close()
except sql.err.OperationalError as err:
    print(err) 