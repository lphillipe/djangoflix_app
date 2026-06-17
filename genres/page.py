import streamlit as st
from st_aggrid import AgGrid

genres = [
    {
        'id': 1,
        'name': 'Ação'
    }
    {
        'id': 2,
        'name': 'Comedia'
    }
    {
        'id': 3,
        'name': 'Terror'
    }
]

def show_genres():
    st.write('Lista de Gêneros:')