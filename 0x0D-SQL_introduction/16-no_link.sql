-- Script that lists all records of
-- second_table with no name value
-- descending order by score
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
