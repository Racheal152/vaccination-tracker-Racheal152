from db_connection import get_db_connection
import mysql.connector
import hashlib
import os
from auth import verify_password
from individuals import get_individuals_by_doctor
from vaccination_records import get_vaccination_records_by_doctor
from auth import (
    register_admin,
    register_doctor,
    register_individual,
    login_user,
)

from vaccination_records import (
    get_all_vaccination_records,
    get_vaccination_record_by_id,
    get_vaccination_records_by_individual,
    add_vaccination_record,
    update_vaccination_record,
    delete_vaccination_record,
)

from individuals import (
    get_all_individuals,
    get_individual_by_id,
    add_individual,
    update_individual,
    delete_individual,
)

from vaccinations import (
    get_all_vaccinations,
    get_vaccination_by_id,
    add_vaccination,
    update_vaccination,
    delete_vaccination,
)

from doctors import (
    get_all_doctors,
    get_doctor_by_id,
    add_doctor,
    update_doctor,
    delete_doctor,
)

from users import (
    get_all_users,
    get_user_by_id,
    get_user_by_email,
    add_user,
    update_user,
    delete_user,
)

from admin import (
    get_all_admins,
    get_admin_by_id,
    add_admin,
    update_admin,
    delete_admin,
)
def main():
    print("Welcome to the Vaccination System!")
    initial_menu()

def initial_menu():
    print("Welcome to the System!")
    print("1. Register")
    print("2. Log In")
    
    choice = input("Please select an option (1/2): ")
    
    if choice == '1':
        register_user()  # Proceed to registration
    elif choice == '2':
        login_user()  # Proceed to login
    else:
        print("Invalid choice. Please select 1 or 2.")
        initial_menu()

# ------------ Step 2: Register User (Role Selection) ------------

def register_user():
    print("Welcome to the registration page!")
    print("1. Register as Admin")
    print("2. Register as Doctor")
    print("3. Register as Individual")
    
    role_choice = input("Select a role (1/2/3): ")
    
    if role_choice == '1':
        register_admin()  # Register as Admin
    elif role_choice == '2':
        register_doctor()  # Register as Doctor
    elif role_choice == '3':
        register_individual()  # Register as Individual
    else:
        print("Invalid choice. Please try again.")
        register_user()

# ------------ Admin Registration ------------

def register_admin():
    print("Admin Registration")
    email = input("Enter email: ")
    password = input("Enter password: ")
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    phone_number = input("Enter phone number: ")

    # Insert the admin into the database (use your actual database function)
    add_admin(email, password, first_name, last_name, phone_number)
    print("Admin registered successfully!")
    login_user()

# ------------ Doctor Registration ------------

def register_doctor():
    print("Doctor Registration")
    email = input("Enter email: ")
    password = input("Enter password: ")
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    phone_number = input("Enter phone number: ")
    specialization = input("Enter specialization: ")
    license_number = input("Enter license number: ")

    # Insert the doctor into the database
    add_doctor(email, password, first_name, last_name, phone_number, specialization, license_number)
    print("Doctor registered successfully!")
    login_user()

# ------------ Individual Registration ------------

def register_individual():
    print("Individual Registration")
    email = input("Enter email: ")
    password = input("Enter password: ")
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    phone_number = input("Enter phone number: ")
    age = int(input("Enter age: "))
    gender = input("Enter gender (Male/Female/Other): ")
    address = input("Enter address: ")
    medical_conditions = input("Enter medical conditions (if any): ")
    allergies = input("Enter allergies (if any): ")

    # Insert the individual into the database
    add_individual(email, password, first_name, last_name, phone_number, age, gender, address, medical_conditions, allergies)
    print("Individual registered successfully!")
    login_user()

# ------------ Step 3: Login User ------------



