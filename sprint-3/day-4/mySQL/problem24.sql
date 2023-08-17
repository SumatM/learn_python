Problem: Write a query to fetch the top 5 restaurants when ordered by average_rating in descending order.


SELECT *
FROM Restaurants
ORDER BY average_rating DESC
LIMIT 5;
