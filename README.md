# Project overview

## SalarySense AI

SalarySense AI is a platform that provides valuable insights into salary trends across various job roles, countries, and industries. It leverages machine learning algorithms and data analysis to deliver up-to-date salary predictions and detailed visualizations for professionals and employers alike.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Modeling Process](#modeling-process)
- [Dashboard and Visualization](#dashboard-and-visualization)
- [Technologies](#technologies)
- [Contributing](#contributing)
- [License](#license)

## Introduction

SalarySense AI aims to provide an intuitive, data-driven platform for understanding salary trends across various job markets and demographics. The project combines data analysis, machine learning, and visualization tools to offer a holistic view of salary distribution, predictions, and related insights.

## Features

- **Salary Prediction Model**: Predicts salary based on factors such as job title, location, years of experience, education level, and more.
- **Data Visualization**: Provides visual insights using Tableau and Plotly dashboards to show trends in salary distribution by country, year, and job type.
- **Exploratory Analysis**: Allows users to explore salary data and see relationships between job characteristics and salary trends.
- **Streamlit App**: An interactive user interface to predict salaries and explore trends.

## Installation

1. **Clone the repository**:

```bash
git clone https://github.com/YourUsername/SalarySenseAI.git
```

2. **Install dependencies**:

```bash
pip install -r requirements.txt
```

3. **Run the Streamlit App**:

```bash
streamlit run app/app.py
```

4. **Run the Flask Backend (if applicable)**:

```bash
python app/flask_app.py
```

## Usage

The project consists of two key components:

1. **Salary Prediction**: Users can input specific details (job title, country, experience, etc.) to get a salary prediction based on the machine learning model.
2. **Exploratory Analysis**: Users can visualize and interact with salary trends using interactive charts, either through Streamlit or Tableau dashboards.

## Modeling Process

1. **Data Collection**: The dataset used for the model consists of developer salary data from 2021 to 2024, collected from Stack Overflow yearly developer survey.
2. **Data Cleaning and Preprocessing**: Handling missing data, transformed columns like job titles and locations using label encoding, and standardized the salary data to EUR for uniformity.
3. **Feature Engineering**: Relevant features such as years of experience, education, country, and job type were selected.
4. **Model Selection**: A variety of models were tried, including Linear Regression, Decision Trees, and Random Forests. The Random Forest model was fine-tuned using hyperparameter tuning and cross-validation.
5. **Model Evaluation**: The Random Forest model performed the best, with an R² of 0.55, which was selected for the final prediction.

## Dashboard and Visualization

1. **Streamlit App**:
   - **Prediction Page**: Allows users to predict salaries based on selected criteria.
   - **Explore Page**: Users can visualize salary distributions across various countries, job types, and demographics.
2. **Tableau Dashboard**: A comprehensive dashboard that shows salary trends across different job roles and countries for further exploration.

## Technologies

- **Python**: Core programming language used for data analysis, model building, and backend development.
- **Pandas and NumPy**: Used for data manipulation and analysis.
- **Scikit-learn**: For building and evaluating machine learning models.
- **Streamlit**: For building an interactive frontend application.
- **Tableau**: Used for creating rich, interactive visualizations.
- **Flask**: Backend framework for serving web pages and APIs.
- **Plotly**: For generating interactive visualizations.
- **Pickle**: For model serialization and saving encoders.