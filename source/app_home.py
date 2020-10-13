import streamlit as st

def main():
    #st.title("Basic Machine Learning Based Medical App")
    html_temp = """
        <div style="background-color:tomato;padding:10px">
        <h2 style="color:white;text-align:center;">Basic Machine Learning Based Medical App</h2>
        </div>
        """
    st.markdown(html_temp, unsafe_allow_html=True)
    st.write("""
    # Details
    Welcome to the **Home page** of the app.
    This is mainly based on as the application of the machine learning,meant to be employed in the remote and the downtrodden area.
    
    # Overview
    In todays time we see a lot of the shortage of the doctors in the world especially in India.
    A lot of people are suffering a lot without the help of the proper medical checkup.
    Also most of the cases many cases arise leading to dealth due to lack of timely medical checkup
    So to cope up with all of those problems this app is designed which would prove its benefits upto much extent.
    
    # Applications
    - To remove the dependencies on the doctors
    - To help out the poor and helpless people with the normal medical checkup
    - To help people avoid paying huge amount to the doctors unnecessarily
    - To extend the role of the technology in the medical field
    
    # Note
    This machine Learning based Medical App is just one of the applications of Machine Learning in Medical Field and tells
    us how these ML technologies are having a huge role/impact in this sector.
    
    # Creator :
    - **B.Sudharsan**
    - **K.Gowri Shankar**
    - **S.Sriaakash**
    - **M.Hariharan**
    
    """)

if __name__ == "__main__":
    main()


