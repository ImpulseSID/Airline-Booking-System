import random
import datetime
import mysql.connector as msql
import PNR_Generator

mydb = msql.connect(host="localhost", user="root", password="qwerty", database="airline")


def login_db():
    mycursor = mydb.cursor()
    while True:
        print("Menu")
        print("1. Login to Account")
        print("2. Create an Account")
        user_inp = int(input("Enter your selection(1-2): "))
        if user_inp == 1:

            # Check if entered username is correct
            query = " SELECT * FROM Login "
            mycursor.execute(query)
            result = mycursor.fetchall()
            inp = input("Enter the Username: ")
            temp = False
            for x in result:
                if inp in x:
                    temp = True
            if temp:
                print("Enter Password for user: ", inp)
                # Check if entered password is correct
                query = " SELECT * FROM Login "
                mycursor.execute(query)
                result = mycursor.fetchall()
                inp = input("Enter the Password: ")
                temp = False
                for x in result:
                    if inp in x:
                        temp = True
                if temp:
                    print("Logged in as Admin")
                    admin_main()
                else:
                    print("Wrong Password")
                break
            else:
                print("Wrong Username, Try Again!!")

        elif user_inp == 2:
            username = input("Enter Username: ")

            mycursor.execute("SELECT username, COUNT(*) FROM login WHERE username = %s GROUP BY username",
                             (username,))
            # Add THIS LINE
            results = mycursor.fetchall()
            # gets the number of rows affected by the command executed
            row_count = mycursor.rowcount
            if row_count == 0:
                print("Enter the Password")
                passwd = input("Enter Password: ")
                sql = "INSERT INTO login (username, password) VALUES (%s, %s)"
                val = (username, passwd)
                mycursor.execute(sql, val)
                mydb.commit()
                print("Successfully Created")
            else:
                print("User Exists")
        else:
            print("Invalid Selection")


def admin_main():
    while True:
        print("Menu")
        print("1. Book Tickets")
        print("2. Check Booking Status")
        print("3. Cancel Booking")
        print("4. Book Seats")
        print("5. Exit")
        # Check if database exist else create the database
        mycursor = mydb.cursor()
        # Check if table exists else create table
        mycursor.execute("CREATE TABLE IF NOT EXISTS Booking(pnr varchar(11), date_of_journey date, source varchar(50),"
                         "destination varchar(30), passenger_name varchar(30), passenger_age int, fare int);")
        # Ask for user Selection
        user_inp = int(input("Enter your selection(1-5): "))
        global passenger_name

        # List of Cities with domestic Airports
        cities = ["Agartala", "Agra", "Ahmedabad", "Aizawl", "Amritsar", "Aurangabad", "Bagdogra", "Bareilly",
                  "Belagavi", "Bengaluru", "Bhopal", "Bhubaneswar", "Chandigarh", "Chennai", "Coimbatore",
                  "Darbhanga", "Jabalpur", "Jaipur", "Jammu", "Jodhpur", "Jorhat", "Kadapa", "Kannur", "Kanpur",
                  "Kochi", "Dehradun", "Delhi", "Durgapur", "Gaya", "Goa", "Gorakhpur", "Guwahati", "Gwalior",
                  "Hubli", "Hyderabad", "Imphal", "Indore",
                  "Itanagar", "Kolhapur", "Kolkata", "Kozhikode", "Kurnool", "Leh", "Lucknow", "Madurai",
                  "Mangaluru", "Mumbai", "Mysuru", "Nagpur", "North Goa", "Pantnagar", "Patna", "Port-Blair",
                  "Prayagraj", "Pune", "Raipur", "Rajahmundry", "Rajkot", "Ranchi", "Shillong", "Shirdi",
                  "Silchar", "Srinagar", "Surat", "Thiruvananthapuram", "Tiruchirappalli", "Tirupati",
                  "Tuticorin", "Udaipur", "Vadodara", "Varanasi", "Vijayawada", "Visakhapatnam"]

        # Loop for operations on the input user selection
        if user_inp == 1:
            passenger_number = int(input("Enter Number of Passengers: "))
            # Printing List of Cities
            print("List of Cities:- ")
            print(cities[0], end='\t\t')
            for i in range(1, len(cities)):
                if i % 10 == 0:
                    print(cities[i])
                else:
                    print(cities[i], end='\t\t')
            print()
            source = input("Enter Departure City: ").capitalize()
            destination = input("Enter Arrival City: ").capitalize()
            if source not in cities or destination not in cities:
                print("Airport does not exist at the entered location")
                print("Please enter a new Location")
            else:
                # Asking for date of Journey
                date_entry = input("Enter a date in YYYY-MM-DD format: ")
                year, month, day = map(int, date_entry.split('-'))
                date_of_journey = datetime.date(year, month, day)
                day_of_journey = date_of_journey.strftime("%A")

                if (day_of_journey == "Monday" or day_of_journey == "Tuesday" or day_of_journey == "Wednesday" or
                        day_of_journey == "Thursday" or day_of_journey == "Friday"):
                    fare = random.randrange(3500, 9000)
                    print("Your Fare is: ", fare)
                    print()
                else:
                    # Print Ticket Fare using Random Module
                    fare = random.randrange(7500, 12000)
                    print("Your Fare is: ", fare)
                    print()

                # Getting PNR for the PNR Generator File
                pnr_num = PNR_Generator.generator()

                for i in range(passenger_number):
                    passenger_name = input("Enter Passenger Name: ").capitalize()
                    passenger_age = int(input("Enter Passenger Age: "))

                    # Ask Confirmation for Booking
                    confirm = input("Do you want to book this ticket(YES/NO): ").upper()
                    if confirm == "NO":
                        print("Booking Cancelled")
                        print()
                    elif confirm == "YES":
                        sql = ("INSERT INTO Booking (pnr, date_of_journey, source, destination, passenger_name, "
                               "passenger_age, fare) VALUES (%s, %s, %s, %s, %s, %s, %s);")
                        val = (pnr_num, date_of_journey, source, destination, passenger_name, passenger_age, fare)
                        mycursor.execute(sql, val)
                        mydb.commit()
                        print("Ticket Booked Successfully")
                        print("PNR for your Booking is: ", pnr_num)
                        print()
                    else:
                        print("Invalid Input! \n Try Again")
                        print()

            # Checking if input city has an Airport

        elif user_inp == 2:
            pnr_numb = input("Enter the PNR number to Find Booking: ")
            mycursor.execute("SELECT * FROM BOOKING WHERE pnr = %s", (pnr_numb,))
            myresult = mycursor.fetchall()
            for x in myresult:
                print(x)
            print()

        elif user_inp == 3:
            pnr_numb = input("Enter the PNR number to Find Booking: ")

            # Deleting Data from Booking Table
            mycursor.execute("DELETE FROM booking WHERE pnr = %s;", (pnr_numb,))
            mydb.commit()
            print(mycursor.rowcount, "record(s) deleted")

            # Updating Data in Seats table to Default Values
            mycursor.execute("SELECT seat_number FROM seats WHERE pnr = %s;", (pnr_numb,))
            result = mycursor.fetchall()
            for sea in result:
                mycursor.execute("UPDATE seats SET passenger_name = NULL, pnr = NULL, Booking_Status = NULL "
                                 "WHERE seat_number = %s; ", sea)
                mydb.commit()

            print()

        elif user_inp == 4:
            checkTableExists("Seats")

        elif user_inp == 5:
            print("Thank You")
            print()
            break

        else:
            print("Invalid Selection")
            print()


