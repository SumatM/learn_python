Problem: Write a query to fetch all customers where the phone_number field is not set or is null.


SELECT *
FROM Customers
WHERE phone_number IS NULL OR phone_number = '';


