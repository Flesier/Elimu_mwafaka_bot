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
table_name = "Topics"
create_table_query = """
CREATE TABLE {} (
    id INT AUTO_INCREMENT PRIMARY KEY,
    form INT,
    topic_name VARCHAR(255)
)
""".format(table_name)

cursor.execute(create_table_query)

# Close the cursor and connection
cursor.close()
connection.close()

print("Database and table created successfully.")
