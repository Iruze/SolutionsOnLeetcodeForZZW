# Write your MySQL query statement below
SELECT a.Name Employee
FROM Employee a, Employee b
WHERE a.ManagerId = b.Id
    AND a.Salary > b.Salary;
    
    
SELECT a.Name Employee
FROM Employee a
INNER JOIN Employee b
ON a.ManagerId = b.Id
    AND a.Salary > b.Salary;
