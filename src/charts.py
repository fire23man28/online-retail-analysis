import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("data/processed/clean_orders.csv", parse_dates=["InvoiceDate"])
sales = df[~df["IsReturn"]]

monthly = sales.set_index("InvoiceDate")["Revenue"].resample("ME").sum()

labels = [d.strftime("%b %Y") for d in monthly.index]

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(range(len(monthly)), monthly.values, marker="o", color="#2563EB")
ax.set_xticks(range(len(monthly)))
ax.set_xticklabels(labels, rotation=45, ha="right")
ax.set_title("Chiffre d'affaires brut par mois (déc. 2011 partiel : données jusqu'au 9)")
ax.set_ylabel("£")
ax.grid(alpha=0.3)
fig.tight_layout()
fig.savefig("reports/monthly_revenue.png", dpi=150)
print("Graphique sauvegardé dans reports/monthly_revenue.png")