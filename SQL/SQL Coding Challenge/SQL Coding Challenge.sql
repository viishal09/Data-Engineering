create database CodingChallenge1;

use CodingChallenge1;

CREATE TABLE Customers (
  CustomerID INT PRIMARY KEY,
  CustomerName VARCHAR(50),
  Country VARCHAR(50)
);

INSERT INTO Customers VALUES (1, 'John Doe', 'USA');
INSERT INTO Customers VALUES (2, 'Jane Smith', 'Canada');

CREATE TABLE Orders (
  OrderID INT PRIMARY KEY,
  CustomerID INT,
  OrderDate DATE,
  Amount DECIMAL(10, 2),
  FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);

INSERT INTO Orders VALUES (101, 1, '2024-01-01', 150.00);
INSERT INTO Orders VALUES (102, 1, '2024-01-02', 200.00);
INSERT INTO Orders VALUES (103, 2, '2024-01-03', 100.00);


/*Inner Join*/  
SELECT
  Orders.OrderID,
  Customers.CustomerName,
  Orders.OrderDate,
  Orders.Amount
FROM
  Orders
INNER JOIN
  Customers ON Orders.CustomerID = Customers.CustomerID;

/* Left Join*/
SELECT
  Customers.CustomerName,
  Orders.OrderID,
  Orders.OrderDate,
  Orders.Amount
FROM
  Customers
LEFT JOIN
  Orders ON Customers.CustomerID = Orders.CustomerID;
  

/*Right Join*/
SELECT
  Orders.OrderID,
  Customers.CustomerName,
  Orders.OrderDate,
  Orders.Amount
FROM
  Orders
RIGHT JOIN
  Customers ON Orders.CustomerID = Customers.CustomerID;

/*Cross JOin*/
SELECT
  Customers.CustomerName,
  Orders.OrderID,
  Orders.OrderDate,
  Orders.Amount
FROM
  Customers
CROSS JOIN
  Orders;
  
/*SubTotal*/
SELECT
  OrderID,
  CustomerID,
  OrderDate,
  Amount,
  SUM(Amount) OVER (PARTITION BY CustomerID ORDER BY OrderDate) AS CustomerSubtotal
FROM
  Orders;


/*Total Aggregations*/
SELECT
  OrderID,
  CustomerID,
  OrderDate,
  Amount,
  SUM(Amount) OVER () AS TotalAmount
FROM
  Orders;
  
/* Self Join */
SELECT
  o1.OrderID AS OrderID1,
  o1.CustomerID AS CustomerID1,
  o1.OrderDate AS OrderDate1,
  o1.Amount AS Amount1,
  o2.OrderID AS OrderID2,
  o2.CustomerID AS CustomerID2,
  o2.OrderDate AS OrderDate2,
  o2.Amount AS Amount2
FROM
  Orders o1
JOIN
  Orders o2 ON o1.CustomerID = o2.CustomerID
WHERE
  o1.OrderID <> o2.OrderID;
  
  
/* Full Outer Join*/
SELECT
  Customers.CustomerName,
  Orders.OrderID,
  Orders.OrderDate,
  Orders.Amount
FROM
  Customers
LEFT JOIN
  Orders ON Customers.CustomerID = Orders.CustomerID

UNION

SELECT
  Customers.CustomerName,
  Orders.OrderID,
  Orders.OrderDate,
  Orders.Amount
FROM
  Orders
RIGHT JOIN
  Customers ON Orders.CustomerID = Customers.CustomerID;




