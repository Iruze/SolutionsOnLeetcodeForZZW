# Write your MySQL query statement below
SELECT a.player_id, a.device_id
FROM Activity a
JOIN 
    (
        SELECT player_id, device_id, MIN(event_date) first_date
        FROM Activity
        GROUP BY player_id
    ) tmp
ON a.player_id = tmp.player_id
    AND a.event_date = tmp.first_date;
