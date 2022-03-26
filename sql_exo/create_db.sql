


---------- execute in psql : \i documents/technical_test_CodaBene/sql_exo/create_db.sql



DROP TABLE IF EXISTS tracked_products ;
DROP TABLE IF EXISTS store_products ;

DROP DATABASE IF EXISTS cbDB ;


CREATE DATABASE cbDB OWNER=postgres;


CREATE TABLE initialized_products (
	expiry_date DATE NOT NULL,
	reference_id NUMERIC,
	control_timestamp DATE  NOT NULL,
	allee VARCHAR(255) NOT NULL,

	PRIMARY KEY (expiry_date, reference_id, control_timestamp, allee)
);


CREATE TABLE store_products (
	Code_Secteur NUMERIC,
	Libelle_Secteur VARCHAR(50),
	Code_Rayon NUMERIC,
	Libelle_Rayon VARCHAR(50),
	Code_Groupe_de_Famille NUMERIC,
	Libelle_Groupe_de_Famille VARCHAR(50),
	Code_Famille NUMERIC,
	Libelle_Famille VARCHAR(50),
	Code_Sous_Famille NUMERIC,
	Libelle_Sous_Famille VARCHAR(50),
	Code_Unite_de_Besoin NUMERIC,
	Libelle_Unite_de_Besoin VARCHAR(50),
	Code_interne_Enseigne_sanitise NUMERIC,
	Libelle_code_interne_Enseigne VARCHAR(50),
	Code_logistique VARCHAR(50),
	EAN NUMERIC,
	Article_Libelle_Court VARCHAR(50),
	Article_Libelle_Long VARCHAR(100),
	PV_Mag VARCHAR(20),
	Quantite_vendue INTEGER,
	Stock_en_quantite INTEGER,
	Date_Deb_Cad DATE,
	Date_deref DATE,

	PRIMARY KEY (EAN)
);

