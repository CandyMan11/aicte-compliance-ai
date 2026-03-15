import pandas as pd


def load_questions(path: str):
    """
    Load compliance questions from Excel file
    """

    df = pd.read_excel(path)

    # remove completely empty rows
    df = df.dropna(how="all")

    # replace NaN values
    df = df.fillna("")

    return df