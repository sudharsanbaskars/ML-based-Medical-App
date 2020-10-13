import numpy as np
import pickle
import pandas as pd
import streamlit as st
from sklearn.preprocessing import StandardScaler


pickle_in = open("liver.pkl", "rb")
classifier = pickle.load(pickle_in)
scaler = StandardScaler()

df = pd.read_csv("liver dataset.csv")

gender_mapper = {'Male':1, 'Female':0}
df['Gender'] = df['Gender'].map(gender_mapper)

X_Data = df.drop("Dataset", axis="columns")
Y_Data = df["Dataset"]

X_Data = scaler.fit_transform(X_Data)


def liver_disease_prediction(Age,Gender,Total_Bilirubin,Direct_Bilirubin,
                Alkaline_Phosphotase,Alamine_Aminotransferase,Aspartate_Aminotransferase,
                             Total_Protiens,Albumin,Albumin_and_Globulin_Ratio):


    if Gender=="Male":
        Gender=1
    else:
        Gender=0

    x = np.array([Age,Gender,Total_Bilirubin,Direct_Bilirubin,
                Alkaline_Phosphotase,Alamine_Aminotransferase,Aspartate_Aminotransferase,
                             Total_Protiens,Albumin,Albumin_and_Globulin_Ratio])

    x = scaler.transform([x])

    prediction = classifier.predict(x)
    print(prediction)
    return prediction


def main():
    st.title("Liver Disease Prediction")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Liver Disease Prediction ML App </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    Age = st.number_input("Age")
    Gender = st.selectbox("Gender",("Male", "Female"))
    Total_Bilirubin = st.number_input("Total_Bilirubin")
    Direct_Bilirubin = st.number_input("Direct_Bilirubin")
    Alkaline_Phosphotase = st.number_input("Alkaline_Phosphotase")
    Alamine_Aminotransferase = st.number_input("Alamine_Aminotransferase")
    Aspartate_Aminotransferase = st.number_input("Aspartate_Aminotransferase")
    Total_Protiens = st.number_input("Total_Protiens")
    Albumin = st.number_input("Albumin")
    Albumin_and_Globulin_Ratio = st.number_input("Albumin_and_Globulin_Ratio")


    if st.button("Predict"):
        result = liver_disease_prediction(Age,Gender,Total_Bilirubin,Direct_Bilirubin,
                Alkaline_Phosphotase,Alamine_Aminotransferase,Aspartate_Aminotransferase,
                             Total_Protiens,Albumin,Albumin_and_Globulin_Ratio)
        if result ==0:
            st.write("**Congratulations! You do not have Liver Disease**")
        else:
            st.write('**You Have Liver Disease.Take care of your Health**')
        #st.success('The output is {}'.format(result))

    if st.button("About"):
        st.text("Lets Learn")
        st.text("Built with Streamlit")


if __name__ == '__main__':
    main()