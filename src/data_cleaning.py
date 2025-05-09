import pandas as pd

def load_data(file_path):
    return pd.read_excel(file_path)

def check_missing_values(df):
    return df.isnull().sum()

def check_duplicates(df):
    return df.duplicated().sum()

def clean_data(df):
    # Exemple de nettoyage : supprimer les doublons et les valeurs manquantes
    df = df.drop_duplicates()
    df = df.dropna()
    return df
