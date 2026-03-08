import pymysql as sql
try:
    conn=sql.connect(host="localhost",user="root",password="1234",port=3306,database="company",cursorclass=sql.cursors.DictCursor)
    smt=conn.cursor()
    pat=input("Enter Patten:")
    q=f"select * from employees where employeename like '%{pat}%'"
    print(q)
    smt.execute(q)
    rows=smt.fetchall()
    if(len(rows)>0):
        for row in rows:
            print(row['employeeid'],row['employeename'],row['dob'],row['gender'])
    else:
        print("Record not found...")  
except sql.err.OperationalError as err:
    print(err)