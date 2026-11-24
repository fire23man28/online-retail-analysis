# online-retail-analysis

![CI](https://github.com/fire23man28/online-retail-analysis/actions/workflows/ci.yml/badge.svg)

Analyse exploratoire et nettoyage des ventes d'un détaillant en ligne britannique (novembre 2010 à décembre 2011), à partir du jeu de données **Online Retail** de l'UCI Machine Learning Repository.

Source : https://archive.ics.uci.edu/dataset/352/online-retail

## Structure

```
src/
  clean.py      Chargement, nettoyage et sauvegarde des données
  analysis.py   Calcul des indicateurs (top produits, pays, mois, clients)
  charts.py     Graphique du chiffre d'affaires mensuel
  explore.py    Exploration initiale des données brutes
tests/
  test_clean.py Tests unitaires de la fonction de nettoyage
reports/
  monthly_revenue.png
```

## Installation

```bash
pip install pandas openpyxl matplotlib pytest ruff
```

## Utilisation

1. Télécharge `Online Retail.xlsx` depuis la source ci-dessus et place-le dans `data/raw/`. Le fichier n'est pas versionné (voir `.gitignore`).
2. Nettoie les données :
   ```bash
   python src/clean.py
   ```
3. Calcule les indicateurs et génère le graphique :
   ```bash
   python src/analysis.py
   python src/charts.py
   ```
4. Lance les tests et le linter :
   ```bash
   pytest
   ruff check .
   ```

## Choix de nettoyage

- Les doublons exacts sont supprimés (5 268 lignes dans les données brutes).
- Les lignes avec un prix unitaire nul ou négatif sont supprimées.
- Les retours (factures commençant par `C` ou quantité négative) sont **conservés** et marqués par la colonne `IsReturn`. Le chiffre d'affaires net en tient compte.
- Le `CustomerID` manquant (environ 25 % des lignes) n'est pas imputé. Ces lignes sont gardées, mais exclues de l'analyse par client.
- `Revenue = Quantity × UnitPrice`.

Résultat : 541 909 lignes brutes, 534 129 lignes après nettoyage.

## Résultats principaux

| Indicateur | Valeur |
|---|---|
| Chiffre d'affaires brut | 10 642 110,80 £ |
| Chiffre d'affaires net (après retours) | 9 748 131,07 £ |
| Montant des retours | ≈ 893 980 £ |
| Pays principal (Royaume-Uni), CA brut | 9 001 744,09 £ |
| Meilleur client (ID 14646.0) | 280 206,02 £ |

Mois de pic : novembre 2011 avec environ 1 503 867 £. Décembre 2011 est partiel (données jusqu'au 9 décembre).

## Limites

- **Décembre 2011 est incomplet** : les comparaisons mensuelles doivent en tenir compte.
- **Un gros achat fausse le classement produit.** « PAPER CRAFT , LITTLE BIRDIE » (168 470 £) correspond à une commande en gros unique. Il ne doit pas être présenté comme un best-seller récurrent sans vérification.
- **Les frais (port, frais bancaires, « Manual », « Amazon fee ») sont exclus** du classement des produits.
- **Environ 25 % des lignes n'ont pas de client identifié**, ce qui limite les analyses par client.