from db_connection import get_db_connection

def add_vaccination_record(individual_id, vaccination_id, doctor_id, date_administered):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("""
        INSERT INTO vaccination_records (individual_id, vaccination_id, date_administered)
        VALUES (%s, %s, %s)
    """, (individual_id, vaccination_id, date_administered))
    connection.commit()
    cursor.close()
    connection.close()
    print("Vaccination record added successfully!")

def get_all_vaccination_records():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("""
        SELECT vr.id, i.first_name AS individual_first_name, i.last_name AS individual_last_name, 
               v.name AS vaccination, vr.date_given, vr.status, vr.administered_by, 
               vr.location, vr.next_dose_due, vr.side_effects_reported
        FROM vaccination_records vr
        JOIN individuals i ON vr.individual_id = i.id
        JOIN vaccinations v ON vr.vaccination_id = v.id
    """)
    records = cursor.fetchall()
    cursor.close()
    connection.close()
    return records

def get_vaccination_record_by_id(record_id):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("""
        SELECT vr.id, i.first_name AS individual_first_name, i.last_name AS individual_last_name, 
               v.name AS vaccination, vr.date_given, vr.status, vr.administered_by, 
               vr.location, vr.next_dose_due, vr.side_effects_reported
        FROM vaccination_records vr
        JOIN individuals i ON vr.individual_id = i.id
        JOIN vaccinations v ON vr.vaccination_id = v.id
        WHERE vr.id = %s
    """, (record_id,))
    record = cursor.fetchone()
    cursor.close()
    connection.close()
    return record

def get_vaccination_records_by_individual(individual_id):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("""
        SELECT vr.id, v.name AS vaccination, vr.date_given, vr.status, vr.administered_by, 
               vr.location, vr.next_dose_due, vr.side_effects_reported
        FROM vaccination_records vr
        JOIN vaccinations v ON vr.vaccination_id = v.id
        WHERE vr.individual_id = %s
    """, (individual_id,))
    records = cursor.fetchall()
    cursor.close()
    connection.close()
    return records

def get_vaccination_records_by_doctor(doctors_id):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    
    query = """
        SELECT vr.id, i.first_name AS patient_name, v.name AS vaccine_name, vr.date_given, 
               vr.status, vr.administered_by, vr.location, vr.next_dose_due, 
               vr.side_effects_reported
        FROM vaccination_records vr
        JOIN individuals i ON vr.individual_id = i.id
        JOIN vaccinations v ON vr.vaccination_id = v.id
        JOIN users u ON i.user_id = u.id
        JOIN doctors d ON u.id = d.user_id
        WHERE d.id = %s
    """
    
    cursor.execute(query, (doctors_id,))  # Execute query
    records = cursor.fetchall()  # Fetch all records
    
    cursor.close()  # Close the cursor
    connection.close()  # Close the connection
    
    return records


def update_vaccination_record(record_id, individual_id, vaccination_id, date_given, status, administered_by, location, next_dose_due, side_effects_reported):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("""
        UPDATE vaccination_records
        SET individual_id = %s, vaccination_id = %s, date_given = %s, status = %s, 
            administered_by = %s, location = %s, next_dose_due = %s, side_effects_reported = %s
        WHERE id = %s
    """, (individual_id, vaccination_id, date_given, status, administered_by, location, next_dose_due, side_effects_reported, record_id))
    connection.commit()
    cursor.close()
    connection.close()
    print(f"Vaccination record '{record_id}' updated successfully!")

def delete_vaccination_record(record_id):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM vaccination_records WHERE id = %s", (record_id,))
    connection.commit()
    cursor.close()
    connection.close()
    print(f"Vaccination record '{record_id}' deleted successfully!")
