import streamlit as st
import pandas as pd

# col1,col2,col3, col4 , col5 = st.columns (gap=5 , gap="small")
#
# with col1:
#     st.header("Column1")
#     st.write("column1")
#
# with col1:
#     st.header("Column2")
#     st.write("column2")
#
# with col3:
#     st.header("Column3")
#     st.write("column3")
#
# with col4:
#     st.header("Column4")
#     st.write("column4")
#
# with col5:
#     st.header("Column5")
#     st.write("column5")


with st.form("my_form", clear_on_submit=True):
    name = st.text_input('Name')
    age =st.slider('Age', min_value=0, max_value=100)
    email = st.text_input('Email')
    biography = st.text_area('Short Bio')
    terms = st.checkbox('I agree to the terms')
    submit_button = st.form_submit_button(label='Submit')

if submit_button:
    st.write(f"Name {name}")
    st.write(f"Age {age}")
    st.write(f"Email: {email}")
    st.write(f"shortBio: {biography}")

    if terms:
        st.write('Your agreed with terms')
    else:
        st.write('You did not agree with terms')


tab1,tab2,tab3 = st.tabs(["Tab1", "Tab2", "Tab3"])

with tab1:
    st.header("Column1")
    st.write("column1")

with tab2:
    st.header("Column2")
    st.write("column2")

with tab3:
    st.header("Column3")
    st.write("column3")

st.header("Displaying Data Frames")

df = pd.DataFrame({
    'Name': ["Andy","Michel", "Martin"],
    'Age': [16, 20, 60],
    'City': ["New York", "Santa Blanca" , "Rio De Janiro"]
})

st.write(df)