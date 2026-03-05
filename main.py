import streamlit as sl
import pandas as pd

path = r"C:\Users\cazal\OneDrive\Documents\FACULTATE\ANUL III\Sem 2 ASE\Pachete Software\proiect\PSW\data\listings.csv"
df=pd.read_csv(path)

sl.dataframe(df)



info = df.info()
type(info)
