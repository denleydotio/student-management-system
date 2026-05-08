import mysql.connector
import config

def get_server_connection():
    return mysql.connector.connect(
        host = config.DB_HOST,
        user = config.DB_USER,
        password = config.DB_PASSWORD
    )

def get_database_connection():
    return mysql.connector.connect(
        host = config.DB_HOST,
        user = config.DB_USER,
        password = config.DB_PASSWORD,
        database = config.DB_NAME
    )

def setup_database():
    server_conn = get_server_connection()
    server_cursor = server_conn.cursor()

    server_cursor.execute("create database if not exists students_system")
    server_conn.commit()

    server_cursor.close()
    server_conn.close()

    db_conn = get_database_connection()
    db_cursor = db_conn.cursor()

    table_blueprint = """
        create table if not exists students(
            student_id int auto_increment primary key,
            reg_no varchar(15) unique,
            name varchar(50),
            age int
        )
    """

    db_cursor.execute(table_blueprint)
    db_conn.commit()

    db_cursor.close()
    db_conn.close()

    print("Database live!")

def add_student_to_database(reg_no, name, age):
    conn = get_database_connection()
    cursor = conn.cursor()

    query = "insert into students (reg_no, name, age) values(%s, %s, %s)"
    try:
        cursor.execute(query, (reg_no, name,age))
        conn.commit()
        return True
    except mysql.connector.errors.IntegrityError:
        return False
    finally:
        cursor.close()
        conn.close()

def display_all_students():
    conn = get_database_connection()
    cursor = conn.cursor()

    cursor.execute("select * from students")
    results = cursor.fetchall()

    cursor.close()
    conn.close()

    return results

def search_students(reg_no):
    conn = get_database_connection()
    cursor = conn.cursor()

    query = "select * from students where reg_no = %s"
    cursor.execute(query, (reg_no,))
    results = cursor.fetchall()

    cursor.close()
    conn.close()

    return results

def delete_student_record(reg_no):
    conn = get_database_connection()
    cursor = conn.cursor()

    query = "delete from students where reg_no = %s"
    cursor.execute(query, (reg_no,))
    conn.commit()

    cursor.close()
    conn.close()

def update_student_reg(reg_no_new, reg_no_old):
    conn = get_database_connection()
    cursor = conn.cursor()

    query = "update students set reg_no = %s where reg_no = %s"
    cursor.execute(query, (reg_no_new, reg_no_old))
    conn.commit()

    rows_changed = cursor.rowcount

    cursor.close()
    conn.close()

    return rows_changed > 0

def update_student_name(name, reg_no_old):
    conn = get_database_connection()
    cursor = conn.cursor()

    query = "update students set name = %s where reg_no = %s"
    cursor.execute(query, (name, reg_no_old))
    conn.commit()

    rows_changed = cursor.rowcount

    cursor.close()
    conn.close()

    return rows_changed > 0

def update_student_age(age, reg_no_old):
    conn = get_database_connection()
    cursor = conn.cursor()

    query = "update students set age = %s where reg_no = %s"
    cursor.execute(query, (age, reg_no_old))
    conn.commit()

    rows_changed = cursor.rowcount

    cursor.close()
    conn.close()

    return rows_changed > 0
