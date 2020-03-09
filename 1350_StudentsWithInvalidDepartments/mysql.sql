# 解法一：left join解法
# Write your MySQL query statement below
SELECT s.id, s.name
FROM Students s
LEFT OUTER JOIN Departments d 
ON s.department_id = d.id
WHERE ISNULL(d.id);


# 解法二： 暴力直接解法
# Write your MySQL query statement below
SELECT id, name
FROM Students
WHERE department_id NOT IN
    (
        SELECT DISTINCT id
        FROM Departments
    )
;
