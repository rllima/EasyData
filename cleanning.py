import pandas as pd
import numpy as np 
import streamlit as st 
SPACES = '&nbsp;' * 10


def load_page(df):
    prepare_layout()
    side_bar_infos(df)
    basic_infos(df)




def prepare_layout():
    st.title("🎲 Data Cleanning")
    st.write("This page contains basic methods for a first exploration and cleaning of the data. ".format(SPACES))
    st.markdown("There are several things you see on this page:".format(SPACES))

def side_bar_infos(df):
    st.sidebar.markdown('**Number of Rows:**')
    st.sidebar.markdown(df.shape[0])
    st.sidebar.markdown('**Number of columns:**')
    st.sidebar.markdown(df.shape[1])

def basic_infos(df):
    number = st.slider('Choose the number of rows', min_value=1, max_value=20)
    st.dataframe(df.head(number))
    exploration = pd.DataFrame({'names' : df.columns, 'types' : df.dtypes, 'NA #': df.isna().sum(), 'NA %' : (df.isna().sum() / df.shape[0]) * 100})
    st.markdown('**Counting data types:**')
    st.write(exploration.types.value_counts())
    st.markdown('**Type Columns - int64:**')
    st.markdown(list(exploration[exploration['types'] == 'int64']['names']))
    st.markdown('**Type Columns -  float64:**')
    st.markdown(list(exploration[exploration['types'] == 'float64']['names']))
    st.markdown('**Type Columns -  object:**')
    st.markdown(list(exploration[exploration['types'] == 'object']['names']))
    st.markdown('**Table with missing types and data :**')
    missing_data = exploration[exploration['NA #'] != 0][['types', 'NA %']]
    if len(missing_data) == 0:
        st.markdown("No missing data")
    else:
        st.table(exploration[exploration['NA #'] != 0][['types', 'NA %']])
        select_fill_data = st.radio("Do you want fill missig data?", ("Yes","No"))
        if select_fill_data == "Yes":
            input_missing_data(df)

def input_missing_data(df):
    percentual = st.slider('Escolha o limite de percentual faltante limite para as colunas vocë deseja inputar os dados', min_value=0, max_value=100)
    lista_colunas = list(exploracao[exploracao['NA %']  < percentual]['nomes'])
    select_method = st.radio('Escolha um metodo abaixo :', ('Média', 'Mediana'))
    st.markdown('Você selecionou : ' +str(select_method))
