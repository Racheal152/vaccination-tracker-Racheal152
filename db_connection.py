import mysql.connector

# Database connection
def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Mnbvcxzq@1",
            database="vaccination_tracker"
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Database connection failed: {err}")
        return None
