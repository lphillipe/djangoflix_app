import streamlit as st
from movies.service import MovieService

def show_home():
    movie_service = MovieService()
    movie_stats = movie_service.get_movie_stats()
    
    st.title('Estatísticas de Filmes')

    if movie_stats is None:
        st.error('Erro ao carregar estatísticas de filmes')
        return

    st.subheader('Total de Filmes Cadastrados:')
    st.write(movie_stats['total_movies'])

    st.subheader('Total de Avaliações Cadastradas:')
    st.write(movie_stats['total_reviews'])

    st.subheader('Média Geral de Estrelas nas Avaliações:')
    st.write(movie_stats['average_stars'])