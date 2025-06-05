import streamlit as st
import pickle
import pandas as pd

def recommend(movie):
    movie_index = movies_list[movies_list ['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list2 = sorted(list(enumerate(distances)),reverse =True, key = lambda x:x[1])[1:6]

    recommend_movies = []
    for i in movies_list2:
        
        recommend_movies.append(movies_list.iloc[i[0]].title)

    return recommend_movies

movies_list = pickle.load(open('movies.pkl', 'rb'))
movies_list1 = movies_list['title'].values

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommender System')

selected_movies_name = st.selectbox(
'how would you like to be contacted?',
movies_list1)

if st.button('Recommend'):
    recommendations = recommend(selected_movies_name)
    for i in recommendations:
        st.write(i)