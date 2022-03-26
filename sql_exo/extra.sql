

---------- EXTRA ---------- 


---------- execute in psql : \i documents/technical_test_CodaBene/sql_exo/extra.sql


---------- Number of untracked products for which Date_deref is not NAN ----------


---------- 13039

SELECT COUNT(*) 
FROM store_products s 
LEFT OUTER JOIN initialized_products i 
ON s.EAN = i.reference_id 
WHERE i.reference_id IS NULL AND s.Date_deref IS NOT NULL;

