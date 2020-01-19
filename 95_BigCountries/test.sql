# Write your MySQL query statement below
SELECT w.name, w.population, w.area
FROM World w
WHERE w.area > 300 * 10000 OR w.population > 2500 * 10000;



# solution2: 使用UNION语句
SELECT 
    name, population, area
FROM 
    World
WHERE 
    area > 300 * 10000

UNION

SELECT 
    name, population, area
FROM 
    World
WHERE 
    population > 2500 * 10000;
  
  
  
UNION:
语句的使用方法：
SQL UNION 操作符
UNION 操作符用于合并两个或多个 SELECT 语句的结果集。
请注意，UNION 内部的 SELECT 语句必须拥有相同数量的列。列也必须拥有相似的数据类型。同时，每条 SELECT 语句中的列的顺序必须相同。
SELECT column_name(s) FROM table_name1
UNION
SELECT column_name(s) FROM table_name2


UNION ALL:
命令和 UNION 命令几乎是等效的，不过 UNION ALL 命令会列出所有的值。
SQL Statement 1
UNION ALL
SQL Statement 2
