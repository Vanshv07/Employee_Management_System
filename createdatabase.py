"""This program connects to MySQL and creates a database schema."""
try:
    import pymysql as sql
    conn=sql.connect(host="localhost",user="root",password="1234",port=3306)
    smt=conn.cursor()
    smt.execute("create schema company")
    print("Database created...")
    conn.close()
except sql.err.ProgrammingError as err:
    print(err)
