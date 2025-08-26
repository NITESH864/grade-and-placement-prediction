# Student Performance Analysis
import streamlit as st
import pandas as pd
import joblib

# Load model and encoders
model=joblib.load('student_performance_model.pkl')
technology_encoder=joblib.load('technology_encoder.pkl')
grade_encoder=joblib.load('grade_encoder.pkl')

st.subheader('Student Performance Analysis And Prediction App')
st.write('Fill the student scores below to predict their final grade')

# User inputs
technology=st.selectbox('Technology',technology_encoder.classes_)
welcome_test=st.slider('Welcome Test',30,50,40)
presentation=st.slider('Presentation',90,150,120)
mini_project=st.slider('Mini_Projects',60,100,80)
hrskills=st.slider('HR Skills',90,150,120)
project_presentation=st.slider('Project Presentation',160,250,205)
project_submission=st.slider('Project submission',200,300,251)
attendance=st.slider('Attendance',70,100,85)
discipline=st.slider('Discipline',60,100,80)

button=st.button("Predict")
if button:
    input_data=pd.DataFrame({
        'Technology':[technology_encoder.transform([technology])[0]],
        'Welcome_test':[welcome_test],
        'Presentation':[presentation],
        'Mini_projects':[mini_project],
        'Hrskills':[hrskills],
        'Project_presentation':[project_presentation],
        'Project_submission':[project_presentation],
        'Attendance':[attendance],
        'Discipline':[discipline]
    })
    prediction=model.predict(input_data)
    result=grade_encoder.inverse_transform(prediction)[0]
    st.success(f"Predicted Grade: **{result}**")