Problem: Write a query to fetch all customers whose id is greater than 2 and name starts with 'B'.


SELECT *
FROM Customers
WHERE id > 2 AND name LIKE 'B%';


