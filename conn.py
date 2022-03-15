#setting up a database connection
import pymysql

mypass = ''
database_name = ''

con = pymysql.connect(host='localhost', user='root', password=mypass, database=database_name)
cur = con.cursor()


