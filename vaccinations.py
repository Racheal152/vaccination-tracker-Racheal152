from db_connection import get_db_connection

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
    print(f"Vaccination '{name}' added successfully!")

def get_all_vaccinations():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM vaccinations")
    vaccinations = cursor.fetchall()
    cursor.close()
    connection.close()
    return vaccinations

def get_vaccination_by_id(vaccination_id):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM vaccinations WHERE id = %s", (vaccination_id,))
    vaccination = cursor.fetchone()
    cursor.close()
    connection.close()
    return vaccination

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
    print(f"Vaccination '{vaccination_id}' updated successfully!")

def delete_vaccination(vaccination_id):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM vaccinations WHERE id = %s", (vaccination_id,))
    connection.commit()
    cursor.close()
    connection.close()
    print(f"Vaccination '{vaccination_id}' deleted successfully!")
