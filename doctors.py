from db_connection import get_db_connection

import hashlib

# Define the hash_password function
def hash_password(password):
    # Hash the password using SHA-256
    return hashlib.sha256(password.encode('utf-8')).hexdigest()
def add_doctor(email, password, first_name, last_name, phone_number, specialization, license_number):
    hashed_password = hash_password(password) 
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("""
        INSERT INTO doctors (email, password, first_name, last_name, phone_number, specialization, license_number)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (email, hashed_password, first_name, last_name, phone_number, specialization, license_number))
    connection.commit()
    cursor.close()
    connection.close()
    print(f"Doctor '{first_name}' added successfully!")

def get_all_doctors():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM doctors")
    doctors = cursor.fetchall()
    cursor.close()
    connection.close()
    return doctors

def get_doctor_by_id(doctor_id):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM doctors WHERE id = %s", (doctor_id,))
    doctor = cursor.fetchone()
    cursor.close()
    connection.close()
    return doctor

def update_doctor(doctor_id, last_name, first_name, specialization, email):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("""
        UPDATE doctors
        SET first_name = %s, last_name = %s, specialization = %s, email = %s
        WHERE id = %s
    """, (first_name, last_name, specialization, email, doctor_id))
    connection.commit()
    cursor.close()
    connection.close()
    print(f"Doctor '{doctor_id}' updated successfully!")

def delete_doctor(doctor_id):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM doctors WHERE id = %s", (doctor_id,))
    connection.commit()
    cursor.close()
    connection.close()
    print(f"Doctor '{doctor_id}' deleted successfully!")
