import streamlit as st
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import src.load_data as ld
import numpy as np

df = ld.load()

st.set_page_config(page_title="WordCloud", page_icon=":movie_camera:", layout="wide")

st.title("Word Cloud Generator")

st.header("Select a Character")

# Selectbox to select ANY character you want
characters = df["Character"].unique()
characters=np.insert(characters, 0, "All Characters") #with this, i can insert the "All Characters" in the first poistion. 
selected_character = st.selectbox(" ", characters)

# The variable lines depends on your selectbox selection. As it is very user friendly, you can change it as many times you want as a user and with no complications in the code!
if selected_character == "All Characters":
    lines = df["Line"]
else:
    lines = df[df["Character"] == selected_character]["Line"]

#join every line related with each character to form a text where we can obtain a Wordcloud from. you can change the shape and the color, or use STOPWORDS (REALLY useful)
text = " ".join(lines)

# Create a WordCloud
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)

st.image(wordcloud.to_array(), use_column_width=True)