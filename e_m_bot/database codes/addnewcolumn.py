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

# Alter table to add a new column
alter_table_query = """
    ALTER TABLE students
    ADD COLUMN classe INT
"""

cursor.execute(alter_table_query)

# Commit the changes
connection.commit()

# Close the cursor and connection
cursor.close()
connection.close()

print("New column added successfully.")
