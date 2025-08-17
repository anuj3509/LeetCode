# Write your MySQL query statement below

select *
from Users
where binary right(mail, 13) = '@leetcode.com'
  and left(mail, LENGTH(mail) - 13) regexp '^[A-Za-z][A-Za-z0-9_.-]*$';




-- ****************************** not working ******************************

-- select *
-- from Users
-- where mail REGEXP_LIKE(mail, '^[A-Za-z][A-Za-z0-9._-]*@leetcode\\.com$', 'c')