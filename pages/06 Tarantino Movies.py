import streamlit as st
import pandas as pd
import requests


# Our main goal in this page is to create a direct connection with the Free API of OMDB 
st.set_page_config(page_title="Tarantino Movies", page_icon=":film_frames:", layout="wide")
# Here are all the titles of Tarantino Movies. OMDB is free but can not filter for director, so I had to do it manually. For every problem there is a solution!
titles=["Once Upon a Time in Hollywood", "Pulp Fiction", "Jackie Brown", "The Hateful Eight", "Kill Bill: Vol. 1", "Kill Bill: Vol. 2", "Reservoir Dogs", "Django Unchained", "Inglourious Basterds", "Death Proof"]
key="e77bc4c9"
# Function to get movie details from the OMDb API. 
def get_movie_details(key, title):
    url = f"http://www.omdbapi.com/?apikey={key}&t={title}"
    response = requests.get(url)
    return response.json()

st.title("Tarantino Movies")
st.markdown("*Information obtained using OMDB API*")

# I think Sidebar works perfectly in this particular situation so you can see every movie independently from the rest in the main page. 
# In the last example I used radio (a list of options, all displayed) while here I opted for a Selectbox
selected_movie = st.sidebar.selectbox('Select a movie', titles)

# Get movie details from the OMDb API
movie_details = get_movie_details(key, selected_movie)
col1, col2=st.columns(2)
# There is not infinite information but is not bad. As there is also a cool Poster photo, I decidied to divide it into two columns: One per text and the other one for the poster
col1.subheader(movie_details['Title'])
col1.write(f"**Year:** {movie_details['Year']}")
col1.write(f"**Runtime:** {movie_details['Runtime']}")
col1.write(f"**Actors:** {movie_details['Actors']}")
col1.write(f"**Plot:** {movie_details['Plot']}")
col1.write(f"**Box Office:** {movie_details['BoxOffice']}")
col1.write(f"**Awards:** {movie_details['Awards']}")
col1.markdown("## Ratings")
col1.write(f"**IMDB Rating:** {movie_details['imdbRating']}")
col1.write(f"**Rotten Tomatoes Rating:** {movie_details['Ratings'][1]['Value']}")

# As you can see, the use_column_width is really useful. And streamlit is cool. Pedro the variable has no idea. 
col2.image(movie_details['Poster'], caption='Movie Poster', use_column_width=True)
