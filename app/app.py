import streamlit as st
import pandas as pd
import plotly.express as px
from predict_page import show_predict_page

# Set page config must be the first Streamlit command
st.set_page_config(layout="wide")

show_predict_page()



