import streamlit as st
from PIL import Image
import streamlit.components.v1 as components
import codecs

# In every page I will set a different page_title with a new icon, while in this first I will do a couple of different things:The Get Help will have a link to the Filmaffinity page, and in the "About" Section there will be quoted the mytical Jules biblical sentence.
# Apart from the text, you can add emojis between ":". The complete list is here: https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/
st.set_page_config(
     page_title="Pulp Fiction",
     page_icon=":octopus:",
     layout="wide",
     initial_sidebar_state="expanded",
     menu_items={
         'Get help': "https://www.filmaffinity.com/es/film160882.html",
         'About': "*Ezequiel 25:17*. The path of the righteous man is beset on all sides by the inequities of the selfish and the tyranny of evil men. Blessed is he who, in the name of charity and good will, shepherds the weak through the valley of the darkness. For he is truly his brother's keeper and the finder of lost children. And I will strike down upon thee with great vengeance and furious anger those who attempt to poison and destroy my brothers. And you will know I am the Lord when I lay my vengeance upon you."
     }
 )

#title, header,  markdown, write... Lots of ways of putting your text together. With the Markdown you have the same functionalities as a Markdown in Tableau: # for the titles, ** for bolds and * for cursives. 
st.title("Pulp Fiction")

st.header("The Movie Analysis")


# To make it pretty, all the images are saved in a "image" folder inside my github repository. It really makes everything more scalable without making it too messy. 
cover = Image.open("images/pf.jpg")

#use_column_width really useful for having control over the size of your images. 
st.image(cover, use_column_width=True)
# If I don`t use the "st.", NOTHING will be shown. Although it is useful for saving variables and calculate a bunch of stuff (really useful if you want to import functions and libraries or use Machine Learning in you code)
movie_info = {
    "Title": "Pulp Fiction",
    "Director": "Quentin Tarantino",
    "Duration": "154 minutes",
    "Actors": "John Travolta, Samuel L. Jackson, Uma Thurman, Bruce Willis",
}

synopsis = """
"Pulp Fiction" is a 1994 crime film written and directed by Quentin Tarantino. 
The film weaves together multiple interconnected stories involving two hitmen, 
a boxer, a gangster's wife, and a pair of small-time criminals. 
It is known for its non-linear narrative, sharp dialogue, and iconic characters.
"""

# Columns: A way of splitting equally your text. You can have as much as you want (sin fliparse tampoco)
col1, col2 = st.columns(2)

# Left Column for the movie information
col1.subheader("**General Information**")
for key, value in movie_info.items():
    col1.write(f"**{key}:** {value}")

# Right column for the movie synopsis
col2.subheader("*Movie Synopsis*")
col2.write(synopsis)

# https://youtubeembedcode.com/es/
# Replicate this code (using also the html in the data folder) if you want to embed a youtube video inside your App. Useful
f=codecs.open("data/youtube.html", 'r')
pedro = f.read()
# Pedro was a nice guy until he told me that Streamlit was terrible. Now he is a variable, unable to broke more hearts. 
components.html(pedro,height=550,scrolling=True)

#to execute your code and generate and app in your localhost, you just need to open a terminal using the path of the repository and execute "streamlit run main.py". main.py corresponds to the name of my main, but you have to change it for the name you will like!