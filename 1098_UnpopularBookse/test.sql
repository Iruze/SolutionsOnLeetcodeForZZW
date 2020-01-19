# Write your MySQL query statement below
SELECT books.book_id,books.name
FROM books
LEFT OUTER JOIN orders
ON books.book_id=orders.book_id 
WHERE books.available_from <= DATE_ADD('2019-06-23',INTERVAL -1 MONTH)
GROUP BY book_id
HAVING IFNULL(SUM(IF(dispatch_date >= DATE_ADD('2019-06-23',INTERVAL -1 YEAR), quantity, 0)),0)<10;


# solution2:
# Write your MySQL query statement below
SELECT books.book_id,books.name
FROM books
LEFT OUTER JOIN orders
ON books.book_id=orders.book_id 
AND orders.dispatch_date >= DATE_ADD('2019-06-23',INTERVAL -1 YEAR)
WHERE books.available_from <= DATE_ADD('2019-06-23',INTERVAL -1 MONTH)
GROUP BY book_id
HAVING IFNULL(SUM(quantity),0)<10;
