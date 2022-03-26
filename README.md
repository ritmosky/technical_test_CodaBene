
###########################################

**# technical_test_CodaBene

Data Analysis | Data Engineering project**


This project was carried out as part of an application for a Data Engineer position at CodaBene.
It consists of 2 parts.

In the first part, we put ourselves in the shoes of a Data Analyst with large data sets and a complex problem 
to solve. Here's the background: ExpiryApp is a CodaBene app that helps in-store teams manage product expiration dates.
The problem to be solved is the following: when new products are physically added to the shelves, the teams in store do 
not always remember to initialize these products in the application; and set expiration dates for them. Therefore, ExpiryApp 
does not know about them and products may be missed during the daily check routine.
The analysis aims at determining if ExpiryApp is successfully tracking all relevant products in a specific store, and if not,
at suggesting products to track.


The second part is based on the manipulation of the SQL language and therefore on establishing queries in order to answer specific questions.
The questions refer to the same previous dataset.



############################################


To be able to run the different programs, you must first clone this directory or otherwise replicate the architecture 
of this directory with the same names (for folders and files) in your computer **Documents** folder.






#### SQL


For the SQL part, you must first connect with the **PSQL client**. Then, you have to go to the default directory using the command: **\cd**
Then to run the **create_db.sql** file, enter the command: **\i documents/technical_test_CodaBene/sql_exo/create_db.sql**. This will create 
a database for the project as well as 2 tables that will contain the data.

To check the creation use : **\l** which lists the existing databases

You must then place your dataset in format **CSV** in the **data** folder contained in the **technical_test_CodaBene** folder.

To import a csv file, you must first go to the directory containing this file. For us the command is as 
follows : **\cd documents/technical_test_CodaBene/data**.

Then load the 2 CSV files with : **\copy initialized_products FROM 'references_initialized_in_shop.csv' WITH CSV HEADER DELIMITER ';' QUOTE '"'** 
and **\copy store_products FROM 'new_retailer_extract.csv' WITH CSV HEADER DELIMITER ';' QUOTE '"'**.

After to execute an SQL file with the help of PSQL, follow these steps:
- first, return to the default directory with: **\cd**
- then run : **\i path_of_file/name_of_file.sql**

You will be able to run :
- **\i documents/technical_test_CodaBene/sql_exo/q1.sql**
- **\i documents/technical_test_CodaBene/sql_exo/q2.sql**
- **\i documents/technical_test_CodaBene/sql_exo/q3.sql**
- **\i documents/technical_test_CodaBene/sql_exo/q4.sql**
- **\i documents/technical_test_CodaBene/sql_exo/extra.sql**





                                                                                                                                                         
                                                                                                                                                         
`7MMF'     A     `7MF'`7MM"""YMM      `7MMF'        .g8""8q.`7MMF'   `7MF'`7MM"""YMM      `7MM"""Yb.      db   MMP""MM""YMM   db                         
  `MA     ,MA     ,V    MM    `7        MM        .dP'    `YM.`MA     ,V    MM    `7        MM    `Yb.   ;MM:  P'   MM   `7  ;MM:                        
   VM:   ,VVM:   ,V     MM   d          MM        dM'      `MM VM:   ,V     MM   d          MM     `Mb  ,V^MM.      MM      ,V^MM.                       
    MM.  M' MM.  M'     MMmmMM          MM        MM        MM  MM.  M'     MMmmMM          MM      MM ,M  `MM      MM     ,M  `MM                       
    `MM A'  `MM A'      MM   Y  ,       MM      , MM.      ,MP  `MM A'      MM   Y  ,       MM     ,MP AbmmmqMA     MM     AbmmmqMA                      
     :MM;    :MM;       MM     ,M       MM     ,M `Mb.    ,dP'   :MM;       MM     ,M       MM    ,dP'A'     VML    MM    A'     VML  ,,                 
      VF      VF      .JMMmmmmMMM     .JMMmmmmMMM   `"bmmd"'      VF      .JMMmmmmMMM     .JMMmmmdP'.AMA.   .AMMA..JMML..AMA.   .AMMA.dg                 
                                                                                                                                      ,j                 
                                                                                                                                     ,'                  
`7MM"""Mq.`YMM'   `MM'MMP""MM""YMM `7MMF'  `7MMF' .g8""8q. `7MN.   `7MF'          db      `7MN.   `7MF'`7MM"""Yb.        .M"""bgd   .g8""8q. `7MMF'      
  MM   `MM. VMA   ,V  P'   MM   `7   MM      MM .dP'    `YM. MMN.    M           ;MM:       MMN.    M    MM    `Yb.     ,MI    "Y .dP'    `YM. MM        
  MM   ,M9   VMA ,V        MM        MM      MM dM'      `MM M YMb   M          ,V^MM.      M YMb   M    MM     `Mb     `MMb.     dM'      `MM MM        
  MMmmdM9     VMMP         MM        MMmmmmmmMM MM        MM M  `MN. M         ,M  `MM      M  `MN. M    MM      MM       `YMMNq. MM        MM MM        
  MM           MM          MM        MM      MM MM.      ,MP M   `MM.M         AbmmmqMA     M   `MM.M    MM     ,MP     .     `MM MM.      ,MP MM      , 
  MM           MM          MM        MM      MM `Mb.    ,dP' M     YMM        A'     VML    M     YMM    MM    ,dP'     Mb     dM `Mb.    ,dP' MM     ,M 
.JMML.       .JMML.      .JMML.    .JMML.  .JMML. `"bmmd"' .JML.    YM      .AMA.   .AMMA..JML.    YM  .JMMmmmdP'       P"Ybmmd"    `"bmmd"' .JMMmmmmMMM 
                                                                                                                                        MMb              
                                                                                                                                         `bood'          
                                                                                                                                         
                                                                                                                                         
                                                                                                                                         
                                                                                                                                         
                                                                                                                                         

                                     /$$$$$$$$ /$$   /$$  /$$$$$$  /$$   /$$ /$$   /$$       /$$   /$$       /$$ /$$ /$$
                                    |__  $$__/| $$  | $$ /$$__  $$| $$$ | $$| $$  /$$/      | $$  | $$      | $$| $$| $$
                                       | $$   | $$  | $$| $$  \ $$| $$$$| $$| $$ /$$/       | $$  | $$      | $$| $$| $$
                                       | $$   | $$$$$$$$| $$$$$$$$| $$ $$ $$| $$$$$/        | $$  | $$      | $$| $$| $$
                                       | $$   | $$__  $$| $$__  $$| $$  $$$$| $$  $$        | $$  | $$      |__/|__/|__/
                                       | $$   | $$  | $$| $$  | $$| $$\  $$$| $$\  $$       | $$  | $$                  
                                       | $$   | $$  | $$| $$  | $$| $$ \  $$| $$ \  $$      |  $$$$$$/       /$$ /$$ /$$
                                       |__/   |__/  |__/|__/  |__/|__/  \__/|__/  \__/       \______/       |__/|__/|__/




                                                                                    
                                                                                                                                    
