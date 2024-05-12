import mysql.connector as msql
import Admin

# Connect to Mysql Database
mydb = msql.connect(host="localhost", user="root", password="qwerty", database="airline")


def seat_matrix():
    # Check if database exist else create the database
    mycursor = mydb.cursor()
    mycursor.execute("USE airline")

    # Check if table exists else create table
    mycursor.execute(
        'CREATE TABLE IF NOT EXISTS Seats(seat_number varchar(4), passenger_name varchar(30) DEFAULT Null, '
        'pnr varchar(11) DEFAULT Null);')

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
    mycursor.execute("SELECT * FROM BOOKING WHERE pnr = %s;", (pnr_num,))
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)
        if x:
            print("Seat Number Range from A1 - A6, B1 - B6, .... , P1 - P6")
            print()
            seat = input("Enter seat numbers for booking: ")
            pass_name = "gary"
            mycursor.execute("UPDATE seats SET  passenger_name = %s, pnr = %s, WHERE seat_number = %s;",
                             (pass_name, pnr_num, seat))
            mydb.commit()
            print("Seat", seat, "has been booked Successfully!")
        else:
            print("Passenger does not Exist!")
    print()