def checkTableExists(tablename):
    mycursor = mydb.cursor()
    mycursor.execute("SELECT COUNT(*) FROM information_schema.tables WHERE table_name = '{0}'"
                     .format(tablename.replace('\'', '\'\'')))
    if mycursor.fetchone()[0] == 1:
        seat_booking()
    else:
        seat_matrix()


def seat_matrix():
    mycursor = mydb.cursor()

    # Check if table exists else create table
    mycursor.execute(
        'CREATE TABLE IF NOT EXISTS Seats(seat_number varchar(4), passenger_name varchar(30) DEFAULT Null, '
        'pnr varchar(11) DEFAULT Null, Booking_Status char(4) DEFAULT Null);')
    # Creating Seat Matrix
    asci = 65
    seat_char = chr(asci)
    seat_val = [1, 2, 3, 4, 5, 6]

    for i in range(65, 81):
        seat_char = chr(i)
        for j in seat_val:
            seat = seat_char + str(j)
            mycursor.execute("INSERT INTO seats (seat_number) VALUES (%s);", (seat, ))
            mydb.commit()

    print()
    seat_booking()


def seat_booking():
    mycursor = mydb.cursor()
    print("Seat Booking Menu")
    pnr_num = input("Enter PNR Number of Booking: ")
    mycursor.execute("SELECT passenger_name FROM BOOKING WHERE pnr = %s;", (pnr_num,))
    result = mycursor.fetchall()

    for pass_name in result:
        print("Seat Booking for", pass_name[0])
        print("Seat Number Range from A1 - A6, B1 - B6, .... , P1 - P6")
        print()

        mycursor.execute("SELECT seat_number from seats;")
        res = mycursor.fetchall()
        seat = input("Enter seat numbers for booking: ").capitalize()

        seat_exists = False

        for s in res:
            if seat in s:
                mycursor.execute("UPDATE seats SET passenger_name = %s, pnr = %s, Booking_Status = 'YES' "
                                 "WHERE seat_number = %s; ", (pass_name[0], pnr_num, seat))
                mydb.commit()
                print("Seat", seat, "has been booked Successfully!")
                seat_exists = True
                break

        if not seat_exists:
            print("Seat Does Not Exist")
        print()
    print()
