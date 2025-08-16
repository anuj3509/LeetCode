# Write your MySQL query statement below

-- SELECT name 
-- FROM Customer
-- Where referee_id != 2 or referee_id is null


SELECT name
FROM Customer
Where Coalesce(referee_id, 'null') <> 2     -- we can also use != instead of <>