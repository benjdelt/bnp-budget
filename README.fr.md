[English](./README.md)

# BNP Paribas Fortis Budget

Un script Python qui, depuis un fichier CSV reprenant des transactions bancaires exportées depuis l'application PC
Banking de BNP Paribas Fortis, produit une série de graphiques représentant les revenus, dépenses et soldes mensuels et 
trimestriels. Le script affiche également ces données sur le terminal (STDOUT)

## Installation et utilisation

- Assurez-vous que Python (>=3.10.0) et Pip (>=21.2.3) sont installés.
- Clonez le dépôt et allez à sa racine
- Créez un environnment virtuel avec venv en suivant [ces instructions](https://docs.python.org/fr/3/library/venv.html).
- Installez les dépendances logicielles
```
pip install -r requirements.txt
```
- Lancez le script.
```
python script.py
```
Les graphiques générés s'ouvrent automatiquement et sont sauvegardés sous forme de fichiers png ignorés par Git.

### Dépendances logicielles

- [Numpy](https://numpy.org/)
- [Matplotlib](https://matplotlib.org/)


