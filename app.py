import streamlit as st
import pandas as pd

# Load project targets from CSV file
data_file = 'data/targets.csv'
targets = pd.read_csv(data_file)

# Set the title of the app
st.title('Project Targets')

# Display the targets in a table
st.subheader('Targets Overview')
st.write(targets)