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
    # for sex
    if sex=="Male":
        sex=1
    else:
        sex=0
    #for fbs
    if fbs=="True":
        fbs=1
    else:
        fbs=0
    #for exang
    if exang=="Yes":
        exang=1
    else:
        exang=0
    #for thal
    if thal=="Normal":
        thal=1
    elif thal=="Fixed defect":
        thal=2
    elif thal=="Reversable defect":
        thal=3
    else:
        thal=0

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
    sex = st.selectbox("Sex",("Male","Female"))
    cp = st.selectbox("Chest Pain Type",(0,1,2,3))
    trestbps = st.number_input("Trestbps(resting blood pressure (in mm Hg on admission to the hospital))")
    chol = st.number_input("Serum cholestoral in mg/dl")
    fbs = st.selectbox("fasting blood sugar &gt; 120 mg/dl",("True", "False"))
    restecg = st.number_input("Restecg(resting electrocardiographic results)")
    thalach = st.number_input("Thalach(maximum heart rate achieved)")
    exang = st.selectbox("Exercise Induced Angina", ("Yes", "No"))
    oldpeak = st.number_input("Oldpeak(ST depression induced by exercise relative to rest)")
    slope = st.number_input("Slope(slope of the peak exercise ST segment)")
    ca = st.number_input("Number of major vessels (0-3) colored by flourosopy")
    thal = st.selectbox("Thal",("Normal","Fixed defect","Reversable defect","Nothing"))

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

