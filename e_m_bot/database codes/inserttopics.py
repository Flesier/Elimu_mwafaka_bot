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
INSERT INTO  topics(form,topic_name)
VALUES ( %s, %s)
"""

dummy_data = [
    (1,"Whole Numbers"),
    (1, "Integers"),
    (1,"Fractions"),
    (1,"Decimals"),
    (1,"Factors and Multiples"),
    (1,"Ratio, Proportion, and Rate"),
    (1,"Percentages"),
    (1,"Measurement"),
    (1,"Algebraic Expressions"),
    (1,"Angles"),
    (1,"Quadrilaterals"),
    (1,"Circles"),
    (1,"Three-Dimensional Figures"),
    (1,"Statistics and Probability"),
    (1,"Simultaneous Linear Equations"),
    (1,"Indices and Logarithms"),
    (1,"Expansion and Factorization of Algebraic Expressions"),
    (1,"Simple and Compound Interest"),
    (1,"Consumer Arithmetic"),
    (1,"Data Handling"),
    (2,"Quadrilaterals"),
    (2,"Circles"),
    (2,"Three-Dimensional Figures"),
    (2,"Statistics and Probability"),
    (2,"Simultaneous Linear Equations"),
    (2,"Indices and Logarithms"),
    (2,"Expansion and Factorization of Algebraic Expressions"),
    (2,"Simple and Compound Interest"),
    (2,"Consumer Arithmetic"),
    (2,"Data Handling"),
    (2,"Linear Equations and Inequalities"),
    (2,"Functions"),
    (2,"Mensuration"),
    (2,"Trigonometry"),
    (2,"Matrices"),
    (2,"Sets and Venn Diagrams"),
    (2,"Quadratic Equations"),
    (2,"Probability"),
    (2,"Indices, Logarithms, and Exponential Functions"),
    (2,"Variation"),
    (3,"Quadratic Equations"),
    (3,"Probability"),
    (3,"Indices, Logarithms, and Exponential Functions"),
    (3,"Variation"),
    (3,"Coordinate Geometry"),
    (3,"Plane Geometry"),
    (3,"Trigonometry"),
    (3,"Statistics"),
    (3,"Matrices and Transformations"),
    (3,"Arithmetic and Geometric Progressions"),
    (3,"Calculus"),
    (3,"Financial Mathematics"),
    (3,"Set Theory"),
    (3,"Probability Distributions"),
    (3,"Geometry of Circles"),
    (3,"Data Analysis and Presentation"),
    (3,"Indices and Surds"),
    (3,"Functions and Graphs"),
    (4,"Trigonometry"),
    (4,"Calculus"),
    (4,"Financial Mathematics"),
    (4,"Set Theory"),
    (4,"Probability Distributions"),
    (4,"Geometry of Circles"),
    (4,"Data Analysis and Presentation"),
    (4,"Indices and Surds"),
    (4,"Functions and Graphs"),
    (4,"Vectors"),
    (4,"Probability and Statistics"),
    (4,"Geometry of Triangles"),
    (4,"Linear Programming"),
    (4,"Matrices and Transformations"),
    (4,"Sequences and Series"),
    (4,"Differentiation and Integration"),
    (4,"Index Numbers"),
    (4,"Geometry of Solids"),
    (4,"Further Calculus"),
    (4,"Coordinate Geometry"),
    (4,"Linear Algebra"),
    (4,"Trigonometric Equations"),
    (4,"Financial Applications"),
    (4,"Statistics and Probability"),
    (4,"Differential Equations"),
    (4,"Indices and Logarithms"),
    (4,"Complex Numbers"),
    (4,"Statistics"),
    (4,"Business Mathematics")
    # Add more dummy data as needed
]

cursor.executemany(insert_query, dummy_data)
connection.commit()

# Close the cursor and connection
cursor.close()
connection.close()

print("Dummy data inserted successfully.")
