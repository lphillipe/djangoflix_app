import pandas as pd
import streamlit as st
from st_aggrid import AgGrid

movies = [
    {
        'id': 1,
        'name': 'Titanic'
    },
    {
        'id': 2,
        'name': 'Todo mundo odeia o chris'
    },
    {
        'id': 3,
        'name': 'Velozes e furiosos 5'
    },
]


def show_movies():
    st.write('Lista de Filmes:')

    AgGrid(
        data=pd.DataFrame(movies),
        reload_data=True,
        key='movies_grid',
    )

    st.title('Cadastrar novo filme')
    name = st.text_input('Nome do filme')
    if st.button('Cadastrar'):
        st.success(f'Filme "{name}" cadastrado(a) com sucesso!')