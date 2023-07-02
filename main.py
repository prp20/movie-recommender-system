import streamlit as st
import pandas as pd
import pickle


def recommend_movie(movie):
    movie_index = movies[movies['title_x'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),
                         reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    posters = []
    for i in movies_list:
        movie_id = i[0]
        recommended_movies.append(movies.iloc[movie_id].title_x)
    return recommended_movies


movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommender System')
selected_movie_name = st.selectbox(
    'Select a sample movie', movies['title_x'].values)

if st.button('Recommend'):
    name = recommend_movie(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.header(name[0])

    with col2:
        st.header(name[1])

    with col3:
        st.header(name[2])

    with col4:
        st.header(name[3])

    with col5:
        st.header(name[4])
