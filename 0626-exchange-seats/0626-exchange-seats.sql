# Write your MySQL query statement below

select 
    case
        when        -- this when is selecting the last odd id and if it is odd
            id = (select max(id) from Seat) and mod(id, 2) = 1   
            then id
        when 
            mod(id, 2) = 1
            then id + 1
        else
            id - 1
    end as id, student
from Seat
order by id