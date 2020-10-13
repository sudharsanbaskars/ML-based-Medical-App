import numpy as np
import pickle
import pandas as pd
import streamlit as st
from sklearn.preprocessing import StandardScaler


pickle_in = open("heart.pkl", "rb")
classifier = pickle.load(pickle_in)
scaler = StandardScaler()

df = pd.read_csv("Heart_disease_dataset.csv")
X_Data = df.drop("target", axis="columns")
Y_Data = df["target"]

X_Data = scaler.fit_transform(X_Data)


def heart_disease_prediction(age,sex,cp,
                        trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal):
    x = np.array([age, sex, cp, trestbps, chol, fbs, restecg,thalach, exang,oldpeak,slope,ca,thal])

    x = scaler.transform([x])

    prediction = classifier.predict(x)
    print(prediction)
    return prediction


def main():
    st.title("Heart Disease Prediction")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Heart Disease Prediction ML App </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    age = st.number_input("Age")
    sex = st.number_input("Sex((1 = male; 0 = female))")
    cp = st.number_input("Chest Pain Type")
    trestbps = st.number_input("Trestbps")
    chol = st.number_input("Serum cholestoral in mg/dl")
    fbs = st.number_input("Fasting blood sugar level(FBS)(1 = true; 0 = false)")
    restecg = st.number_input("Restecg")
    thalach = st.number_input("Thalach(maximum heart rate achieved)")
    exang = st.number_input("Exercise Induced Angina (1 = yes; 0 = no)")
    oldpeak = st.number_input("Oldpeak(ST depression induced by exercise relative to rest)")
    slope = st.number_input("Slope")
    ca = st.number_input("Number of major vessels (0-3) colored by flourosopy")
    thal = st.number_input("Thal(0 = normal; 1 = fixed defect; 2 = reversable defect)")
    #result = ""
    #output_mapper = {0:"Not Diabetic", 1:"You are Diabetic"}

    if st.button("Predict"):
        result = heart_disease_prediction(age,sex,cp,
                        trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal)
        if result ==0:
            st.write("**Congratulations! You Do Not Heart Disease**")
        else:
            st.write('**You Have Heart Disease.Take Care of your health**')
        #st.success('The output is {}'.format(result))

    if st.button("About"):
        st.text("Lets Learn")
        st.text("Built with Streamlit")


if __name__ == '__main__':
    main()

