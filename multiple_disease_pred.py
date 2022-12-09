# -*- coding: utf-8 -*-
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# loading the saved models
diabetes_model = pickle.load(open('saved_models/diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('saved_models/heart_disease_model.sav', 'rb'))

# sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System Using Machine Learning',
                           ['Heart Disease Prediction',
                           'Diabetes Prediction'],
                           icons=['heart', 'activity'],
                           default_index=0)

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':
    # page title
    st.title('Heart Disease Prediction')

    col1, col2 = st.columns(2)

    with col1:
        age = st.text_input('Age')

    with col2:
        sex_selected = st.selectbox("Sex:",
                       ['', 'Male', 'Female'])
        if sex_selected == "Female":
            sex = 1
        else:
            sex = 0

    with col1:
        cp_selected = st.selectbox("Chest Pain types: ",
                                     ['', 'Typical Angina', 'Atypical Angina', 'Non-anginal Pain', 'Asymptotic'])
        if cp_selected == 'Typical Angina':
            cp = 1
        elif cp_selected == 'Atypical Angina':
            cp = 2
        elif cp_selected == "Non-anginal Pain":
            cp = 3
        elif cp_selected == 'Asymptotic':
            cp = 4

    with col2:
        trestbps = st.text_input('Resting Blood Pressure')

    with col1:
        chol = st.text_input('Serum Cholesterol in mg/dl',)

    with col2:
        fbs_selected = st.selectbox("Fasting Blood Sugar > 120 mg/dl:",
                     ['', 'Yes', 'No'])
        if fbs_selected == "Yes":
            fbs = 1
        else:
            fbs = 0

    with col1:
        restecg_selected = st.selectbox("Resting Electrocardiographic results: ",
                                    ['', 'Yes', 'No'])
        if restecg_selected == "Yes":
            restecg = 1
        else:
            restecg = 0


    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')

    with col1:
        exang_selected = st.selectbox("Exercise Induced Angina: ",
                                        ['', 'Yes', 'No'])
        if exang_selected == 'Yes':
            exang = 1
        else:
            exang = 0

    with col2:
        oldpeak = st.text_input('ST depression induced by exercise')

    with col1:
        slope = st.selectbox("Slope of the peak exercise ST segment: ",
                     ['', '0', '1', '2'])

    with col2:
        ca = st.selectbox("Major vessels colored by fluoroscopy: ",
                     ['', '0', '1', '2', '3', '4'])
    with col1:
        thal_selected = st.selectbox("thal: ",
                     ['','Normal', 'Fixed Defect', 'Reversible Defect'])
        if thal_selected == 'Normal':
            thal = 1
        elif thal_selected == 'Fixed Defect':
            thal = 2
        elif thal_selected == "Reversible Defect":
            thal = 3

    # code for Prediction
    heart_diagnosis = ''

    # creating a button for Prediction
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])

        if heart_prediction[0] == 1:
          heart_diagnosis = 'The person is having heart disease'
        else:
          heart_diagnosis = 'The person does not have any heart disease'

    st.success(heart_diagnosis)




# Diabetes Prediction Page
if selected == 'Diabetes Prediction':

    # page title
    st.title('Diabetes Prediction using ML')

    # getting the input data from the user
    col1, col2 = st.columns(2)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies (min: 0, max: 17)')

    with col2:
        Glucose = st.text_input('Glucose Level (min: 0, max: 199)')

    with col1:
        BloodPressure = st.text_input('Blood Pressure value (min: 0, max: 122)')

    with col2:
        SkinThickness = st.text_input('Skin Thickness value (min: 0, max: 99)')

    with col1:
        Insulin = st.text_input('Insulin Level (min: 0, max: 846)')

    with col2:
        BMI = st.text_input('BMI value (min: 0, max: 67.1)')

    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value (min: 0.078, max: 2.42)')

    with col2:
        Age = st.text_input('Age of the Person (min: 21, max: 81)')

    # code for Prediction
    diab_diagnosis = ''

    # creating a button for Prediction
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

        if diab_prediction[0] == 1:
          diab_diagnosis = 'The person is diabetic'
        else:
          diab_diagnosis = 'The person is not diabetic'

    st.success(diab_diagnosis)

