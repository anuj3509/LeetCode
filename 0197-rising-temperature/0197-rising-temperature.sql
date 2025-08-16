# Write your MySQL query statement below

select w1.id        -- you can also use id of w2, both are same
from Weather w1
inner join Weather w2
on datediff(w1.recordDate, w2.recordDate) = 1    -- calculates diff in dates ; you can also use ON instead od where
and w1.temperature > w2.temperature