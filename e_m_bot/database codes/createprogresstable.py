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
table_name = "maths_progress"
create_table_query = """
CREATE TABLE {} (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    column1 INT,
    column2 INT,
    column3 INT,
    column4 INT,
    column5 INT,
    column6 INT,column7 INT,column8 INT,column9 INT,column10 INT,column11 INT,column12 INT,
    column13 INT,column14 INT,column15 INT,column16 INT,column17 INT,column18 INT,column19 INT,column20 INT,column21 INT,column22 INT,column23 INT,column24 INT
    ,column25 INT,column26 INT,column27 INT ,column28 INT,column29 INT,column30 INT,column31 INT,column32 INT,column33 INT,column34 INT,column35 INT,column36 INT,
    column37 INT,column38 INT,column39 INT,column40 INT,column41 INT,column42 INT,column43 INT,column44 INT,column45 INT,column46 INT,column47 INT,column48 INT,column49 INT,column50 INT,column51 INT,column52 INT,
    column53 INT,column54 INT,column55 INT,column56 INT,column57 INT,column58 INT ,column59 INT, column60 INT,column61 INT,column62 INT,column63 INT,column64 INT,column65 INT,column66 INT,column67 INT,column68 INT,
    column69 INT,column70 INT,column71 INT,column72 INT,column73 INT,column74 INT,column75 INT,column76 INT,column77 INT,column78 INT,column79 INT,column80 INT,column81 INT,column82 INT,column83 INT,column84 INT,
    column85 INT,column86 INT,column87 INT
)
""".format(table_name)
#each column represents the id of topics
cursor.execute(create_table_query)

# Close the cursor and connection
cursor.close()
connection.close()

print("Database and table created successfully.")
