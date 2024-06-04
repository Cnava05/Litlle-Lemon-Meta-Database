CREATE PROCEDURE MakeBooking(booking_id INT, customer_id INT, table_no INT, booking_date DATE, booking_slot TIME, first_name VARCHAR(255), last_name VARCHAR(255))
INSERT INTO Bookings (BookingID, TableNumber, BookingSlot, CustomerID, GuestFirstName, GuestLastName, BookingDate)
VALUES
(booking_id, table_no, booking_slot, customer_id, first_name, last_name, booking_date);