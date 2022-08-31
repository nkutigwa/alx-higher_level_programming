-- Script that shows some cols
-- ordered by score where score
-- is greater than or equal to 10
SELECT score, name
FROM second_table
HAVING score >= 10
ORDER BY score DESC;
