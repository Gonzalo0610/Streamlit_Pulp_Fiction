import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.metrics import accuracy_score
import src.load_data as ld

# Naive Bayes Classification Model: Depending on your input, it repplies with a prediction of "who could have say it". It works meh, still working on it. But the concept is clear.


df = ld.load()

X_train, X_test, y_train, y_test = train_test_split(df['Line'], df['Character'], test_size=0.2, random_state=42)
model = make_pipeline(CountVectorizer(), MultinomialNB())
model.fit(X_train, y_train)

st.title('Character Imitator')
st.markdown("*Using the Naive Bayes Classification Model, enter a sentence to know which character could say it*")

user_input=st.text_input('', 'This is a test sentence.')

# Jules: AND MY NAME IS THE LORD
# Pumpkin: Shut up Honey Bunny
# hi vs hey
# Mia: Let's dance
# Vincent: It was an accident

if st.button('Predict Character'):
    prediction = model.predict([user_input])[0]
    st.success(f'The model predicts that "{user_input}" might be said by: {prediction}')
