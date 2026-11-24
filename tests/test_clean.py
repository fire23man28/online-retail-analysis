import pandas as pd

from src.clean import clean_orders


def make_df(rows):
    return pd.DataFrame(
        rows,
        columns=["InvoiceNo", "StockCode", "Description", "Quantity",
                 "InvoiceDate", "UnitPrice", "CustomerID", "Country"],
    )


def test_duplicates_are_removed():
    row = ["536365", "85123A", "ITEM", 6, "2010-12-01", 2.55, 17850.0, "UK"]
    clean = clean_orders(make_df([row, row]))
    assert len(clean) == 1


def test_returns_are_flagged_not_removed():
    rows = [
        ["536365", "85123A", "ITEM", 6, "2010-12-01", 2.5, 17850.0, "UK"],
        ["C536379", "85123A", "ITEM", -6, "2010-12-01", 2.5, 17850.0, "UK"],
    ]
    clean = clean_orders(make_df(rows))
    assert len(clean) == 2
    assert clean["IsReturn"].tolist() == [False, True]
    assert clean.loc[clean["IsReturn"], "Revenue"].iloc[0] < 0


def test_zero_price_is_removed():
    row = ["536365", "85123A", "ITEM", 6, "2010-12-01", 0.0, 17850.0, "UK"]
    clean = clean_orders(make_df([row]))
    assert len(clean) == 0