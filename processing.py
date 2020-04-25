import pandas as pd 
import numpy as np 
import streamlit as st 

@st.cache
def check_file(file):
    if file is not None:
        df = pd.read_csv(file)
        return df
    else:
        return None