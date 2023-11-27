import streamlit as st
import src.load_data as ld

st.set_page_config(page_title="The Script", page_icon=":clapper:", layout="wide")
# 1. Show the data of the dataframe already transformed in the load_data.py, with a Sentiment Analysis column
st.write("# The full script!")
st.dataframe(ld.load())