import pandas as pd
import numpy as np
import streamlit as sl

path = r"C:\Users\cazal\OneDrive\Documents\FACULTATE\ANUL III\Sem 2 ASE\Pachete Software\proiect\PSW\data\listings.csv"


def load_data(path: str) -> pd.DataFrame:
    return pd.read_csv(path)

def clean_listings(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # examples (replace with your real rules)
    df.columns = [c.strip().lower() for c in df.columns]
    df = df.drop_duplicates()

    # if you have price like "$1,200.00"
    if "price" in df.columns:
        df["price"] = (
            df["price"].astype(str)
            .str.replace(r"[\$,]", "", regex=True)
            .astype(float)
        )

    return df

df = load_data(path)
sl.dataframe(df)
df_clean = clean_listings(df)
sl.dataframe(df_clean)

sl.write(df.isnull().sum())

