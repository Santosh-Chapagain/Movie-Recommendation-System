import streamlit as st
import pickle
import requests

from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("TMDB_API_KEY")

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"
    data = requests.get(url).json()

    poster_path = data.get("poster_path")
    if poster_path:
        return "https://image.tmdb.org/t/p/w500" + poster_path
    else:
        return "https://via.placeholder.com/500x750?text=No+Image"

# Load Data
movies_df = pickle.load(open('movies.pkl', 'rb'))
movies_list = movies_df['title'].values

similarity = pickle.load(open('similarity.pkl', 'rb'))

# Recommend Function


def recommend(movie):
    movie_index = movies_df[movies_df['title'] == movie].index[0]
    distances = similarity[movie_index]

    movies_with_distance = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movies = []
    recommended_movies_posters = []

    for i, _ in movies_with_distance:

        movie_id = movies_df.iloc[i].movie_id  

        recommended_movies.append(movies_df.iloc[i].title)
        recommended_movies_posters.append(fetch_poster(movie_id))

    return recommended_movies, recommended_movies_posters



# Streamlit UI
st.title("🎬 Movie Recommender System")

select_movie_name = st.selectbox(
    "Which movie do you want to select?",
    movies_list,
    index=None,
    placeholder="Select a movie...",
)

if st.button("Recommend"):
    if select_movie_name is not None:
        names , posters = recommend(select_movie_name)
        st.subheader("Recommended Movies:")
        

        col1, col2, col3, col4, col5= st.columns(5)

        with col1:
            st.caption(names[0])
            st.image(posters[0])

        with col2:
            st.caption(names[1])
            st.image(posters[1])

        with col3:
            st.caption(names[2])
            st.image(posters[2])
        with col4:
            st.caption(names[3])
            st.image(posters[3])
        with col5:
            st.caption(names[4])
            st.image(posters[4])
