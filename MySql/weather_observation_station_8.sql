SELECT DISTINCT CITY
FROM STATION
WHERE CITY
REGEXP'^[AEIOU]' AND CITY REGEXP'[AEIOU]$';