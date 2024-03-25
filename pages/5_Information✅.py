import streamlit as st
import pandas as pd
import numpy as np
import pickle
st.header('Give a Survey')
st.warning('Streamlit App Predicting Autism Spectrum Disorder Using Machine Learning')

def load_data():
    df_autism = pd.read_csv('autism_screening.csv')
    df_autism = df_autism[['A1_Score', 'A2_Score', 'A3_Score', 'A4_Score', 'A5_Score', 'A6_Score', 'A7_Score', 'A8_Score', 'A9_Score', 'A10_Score', 'age', 'gender', 'jundice', 'austim', 'Class/ASD']].copy()
    df_autism = df_autism.dropna()
    df_autism['gender'] = np.where(df_autism['gender']=='m', 1, 0)
    df_autism['jundice'] = np.where(df_autism['jundice']=='yes', 1, 0)
    df_autism['austim'] = np.where(df_autism['austim']=='yes', 1, 0)
    df_autism['Class/ASD'] = np.where(df_autism['Class/ASD']=='YES', 1, 0)
    return df_autism

def user_input_features():
    a1_score = st.slider('A1_Score', 0.00, 1.00)
    a2_score = st.slider('A2_Score', 0.00, 1.00)
    a3_score = st.slider('A3_Score', 0.00, 1.00)
    a4_score = st.slider('A4_Score', 0.00, 1.00)
    a5_score = st.slider('A5_Score', 0.00, 1.00)
    a6_score = st.slider('A6_Score', 0.00, 1.00)
    a7_score = st.slider('A7_Score', 0.00, 1.00)
    a8_score = st.slider('A8_Score', 0.00, 1.00)
    a9_score = st.slider('A9_Score', 0.00, 1.00)
    a10_score = st.slider('A10_Score', 0.00, 1.00)

    data = {
        'A1_Score': [a1_score], 
        'A2_Score': [a2_score],
        'A3_Score': [a3_score],
        'A4_Score': [a4_score],
        'A5_Score': [a5_score],
        'A6_Score': [a6_score],
        'A7_Score': [a7_score],
        'A8_Score': [a8_score],
        'A9_Score': [a9_score],
        'A10_Score': [a10_score]
    }

    features = pd.DataFrame(data)
    return features

input_df = user_input_features()

df_autism = load_data()
df = df_autism.drop(columns=['Class/ASD'])

# Concatenate input features with the original dataframe
df = pd.concat([input_df, df], axis=0)

# Select only the first row (the user input data)
df = df[:1] 
df.fillna(0, inplace=True)

# Ensure the feature names match those used during model training
features = ['A1_Score', 'A2_Score', 'A3_Score', 'A4_Score', 'A5_Score', 
            'A6_Score', 'A7_Score', 'A8_Score', 'A9_Score', 'A10_Score', 
            'age', 'gender', 'jundice', 'austim']

df = df[features]

# Load the model
load_clf = pickle.load(open('autism_clf.pkl', 'rb'))

# Make prediction
prediction = load_clf.predict(df)
prediction_proba = load_clf.predict_proba(df)

# Display results
autism_labels = np.array(['No', 'Yes'])
st.subheader('Prediction')
st.write(autism_labels[prediction])
st.subheader('Prediction Probability')
st.write(prediction_proba)