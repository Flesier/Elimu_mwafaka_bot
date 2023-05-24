import  mysql.connector 

tutordb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "kenyafo_beast"
)

#print(tutordb)
mycursor = tutordb.cursor()

#select all users
print(mycursor.execute("select * from affiliateuser"))
myresult = mycursor.fetchall() # store the information in a variable
for x in myresult:#loop through the variable
  print(x)


#execute this query
sql = "SELECT * FROM affiliateuser WHERE username ='Phill'"
mycursor.execute(sql)
myresults = mycursor.fetchall()
for y in myresults:
    print("Hello niggah{}".format(y))
    #loop in the tuple and set the formats.
    (Id, username, password, date, fname, address,email,referedby,ipaddress,*others) = y
    #Get the email in the tuple
    email = email
    print("Code runner : {}".format(email))
