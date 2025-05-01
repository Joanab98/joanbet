import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Fonction pour obtenir les prochains matchs de l'équipe (données fictives ici)
def get_next_matches(team_name):
    # Pour l'instant, on utilise des données fictives, tu devras remplacer par un appel API pour des données réelles
    return [
        {'team': team_name, 'opponent': 'Team A', 'date': '2025-05-05', 'home': True},
        {'team': team_name, 'opponent': 'Team B', 'date': '2025-05-10', 'home': False},
        {'team': team_name, 'opponent': 'Team C', 'date': '2025-05-15', 'home': True},
    ]

# Fonction pour obtenir les derniers matchs de l'équipe
def get_last_matches(team_name):
    return [
        {'date': '2025-04-25', 'score': '2-1', 'home': True, 'goals_scored': 2, 'goals_conceded': 1},
        {'date': '2025-04-20', 'score': '0-0', 'home': False, 'goals_scored': 0, 'goals_conceded': 0},
        {'date': '2025-04-15', 'score': '1-3', 'home': True, 'goals_scored': 1, 'goals_conceded': 3},
        {'date': '2025-04-10', 'score': '2-2', 'home': False, 'goals_scored': 2, 'goals_conceded': 2},
        {'date': '2025-04-05', 'score': '3-1', 'home': True, 'goals_scored': 3, 'goals_conceded': 1},
    ]

# Fonction pour obtenir les probabilités de buts (en fonction des performances récentes)
def get_goal_probabilities(team_name):
    # Probabilité fictive des buts (remplace par une logique basée sur l'API ou les données réelles)
    return {
        "1st_half": [0.1, 0.25, 0.5, 0.75, 0.9],
        "2nd_half": [0.05, 0.2, 0.45, 0.7, 0.85],
        "full_game": [0.15, 0.3, 0.6, 0.8, 0.95]
    }

# Fonction pour obtenir les cotes des bookmakers (données fictives ici)
def get_bookmaker_odds(team_name, opponent):
    return {
        "1x2": {"win": 2.5, "draw": 3.0, "lose": 2.8},
        "over_under": {"over_2.5": 1.8, "under_2.5": 2.0},
    }

# Fonction pour afficher les prochains matchs
def display_next_matches(team_name):
    matches = get_next_matches(team_name)
    st.write(f"### Prochains matchs de {team_name}")
    for match in matches:
        st.write(f"Date : {match['date']} | Adversaire : {match['opponent']} | Lieu : {'Domicile' if match['home'] else 'Extérieur'}")

# Fonction pour afficher les derniers matchs
def display_last_matches(team_name):
    matches = get_last_matches(team_name)
    st.write(f"### Derniers matchs de {team_name}")
    for match in matches:
        st.write(f"Date : {match['date']} | Score : {match['score']} | {'Domicile' if match['home'] else 'Extérieur'}")

# Fonction pour afficher les cotes des bookmakers
def display_bookmaker_odds(team_name, opponent):
    odds = get_bookmaker_odds(team_name, opponent)
    st.write(f"### Cotes des bookmakers pour {team_name} vs {opponent}")
    st.write(f"Victoire de {team_name}: {odds['1x2']['win']}")
    st.write(f"Match nul: {odds['1x2']['draw']}")
    st.write(f"Victoire de {opponent}: {odds['1x2']['lose']}")
    st.write(f"Plus de 2,5 buts: {odds['over_under']['over_2.5']}")
    st.write(f"Moins de 2,5 buts: {odds['over_under']['under_2.5']}")

# Fonction pour afficher les probabilités de buts
def display_goal_probabilities(team_name):
    probabilities = get_goal_probabilities(team_name)
    st.write(f"### Probabilités de buts pour {team_name}")
    st.write(f"1ère mi-temps : {probabilities['1st_half']}")
    st.write(f"2ème mi-temps : {probabilities['2nd_half']}")
    st.write(f"Match entier : {probabilities['full_game']}")

# Fonction pour afficher une analyse de l'équipe
def display_analysis(team_name):
    st.write(f"### Analyse de {team_name}")
    st.write("Analyse des résultats récents, tendances de performance...")

# Fonction pour générer un graphique des performances
def generate_performance_graph(team_name):
    # Graphique fictif de la forme de l’équipe
    data = {'dates': ['2025-04-05', '2025-04-10', '2025-04-15', '2025-04-20', '2025-04-25'],
            'goals_scored': [3, 2, 1, 0, 2],
            'goals_conceded': [1, 2, 3, 0, 1]}
    df = pd.DataFrame(data)
    
    fig, ax = plt.subplots()
    ax.plot(df['dates'], df['goals_scored'], label="Buts marqués", color='green', marker='o')
    ax.plot(df['dates'], df['goals_conceded'], label="Buts encaissés", color='red', marker='o')
    
    ax.set_xlabel('Date')
    ax.set_ylabel('Buts')
    ax.set_title(f'Performances récentes de {team_name}')
    ax.legend()
    
    st.pyplot(fig)

# Interface utilisateur
st.title("JOAN'BET - Assistant pour Paris Sportifs")

team_name = st.text_input("Entrez le nom de l'équipe :")

if team_name:
    display_next_matches(team_name)
    display_last_matches(team_name)
    display_analysis(team_name)
    generate_performance_graph(team_name)

    opponent = st.text_input("Entrez le nom de l'adversaire :")
    if opponent:
        display_bookmaker_odds(team_name, opponent)
        display_goal_probabilities(team_name)
