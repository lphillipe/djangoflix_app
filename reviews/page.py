import pandas as pd
import streamlit as st
from st_aggrid import AgGrid

reviews = [
    {
        'id': 1,
        'stars': 5
    },
    {
        'id': 2,
        'stars': 2
    },
    {
        'id': 3,
        'stars': 4
    },
]


def show_reviews():
    st.write('Lista de Avaliações:')

    AgGrid(
        data=pd.DataFrame(reviews),
        reload_data=True,
        key='reviews_grid',
    )

    st.title('Cadastrar nova avaliação')
    name = st.text_input('Avaliações')
    if st.button('Cadastrar'):
        st.success(f'Avaliação "{name}" cadastrada com sucesso!')