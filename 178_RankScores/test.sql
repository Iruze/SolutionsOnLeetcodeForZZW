# Write your MySQL query statement below
SELECT a.Score, 
    (
        SELECT COUNT(DISTINCT b.Score)
        FROM Scores b
        WHERE b.Score >= a.Score
    ) Rank
FROM Scores a
ORDER BY a.Score DESC;
