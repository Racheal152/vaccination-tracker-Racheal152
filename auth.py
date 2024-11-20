import hashlib
import os
import mysql.connector
from mysql.connector import Error

# MySQL Database Connection Setup
def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',  # replace with your host
            user='root',       # replace with your username
            password='password', # replace with your password
            database='telemedicine_db'  # replace with your actual database name
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error: {e}")
        return None

# Function to hash the password before saving
def hash_password(password):
    salt = os.urandom(16)  # Generate a salt
    hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    return salt + hashed_password  # Return salt + hash

# Function to verify password
def verify_password(stored_password_hash, password):
    if isinstance(stored_password_hash, str):  # If it's a string, decode it to bytes
        stored_password_hash = stored_password_hash.encode()
    salt = stored_password_hash[:16]  # Extract the salt from the stored hash
    stored_hash = stored_password_hash[16:]  # Extract the actual stored hash
    new_hash = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)  # Hash the entered password with the same salt
    return stored_hash == new_hash  # Compare hashes

# Register a new admin
def register_admin(first_name, last_name, email, phone_number, password):
    connection = get_db_connection()  # Corrected function name
    if not connection:
        return "Database connection failed."
    
    cursor = connection.cursor()
    hashed_password = hash_password(password)
    
    query = """INSERT INTO admin (first_name, last_name, email, phone_number, password) 
               VALUES (%s, %s, %s, %s, %s)"""
    cursor.execute(query, (first_name, last_name, email, phone_number, hashed_password))
    
    connection.commit()
    user_id = cursor.lastrowid  # Get the generated user_id
    cursor.close()
    connection.close()

    return user_id

# Register a new doctor
def register_doctor(first_name, last_name, specialization, phone_number, email, license_number, password):
    connection = get_db_connection()  # Corrected function name
    if not connection:
        return "Database connection failed."
    
    cursor = connection.cursor()
    hashed_password = hash_password(password)
    
    query = """INSERT INTO doctors (first_name, last_name, specialization, phone_number, email, license_number, password) 
               VALUES (%s, %s, %s, %s, %s, %s, %s)"""
    cursor.execute(query, (first_name, last_name, specialization, phone_number, email, license_number, hashed_password))
    
    connection.commit()
    user_id = cursor.lastrowid  # Get the generated user_id
    cursor.close()
    connection.close()

    return user_id

# Register a new individual
def register_individual(first_name, last_name, age, gender, email, phone_number, address, medical_conditions, allergies, password):
    connection = get_db_connection()  # Corrected function name
    if not connection:
        return "Database connection failed."
    
    cursor = connection.cursor()
    hashed_password = hash_password(password)
    
    query = """INSERT INTO individuals (first_name, last_name, age, gender, email, phone_number, address, medical_conditions, allergies, password) 
               VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    cursor.execute(query, (first_name, last_name, age, gender, email, phone_number, address, medical_conditions, allergies, hashed_password))
    
    connection.commit()
    user_id = cursor.lastrowid  # Get the generated user_id
    cursor.close()
    connection.close()

    return user_id

# Login a user (verify password)
def login_user(email, password):
    connection = get_db_connection()  # Corrected function name
    if not connection:
        return "Database connection failed."

    cursor = connection.cursor()
    
    # Check if user exists in the admin table
    cursor.execute("SELECT password FROM admin WHERE email = %s", (email,))
    result = cursor.fetchone()
    if result:
        stored_password_hash = result[0]
    else:
        # Check if user exists in the doctors table
        cursor.execute("SELECT password FROM doctors WHERE email = %s", (email,))
        result = cursor.fetchone()
        if result:
            stored_password_hash = result[0]
        else:
            # Check if user exists in the individuals table
            cursor.execute("SELECT password FROM individuals WHERE email = %s", (email,))
            result = cursor.fetchone()
            if result:
                stored_password_hash = result[0]
            else:
                return "User does not exist."
    
    # Verify the password
    if verify_password(stored_password_hash, password):
        return "Login successful."
    else:
        return "Invalid password."

