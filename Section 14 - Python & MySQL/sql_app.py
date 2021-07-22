from re import T
import mysql.connector

# connects to ardit's dictionary database
con = mysql.connector.connect(
    user = "ardit700_student",
    password = "ardit700_student",
    host = "108.167.140.122",
    database = "ardit700_pm1database"
)

cursor = con.cursor()

def func(user_word):
    # cursor = con.cursor()

    # a table to store userinput for SQL query
    # cursor.execute("CREATE TABLE DemoTable ")

    # givenUsername = 'testUser123'
    # checkUserAuthQuery = ("SELECT password FROM UserAuth WHERE username = %s")
    # userAuthInfo = (givenUsername)
    # cursor.execute(checkUserAuthQuery, userAuthInfo)

    query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '{}'".format(user_word))
    results = cursor.fetchall()
    
    return results

while True:
    user_input = input("Enter a word: ")
    output = func(user_input)
    
    print(output)

    if(input("Do you want to continue? (Y/N) ").lower() == "n"):
        break