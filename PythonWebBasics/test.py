import psycopg2

connection = psycopg2.connect(
    host='localhost',
    database='demo_db',
    user='postgres',
    password='1123QwER'

)
connection.close()
 