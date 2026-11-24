import pandas as pd

df = pd.read_csv("data/processed/clean_orders.csv", parse_dates=["InvoiceDate"])
sales = df[~df["IsReturn"]]  # ventes brutes, sans retours

# Frais et ajustements qui ne sont pas des articles vendus
NON_PRODUCTS = ["POSTAGE", "DOTCOM POSTAGE", "Manual", "BANK CHARGES", "AMAZON FEE"]
products = sales[~sales["Description"].isin(NON_PRODUCTS)]

# 1. Top 10 produits (articles réels uniquement)
top_products = (
    products.groupby("Description")["Revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

# 2. Chiffre d'affaires par pays
by_country = (
    sales.groupby("Country")["Revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

# 3. Évolution mensuelle (décembre 2011 est partiel : données jusqu'au 9 décembre)
monthly = sales.set_index("InvoiceDate")["Revenue"].resample("ME").sum()

# 4. Top 10 clients (seulement ceux qui ont un identifiant)
known = sales[sales["CustomerID"].notna()]
top_customers = (
    known.groupby("CustomerID")["Revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

if __name__ == "__main__":
    print("\nTop 10 produits:\n", top_products.round(2).to_string())
    print("\nCA par pays (top 10):\n", by_country.round(2).to_string())
    print("\nCA mensuel:\n", monthly.round(2).to_string())
    print("\nTop 10 clients:\n", top_customers.round(2).to_string())