# Write your MySQL query statement below
SELECT c.class 
FROM courses c
GROUP BY c.class
HAVING COUNT(DISTINCT c.student) >= 5;



# solutions2:
SELECT class
FROM
    (
        SELECT class, COUNT(DISTINCT student) num
        FROM courses
        GROUP BY class
    ) temp_talbe
WHERE num >= 5;
