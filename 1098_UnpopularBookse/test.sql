# Write your MySQL query statement below
SELECT books.book_id,books.name
FROM books
LEFT OUTER JOIN orders
ON books.book_id=orders.book_id 
WHERE books.available_from <= DATE_ADD('2019-06-23',INTERVAL -1 MONTH)
GROUP BY book_id
HAVING IFNULL(SUM(IF(dispatch_date >= DATE_ADD('2019-06-23',INTERVAL -1 YEAR), quantity, 0)),0)<10;


# solution2:
SELECT b.book_id, b.name
FROM Books b
LEFT OUTER JOIN Orders o
ON b.book_id = o.book_id
AND o.dispatch_date >= DATE_ADD('2019-06-23', INTERVAL -1 YEAR)
WHERE b.available_from <= DATE_ADD('2019-06-23', INTERVAL -1 MONTH)
GROUP BY b.book_id
HAVING IFNULL(SUM(o.quantity), 0) < 10
