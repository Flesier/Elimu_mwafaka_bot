import mysql.connector

# MySQL Connector configuration
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "elimumwafaka"
}

# Establish a MySQL connection
connection = mysql.connector.connect(**db_config)
cursor = connection.cursor()

# Insert dummy data
insert_query = """
INSERT INTO students (username, first_name, last_name, adm, parent, parent_id, parent_phone, paid, last_point, password, current_school, location, progress, classe)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

dummy_data = [
    ("john", "John", "Simiyu", "john.sim@example.com", "Parent 1", 12345, "123-456-7890", "Yes", 80, "password1234", "Meru Boys High School", "Nakuru", 3, "3"),
    ("Wambui", "Jane", "wambu", "jane.wambu@example.com", "Parent 2", 67890, "987-654-3210", "No", 65, "password2234", "Pangani Girls high School", "Nakuru", 2, "2"),
    # Add more dummy data as needed
]

cursor.executemany(insert_query, dummy_data)
connection.commit()

# Close the cursor and connection
cursor.close()
connection.close()

print("Dummy data inserted successfully.")
