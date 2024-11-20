from db_connection import get_db_connection

import hashlib

# Define the hash_password function
def hash_password(password):
    # Hash the password using SHA-256
    return hashlib.sha256(password.encode('utf-8')).hexdigest()
def add_admin(email, password, first_name, last_name, phone_number):
    hashed_password = hash_password(password)  # Hash the password
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("""
        INSERT INTO admin (email, password, first_name, last_name, phone_number)
        VALUES (%s, %s, %s, %s, %s)
    """, (email, hashed_password, first_name, last_name, phone_number))
    connection.commit()
    cursor.close()
    connection.close()
    print(f"Admin '{first_name}' added successfully!")

def get_all_admins():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM admins")
    admins = cursor.fetchall()
    cursor.close()
    connection.close()
    return admins

def get_admin_by_id(admin_id):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM admins WHERE id = %s", (admin_id,))
    admin = cursor.fetchone()
    cursor.close()
    connection.close()
    return admin

def update_admin(admin_id, username, password, email):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("""
        UPDATE admins
        SET username = %s, password = %s, email = %s
        WHERE id = %s
    """, (username, password, email, admin_id))
    connection.commit()
    cursor.close()
    connection.close()
    print(f"Admin '{admin_id}' updated successfully!")

def delete_admin(admin_id):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM admins WHERE id = %s", (admin_id,))
    connection.commit()
    cursor.close()
    connection.close()
    print(f"Admin '{admin_id}' deleted successfully!")
