

---------- // Q2 // ---------- 


---------- execute in psql : \i documents/technical_test_CodaBene/sql_exo/q2.sql


---------- Number of products expired before 2021-10-20 ---------- 

---------- 1100


SELECT COUNT(*) 
FROM initialized_products 
WHERE expiry_date < '2021-10-20';




---------- Number of products which will expire in less than 5 days ---------- 

---------- 82


SELECT COUNT(*) 
FROM initialized_products 
WHERE expiry_date >= '2021-10-20' AND expiry_date <= '2021-10-25';



---------- Number of products which will expire in more than 5 days ---------- 

---------- 4877


SELECT COUNT(*) 
FROM initialized_products 
WHERE expiry_date > '2021-10-25';

