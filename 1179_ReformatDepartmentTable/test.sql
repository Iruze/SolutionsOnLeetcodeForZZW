# Write your MySQL query statement below
SELECT id
    , SUM(CASE month WHEN 'Jan' THEN revenue ELSE NULL END) Jan_Revenue
    , SUM(CASE month WHEN 'Feb' THEN revenue ELSE NULL END) Feb_Revenue
    , SUM(CASE month WHEN 'Mar' THEN revenue ELSE NULL END) Mar_Revenue
    , SUM(CASE month WHEN 'Apr' THEN revenue ELSE NULL END) Apr_Revenue
    , SUM(CASE month WHEN 'May' THEN revenue ELSE NULL END) May_Revenue
    , SUM(CASE month WHEN 'Jun' THEN revenue ELSE NULL END) Jun_Revenue
    , SUM(CASE month WHEN 'Jul' THEN revenue ELSE NULL END) Jul_Revenue
    , SUM(CASE month WHEN 'Aug' THEN revenue ELSE NULL END) Aug_Revenue
    , SUM(CASE month WHEN 'Sep' THEN revenue ELSE NULL END) Sep_Revenue
    , SUM(CASE month WHEN 'Oct' THEN revenue ELSE NULL END) Oct_Revenue
    , SUM(CASE month WHEN 'Nov' THEN revenue ELSE NULL END) Nov_Revenue
    , SUM(CASE month WHEN 'Dec' THEN revenue ELSE NULL END) Dec_Revenue
FROM Department
Group BY id;



# solution 2:
SELECT id
    , MAX(CASE  WHEN month = 'Jan' THEN revenue ELSE NULL END) Jan_Revenue
    , MAX(CASE  WHEN month = 'Feb' THEN revenue ELSE NULL END) Feb_Revenue
    , MAX(CASE  WHEN month = 'Mar' THEN revenue ELSE NULL END) Mar_Revenue
    , MAX(CASE  WHEN month = 'Apr' THEN revenue ELSE NULL END) Apr_Revenue
    , MAX(CASE  WHEN month = 'May' THEN revenue ELSE NULL END) May_Revenue
    , MAX(CASE  WHEN month = 'Jun' THEN revenue ELSE NULL END) Jun_Revenue
    , MAX(CASE  WHEN month = 'Jul' THEN revenue ELSE NULL END) Jul_Revenue
    , MAX(CASE  WHEN month = 'Aug' THEN revenue ELSE NULL END) Aug_Revenue
    , MAX(CASE  WHEN month = 'Sep' THEN revenue ELSE NULL END) Sep_Revenue
    , MAX(CASE  WHEN month = 'Oct' THEN revenue ELSE NULL END) Oct_Revenue
    , MAX(CASE  WHEN month = 'Nov' THEN revenue ELSE NULL END) Nov_Revenue
    , MAX(CASE  WHEN month = 'Dec' THEN revenue ELSE NULL END) Dec_Revenue
FROM Department
Group BY id;



# solution3:
SELECT id
    , MAX(IF(month = 'Jan', revenue ,NULL)) Jan_Revenue
    , MAX(IF(month = 'Feb', revenue ,NULL)) Feb_Revenue
    , MAX(IF(month = 'Mar', revenue ,NULL)) Mar_Revenue
    , MAX(IF(month = 'Apr', revenue ,NULL)) Apr_Revenue
    , MAX(IF(month = 'May', revenue ,NULL)) May_Revenue
    , MAX(IF(month = 'Jun', revenue ,NULL)) Jun_Revenue
    , MAX(IF(month = 'Jul', revenue ,NULL)) Jul_Revenue
    , MAX(IF(month = 'Aug', revenue ,NULL)) Aug_Revenue
    , MAX(IF(month = 'Sep', revenue ,NULL)) Sep_Revenue
    , MAX(IF(month = 'Oct', revenue ,NULL)) Oct_Revenue
    , MAX(IF(month = 'Nov', revenue ,NULL)) Nov_Revenue
    , MAX(IF(month = 'Dec', revenue ,NULL)) Dec_Revenue
FROM Department
Group BY id;
