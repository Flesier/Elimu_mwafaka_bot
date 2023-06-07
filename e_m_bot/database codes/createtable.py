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


# Create a new table
table_name = "students"
create_table_query = """
CREATE TABLE {} (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255),
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    adm VARCHAR(255),
    parent VARCHAR(255),
    parent_id INT,
    parent_phone VARCHAR(255),
    paid ENUM('Yes', 'No'),
    last_point INT,
    password VARCHAR(255),
    current_school VARCHAR(255),
    location VARCHAR(255),
    progress INT,
    classe ENUM('1', '2', '3', '4')
)
""".format(table_name)

cursor.execute(create_table_query)

# Close the cursor and connection
cursor.close()
connection.close()

print("Database and table created successfully.")
