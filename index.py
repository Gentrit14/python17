import streamlit as st
from numpy.ma.core import maximum


def main():
    st.title('Hello world')

if __name__ == '__main__':
    main()

if st.button("Click me"):
    st.write("Button")

st.checkbox("checkbox")

if st.checkbox("show some text"):
    st.write("trrararaarararararrarararm")

user_input = st.text_input("Enteret text","Shkruaj diqka")
st.write("texti juaj:", user_input)

age = st.number_input("You entered age:")
st.write(f"Your age is {age}")

message = st.text_area("Entered text:")
st.write(f"you entered text {message}")

choice = st.radio("Select Choice", ["Choice1", "Choice2", "Choice 3"])
st.write(f"your Choice: {choice}")

if st.button("Success")
st.success()


