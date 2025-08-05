/* Write your PL/SQL query statement below */


DELETE FROM person
WHERE id not in (
SELECT MIN(id)
FROM person
GROUP BY email
);