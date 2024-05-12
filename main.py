import Admin
import mysql.connector as msql


# Connect to Mysql Database
mydb = msql.connect(host="localhost", user="root", password="qwerty")


def db_creation():
    # Check if database exist else create the database
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE IF NOT Exists airline")
    mycursor.execute("USE airline")

    # Check if table exists else create table
    mycursor.execute("CREATE TABLE IF NOT EXISTS Login(Username varchar(50), Password varchar(30));")

    Admin.login_db()


def main():
    while True:
        print("Airline Booking System")
        print("Main Menu")
        print()
        db_creation()
        break


main()
