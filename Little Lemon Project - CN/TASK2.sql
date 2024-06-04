SELECT customers.CustomerID, customers.FullName,
Orders.OrderID, Orders.Cost, menus.Cuisine FROM 
Customers INNER JOIN Orders ON
menuitems.MenuItemID = menus.MenuItemsID
WHERE Cost > 150
ORDER BY Cost;