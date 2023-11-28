import streamlit as st

import pandas as pd
import random

st.set_page_config(page_title="Random Facts", page_icon=":interrobang:", layout="wide")


facts=pd.read_csv("ws/Facts.csv")

def get_random_quote():
    return facts.sample(1)

# instead of importing the random library, I use the random library inside Pandas with the sample selection. It works in this situation. 

st.title("Pulp Fiction Quotes")
st.markdown("*Using Web Scrapping*")

#In this particular case as seen before, every time the user hits the button something will happen. If not, as there is not else, we can be there for hours. 

if st.button ("Find a Random Quote"):
    random_row=get_random_quote().iloc[0]
    st.markdown(f"## **{random_row['Quote']}**")
    st.markdown(random_row["Text"])
    st.image(random_row['Links'], use_column_width=True)