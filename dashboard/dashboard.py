import streamlit as st
import requests
import pandas as pd
import plotly.express as px

# Fetch data from the Flask API
data = {    "Month": ["January", "February", "March", "April", "May", "June"],
    "Sales": [150, 200, 250, 300, 350, 290]}

# Convert the data to a DataFrame
df = pd.DataFrame(data)

# Title for the Streamlit app
st.title("Sales Data Visualization Dashboard")

# Plotly chart
fig = px.bar(df, x="Month", y="Sales", title="Monthly Sales")

# Display the chart in Streamlit
st.plotly_chart(fig)

# Optionally, show the data in a table
st.dataframe(df)
