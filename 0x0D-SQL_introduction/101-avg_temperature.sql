-- Script that shows the average
-- temperature by city ordered by
-- temperature
SELECT city, AVG(value) as average_temperature
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
