import mysql.connector as connector

connection =  connector.connect(user="root", password="AdminRoot123$")
cursor = connection.cursor()
cursor.execute("USE little_lemon_db")
join_query = """SELECT Bookings.BookingID, Bookings.Tablenumber,
                 Bookings.GuestFirstName, Orders.BillAmount AS TotalCost
                 From Bookings LEFT JOIN Orders ON
                 Bookings.BookingID = Orders.BookingID
                 WHERE Orders.BillAmount > 60;"""
cursor.execute(join_query)
results = cursor.fetchall()

cols = cursor.column_names
print(cols)

for i in results:
    print(i)
