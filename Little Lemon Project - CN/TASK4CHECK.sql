CREATE PROCEDURE CheckBooking(booking_date Date, table_number INT)
BEGIN
DECLARE bookedTable INT DEFAULT 0
	SELECT Count(bookedTable)
		INTO Bookings WHERE BookingDate = booking_date AND TableNumber = table_number
        IF bookedTable > 0 THEN 
			SELECT CONCAT ("Table", table_number, " is already booked") AS "Booking Status"
		ELSE
			SELECT CONCAT ("Table", table_number, " is not booked") AS "Booking Status"
        END IF;
END
        
         
        


