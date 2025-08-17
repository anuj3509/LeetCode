# Write your MySQL query statement below

-- select *
-- from Users
-- where mail REGEXP_LIKE(mail, '^[A-Za-z][A-Za-z0-9._-]*@leetcode\\.com$', 'c')


select *
from Users
where BINARY right(mail, 13) = '@leetcode.com'
  and left(mail, LENGTH(mail) - 13) REGEXP '^[A-Za-z][A-Za-z0-9_.-]*$';
