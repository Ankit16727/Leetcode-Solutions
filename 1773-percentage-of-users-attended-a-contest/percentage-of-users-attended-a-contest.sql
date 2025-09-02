# Write your MySQL query statement below
# For each contest, finding the percentage, idea is to group by contest_id.


SELECT contest_id, ROUND ((COUNT(*) / (SELECT COUNT(*) FROM users)) * 100, 2) AS percentage
FROM register
GROUP BY contest_id
ORDER BY percentage DESC, contest_id ASC;
