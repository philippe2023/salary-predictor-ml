import streamlit as st
import pickle
import pandas as pd

# Load model
def load_model():
    model_filename = './models/tuned_random_forest_model.pkl'
    with open(model_filename, 'rb') as file:
        loaded_model = pickle.load(file)
    return loaded_model

# Load encoders
def load_encoders():
    with open('encoders/encoders.pkl', 'rb') as file:
        encoders = pickle.load(file)
    return encoders

loaded_model = load_model()
encoders = load_encoders()

def show_predict_page():
    st.title("Salary and Job Insights App")
    st.write("This app provides visual insights into salary trends and job types across different countries from 2021 to 2024.")

    countries = (
        'Australia', 'Austria', 'Belgium', 'Brazil', 'Canada', 'Czech Republic', 
        'Denmark', 'Finland', 'France', 'India', 'Italy', 'Germany', 'Mexico', 
        'Netherlands', 'New Zealand', 'Norway', 'Poland', 'Portugal', 'Romania', 
        'Spain', 'Sweden', 'Switzerland', 'Turkey', 'United Kingdom', 
        'United States', 'Ukraine'
    )
    country = st.selectbox("Countries", countries)

    age_range = (
        '18-24 years old', '25-34 years old', '35-44 years old',
        '45-54 years old', '55-64 years old', '65 years or older'
    )
    age = st.selectbox("Age", age_range)

    employment = (
        'Employed, full-time', 'Employed, part-time', 'Freelancer/Contractor'
    )
    employment_contract = st.selectbox("Contract type", employment)

    work_location = (
        'Full in-person', 'Fully remote', 'In-person', 'Hybrid', 'Remote'
    )
    location = st.selectbox("Place of Work", work_location)

    education_level = (
        'High School or Less', 'Bachelor Degree', 'Master Degree', 
        'Professional/Doctoral', 'Some College', 'Other'
    )
    highest_education = st.selectbox("Education level", education_level)

    type = (
        'Full Stack Developer', 'Front-End Developer', 'Back-End Developer', 
        'Data Scientist', 'Data Analyst', 'Data Engineer', 'Designer'
    )
    type_developer = st.selectbox("Job title", type)

    experience_coding = st.slider("Years of coding experience", 0, 30, 3)
    experience_working = st.slider("Years of work experience", 0, 30, 1)

    year = 2024

    submit_button = st.button(label='Predict')

    if submit_button:
        # Encode user input using the encoders
        country_encoded = encoders['country_encoder'].transform([country])[0]
        age_encoded = encoders['age_encoder'].transform([age])[0]
        employment_encoded = encoders['employment_encoder'].transform([employment_contract])[0]
        location_encoded = encoders['location_encoder'].transform([location])[0]
        education_encoded = encoders['education_encoder'].transform([highest_education])[0]
        type_encoded = encoders['type_encoder'].transform([type_developer])[0]

        # Prepare input data for the model
        input_data = pd.DataFrame([[year, country_encoded, age_encoded, employment_encoded, location_encoded, education_encoded, experience_coding, experience_working, type_encoded]],
                                    columns=['year', 'country', 'age_range', 'employment', 'work_location', 'education_level', 'years_coding', 'years_coding_pro', 'type'])

        # Make the prediction
        prediction = loaded_model.predict(input_data)
        st.success(f"The predicted salary is: {prediction[0]:,.2f} EUR")