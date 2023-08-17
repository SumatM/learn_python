
Problem: Write a query to fetch all restaurants that offer delivery_available and have an average_rating of more than 4.



SELECT *
FROM Restaurants
WHERE delivery_available = TRUE AND average_rating > 4;
