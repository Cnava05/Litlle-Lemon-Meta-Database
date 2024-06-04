CREATE VIEW `orderview1` AS
SELECT OrderID, Quantity, Cost From Orders Where Quantity > 2;