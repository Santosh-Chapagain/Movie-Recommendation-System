import streamlit as st
import pickle

# Load Data
movies_df = pickle.load(open('movies.pkl', 'rb'))
movies_list = movies_df['title'].values

similarity = pickle.load(open('similarity.pkl', 'rb'))

# Recommend Function


def recommend(movie):
    # 1. Find index of selected movie
    movie_index = movies_df[movies_df['title'] == movie].index[0]

    # 2. Get similarity distances
    distances = similarity[movie_index]

    # 3. Sort movies by similarity score
    movies_with_distance = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]  # skip first (same movie)

    # 4. Collect recommended movie titles
    recommended_movies = []
    for i, _ in movies_with_distance:
        recommended_movies.append(movies_df.iloc[i].title)

    return recommended_movies


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
        recommendations = recommend(select_movie_name)
        st.subheader("Recommended Movies:")
        for movie in recommendations:
            st.write(movie)
    else:
        st.warning("Please select a movie first!")
