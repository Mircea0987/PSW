import streamlit as sl
import pandas as pd

path = r"..\data\student.csv"
df=pd.read_csv(path)

sl.dataframe(df)



info = df.info()
type(info)
