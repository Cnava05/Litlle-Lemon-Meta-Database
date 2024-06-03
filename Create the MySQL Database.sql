CREATE DATABASE IF NOT EXISTS LittleLemon;
USE LittleLemon;

-- Table: Customer
CREATE TABLE Customer (
    CustomerID VARCHAR(20) PRIMARY KEY,
    CustomerName VARCHAR(100),
    City VARCHAR(50),
    Country VARCHAR(50),
    PostalCode VARCHAR(20),
    CountryCode VARCHAR(5)
);

-- Table: Order
CREATE TABLE `Order` (
    OrderID VARCHAR(20) PRIMARY KEY,
    OrderDate DATE,
    DeliveryDate DATE,
    CustomerID VARCHAR(20),
    Sales DECIMAL(10, 2),
    Quantity INT,
    Discount DECIMAL(5, 2),
    DeliveryCost DECIMAL(10, 2),
    FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID)
);

-- Table: Product
CREATE TABLE Product (
    ProductCode VARCHAR(20) PRIMARY KEY,
    ProductName VARCHAR(100),
    SKU VARCHAR(20),
    Price DECIMAL(10, 2)
);

-- Table: Cuisine
CREATE TABLE Cuisine (
    CuisineName VARCHAR(50) PRIMARY KEY
);

-- Table: MenuItems
CREATE TABLE MenuItems (
    OrderID VARCHAR(20),
    CourseName VARCHAR(100),
    CuisineName VARCHAR(50),
    StarterName VARCHAR(100),
    DessertName VARCHAR(100),
    Drink VARCHAR(100),
    Sides VARCHAR(100),
    PRIMARY KEY (OrderID),
    FOREIGN KEY (OrderID) REFERENCES `Order`(OrderID),
    FOREIGN KEY (CuisineName) REFERENCES Cuisine(CuisineName)
);
