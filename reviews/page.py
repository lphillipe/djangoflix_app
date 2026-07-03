import pandas as pd
import streamlit as st
from movies.service import MovieService
from reviews.service import ReviewService
from st_aggrid import AgGrid


def show_reviews():
    review_service = ReviewService()
    reviews = review_service.get_reviews()
    
    if reviews:

        st.write('Lista de Avaliações:')
        reviews_df = pd.json_normalize(reviews)

        AgGrid(
            data=reviews_df,
            reload_data=True,
            key='reviews_grid',
        )
    else:
        st.warning('Nenhuma avaliação encontrada.')

    st.title('Cadastrar nova avaliação')
    
    movie_service = MovieService()
    movies = movie_service.get_movies()
    movie_titles = {movie['title']: movie['id'] for movie in movies}
    selected_movie_title = st.selectbox('Filme', list(movie_titles.keys()))