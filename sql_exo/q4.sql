

---------- // 4 // ----------


---------- execute in psql : \i documents/technical_test_CodaBene/sql_exo/q4.sql


---------- CHARCUTERIE Products expired before 2021-10-20 ---------- 

SELECT i.allee, s.Libelle_Sous_Famille, COUNT(*) AS n 
FROM store_products s 
LEFT OUTER JOIN initialized_products i 
ON s.EAN = i.reference_id 
WHERE i.expiry_date < '2021-10-20' AND s.Libelle_Groupe_de_Famille = 'CHARCUTERIE' 
GROUP BY i.allee, s.Libelle_Sous_Famille 
ORDER BY n;


---------- CHARCUTERIE Products which will expire in less than 5 days ---------- 

SELECT i.allee, s.Libelle_Sous_Famille, COUNT(*) AS n 
FROM store_products s 
LEFT OUTER JOIN initialized_products i 
ON s.EAN = i.reference_id 
WHERE i.expiry_date >= '2021-10-20' AND i.expiry_date <= '2021-10-25' AND s.Libelle_Groupe_de_Famille = 'CHARCUTERIE' 
GROUP BY i.allee, s.Libelle_Sous_Famille 
ORDER BY n;


---------- CHARCUTERIE products which will expire in more than 5 days ---------- 

SELECT i.allee, s.Libelle_Sous_Famille, COUNT(*) AS n 
FROM store_products s 
LEFT OUTER JOIN initialized_products i 
ON s.EAN = i.reference_id WHERE i.expiry_date > '2021-10-25' AND s.Libelle_Groupe_de_Famille = 'CHARCUTERIE' 
GROUP BY i.allee, s.Libelle_Sous_Famille 
ORDER BY n;

