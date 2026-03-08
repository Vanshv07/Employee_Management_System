"""Program to create employees table in MySQL database"""
import pymysql as sql
try:
    conn=sql.connect(host="localhost",user="root",password="1234",port=3306,database="company")
    smt=conn.cursor()
    smt.execute("create table employees(employeeid int primary key,employeename varchar(30) not null,salary decimal(10,2),city varchar(30),dob date,gender varchar(30),department varchar(30))")
    print("Table create...")
    conn.close()
except sql.err.OperationalError as err:
    print(err)