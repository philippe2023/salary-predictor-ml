import streamlit as st
from predict_page import show_predict_page
from explore_page import show_explore_page

# Set page config (wide layout)
st.set_page_config(layout="wide")

st.markdown(
    """
    <style>
    /* Style the entire slider track and thumb */
    .stSlider > div > div > div > input[type=range] {
        accent-color: #5e17eb; /* This will change the thumb and active track color */
    }

    /* Customize the track for both filled and unfilled portions */
    .stSlider > div > div > div > div {
        background-color: #5e17eb !important; /* Active portion of the track */
    }

    /* Customize the thumb specifically */
    div[role="slider"] {
        background-color: #5e17eb !important; /* Thumb color */
        border-color: #5e17eb !important; /* Thumb border */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Get query parameters to decide which page to render
query_params = st.query_params

# Check if 'page' query param is set to 'explore'
if query_params.get("page") == "explore":
    show_explore_page()
else:
    show_predict_page()



