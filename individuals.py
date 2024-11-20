from db_connection import get_db_connection
import mysql.connector
import hashlib

# Define the hash_password function
def hash_password(password):
    # Hash the password using SHA-256
    return hashlib.sha256(password.encode('utf-8')).hexdigest()
def add_individual(email, password, first_name, last_name, phone_number, age, gender, address, medical_conditions, allergies):
    hashed_password = hash_password(password) 
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("""
        INSERT INTO individuals (email, password, first_name, last_name, phone_number, age, gender, address, medical_conditions, allergies)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (email, hashed_password, first_name, last_name, phone_number, age, gender, address, medical_conditions, allergies))
    connection.commit()
    cursor.close()
    connection.close()
    print(f"Individual '{first_name}' added successfully!")

def get_all_individuals():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM individuals")
    individuals = cursor.fetchall()
    cursor.close()
    connection.close()
    return individuals

def get_individual_by_id(individual_id):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM individuals WHERE id = %s", (individual_id,))
    individual = cursor.fetchone()
    cursor.close()
    connection.close()
    return individual

def get_individuals_by_doctor(doctors_id):
    # First, establish the database connection
    connection = get_db_connection()

    # The query to fetch individuals assigned to the specified doctor
    query = """
        SELECT i.id, i.first_name, i.last_name, i.email, i.phone_number, i.age
        FROM individuals i
        JOIN users u ON i.user_id = u.id
        JOIN doctors d ON u.id = d.user_id
        WHERE d.id = %s
    """
    
    try:
        # Use a dictionary cursor for easier handling of results
        cursor = connection.cursor(dictionary=True)
        
        # Execute the query, passing in the doctor's ID
        cursor.execute(query, (doctors_id,))
        
        # Fetch all the records that match the query
        individuals = cursor.fetchall()
        
    except mysql.connector.Error as err:
        # Handle any errors that occur during query execution
        print(f"Error: {err}")
        individuals = None
    
    finally:
        # Close the cursor and connection after the operation is complete
        cursor.close()
        connection.close()
    
    return individuals

def update_individual(individual_id, name, age, address):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("""
        UPDATE individuals
        SET name = %s, age = %s, address = %s
        WHERE id = %s
    """, (name, age, address, individual_id))
    connection.commit()
    cursor.close()
    connection.close()
    print(f"Individual '{individual_id}' updated successfully!")

def delete_individual(individual_id):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM individuals WHERE id = %s", (individual_id,))
    connection.commit()
    cursor.close()
    connection.close()
    print(f"Individual '{individual_id}' deleted successfully!")

