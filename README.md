![Image application streamlit sentiment analysis](https://github.com/Lmssnlab/Streamlit_sentiment_analysis/blob/main/Capture%20d%E2%80%99e%CC%81cran%202024-06-23%20a%CC%80%2022.15.58.png)

# Application d'Analyse de Sentiment

## Description
Cette application Streamlit permet d'effectuer une analyse de sentiment sur des commentaires contenus dans un fichier CSV. Elle utilise la bibliothèque TextBlob pour l'analyse de sentiment et offre des fonctionnalités de visualisation et d'exportation des résultats.

## Fonctionnalités
- Chargement de fichiers CSV contenant des commentaires
- Analyse de sentiment des commentaires (Positif, Neutre, Négatif)
- Filtrage des commentaires par sentiment
- Recherche de mots-clés dans les commentaires
- Visualisation graphique de la répartition des sentiments
- Exportation des résultats en format CSV

## Installation

### Prérequis
- Python 3.7+
- pip

### Étapes d'installation
1. Clonez ce dépôt : (git clone)[https://github.com/Lmssnlab/Streamlit_sentiment_analysis.git]


2. Installez les dépendances :
pip install -r requirements.txt

## Utilisation
1. Lancez l'application :

streamlit run app.py

2. Ouvrez votre navigateur et accédez à l'URL indiquée (généralement http://localhost:8501)

3. Utilisez l'interface pour charger un fichier CSV, analyser les sentiments et explorer les résultats

## Structure du fichier CSV
Le fichier CSV doit contenir une colonne nommée 'comment' contenant les commentaires à analyser.

Exemple :

comment
"This is a great product!"
"I am not satisfied with the service."
"The experience was average."

## Contribution
Les contributions à ce projet sont les bienvenues. N'hésitez pas à ouvrir une issue ou à soumettre une pull request.

