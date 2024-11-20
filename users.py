from db_connection import get_db_connection

def add_user(name, email):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("""
        INSERT INTO users (name, email)
        VALUES (%s, %s)
    """, (name, email))
    connection.commit()
    cursor.close()
    connection.close()
    print(f"User '{name}' added successfully!")

def get_all_users():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    cursor.close()
    connection.close()
    return users

def get_user_by_id(user_id):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
    user = cursor.fetchone()
    cursor.close()
    connection.close()
    return user

def get_user_by_email(email):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
    user = cursor.fetchone()
    cursor.close()
    connection.close()
    return user

def update_user(user_id, name, email):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("""
        UPDATE users
        SET name = %s, email = %s
        WHERE id = %s
    """, (name, email, user_id))
    connection.commit()
    cursor.close()
    connection.close()
    print(f"User '{user_id}' updated successfully!")

def delete_user(user_id):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
    connection.commit()
    cursor.close()
    connection.close()
    print(f"User '{user_id}' deleted successfully!")
