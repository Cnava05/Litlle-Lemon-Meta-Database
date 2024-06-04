CREATE DEFINER=`root`@`localhost` PROCEDURE `CancelBooking`(booking_id INT, booking_date DATE)
BEGIN
UPDATE Bookings SET BookingDate = booking_date, TableNumber = 0 WHERE BookingID = booking_id;
SELECT CONCAT("Booking", booking_is, "cancelled" ) AS "Confirmation";
END