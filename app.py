import streamlit as st
import pandas as pd
import numpy as np
import pickle

st.set_page_config(
    page_title="Autism App"
)

st.title('Autism Screening on Adults')
st.image('image/asd_child.jpg')
st.divider()
st.header('Abstract')
st.write('Improve Autism Screening by predicting the likelihood of having this condition')
st.image('image/causes-of-autism.png')
st.divider()
st.header('What is Autism')
st.image('image/autism.png')
st.write("""Autism, or autism spectrum disorder (ASD), refers to a broad range of conditions characterized by challenges with social skills, repetitive behaviors, speech and nonverbal communication.

Causes and Challenges

It is mostly influenced by a combination of genetic and environmental factors. Because autism is a spectrum disorder, each person with autism has a distinct set of strengths and challenges. The ways in which people with autism learn, think and problem-solve can range from highly skilled to severely challenged.

Research has made clear that high quality early intervention can improve learning, communication and social skills, as well as underlying brain development. Yet the diagnostic process can take several years.

 The Role of Machine Learning

This dataset is composed of survey results for more than 700 people who filled out an app form. There are labels portraying whether the person received a diagnosis of autism, allowing machine learning models to predict the likelihood of having autism, therefore allowing healthcare professionals to prioritize their resources.
""")
st.info('How to use')
st.write("""
Predict the likelihood of a person having autism using survey and demographic variables.
Explore Autism across Gender, Age, and other variables""")

