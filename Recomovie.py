import streamlit as st
import requests
import pandas as pd
import numpy as np

# Vamsi's code starts here
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
  #Vanya's code starts here
  st.subheader("Box office performance over the first week (in millions)")
  movie1_data = {'Sonic the Hedgehog 2': [226.3, 26.8, 18.8, 4.3, 5.0, 3.6, 4.4]}
  chart_data = pd.DataFrame(movie1_data, index=['Day 1', 'Day 2', 'Day 3', 'Day 4', 'Day 5', 'Day 6', 'Day 7'])
  st.line_chart(chart_data)
  #Vanya's code ends here

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
  #Vanya's code starts here
  st.subheader("Box office performance over the first week (in millions)")
  movie2_data = {'Morbius':[17.3,13.1,8.5,2.1,2.7,1.6,1.3]}
  chart_data = pd.DataFrame(movie2_data, index=['Day 1', 'Day 2', 'Day 3', 'Day 4', 'Day 5', 'Day 6', 'Day 7'])
  st.line_chart(chart_data)
  #Vanya's code ends here

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
  #Vanya's code starts here
  st.subheader("Box office performance over the first week (in millions)")
  movie3_data = {'The Lost City':[2.0,0.91,0.74,0.96,0.74,2.2,4.1]}
  chart_data = pd.DataFrame(movie3_data, index=['Day 1', 'Day 2', 'Day 3', 'Day 4', 'Day 5', 'Day 6', 'Day 7'])
  st.line_chart(chart_data)
  #Vanya's code ends here

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
  #Vanya's code starts here
  st.subheader("Box office performance over the first week (in millions)")
  movie4_data = {'Ambulance':[56.6,43.2,34.1,10.8,10.7,8.4,8.4]}
  chart_data = pd.DataFrame(movie4_data, index=['Day 1', 'Day 2', 'Day 3', 'Day 4', 'Day 5', 'Day 6', 'Day 7'])
  st.line_chart(chart_data)
  #Vanya's code ends here

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
  #Vanya's code starts here
  st.subheader("Box office performance over the first week (in millions)")
  movie5_data = {'The Batman':[3.2,3.3,2.1,0.72,0.92,0.63,1.3]}
  chart_data = pd.DataFrame(movie5_data, index=['Day 1', 'Day 2', 'Day 3', 'Day 4', 'Day 5', 'Day 6', 'Day 7'])
  st.line_chart(chart_data)
  #Vanya's code ends here
# Vamsi's code ends here

# Charlie's code starts here
theatres_map = st.checkbox("See theatres near FIU")
if theatres_map:
    map_data = pd.DataFrame(
      np.array([
              [25.751513, -80.389932],
              [25.790486, -80.380745],
              [25.809388, -80.332901],
              [25.691108, -80.391781],
              [25.648025, -80.338955],
              [25.707588, -80.285397],
              [25.736138, -80.241658],
              [25.785799, -80.131087],
              [25.650725, -80.340989],
              [25.581568, -80.365570],
              [25.698084, -80.392521],
              [25.691941, -80.395018],
              [25.783171, -80.263755]]),
    columns=['lat','lon'])
    st.map(map_data)
# Charlie's code ends here
  
# Ted's code starts here
agree = st.checkbox('Feedback')

if agree:

    st.subheader("Feedback")
    odd_Number = st.slider('Select your interest level in the movie: (with 5 being the highest)', 0, 5, 0)
    st.write("From 1 - 5, the likelihood of me going to watch this movie is a: ", odd_Number)

    if odd_Number < 3:
        odd = st.error("Not interested.")
    elif odd_Number == 3:
        odd = st.warning("Maybe?")
    elif odd_Number >= 3:
        odd = st.success("Heck yeah, I'm going!")

    Playa = st.radio(
        "Who will be accompanying you?",
        ('', 'Date', 'Friend', 'Solo'))

    if Playa == 'Date':
        st.write('Playa Playa!!!')
    elif Playa == 'Friend':
        st.write("We going Dutch!!!")
    elif Playa == 'Solo':
        st.write("More popcorn for me!!!")

budget = st.checkbox('Select a budget')

if budget:
    number = st.number_input("What's your budget?", min_value=1, max_value=100, value=1, step=1)
    st.write('Budget: $', number)
    if number <= 20:
        st.write("That's cold.")
        st.snow()
    elif 20 < number < 50:
        st.write("We can work with that.")
    elif number >= 50:
        st.write("Ballin'!!!")
        st.balloons()
# Ted's code ends here
