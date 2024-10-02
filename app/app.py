import streamlit as st
from predict_page import show_predict_page
from explore_page import show_explore_page

# Set page config (wide layout)
st.set_page_config(layout="wide")

# Get query parameters to decide which page to render
query_params = st.query_params

# Check if 'page' query param is set to 'explore'
if query_params.get("page") == "explore":
    show_explore_page()
else:
    show_predict_page()



