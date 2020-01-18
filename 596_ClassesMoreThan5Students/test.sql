# Write your MySQL query statement below
SELECT c.class 
FROM courses c
GROUP BY c.class
HAVING COUNT(DISTINCT c.student) >= 5;



# solutions2:
