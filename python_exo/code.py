
########## IMPORTING LIBRARIES ##########

import numpy as np
import pandas as pd

########## LOADING FILES ##########

"""
# ----- exécuter requête sql

\i documents/technical_test_CodaBene/sql_exo/create_db.sql

\l -> pour vérifier la création

# ----- pour importer un fichier csv (se placer dans le répertoire contenant ce ficier)

\! pwd  	= pour afficher le pwd

\cd documents/technical_test_CodaBene/data

\copy initialized_products FROM 'references_initialized_in_shop.csv' WITH CSV HEADER DELIMITER  ';' QUOTE '"'
\copy store_products FROM 'new_retailer_extract.csv' WITH CSV HEADER DELIMITER  ';' QUOTE '"'


"""

#  all the products present in the shop
store_df = pd.read_csv("documents/technical_test_CodaBene/data/retailer_extract.csv", sep=";", decimal=",", parse_dates=[21, 22], dayfirst=True, low_memory=False)

# products currently tracked by the app
initialized_df = pd.read_csv("documents/technical_test_CodaBene/data/references_initialized_in_shop.csv", sep=";")


########## BROWSE DATA FILES ##########
"""
eg of query

store_df[store_df.Quantite_vendue==1]
store_df.query("Quantite_vendue==1")

"""

# ----- store_df ----- #

store_df.shape  # (39264, 23)
store_df.head()
store_df.tail()

store_df.columns
store_df.info()

store_df.isna().sum()

# drop row where all values are NA
store_df = store_df.dropna(how='all')  # shape = (39136, 23)
store_df = store_df.reset_index(drop = True)

store_df["EAN"].unique().size  # 39136



# ----- change date format

def permute(ch):  # ch = jj/mm/aaaa
    if ch:
        d = ch.split("/")
        return "-".join(list(reversed(d)))  # return aaaa-mm-jj



for i in range(store_df["Date_deref"].shape[0]):
    if str(store_df["Date_deref"][i]) != "nan":
        store_df["Date_deref"][i] = permute(store_df["Date_deref"][i])



# ----- NaN & dtype management


store_df = store_df.convert_dtypes()
store_df.info()


store_df = store_df.fillna(value={"Stock_en_quantite": 0})
store_df = store_df.fillna(value={"Quantite_vendue": 0})

for i in ["Quantite_vendue", "Stock_en_quantite"]:
    store_df[i] = store_df[i].astype(int)


store_df.info()

store_df[store_df.Date_deref.isna()]
store_df = store_df.fillna(value={"Date_deref": ''})


# ----- save in a csv file

store_df.to_csv('documents/technical_test_CodaBene/data/new_retailer_extract.csv', sep=";", decimal=",",  index=False)

# ----- initialized_df

initialized_df.shape  # (6059, 4)
initialized_df.index
initialized_df.head()
initialized_df.tail()


initialized_df.columns
initialized_df.info()

initialized_df.isna().sum()  # 0
initialized_df.isnull().sum()  # 0

initialized_df["expiry_date"].unique().size  # 800

initialized_df["reference_id"].unique().size  # 5902

initialized_df["control_timestamp"].unique().size  # 6059

initialized_df["allee"].values
initialized_df["allee"].unique()
initialized_df["allee"].unique().size  # 50


########## TOTAL NUMBER OF REFERENCES NOT TRACKED IN THE APP BUT PRESENT IN THE SHOP ##########


# (39280, 27)
df = pd.merge(store_df, initialized_df, how="left", left_on="EAN", right_on="reference_id")

df["allee"].size  # 39280
df["allee"].isna().sum()  # 36055

# ----- products are in the shop but not tracked  =  << 36055 >>

untracked = df[df["reference_id"].isna()]  # = df.query("EAN != reference_id")
untracked = untracked[["EAN", "Libelle_Sous_Famille", "Article_Libelle_Long", "Date_deref"]]

untracked.shape[0]  # 36055


########## LIST (EAN, Reference Name) OF PRODUCTS WHICH ARE NOT TRACKED BUT ARE RELEVANT ##########
"""
- Date_deref is not NAN
- Libelle Sous-Famille is tracked in at least one aisle
"""

# ----- untracked products for which Date_deref is not NAN = 13039
# = df[(df["Date_deref"].isna()==False) & (df.reference_id.isna())]

referenced_untracked = untracked[untracked["Date_deref"].isna()==False]

referenced_untracked = referenced_untracked[["EAN", "Libelle_Sous_Famille", "Article_Libelle_Long"]]


l_relevant = []

for l in range(referenced_untracked.shape[0]):
    ll = []
    for c in range(3):
        ll.append(referenced_untracked.iloc[l,c])
    l_relevant.append(ll)

print(len(l_relevant))


# ----- tracked products

tracked = df[df["reference_id"].isna()==False]

tracked = tracked[["EAN", "Libelle_Sous_Famille", "Article_Libelle_Long"]]
tracked.shape[0]  # 3225


# ----- untracked products for which Libelle Sous-Famille is tracked in at least one aisle

df2 = pd.merge(untracked, tracked, how="left", right_on="Libelle_Sous_Famille", left_on="Libelle_Sous_Famille")

df2.info()

df2 = df2[(df2.EAN_y.isna()==False)]

del df2["Date_deref"]
df2 = df2.drop_duplicates()

df2["Libelle_Sous_Famille"].unique().size  # 193
np.intersect1d(untracked["Libelle_Sous_Famille"], tracked["Libelle_Sous_Famille"]).size  # 193


lsf = list(df2["Libelle_Sous_Famille"].unique())
xx=[]
i=0
for l in range(df2.shape[0]):
    lx, ly = [], []
    if df2.iloc[l, 1] in lsf:
        i=i+1
        lx.append(df2.iloc[l, 0])
        lx.append(df2.iloc[l, 2])
        if lx not in xx:
            xx.append(lx)

        ly.append(df2.iloc[l, 3])
        ly.append(df2.iloc[l, 4])
        if ly not in xx:
            xx.append(ly)


df2[df2.Libelle_Sous_Famille=='BRIES'].drop_duplicates().iloc[0:20, 2:4]
df2[df2.Libelle_Sous_Famille=='BRIES'].iloc[0:20, 0:3]
df2[df2.Libelle_Sous_Famille=='BRIES'].head(5)
df2[df2.Libelle_Sous_Famille=='BRIES']["EAN_x"]
# -----

df2.drop_duplicates()

########## TOTAL SIZE OF RELEVANT PRODUCTS NOT TRACKED ##########


store_df[store_df.Libelle_Groupe_de_Famille=='CHARCUTERIE']


########## SUGGEST AN AISLE RELEVANT FOR PRODUCTS NOT TRACKED ##########