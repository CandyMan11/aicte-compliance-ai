import pandas as pd

def load_questions(path):
    df = pd.read_excel(path)
    df = df.dropna(how="all")
    df = df.fillna("")
    return df