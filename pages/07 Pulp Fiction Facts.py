import streamlit as st
from bs4 import BeautifulSoup
import requests
url="https://www.yardbarker.com/entertainment/articles/20_facts_you_might_not_know_about_pulp_fiction_112123/s1__35170955#slide_15"
response=requests.get(url)
soup=BeautifulSoup(response.content, "html.parser")
import pandas as pd
import random

st.set_page_config(page_title="Random Facts", page_icon=":interrobang:", layout="wide")

# WEB SCRAPPING
#I personally DONT RECOMMEND what i am doing here: As you may know, some pages may change.
# Pro Tip: Do the Web Scrapping, export it to a CSV and import it again with pandas. I am not doing it because I am sweet but a Psycho. 

title=soup.find_all("h2")[1:]
explan=soup.find_all("p")[1:21]
images=soup.find_all("img")[15:35]
links=[]
for i in images:
    try:
        links.append(i["src"])
    except:
        links.append(i["data-src"])  

# SOME ERROR HANDLING HERE: It was complicated to extract the links for the images that I will use for each film, so instead of copypasting them one by one as a uxui i mean as a rookie, I observed that the pattern was clear: src or data-src. Try and Except and it is done!

quote=[]
for i in title:
    quote.append(i.text)

text=[]
for i in explan:
    text.append(i.text)

facts=pd.DataFrame({"Quote":quote, 
                   "Text": text,
                   "Links":links})

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