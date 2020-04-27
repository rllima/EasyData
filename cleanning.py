import pandas as pd
import numpy as np 
import streamlit as st
import base64
from sklearn.impute import KNNImputer
SPACES = '&nbsp;' * 10


def get_table_download_link(df):
    """Generates a link allowing the data in a given panda dataframe to be downloaded
    in:  dataframe
    out: href string
    """
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # some strings <-> bytes conversions necessary here
    href = f'<a href="data:file/csv;base64,{b64}">Download csv file</a>'
    return href


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
            input_missing_data(exploration,df)

def input_missing_data(exploration,df):
    percentual = st.slider('Choose the missing percentage limit for the columns you want to input data', min_value=0, max_value=100)
    columns_list = list(exploration[(exploration['NA %']  < percentual) & ((exploration['types'] == 'int64') | (exploration['types'] == 'float64'))]['names'])
    select_method = st.radio('Choose a metod :', ('Mean', 'Median','KNN_Imputer'))
    st.markdown('You chosse : ' +str(select_method))
    if select_method == 'Mean':

        df_inputed = df[columns_list].fillna(df[columns_list].mean())
        st.table(df_inputed[columns_list].head(10))
        st.subheader('Download data : ')
        st.markdown(get_table_download_link(df_inputed), unsafe_allow_html=True)

    elif select_method == 'Median':

        df_inputed = df[columns_list].fillna(df[columns_list].median())
        st.table(df_inputed[columns_list].head(10))
        st.subheader('Download data : ')
        st.markdown(get_table_download_link(df_inputed), unsafe_allow_html=True)

    elif select_method == 'KNN_Imputer':
        imputer = KNNImputer(n_neighbors=3)
        st.markdown(columns_list)
        df_inputed = pd.DataFrame(imputer.fit_transform(df[columns_list]),columns=columns_list)
        df_inputed = pd.concat([df.drop(columns_list,axis=1),df_inputed])
        st.subheader('Download data : ')
        st.markdown(get_table_download_link(df_inputed), unsafe_allow_html=True)


