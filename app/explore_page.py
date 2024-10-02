import streamlit as st
import plotly.express as px
import pandas as pd

# Load the dataset
df = pd.read_csv('./data/clean/final_merged_df_2021_2024.csv')

def show_explore_page():
    # Define the page title and a brief description
    st.title("See the data")
    st.header("What kind of developer are you?")

    # Define the selectbox for job titles
    job_titles = df['type'].unique()
    selected_job = st.selectbox("Select Job Title", job_titles)

    # Filter the dataset based on the selected job title
    filtered_df = df[df['type'] == selected_job]

    # 1. Evolution of Respondents by Country (for the selected job title)
    responders_by_country_year = filtered_df.groupby(['year', 'country']).size().reset_index(name='respondent_count')
    fig1 = px.line(responders_by_country_year, x='year', y='respondent_count', color='country',
                    title=f'Evolution of Respondents by Country (2021-2024) - {selected_job}', 
                    labels={'respondent_count': 'Number of Respondents', 'year': 'Year'},
                    width=1000, height=600)
    fig1.update_layout(xaxis_title='Year', yaxis_title='Number of Respondents')
    fig1.update_xaxes(tickvals=[2021, 2022, 2023, 2024])

    # 2. Age Distribution by Year (for the selected job title)
    age_distribution_per_year = filtered_df.groupby(['year', 'age_range']).size().reset_index(name='respondent_count')
    fig2 = px.bar(age_distribution_per_year, x='year', y='respondent_count', color='age_range',
                    title=f'Age Distribution by Year (Stacked Bar Chart) (2021-2024) - {selected_job}',
                    labels={'respondent_count': 'Number of Respondents', 'year': 'Year'},
                    width=1000, height=600)
    fig2.update_layout(xaxis_title='Year', yaxis_title='Number of Respondents')
    fig2.update_xaxes(tickvals=[2021, 2022, 2023, 2024])

    # 3. Average Salary by Country Throughout the Years (for the selected job title)
    avg_salary_by_country_year = filtered_df.groupby(['country', 'year'])['salary_eur'].mean().reset_index()

    # Create the bar chart
    fig3 = px.bar(avg_salary_by_country_year, 
                    x='country', 
                    y='salary_eur', 
                    color='year', 
                    barmode='group',
                    title=f'Average Salary by Country Throughout the Years (2021-2024) - {selected_job}',
                    labels={'salary_eur': 'Average Salary (EUR)', 'country': 'Country'}, 
                    width=1000, height=600)

    # Customize layout
    fig3.update_layout(xaxis_tickangle=-45, yaxis_title='Average Salary (EUR)')

    # Displaying the graphs in Streamlit
    st.write("### Graphs for the selected job title:")
    st.plotly_chart(fig1, use_container_width=True)
    st.plotly_chart(fig2, use_container_width=True)
    st.plotly_chart(fig3, use_container_width=True)