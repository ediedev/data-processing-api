import pandas as pd
from io import StringIO

def clean_csv(file_content: bytes):
    # Convert bytes → string
    s = file_content.decode("utf-8")

    # Load into pandas
    df = pd.read_csv(StringIO(s))

    # Remove duplicates
    df = df.drop_duplicates()

    # Clean column names
    df.columns = [
        col.strip().lower().replace(" ", "_")
        for col in df.columns
    ]

    # Remove spaces in string values
    df = df.map(
        lambda x: x.strip() if isinstance(x, str) else x
    )

    # Fill missing values
    df = df.fillna("")

    return df
