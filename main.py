import mysql.connector

# Establish a connection to MySQL database
def get_db_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Mnbvcxzq@1",
        database="vaccination_tracker" 
    )
    return connection


# ------------------------ Users Management -------------------------

# Add a new user (admin or patient)
def add_user(username, password, role):
    connection = get_db_connection()
    cursor = connection.cursor()
    
    cursor.execute("""
        INSERT INTO users (username, password, role)
        VALUES (%s, %s, %s)
    """, (username, password, role))
    
    connection.commit()
    cursor.close()
    connection.close()
    print(f"User {username} added successfully!")

# Get all users
def get_all_users():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    
    cursor.close()
    connection.close()
    return users

# Get a user by ID
def get_user_by_id(user_id):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    
    cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
    user = cursor.fetchone()
    
    cursor.close()
    connection.close()
    return user

# Update a user by ID
def update_user(user_id, username, password, role):
    connection = get_db_connection()
    cursor = connection.cursor()
    
    cursor.execute("""
        UPDATE users
        SET username = %s, password = %s, role = %s
        WHERE id = %s
    """, (username, password, role, user_id))
    
    connection.commit()
    cursor.close()
    connection.close()
    print(f"User {user_id} updated successfully!")

# Delete a user by ID
def delete_user(user_id):
    connection = get_db_connection()
    cursor = connection.cursor()
    
    cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
    
    connection.commit()
    cursor.close()
    connection.close()
    print(f"User {user_id} deleted successfully!")


# ------------------------ Individuals Management -------------------------

# Add a new individual (patient)
def add_individual(first_name, last_name, birth_date, gender, address):
    connection = get_db_connection()
    cursor = connection.cursor()
    
    cursor.execute("""
        INSERT INTO individuals (first_name, last_name, birth_date, gender, address)
        VALUES (%s, %s, %s, %s, %s)
    """, (first_name, last_name, birth_date, gender, address))
    
    connection.commit()
    cursor.close()
    connection.close()
    print(f"Individual {first_name} {last_name} added successfully!")

# Get all individuals
def get_all_individuals():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    
    cursor.execute("SELECT * FROM individuals")
    individuals = cursor.fetchall()
    
    cursor.close()
    connection.close()
    return individuals

# Get an individual by ID
def get_individual_by_id(individual_id):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    
    cursor.execute("SELECT * FROM individuals WHERE id = %s", (individual_id,))
    individual = cursor.fetchone()
    
    cursor.close()
    connection.close()
    return individual

# Update an individual by ID
def update_individual(individual_id, first_name, last_name, birth_date, gender, address):
    connection = get_db_connection()
    cursor = connection.cursor()
    
    cursor.execute("""
        UPDATE individuals
        SET first_name = %s, last_name = %s, birth_date = %s, gender = %s, address = %s
        WHERE id = %s
    """, (first_name, last_name, birth_date, gender, address, individual_id))
    
    connection.commit()
    cursor.close()
    connection.close()
    print(f"Individual {individual_id} updated successfully!")

# Delete an individual by ID
def delete_individual(individual_id):
    connection = get_db_connection()
    cursor = connection.cursor()
    
    cursor.execute("DELETE FROM individuals WHERE id = %s", (individual_id,))
    
    connection.commit()
    cursor.close()
    connection.close()
    print(f"Individual {individual_id} deleted successfully!")


# ------------------------ Doctors Management -------------------------

# Add a new doctor
def add_doctor(first_name, last_name, specialty, phone_number, email):
    connection = get_db_connection()
    cursor = connection.cursor()
    
    cursor.execute("""
        INSERT INTO doctors (first_name, last_name, specialty, phone_number, email)
        VALUES (%s, %s, %s, %s, %s)
    """, (first_name, last_name, specialty, phone_number, email))
    
    connection.commit()
    cursor.close()
    connection.close()
    print(f"Doctor {first_name} {last_name} added successfully!")

# Get all doctors
def get_all_doctors():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    
    cursor.execute("SELECT * FROM doctors")
    doctors = cursor.fetchall()
    
    cursor.close()
    connection.close()
    return doctors

# Get a doctor by ID
def get_doctor_by_id(doctor_id):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    
    cursor.execute("SELECT * FROM doctors WHERE id = %s", (doctor_id,))
    doctor = cursor.fetchone()
    
    cursor.close()
    connection.close()
    return doctor

# Update a doctor by ID
def update_doctor(doctor_id, first_name, last_name, specialty, phone_number, email):
    connection = get_db_connection()
    cursor = connection.cursor()
    
    cursor.execute("""
        UPDATE doctors
        SET first_name = %s, last_name = %s, specialty = %s, phone_number = %s, email = %s
        WHERE id = %s
    """, (first_name, last_name, specialty, phone_number, email, doctor_id))
    
    connection.commit()
    cursor.close()
    connection.close()
    print(f"Doctor {doctor_id} updated successfully!")

# Delete a doctor by ID
def delete_doctor(doctor_id):
    connection = get_db_connection()
    cursor = connection.cursor()
    
    cursor.execute("DELETE FROM doctors WHERE id = %s", (doctor_id,))
    
    connection.commit()
    cursor.close()
    connection.close()
    print(f"Doctor {doctor_id} deleted successfully!")

import mysql.connector

