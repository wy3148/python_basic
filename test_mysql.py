import os
import MySQLdb 

"""
run 'pip install MySQLdb'
"""

user = os.getenv("mysql_user")
pwd = os.getenv("mysql_pwd")
sql_url = "sandbox-mysql.arch.fonality.com"
database = "nf_central"

cnx = MySQLdb.connect(sql_url,user,pwd,database)
cursor = cnx.cursor()

query = "SELECT username FROM user WHERE customer_id=1"

cursor.execute(query)
res = cursor.fetchall()

for row in res:
    print row[0]

cursor.close()
cnx.close()









