import mysql.connector

# MySQL Connector configuration
db_config = {
    "host": "localhost",
    "user": "root",
    "password": ""
}

# Establish a MySQL connection
connection = mysql.connector.connect(**db_config)
cursor = connection.cursor()

# Create a new database
database_name = "elimumwafaka"
cursor.execute("CREATE DATABASE {}".format(database_name))

# Close the cursor and connection
cursor.close()
connection.close()

print("Database created successfully.")