# Establish connection to MySQL database
def get_db_connection():
    connection = mysql.connector.connect(
        host="your_host",  # Replace with your database host
        user="your_username",  # Replace with your database username
        password="your_password",  # Replace with your database password
        database="your_database"  # Replace with your database name
    )
    return connection

# ------------------------ Vaccination Records Management -------------------------

# Add a new vaccination record
def add_vaccination_record(individual_id, vaccination_id, date_given, status, administered_by, location, next_dose_due, side_effects_reported):
    connection = get_db_connection()
    cursor = connection.cursor()
    
    cursor.execute("""
        INSERT INTO vaccination_records (individual_id, vaccination_id, date_given, status, administered_by, location, next_dose_due, side_effects_reported)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """, (individual_id, vaccination_id, date_given, status, administered_by, location, next_dose_due, side_effects_reported))
    
    connection.commit()
    cursor.close()
    connection.close()
    print("Vaccination record added successfully!")

# Get all vaccination records for an individual
def get_vaccination_records_by_individual(individual_id):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    
    cursor.execute("SELECT * FROM vaccination_records WHERE individual_id = %s", (individual_id,))
    records = cursor.fetchall()
    
    cursor.close()
    connection.close()
    return records

# Get a vaccination record by its ID
def get_vaccination_record_by_id(vaccination_id):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    
    cursor.execute("SELECT * FROM vaccination_records WHERE id = %s", (vaccination_id,))
    record = cursor.fetchone()
    
    cursor.close()
    connection.close()
    return record

# Update a vaccination record by ID
def update_vaccination_record(vaccination_id, status, administered_by, location, next_dose_due, side_effects_reported):
    connection = get_db_connection()
    cursor = connection.cursor()
    
    cursor.execute("""
        UPDATE vaccination_records
        SET status = %s, administered_by = %s, location = %s, next_dose_due = %s, side_effects_reported = %s
        WHERE id = %s
    """, (status, administered_by, location, next_dose_due, side_effects_reported, vaccination_id))
    
    connection.commit()
    cursor.close()
    connection.close()
    print(f"Vaccination record {vaccination_id} updated successfully!")

# Delete a vaccination record by ID
def delete_vaccination_record(vaccination_id):
    connection = get_db_connection()
    cursor = connection.cursor()
    
    cursor.execute("DELETE FROM vaccination_records WHERE id = %s", (vaccination_id,))
    
    connection.commit()
    cursor.close()
    connection.close()
    print(f"Vaccination record {vaccination_id} deleted successfully!")

# ------------------------ Vaccinations Table Management -------------------------

# Add a new vaccination record
def add_vaccination(name, manufacturer, required_doses):
    connection = get_db_connection()
    cursor = connection.cursor()
    
    cursor.execute("""
        INSERT INTO vaccinations (name, manufacturer, required_doses)
        VALUES (%s, %s, %s)
    """, (name, manufacturer, required_doses))
    
    connection.commit()
    cursor.close()
    connection.close()
    print(f"Vaccination {name} added successfully!")

# Get a vaccination by ID
def get_vaccination_by_id(vaccination_id):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    
    cursor.execute("SELECT * FROM vaccinations WHERE id = %s", (vaccination_id,))
    vaccination = cursor.fetchone()
    
    cursor.close()
    connection.close()
    return vaccination

# Get all vaccinations
def get_all_vaccinations():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    
    cursor.execute("SELECT * FROM vaccinations")
    vaccinations = cursor.fetchall()
    
    cursor.close()
    connection.close()
    return vaccinations

# Update a vaccination record by ID
def update_vaccination(vaccination_id, name, manufacturer, required_doses):
    connection = get_db_connection()
    cursor = connection.cursor()
    
    cursor.execute("""
        UPDATE vaccinations
        SET name = %s, manufacturer = %s, required_doses = %s
        WHERE id = %s
    """, (name, manufacturer, required_doses, vaccination_id))
    
    connection.commit()
    cursor.close()
    connection.close()
    print(f"Vaccination {vaccination_id} updated successfully!")

# Delete a vaccination record by ID
def delete_vaccination(vaccination_id):
    connection = get_db_connection()
    cursor = connection.cursor()
    
    cursor.execute("DELETE FROM vaccinations WHERE id = %s", (vaccination_id,))
    
    connection.commit()
    cursor.close()
    connection.close()
    print(f"Vaccination {vaccination_id} deleted successfully!")

# 1. Add a new admin
def create_admin():
    username = input("Enter username for admin: ")
    password = input("Enter password for admin: ")
    email = input("Enter email for admin: ")
    add_admin(username, password, email)

# 2. Get all admins
def view_all_admins():
    admins = get_all_admins()
    for admin in admins:
        print(f"ID: {admin['id']}, Username: {admin['username']}, Email: {admin['email']}")

def get_admin_by_id(admin_id):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    
    cursor.execute("SELECT * FROM doctors WHERE id = %s", (admin_id,))
    admin = cursor.fetchone()
    
    cursor.close()
    connection.close()
    return doctor


# 3. Update an admin
def update_existing_admin():
    admin_id = int(input("Enter the admin ID to update: "))
    username = input("Enter new username: ")
    password = input("Enter new password: ")
    email = input("Enter new email: ")
    update_admin(admin_id, username, password, email)

# 4. Delete an admin
def delete_existing_admin():
    admin_id = int(input("Enter the admin ID to delete: "))
    delete_admin(admin_id)
