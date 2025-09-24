import pymysql

def create_connection():
    conn = pymysql.connect(
        host = "localhost",
        user = "student_user",
        password="password123",
        database="student_db",
        ssl_disabled = True
    )
    return conn

conn = create_connection()
print("Connection Successful")
conn.close()