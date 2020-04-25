import pandas as pd
import numpy as nup 
import streamlit as st
import cleanning
import processing

def main():
    st.image("header.png",width=800,use_column_width=True)
    st.sidebar.title("Menu")
    loaded_header = st.sidebar.subheader("⭕️ Data not loaded")

    df = processing.check_file(st.sidebar.file_uploader('Select file (.csv)', type = 'csv'))
    if df is not None:
        create_layout(df,loaded_header)



def create_layout(df,header):
    header.subheader("✔️Data is loaded")
    app_mode = st.sidebar.selectbox("Please select a page", ["---",
                                                             "Cleanning Data",
                                                             "Data Exploration",
                                                             "Player Statistics",
                                                             "Game Statistics",
                                                             "Head to Head"])

    if app_mode == 'Cleanning Data':
        cleanning.load_page(df)


if __name__ == "__main__":
    main()



