import streamlit as st
import source.app_heart
import source.app_liver
import source.app_diabetes
import source.app_home
import source.app_about



pages = {
         "Home":source.app_home,
         "About":source.app_about,
          "Diabetes":source.app_diabetes,
         "Heart":source.app_heart,
         "Liver":source.app_liver}

def main():
    st.sidebar.header("Navigation")


    selection = st.sidebar.radio("Go to", list(pages.keys()))
    page = pages[selection]
    page.main()
    #with st.spinner(f"Loading {selection} ..."):
        #ast.shared.components.write_page(page)
    st.sidebar.title("Creators")
    st.sidebar.write("""
    - **B.Sudharsan**
    - **K.Gowri Shankar**
    - **S.Sriaakash**
    - **M.Hariharan**
            """)


if __name__ == "__main__":
    main()
