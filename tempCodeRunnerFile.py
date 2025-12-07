import streamlit as st
import pickle


def recommend(movie):
    movies_index = movies_list[movies_list['title'] == movie].index[0]
    distances = similarity[movies_index]
    movies_list = sorted(
        list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies_list.iloc[i[0]].title)
    return recommended_movies

movies_list = pickle.load(open('movies.pkl' , 'rb'))
movies_list = movies_list['title'].values
print(movies_list)