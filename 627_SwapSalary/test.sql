# Write your MySQL query statement below
UPDATE salary 
SET sex = (CASE WHEN sex = 'm' THEN 'f' ELSE 'm' END);



# solution2: 使用IF语句
UPDATE salary
SET 
    sex = IF(sex = 'm', 'f', 'm');
