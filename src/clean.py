import pandas as pd


def load_raw(path="data/raw/Online Retail.xlsx"):
    return pd.read_excel(path)


def clean_orders(df):
    df = df.copy()

    # 1. Supprimer les doublons exacts
    df = df.drop_duplicates()

    # 2. Marquer les annulations au lieu de les supprimer
    df["IsReturn"] = df["InvoiceNo"].astype(str).str.startswith("C") | (df["Quantity"] < 0)

    # 3. Supprimer seulement les prix nuls ou négatifs
    df = df[df["UnitPrice"] > 0]

    # 4. Nettoyer le texte et ajouter le chiffre d'affaires
    df["Description"] = df["Description"].fillna("UNKNOWN").str.strip()
    df["Country"] = df["Country"].str.strip()
    df["Revenue"] = df["Quantity"] * df["UnitPrice"]

    return df.reset_index(drop=True)


def save_clean(df, path="data/processed/clean_orders.csv"):
    df.to_csv(path, index=False)


if __name__ == "__main__":
    raw = load_raw()
    clean = clean_orders(raw)
    print("Lignes avant :", len(raw))
    print("Lignes après :", len(clean))
    print("Chiffre d'affaires total :", round(clean["Revenue"].sum(), 2))
    print("CA brut :", round(clean.loc[~clean["IsReturn"], "Revenue"].sum(), 2))
    print("CA net :", round(clean["Revenue"].sum(), 2))
    print("Total des retours :", round(clean.loc[clean["IsReturn"], "Revenue"].sum(), 2))
    save_clean(clean)