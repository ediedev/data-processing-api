import pandas as pd
from io import StringIO

def clean_csv(file_content: bytes):
    # Convert bytes → string
    s = file_content.decode("utf-8")

    # Load into pandas
    df = pd.read_csv(StringIO(s))

    # BASIC CLEANING
    df = df.drop_duplicates()
    df.columns = [col.strip().lower() for col in df.columns]

    # Fill missing values (simple strategy)
    df = df.fillna("")

    return df
