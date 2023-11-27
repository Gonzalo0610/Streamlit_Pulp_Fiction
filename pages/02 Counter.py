import streamlit as st
import pandas as pd
import src.load_data as ld

df = ld.load()
#we are using the same df from the page 01. Sometimes is better to save functions to avoid mixing up and repetitions, see?
st.set_page_config(page_title="Word Count", page_icon=":cinema:", layout="wide")

st.title("Word Frequency Counter")

st.header("And its Script information")
#there are a lot of inputs from the user, from Text to Dataframes and images. Use it wisely in your project!
word_to_search = st.text_input("Enter a word:")

# Count the number of times the word appears in the "Line" column. That is the script!

if word_to_search: #That is aboolean, a TRUE. In the case there is no word (False), a GIF will appear
    word_to_search_lower = word_to_search.lower()  # LOWERCASE! Justincase
    word_count = df["Line"].str.lower().str.count(word_to_search_lower).sum()
    st.write(f'The word "{word_to_search}" appears {word_count} times in the Script.')

    #I also want to know exactly in which part of the script the word is, using a string contains method from pandas.
    filtered_df = df[df["Line"].str.lower().str.contains(word_to_search_lower)]
    st.write(filtered_df)
else: 
    st.image("images/dancegif.gif")