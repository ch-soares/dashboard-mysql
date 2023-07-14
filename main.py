import streamlit as st
from settings import nome, frutas

pagina_selecionada = st.sidebar.selectbox('Nome', nome())
pagina2 = st.sidebar.radio('Fruta', frutas())

if pagina_selecionada:
    st.text(nome()[pagina_selecionada])

if pagina2:
    st.title(frutas()[pagina2])
