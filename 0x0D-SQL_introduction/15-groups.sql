-- Script that lists number of records
-- with the same score
SELECT score, COUNT(*) AS no_of_records
FROM second_table
GROUP BY score DESC;
