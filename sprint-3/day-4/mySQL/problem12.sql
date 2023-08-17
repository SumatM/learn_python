Problem: Write a query to fetch all customers except the first two when ordered by id in ascending order.


SELECT *
FROM Customers
ORDER BY id ASC
OFFSET 2;
