import streamlit as st
import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt

# Titre de l'application
st.title('Application d\'Analyse de Sentiment')

# Interface utilisateur améliorée
st.sidebar.header("Options de l'Application")
st.sidebar.info("Utilisez les options ci-dessous pour filtrer et rechercher des commentaires.")

# Téléchargement de fichier
uploaded_file = st.file_uploader("Choisissez un fichier CSV", type="csv")

if uploaded_file is not None:
    # Lecture du fichier CSV
    df = pd.read_csv(uploaded_file)
    
    # Vérification de la colonne 'comment'
    if 'comment' in df.columns:
        # Fonction pour classifier le sentiment et calculer le pourcentage
        def classify_sentiment(text):
            analysis = TextBlob(text)
            polarity = analysis.sentiment.polarity
            if polarity > 0:
                sentiment = 'Positif'
            elif polarity == 0:
                sentiment = 'Neutre'
            else:
                sentiment = 'Négatif'
            percentage = abs(polarity) * 100
            return f"{sentiment} à {percentage:.2f}%"
        
        # Application de la fonction à la colonne 'comment'
        df['Sentiment'] = df['comment'].apply(classify_sentiment)
        
        # Filtrage des commentaires par sentiment
        sentiment_filter = st.sidebar.selectbox("Filtrer par sentiment", options=["Tous", "Positif", "Neutre", "Négatif"])
        if sentiment_filter != "Tous":
            df = df[df['Sentiment'].str.contains(sentiment_filter)]

        # Recherche de mots-clés
        keyword = st.sidebar.text_input("Rechercher un mot-clé")
        if keyword:
            df = df[df['comment'].str.contains(keyword, case=False)]

        # Affichage du dataframe
        st.write("Voici le dataframe avec l'analyse de sentiment :")
        st.dataframe(df)

        # Visualisation des données
        if not df.empty:
            st.write("Répartition des sentiments :")
            # Extraction des sentiments sans le pourcentage
            df['Sentiment_Category'] = df['Sentiment'].apply(lambda x: x.split()[0])
            sentiment_counts = df['Sentiment_Category'].value_counts()
            fig, ax = plt.subplots()
            sentiment_counts.plot(kind='bar', ax=ax)
            ax.set_title("Répartition des Sentiments")
            ax.set_xlabel("Sentiment")
            ax.set_ylabel("Nombre de Commentaires")
            st.pyplot(fig)

        # Exportation des résultats
        if not df.empty:
            st.write("Télécharger les résultats de l'analyse :")
            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="Télécharger en CSV",
                data=csv,
                file_name='sentiment_analysis_results.csv',
                mime='text/csv',
            )

    else:
        st.error("Le fichier CSV doit contenir une colonne 'comment'.")
else:
    st.info("Veuillez télécharger un fichier CSV.")
