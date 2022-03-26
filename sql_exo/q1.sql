

---------- // Q1 // ---------- 


---------- execute in psql : \i documents/technical_test_CodaBene/sql_exo/q1.sql


---------- Total number of references not tracked in the app but present in the shop assortment ---------- 

---------- 36055


SELECT COUNT(*) FROM store_products s 
LEFT OUTER JOIN initialized_products i 
ON s.EAN = i.reference_id 
WHERE i.reference_id IS NULL;