def hash_password(password):
    """Hashes the password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()

def verify_password(stored_password_hash, entered_password):
    """Verifies that the entered password matches the stored password hash."""
    return stored_password_hash == hash_password(entered_password)

def login_user():
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    # Attempt to retrieve the user and their hashed password from the database
    connection = get_db_connection()  # Ensure this is your database connection method
    if not connection:
        print("Error connecting to the database.")
        return

    cursor = connection.cursor()

    # Query to find the user in any table (admin, doctor, individual)
    query = """
        SELECT 'admin', id, password FROM admin WHERE email = %s
        UNION
        SELECT 'doctor', id, password FROM doctors WHERE email = %s
        UNION
        SELECT 'individual', id, password FROM individuals WHERE email = %s
    """

    cursor.execute(query, (email, email, email))
    result = cursor.fetchone()

    if result:
        user_type, user_id, stored_password_hash = result
        if verify_password(stored_password_hash, password):
            print("Login successful!")
            # Call the respective menu based on the user type (admin, doctor, individual)
            if user_type == 'admin':
                admin_menu(user_id)  # Pass user ID to the admin menu
            elif user_type == 'doctor':
                doctor_menu(user_id)  # Pass user ID to the doctor menu
            elif user_type == 'individual':
                individual_menu(user_id)  # Pass user ID to the individual menu
        else:
            print("Invalid password. Please try again.")
            login_user()  # Recursive call to retry login on invalid password
    else:
        print("User not found. Please check your email and try again.")
        login_user()  # Recursive call to retry login if the user is not found

    cursor.close()
    connection.close()


# Admin Menu - Managing Vaccination Records, Users, Doctors, etc.
def admin_menu(user_id):
    while True:
        print("\nAdmin Menu")
        print("1. Manage Users")
        print("2. Manage Doctors")
        print("3. Manage Individuals")
        print("4. Manage Vaccination Records")
        print("5. Manage Vaccinations")
        print("6. Manage Admins")
        print("7. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            manage_users()
        elif choice == '2':
            manage_doctors()
        elif choice == '3':
            manage_individuals()
        elif choice == '4':
            manage_vaccination_records()
        elif choice == '5':
            manage_vaccinations()
        elif choice == '6':
            manage_admins()
        elif choice == '7':
            break
        else:
            print("Invalid choice. Please try again.")

# --- Users Management ---
def manage_users():
    while True:
        print("\nManage Users")
        print("1. View all users")
        print("2. Get user by ID")
        print("3. Add a new user")
        print("4. Update a user")
        print("5. Delete a user")
        print("6. Go back")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            users = get_all_users()
            for user in users:
                print(user)
        elif choice == '2':
            user_id = input("Enter user ID: ")
            user = get_user_by_id(user_id)
            print(user or f"User with ID {user_id} not found.")
        elif choice == '3':
            user_id = input("Enter user ID: ")
            username = input("Enter username: ")
            password = input("Enter password: ")
            role = input("Enter role: ")
            add_user(user_id, username, password, role)
            print("User added successfully.")
        elif choice == '4':
            user_id = input("Enter user ID to update: ")
            username = input("Enter updated username: ")
            password = input("Enter updated password: ")
            role = input("Enter updated role: ")
            update_user(user_id, username, password, role)
            print("User updated successfully.")
        elif choice == '5':
            user_id = input("Enter user ID to delete: ")
            delete_user(user_id)
            print("User deleted successfully.")
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

# --- Doctors Management ---
def manage_doctors():
    while True:
        print("\nManage Doctors")
        print("1. View all doctors")
        print("2. Get doctor by ID")
        print("3. Add a new doctor")
        print("4. Update a doctor")
        print("5. Delete a doctor")
        print("6. Go back")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            doctors = get_all_doctors()
            for doctor in doctors:
                print(doctor)
        elif choice == '2':
            doctor_id = input("Enter doctor ID: ")
            doctor = get_doctor_by_id(doctor_id)
            print(doctor or f"Doctor with ID {doctor_id} not found.")
        elif choice == '3':
            user_id = input("Enter user ID: ")
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            specialization = input("Enter specialization: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            license_number = input("Enter license number: ")
            password = input("Enter password: ")
            add_doctor(user_id, first_name, last_name, specialization, phone_number, email, license_number, password)
            print("Doctor added successfully.")
        elif choice == '4':
            doctor_id = input("Enter doctor ID to update: ")
            first_name = input("Enter updated first name: ")
            last_name = input("Enter updated last name: ")
            specialization = input("Enter updated specialization: ")
            phone_number = input("Enter updated phone number: ")
            email = input("Enter updated email: ")
            license_number = input("Enter updated license number: ")
            password = input("Enter updated password: ")
            update_doctor(doctor_id, first_name, last_name, specialization, phone_number, email, license_number, password)
            print("Doctor updated successfully.")
        elif choice == '5':
            doctor_id = input("Enter doctor ID to delete: ")
            delete_doctor(doctor_id)
            print("Doctor deleted successfully.")
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

# --- Individuals Management ---
def manage_individuals():
    while True:
        print("\nManage Individuals")
        print("1. View all individuals")
        print("2. Get individual by ID")
        print("3. Add a new individual")
        print("4. Update an individual")
        print("5. Delete an individual")
        print("6. Go back")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            individuals = get_all_individuals()
            for individual in individuals:
                print(individual)
        elif choice == '2':
            individual_id = input("Enter individual ID: ")
            individual = get_individual_by_id(individual_id)
            print(individual or f"Individual with ID {individual_id} not found.")
        elif choice == '3':
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            age = input("Enter age: ")
            gender = input("Enter gender (Male/Female/Other): ")
            email = input("Enter email: ")
            phone_number = input("Enter phone number: ")
            address = input("Enter address: ")
            medical_conditions = input("Enter medical conditions: ")
            allergies = input("Enter allergies: ")
            user_id = input("Enter user ID: ")
            password = input("Enter password: ")
            add_individual(first_name, last_name, age, gender, email, phone_number, address, medical_conditions, allergies, user_id, password)
            print("Individual added successfully.")
        elif choice == '4':
            individual_id = input("Enter individual ID to update: ")
            first_name = input("Enter updated first name: ")
            last_name = input("Enter updated last name: ")
            age = input("Enter updated age: ")
            gender = input("Enter updated gender: ")
            email = input("Enter updated email: ")
            phone_number = input("Enter updated phone number: ")
            address = input("Enter updated address: ")
            medical_conditions = input("Enter updated medical conditions: ")
            allergies = input("Enter updated allergies: ")
            password = input("Enter updated password: ")
            update_individual(individual_id, first_name, last_name, age, gender, email, phone_number, address, medical_conditions, allergies, password)
            print("Individual updated successfully.")
        elif choice == '5':
            individual_id = input("Enter individual ID to delete: ")
            delete_individual(individual_id)
            print("Individual deleted successfully.")
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

# --- Vaccination Records Management ---
def manage_vaccination_records():
    while True:
        print("\nManage Vaccination Records")
        print("1. View all vaccination records")
        print("2. Get vaccination record by ID")
        print("3. Add a new vaccination record")
        print("4. Update a vaccination record")
        print("5. Delete a vaccination record")
        print("6. Get vaccinations by individual")
        print("7. Go back")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            records = get_all_vaccination_records()
            for record in records:
                print(record)
        elif choice == '2':
            record_id = input("Enter vaccination record ID: ")
            record = get_vaccination_record_by_id(record_id)
            print(record or f"Vaccination record with ID {record_id} not found.")
        elif choice == '3':
            individual_id = input("Enter individual ID: ")
            vaccination_id = input("Enter vaccination ID: ")
            date_administered = input("Enter date administered: ")
            add_vaccination_record(individual_id, vaccination_id, date_administered)
            print("Vaccination record added successfully.")
        elif choice == '4':
            record_id = input("Enter vaccination record ID to update: ")
            individual_id = input("Enter updated individual ID: ")
            vaccination_id = input("Enter updated vaccination ID: ")
            date_administered = input("Enter updated date administered: ")
            update_vaccination_record(record_id, individual_id, vaccination_id, date_administered)
            print("Vaccination record updated successfully.")
        elif choice == '5':
            record_id = input("Enter vaccination record ID to delete: ")
            delete_vaccination_record(record_id)
            print("Vaccination record deleted successfully.")
        elif choice == '6':  # New option to get vaccinations by individual
            individual_id = input("Enter individual ID: ")
            vaccinations = get_vaccinations_by_individual(individual_id)
            if vaccinations:
                for vaccination in vaccinations:
                    print(vaccination)
        elif choice == '7':
            break
        else:
            print("Invalid choice. Please try again.")

# --- Vaccinations Management ---
def manage_vaccinations():
    while True:
        print("\nManage Vaccinations")
        print("1. View all vaccinations")
        print("2. Get vaccination by ID")
        print("3. Add a new vaccination")
        print("4. Update a vaccination")
        print("5. Delete a vaccination")
        print("6. Go back")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            vaccinations = get_all_vaccinations()
            for vaccination in vaccinations:
                print(vaccination)
        elif choice == '2':
            vaccination_id = input("Enter vaccination ID: ")
            vaccination = get_vaccination_by_id(vaccination_id)
            print(vaccination or f"Vaccination with ID {vaccination_id} not found.")
        elif choice == '3':
            name = input("Enter vaccination name: ")
            manufacturer = input("Enter manufacturer: ")
            add_vaccination(name, manufacturer)
            print("Vaccination added successfully.")
        elif choice == '4':
            vaccination_id = input("Enter vaccination ID to update: ")
            name = input("Enter updated vaccination name: ")
            manufacturer = input("Enter updated manufacturer: ")
            update_vaccination(vaccination_id, name, manufacturer)
            print("Vaccination updated successfully.")
        elif choice == '5':
            vaccination_id = input("Enter vaccination ID to delete: ")
            delete_vaccination(vaccination_id)
            print("Vaccination deleted successfully.")
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

# --- Admins Management ---
def manage_admins():
    while True:
        print("\nManage Admins")
        print("1. View all admins")
        print("2. Get admin by ID")
        print("3. Add a new admin")
        print("4. Update an admin")
        print("5. Delete an admin")
        print("6. Go back")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            admins = get_all_admins()
            for admin in admins:
                print(admin)
        elif choice == '2':
            admin_id = input("Enter admin ID: ")
            admin = get_admin_by_id(admin_id)
            print(admin or f"Admin with ID {admin_id} not found.")
        elif choice == '3':
            admin_id = input("Enter admin ID: ")
            username = input("Enter username: ")
            password = input("Enter password: ")
            add_admin(admin_id, username, password)
            print("Admin added successfully.")
        elif choice == '4':
            admin_id = input("Enter admin ID to update: ")
            username = input("Enter updated username: ")
            password = input("Enter updated password: ")
            update_admin(admin_id, username, password)
            print("Admin updated successfully.")
        elif choice == '5':
            admin_id = input("Enter admin ID to delete: ")
            delete_admin(admin_id)
            print("Admin deleted successfully.")
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

# ------------ Doctor Menu ------------
def doctor_menu(doctors_id):
    while True:
        print("\nWelcome Doctor!")
        print("1. View and update your profile")
        print("2. View and update patient profiles")
        print("3. View and update vaccination records")
        print("4. Log out")
    
        choice = input("\nPlease select an option: ")
    
        if choice == '1':
            doctor_profile_menu(doctors_id)  # View and update doctor’s profile
        elif choice == '2':
            patient_profile_menu(doctors_id)  # View and update patients’ profiles
        elif choice == '3':
            vaccination_records_menu(doctors_id)  # View and update vaccination records
        elif choice == '4':
            print("\nLogging out...")
            break  # Return to the initial menu
        else:
            print("\nInvalid option. Please try again.")
            

# ------------ View and Update Doctor Profile ------------
def doctor_profile_menu(doctors_id):
    doctor = get_doctor_by_id(doctors_id)  # Fetch doctor data from the DB
    
    print(f"Your Profile: {doctor['first_name']} {doctor['last_name']}")
    print(f"Email: {doctor['email']}")
    print(f"Specialization: {doctor['specialization']}")
    print(f"Phone: {doctor['phone_number']}")
    
    update_choice = input("Would you like to update your profile? (yes/no): ")
    
    if update_choice.lower() == 'yes':
        update_doctor_profile(doctors_id)  # Proceed to update the doctor's profile
    else:
        doctor_menu(doctors_id)

# ------------ Update Doctor Profile ------------
def update_doctor_profile(doctors_id):
    first_name = input("Enter new first name: ")
    last_name = input("Enter new last name: ")
    phone_number = input("Enter new phone number: ")
    specialization = input("Enter new specialization: ")

    update_doctor(doctors_id, first_name, last_name, phone_number, specialization)
    print("Your profile has been updated successfully!")
    doctor_menu(doctors_id)

# ------------ View and Update Patient Profiles ------------
def patient_profile_menu(doctors_id):
    while True:
        print("\nFetching patients...")
        individuals = get_individuals_by_doctor(doctors_id)
        if not individuals:
            print("\nNo patients found.")
            return  # Return to `doctor_menu`

        print("\nPatients assigned to you:")
        for idx, individual in enumerate(individuals, start=1):
            print(f"{idx}. {individual['first_name']} {individual['last_name']} (ID: {individual['id']})")
        print("0. Return to Doctor Menu")

        try:
            choice = int(input("\nSelect a patient to view or update (Enter number): "))
            if choice == 0:
                return  # Go back to `doctor_menu`
            elif 1 <= choice <= len(individuals):
                selected_id = individuals[choice - 1]['id']
                print(f"\nSelected Patient ID: {selected_id}")
                update_patient_profile(selected_id)  # Call the update function for the selected patient
            else:
                print("\nInvalid choice. Please try again.")
        except ValueError:
            print("\nInvalid input. Please enter a number.")


def update_patient_profile(individual_id):
    patient = get_individual_by_id(individual_id)  # Fetch patient data from the database
    
    print(f"Patient Profile: {patient['first_name']} {patient['last_name']}")
    print(f"Email: {patient['email']}")
    print(f"Phone: {patient['phone_number']}")
    print(f"Age: {patient['age']}")
    
    update_choice = input("Would you like to update this patient's profile? (yes/no): ")
    
    if update_choice.lower() == 'yes':
        first_name = input("Enter new first name: ")
        last_name = input("Enter new last name: ")
        phone_number = input("Enter new phone number: ")
        age = input("Enter new age: ")

        update_individual(individual_id, first_name, last_name, phone_number, age)
        print("Patient's profile has been updated.")
    else:
        doctor_menu(individual_id)

# ------------ View and Update Vaccination Records ------------
def vaccination_records_menu(doctors_id):
    print("1. View your patients' vaccination records")
    print("2. Update vaccination records")
    choice = input("Please select an option: ")
    
    if choice == '1':
        view_vaccination_records(doctors_id)
    elif choice == '2':
        update_vaccination_record_menu(doctors_id)
    else:
        print("Invalid option. Please try again.")
        vaccination_records_menu(doctors_id)

def view_vaccination_records(doctors_id):
    vaccination_records = get_vaccination_records_by_doctor(doctors_id)
    
    if vaccination_records:
        for record in vaccination_records:
            print(f"Patient: {record['patient_name']} | Vaccine: {record['vaccine_name']} | Date: {record['date_given']}")
    else:
        print("No vaccination records found.")
    
    doctor_menu(doctors_id)

def update_vaccination_record_menu(doctors_id):
    vaccination_records = get_vaccination_records_by_doctor(doctors_id)
    
    if vaccination_records:
        for idx, record in enumerate(vaccination_records, start=1):
            print(f"{idx}. Patient: {record['patient_name']} | Vaccine: {record['vaccine_name']} | Date: {record['date_given']}")
        
        record_choice = int(input("Select a vaccination record to update (Enter number): "))
        
        if 1 <= record_choice <= len(vaccination_records):
            record_id = vaccination_records[record_choice - 1]['id']
            update_vaccination_record_for_patient(record_id)  # Update selected record
        else:
            print("Invalid choice. Please try again.")
            update_vaccination_record_menu(doctors_id)
    else:
        print("No vaccination records found.")
        doctor_menu(doctors_id)

def update_vaccination_record_for_patient(record_id):
    record = get_vaccination_record_by_id(record_id)
    
    print(f"Vaccination Record: Vaccine: {record['vaccine_name']} | Date: {record['date_given']}")
    
    update_choice = input("Would you like to update this vaccination record? (yes/no): ")
    
    if update_choice.lower() == 'yes':
        vaccine_name = input("Enter new vaccine name: ")
        date = input("Enter new date (YYYY-MM-DD): ")

        update_vaccination_record(record_id, vaccine_name, date)
        print("Vaccination record updated successfully!")
    else:
        doctor_menu(record['individual_id'])

# ------------ Helper Functions ------------

from individuals import get_individuals_by_doctor  # Import the function from individuals.py

def get_individuals_by_doctor(doctors_id):
    """
    Fetch and display individuals (patients) assigned to a specific doctor.
    """
    from individuals import get_individuals_by_doctor as fetch_individuals

    try:
        # Fetch individuals from the database
        individuals = fetch_individuals(doctors_id)
        
        if not individuals:
            print("No patients found for the specified doctor.")
            return []

        # Display fetched patients
        print("Patients assigned to you:")
        for individual in individuals:
            print(
                f"ID: {individual['id']}, Name: {individual['first_name']} {individual['last_name']}, "
                f"Email: {individual['email']}, Phone: {individual['phone_number']}, Age: {individual['age']}"
            )
        return individuals

    except ConnectionError as ce:
        print(f"Database error: {ce}")
        return []

    except Exception as e:
        print(f"An error occurred: {e}")
        return []


def individual_menu(user_id):
    while True:  # Use a while loop to keep the menu running until a valid option is selected
        print("Welcome to the Vaccination Tracking System Patient!")
        print("1. View your profile")
        print("2. Update your profile")
        print("3. View your vaccination record")
        print("4. Log out")
        
        choice = input("Please select an option: ")
        
        if choice == '1':
            get_individual_by_id(user_id)  # View individual’s profile
            
        elif choice == '2':
            update_individual(user_id)  # Update individual’s profile
           
        elif choice == '3':
            get_vaccination_records_by_individual(user_id)  # View individual’s vaccination record
            
        elif choice == '4':
            print("Logging out...")
            initial_menu()  # Return to the initial menu
            
        else:
            print("Invalid option. Please try again.")  # Invalid option, loop again

def get_individual_by_id(user_id):
    try:
        connection = get_db_connection()  # Get DB connection
        cursor = connection.cursor(dictionary=True)

        query = "SELECT first_name, last_name, email, phone_number, age FROM individuals WHERE id = %s"
        cursor.execute(query, (user_id,))
        individual = cursor.fetchone()  # Fetch one user by their ID

        if individual:
            print(f"Profile for {individual['first_name']} {individual['last_name']}:")
            print(f"Email: {individual['email']}")
            print(f"Phone: {individual['phone_number']}")
            print(f"Age: {individual['age']}")
        else:
            print("No profile found for this user.")
        
        cursor.close()
        connection.close()
    
    except Exception as e:
        print(f"An error occurred while fetching your profile: {e}")

def update_individual(user_id):
    try:
        # Prompt for updated details
        new_email = input("Enter new email (or press Enter to keep the same): ")
        new_phone = input("Enter new phone number (or press Enter to keep the same): ")
        new_age = input("Enter new age (or press Enter to keep the same): ")

        # Update query (you can make it dynamic by including only fields that are changed)
        update_query = """
            UPDATE individuals SET
            email = COALESCE(NULLIF(%s, ''), email),
            phone_number = COALESCE(NULLIF(%s, ''), phone_number),
            age = COALESCE(NULLIF(%s, ''), age)
            WHERE id = %s
        """

        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute(update_query, (new_email, new_phone, new_age, user_id))
        connection.commit()

        print("Profile updated successfully!")

        cursor.close()
        connection.close()

    except Exception as e:
        print(f"An error occurred while updating your profile: {e}")

def get_vaccination_records_by_individual(user_id):
    try:
        # Establish a connection to the database
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)

        # Query to fetch vaccine name, date given, and other relevant details
        query = """
            SELECT v.name AS vaccine_name, vr.date_given, vr.status, vr.administered_by, vr.location, 
                   vr.next_dose_due, vr.side_effects_reported
            FROM vaccination_records vr
            JOIN vaccinations v ON vr.vaccination_id = v.id  # Joining vaccination_records with vaccinations table
            WHERE vr.individual_id = %s
        """
        
        cursor.execute(query, (user_id,))
        vaccination_records = cursor.fetchall()

        if vaccination_records:
            print("Vaccination Records:")
            for record in vaccination_records:
                print(f"Vaccine: {record['vaccine_name']}")
                print(f"Date Given: {record['date_given']}")
                print(f"Status: {record['status']}")
                print(f"Administered By: {record['administered_by']}")
                print(f"Location: {record['location']}")
                print(f"Next Dose Due: {record['next_dose_due']}")
                print(f"Side Effects Reported: {record['side_effects_reported']}\n")
        else:
            print("No vaccination records found.")

        cursor.close()
        connection.close()

    except Exception as e:
        print(f"An error occurred while fetching vaccination records: {e}")


if __name__ == "__main__":
    main()
