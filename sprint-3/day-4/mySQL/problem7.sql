- **Problem**: Write a query to fetch all customers, ordered by **`name`** in descending order.


db.Customers.find().sort({ name: -1 });
