



---------- // 3 // Q2 results per aisle and sorted by the number of less risky products ----------


---------- execute in psql : \i documents/technical_test_CodaBene/sql_exo/q3.sql


---------- Products expired before 2021-10-20 ---------- 


SELECT allee, COUNT(*) AS n 
FROM initialized_products 
WHERE expiry_date < '2021-10-20' 
GROUP BY allee 
ORDER BY n;



---------- Products which will expire in less than 5 days ---------- 


SELECT allee, COUNT(*) AS n 
FROM initialized_products 
WHERE expiry_date >= '2021-10-20' AND expiry_date <= '2021-10-25' 
GROUP BY allee 
ORDER BY n;



---------- Products which will expire in more than 5 days ---------- 


SELECT allee, COUNT(*) AS n 
FROM initialized_products 
WHERE expiry_date > '2021-10-25' 
GROUP BY allee 
ORDER BY n;


