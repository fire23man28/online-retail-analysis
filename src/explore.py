import pandas as pd

df = pd.read_excel("data/raw/Online Retail.xlsx")

print("Forme (lignes, colonnes):", df.shape)
print("\nColonnes et types:")
print(df.dtypes)
print("\nTrois premières lignes:")
print(df.head(3).to_string())
print("\nValeurs manquantes par colonne:")
print(df.isna().sum())
print("\nLignes en double:", df.duplicated().sum())
print("\nPériode:", df["InvoiceDate"].min(), "->", df["InvoiceDate"].max())
print("\nPays, top 5:")
print(df["Country"].value_counts().head(5)) 