import streamlit as st

def main():
    st.write("""
    # Details:
    ### This is a basic Machine Learning based Medical App.
    The prediction about the disease is made with the help of the machine learning model which itself is trained on the thousands of the datasets

    So with the following paragraph I gonna be describing about the types of the diseases which gonna be getting employed in this app.

    # 1.Diabetes:
    """)
    st.image("source\images\diabetes.jpg")
    st.write("""
    Diabetes is a disease that occurs when your blood glucose, also called blood sugar, is too high.
    Blood glucose is your main source of energy and comes from the food you eat.
    Insulin, a hormone made by the pancreas, helps glucose from food get into your cells to be used for energy.
    
    ## What health problems can people with diabetes develop?
    Over time, high blood glucose leads to problems such as

    - heart disease
    - stroke
    - kidney disease
    - eye problems
    - dental disease
    - nerve damage
    - foot problems
    
    # 2.Heart Disease:
    """)
    st.image("images/heart.jpg")
    st.write("""
    ## Overview:
    Heart disease describes a range of conditions that affect your heart.
    Diseases under the heart disease umbrella include blood vessel diseases, such as coronary artery disease; heart rhythm problems (arrhythmias); and heart defects you're born with (congenital heart defects), among others.
    The term "heart disease" is often used interchangeably with the term "cardiovascular disease."
    Cardiovascular disease generally refers to conditions that involve narrowed or blocked blood vessels that can lead to a heart attack, chest pain (angina) or stroke.
    Other heart conditions, such as those that affect your heart's muscle, valves or rhythm, also are considered forms of heart disease.
    Many forms of heart disease can be prevented or treated with healthy lifestyle choices.
    
    ## Symptoms
    - Chest pain, chest tightness, chest pressure and chest discomfort (angina)
    - Shortness of breath
    - Pain, numbness, weakness or coldness in your legs or arms if the blood vessels in those parts of your body are narrowed
    - Pain in the neck, jaw, throat, upper abdomen or back
    
    # 3.Liver Disease:
    """)
    st.image("images/liver.jpg")
    st.write("""
     Liver disease is any disturbance of liver function that causes illness. The liver is responsible for many critical functions within the body and should it become diseased or injured, the loss of those functions can cause significant damage to the body.
     Liver disease is also referred to as hepatic disease.
     Liver disease is a broad term that covers all the potential problems that cause the liver to fail to perform its designated functions.
     Usually, more than 75% or three quarters of liver tissue needs to be affected before a decrease in function occurs.
     ## Symptoms:
     Classic symptoms of liver disease include:
    - nausea
    - vomiting
    - right upper quadrant abdominal pain, and
    - jaundice (a yellow discoloration of the skin due to elevated bilirubin concentrations in the bloodstream).
    """)


if __name__ == "__main__":
    main()
