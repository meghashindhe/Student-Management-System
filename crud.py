import pandas as pd
from datab import create_connection
import pymysql
from pymysql.err import IntegrityError


def add_student(student_id, name, email, dob, phone):
    conn = create_connection()
    cursor = conn.cursor()

    dob_str = dob.strftime("%Y-%m-%d")

    query = "INSERT INTO students (student_id, name, email, dob, phone) values (%s, %s, %s, %s, %s)"
    values = (student_id, name, email, dob_str, phone)

    try:
        cursor.execute(query, values)
        conn.commit()
        return True
        print('Student added successfully')
    except IntegrityError:
        return False
    finally:
        cursor.close()
        conn.close()



def delete_student(student_id):
    conn = create_connection()
    cursor = conn.cursor()
    query = "DELETE FROM students WHERE student_id = %s"
    cursor.execute(query, (student_id,))
    conn.commit()
    rows_deleted = cursor.rowcount
    cursor.close()
    conn.close()
    print('Student deleted successfully')
    return rows_deleted


def update_student(student_id, name, email, dob, phone):
    conn = create_connection()
    cursor = conn.cursor()

    dob_str = dob.strftime("%Y-%m-%d")

    query = """
        UPDATE students 
        SET name=%s, email=%s, dob=%s, phone=%s
        WHERE student_id=%s
    """

    values = (name, email, dob, phone, student_id)
    cursor.execute(query, values)
    conn.commit()
    rows_updated = cursor.rowcount
    cursor.close()
    conn.close()
    return rows_updated
    print('Student updated successfully')

def get_students():
    conn = create_connection()
    query = 'SELECT * FROM students'
    df = pd.read_sql(query, conn)
    conn.close()
    df['dob'] = pd.to_datetime(df['dob']).dt.strftime('%d-%m-%y')
    return df