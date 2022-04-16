import streamlit as st
import requests

# Vamsi code starts here

st.set_page_config(
    page_title="Recomovie",
    page_icon="🍿",
    layout="wide",
    menu_items={
        'Get Help' : 'https://docs.streamlit.io/',
        'Report a bug' : 'https://www.streamlit.io',
        'About' : 'Created by Ted Atis, Vanya Farzamipour, Vamsi Kanneganti and Charlie Peralta.'
    }
)
st.title("Recomovie | Weekly Movie Recommendations")

st.subheader("Pick a movie currently out in theaters to learn more about!")
option = st.selectbox("Select one:", ["", "Sonic the Hedgehog 2", "Morbius", "The Lost City", "Ambulance", "The Batman"])

if option == "Sonic the Hedgehog 2":
  movie1_url = "https://imdb-api.com/en/API/Title/k_ahbc2za3/tt12412888"
  movie_info = requests.get(movie1_url).json()
  st.info(movie_info["plot"])
  with st.expander("Official Trailer:", expanded=True):
    st.video("https://youtu.be/G5kzUpWAusI", format="video")
  genres, contentRating, runtime = st.columns(3)
  genres.metric("Genres", movie_info["genres"])
  contentRating.metric("Content Rating", movie_info["contentRating"])
  runtime.metric("Run Time", movie_info["runtimeStr"])
  scoreRT, scoreIMDb, scoreMC = st.columns(3)
  scoreRT.metric("Rotten Tomatoes Score", "69%")
  scoreIMDb.metric("IMDb Score", movie_info["imDbRating"])
  scoreMC.metric("Metacritic Score", movie_info["metacriticRating"])

elif option == "Morbius":
  movie2_url = "https://imdb-api.com/en/API/Title/k_ahbc2za3/tt5108870"
  movie_info = requests.get(movie2_url).json()
  st.info(movie_info["plot"])
  with st.expander("Official Trailer:", expanded=True):
    st.video("https://www.youtube.com/watch?v=oZ6iiRrz1SY", format="video")
  genres, contentRating, runtime = st.columns(3)
  genres.metric("Genres", movie_info["genres"])
  contentRating.metric("Content Rating", movie_info["contentRating"])
  runtime.metric("Run Time", movie_info["runtimeStr"])
  scoreRT, scoreIMDb, scoreMC = st.columns(3)
  scoreRT.metric("Rotten Tomatoes Score", "16%")
  scoreIMDb.metric("IMDb Score", movie_info["imDbRating"])
  scoreMC.metric("Metacritic Score", movie_info["metacriticRating"])

elif option == "The Lost City":
  movie3_url = "https://imdb-api.com/en/API/Title/k_ahbc2za3/tt13320622"
  movie_info = requests.get(movie3_url).json()
  st.info(movie_info["plot"])
  with st.expander("Official Trailer:", expanded=True):
      st.video("https://www.youtube.com/watch?v=nfKO9rYDmE8", format="video")
  genres, contentRating, runtime = st.columns(3)
  genres.metric("Genres", movie_info["genres"])
  contentRating.metric("Content Rating", movie_info["contentRating"])
  runtime.metric("Run Time", movie_info["runtimeStr"])
  scoreRT, scoreIMDb, scoreMC = st.columns(3)
  scoreRT.metric("Rotten Tomatoes Score", "76%")
  scoreIMDb.metric("IMDb Score", movie_info["imDbRating"])
  scoreMC.metric("Metacritic Score", movie_info["metacriticRating"])

elif option == "Ambulance":
  movie4_url = "https://imdb-api.com/en/API/Title/k_ahbc2za3/tt4998632"
  movie_info = requests.get(movie4_url).json()
  st.info(movie_info["plot"])
  with st.expander("Official Trailer:", expanded=True):
      st.video("https://www.youtube.com/watch?v=7NU-STboFeI", format="video")
  genres, contentRating, runtime = st.columns(3)
  genres.metric("Genres", movie_info["genres"])
  contentRating.metric("Content Rating", movie_info["contentRating"])
  runtime.metric("Run Time", movie_info["runtimeStr"])
  scoreRT, scoreIMDb, scoreMC = st.columns(3)
  scoreRT.metric("Rotten Tomatoes Score", "70%")
  scoreIMDb.metric("IMDb Score", movie_info["imDbRating"])
  scoreMC.metric("Metacritic Score", movie_info["metacriticRating"])

elif option == "The Batman":
  movie5_url = "https://imdb-api.com/en/API/Title/k_ahbc2za3/tt1877830"
  movie_info = requests.get(movie5_url).json()
  st.info(movie_info["plot"])
  with st.expander("Official Trailer:", expanded=True):
      st.video("https://www.youtube.com/watch?v=mqqft2x_Aa4", format="video")
  genres, contentRating, runtime = st.columns(3)
  genres.metric("Genres", movie_info["genres"])
  contentRating.metric("Content Rating", movie_info["contentRating"])
  runtime.metric("Run Time", movie_info["runtimeStr"])
  scoreRT, scoreIMDb, scoreMC = st.columns(3)
  scoreRT.metric("Rotten Tomatoes Score", "85%")
  scoreIMDb.metric("IMDb Score", movie_info["imDbRating"])
  scoreMC.metric("Metacritic Score", movie_info["metacriticRating"])

# Vamsi code ends here