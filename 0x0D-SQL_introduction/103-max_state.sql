-- Script that shows maximum temperature
-- of each state ordered by state
SELECT state, MAX(value) AS maximum_temperature
FROM temperatures
GROUP BY state
ORDER BY state;
