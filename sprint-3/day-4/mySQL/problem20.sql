Problem: Write a query to fetch all restaurants where the cuisine_type field is not set or is null.


SELECT *
FROM Restaurants
WHERE cuisine_type IS NULL OR cuisine_type = '';
