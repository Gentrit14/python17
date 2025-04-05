from operator import index

import streamlit as st
import pandas as pd
import plotly.express as px
from numpy.ma.extras import unique, average
from select import select

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


# with st.form("my_form", clear_on_submit=True):
#     name = st.text_input('Name')
#     age =st.slider('Age', min_value=0, max_value=100)
#     email = st.text_input('Email')
#     biography = st.text_area('Short Bio')
#     terms = st.checkbox('I agree to the terms')
#     submit_button = st.form_submit_button(label='Submit')
#
# if submit_button:
#     st.write(f"Name {name}")
#     st.write(f"Age {age}")
#     st.write(f"Email: {email}")
#     st.write(f"shortBio: {biography}")
#
#     if terms:
#         st.write('Your agreed with terms')
#     else:
#         st.write('You did not agree with terms')
#
#
# tab1,tab2,tab3 = st.tabs(["Tab1", "Tab2", "Tab3"])
#
# with tab1:
#     st.header("Column1")
#     st.write("column1")
#
# with tab2:
#     st.header("Column2")
#     st.write("column2")
#
# with tab3:
#     st.header("Column3")
#     st.write("column3")
#
# st.header("Displaying Data Frames")
#
# df = pd.DataFrame({
#     'Name': ["Andy","Michel", "Martin"],
#     'Age': [16, 20, 60],
#     'City': ["New York", "Santa Blanca" , "Rio De Janiro"]
# })

books_df = pd.read_csv('moduli2/bestsellers_with_categories_2022_03_27.csv')

st.title('Best selling Books Analysis')
st.write('This app analyzes the Amazon top selling books.')

st.sidebar.header("Add New Book Data")
with st.sidebar.form("book_form"):
    new_name = st.text_input("book name")
    new_author = st.text_input("Author name")
    new_user_rating = st.slider("User Rating", 0.5,5.0, 0.0, 0.1)
    new_review = st.number_input('Review', min_value=0, step=1)
    new_price = st.number_input('Price', min_value=0, step=1)
    new_year = st.number_input('Year', min_value=2009, max_value=2022)
    new_Genre = st.selectbox("Genre", books_df['Genre'].unique())
    submit_button = st.form_submit_button(label="Add Book")

if submit_button:
    new_data = {
        'Name': new_name,
        'Author': new_author,
        'User Rating': new_user_rating,
        'Reviews': new_review,
        'Price': new_price,
        'Year': new_year,
        'Genre': new_Genre
    }
    books_df = pd.concat([pd.DataFrame(new_data, index=[0]), books_df], ignore_index=True)
    books_df.to_csv('moduli2/bestsellers_with_categories_2022_03_27.csv', index=False)
    st.sidebar.success("New Book Added successfully")

st.sidebar.header("filter Options")
selected_author = st.sidebar.selectbox("Select Author", ['All'] +list(books_df['Author'].unique()))
selected_Year = st.sidebar.selectbox("Select Year", ['All'] +list(books_df['Year'].unique()))
selected_genre = st.sidebar.selectbox("Select Genre", ['All'] +list(books_df['Genre'].unique()))
min_rating = st.sidebar.slider("Minimum User Rating", 0.5,5.0,0.0,0.1)
max_price = st.sidebar.slider("Maximum Price", 0, books_df['Price'].max(), books_df['Price'].max())

filtered_Book_df = books_df.copy()

if selected_author != "All":
    filtered_Book_df = filtered_Book_df[filtered_Book_df['Author'] == selected_author]
if selected_Year != "All":
    filtered_Book_df = filtered_Book_df[filtered_Book_df['Year'] == selected_Year]
if selected_genre != "All":
    filtered_Book_df = filtered_Book_df[filtered_Book_df['Genre'] == selected_genre]

filtered_Book_df = filtered_Book_df[( filtered_Book_df['User Rating'] >= min_rating) & filtered_Book_df['Price'] <= max_price]



st.subheader('Summary List')
total_books = books_df.shape[0]
unique_titles = books_df['Name'].nunique()
average_rating = books_df['User Rating'].mean()
average_price = books_df['Price'].mean()

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Books", total_books)
col2.metric("Unique Titles", unique_titles)
col3.metric("Average Rating", f"{average_rating:.2f}")
col4.metric("Average price", f"{average_price:.2f}")

st.subheader("Dataset Preview")
st.write(books_df.head())

col1, col2 = st.columns(2)

with col1:
    st.subheader("Top 10 Book Titles")
    top_titles = books_df['Name'].value_counts().head(10)
    st.bar_chart(top_titles)

with col2:
    st.subheader("Top 10 Authors")
    top_authors = books_df['Author'].value_counts().head(10)
    st.bar_chart(top_authors)

st.subheader("Genre Distribution")
fig = px.pie(books_df, names='Genre', title='Most liked genre', color='Genre', color_discrete_sequence=px.colors.sequential.Plasma)

st.plotly_chart(fig)

###