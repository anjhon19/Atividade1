import streamlit as st

st.title('Cadastro Simples...')

nome = st.text_input('Digite o seu nome')
idade = st.text_input('Digite a sua idade')
cidade = st.text_input('Digite a sua cidade')

st.title ('Cadastro')

st.write('Nome', nome)
st.write('Idade', idade)
st.write('Cidade', cidade)





