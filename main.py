import streamlit as st
from base import tecnologia

tecnologias = st.sidebar.selectbox('Tecnologias', tecnologia())

if tecnologias:
    st.title(tecnologia()[tecnologias])
