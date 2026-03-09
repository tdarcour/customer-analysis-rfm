-- Distribution of customers by segment

SELECT
Segment,
COUNT(*) AS nb_clients
FROM rfm_clients
GROUP BY Segment
ORDER BY nb_clients DESC;


-- Total revenue by segment

SELECT
Segment,
SUM(Monetary) AS total_revenue
FROM rfm_clients
GROUP BY Segment
ORDER BY total_revenue DESC;


-- Top 10 customers by spending

SELECT TOP 10
CustomerID,
Monetary
FROM rfm_clients
ORDER BY Monetary DESC;


-- Average customer value

SELECT
AVG(TotalSpent) AS average_customer_value
FROM customer_aggregates;


-- Most active customers (by number of orders)

SELECT TOP 10
CustomerID,
NbOrders
FROM customer_aggregates
ORDER BY NbOrders DESC;