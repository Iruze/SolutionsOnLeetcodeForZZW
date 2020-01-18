# solution1: 利用HAVING
SELECT p.Email
FROM Person p
GROUP BY p.Email
HAVING COUNT(p.Id) > 1;




# solution2: 建立临时表
SELECT Email
FROM 
    (
        SELECT Email, COUNT(Email) num
        FROM Person
        GROUP BY Email
    ) temp_table
WHERE num > 1;
