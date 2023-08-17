Problem: Write a query to count the number of restaurants that have delivery_available.


SELECT COUNT(*) AS restaurant_count
FROM Restaurants
WHERE delivery_available = TRUE;
