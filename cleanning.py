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
    number = st.slider('CChoose the number of rows', min_value=1, max_value=20)
    st.dataframe(df.head(number))