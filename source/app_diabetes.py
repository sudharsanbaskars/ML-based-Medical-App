import numpy as np
import pickle
import pandas as pd
import streamlit as st

pickle_in = open("diabetes.pkl", "rb")
classifier = pickle.load(pickle_in)


def diabetes_disease_prediction(Pregnancies,Glucose,BloodPressure,SkinThickness,
                                Insulin,BMI,DiabetesPedigreeFunction,Age):

    prediction = classifier.predict([[Pregnancies,Glucose,BloodPressure,
                                      SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
    print(prediction)
    return prediction


def main():
    st.title("Diabetes Prediction")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Diabetes Prediction ML App </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    Pregnancies = st.number_input("Pregnancies")
    Glucose = st.number_input("Glucose")
    BloodPressure = st.number_input("BloodPressure")
    SkinThickness = st.number_input("SkinThickness")
    Insulin = st.number_input("Insulin")
    BMI = st.number_input("BMI")
    DiabetesPedigreeFunction = st.number_input("DiabetesPedigreeFunction")
    Age = st.number_input("Age")
    #result = ""
    #output_mapper = {0:"Not Diabetic", 1:"You are Diabetic"}

    if st.button("Predict"):
        result = diabetes_disease_prediction(Pregnancies,Glucose,BloodPressure,SkinThickness,
                                Insulin,BMI,DiabetesPedigreeFunction,Age)
        if result ==0:
            st.write("**Congratulations! You are not a Diabetic Patient**")
        else:
            st.write('**You are Diabetic.Take care of you health**')
        #st.success('The output is {}'.format(result))

    if st.button("About"):
        st.text("Lets Learn")
        st.text("Built with Streamlit")


if __name__ == '__main__':
    main()
