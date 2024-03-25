# Import necessary libraries
import pandas as pd
import altair as alt
import streamlit as st
uploaded_file = st.file_uploader("Upload a file", type=['txt', 'csv', 'pdf'])

if uploaded_file is not None:
    # Read and display the file
    file_contents = uploaded_file.read()
    st.write(file_contents)

st.divider()
# Define the accuracy scores data for an ASD detection model
accuracy_scores = {
    'Dataset': ['Training Data', 'Test Data'],
    'Accuracy Score': [0.6919642857142857, 0.7302798982188295]
}

# Create a DataFrame from the accuracy scores data
df = pd.DataFrame(accuracy_scores)

# Create a line chart using Altair to visualize the accuracy scores with enhanced styling
line_chart = alt.Chart(df).mark_line(color='#6C5B7B').encode(
    x=alt.X('Dataset', title='Data Type', axis=alt.Axis(labelFontSize=12, titleFontSize=14)),
    y=alt.Y('Accuracy Score', title='Accuracy', scale=alt.Scale(domain=(0.6, 0.8)), axis=alt.Axis(labelFontSize=12, titleFontSize=14)),
    tooltip=['Dataset', alt.Tooltip('Accuracy Score', format='.2f')],
).properties(
    title={
        'text': 'Accuracy Scores of the Autism Detection Model',
        'subtitle': 'Comparison between training and test data',
        'color': '#2A9D8F',
        'fontSize': 18,
        'subtitleFontSize': 14,
        'anchor': 'start'
    },
    width=500,
    height=300
).configure_title(
    fontWeight='normal',
    fontSize=22
).configure_axis(
    labelColor='#264653',
    titleColor='#264653'
)

# Display the line chart using Streamlit
st.write(line_chart)
