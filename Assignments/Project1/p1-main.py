import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')
df = pd.read_csv("Assignments\Project1\data.csv", sep=',')

st.title("The Best Company")
content='''
Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation. Python is dynamically-typed and garbage-collected. It supports multiple programming paradigms, including structured, object-oriented and functional programming. 
'''
st.write(content)
st.header("Our Team")

col1, emp1, col2, emp2, col3 = st.columns([1.5, 0.5, 1.5, 0.5, 1.5])

with col1:
    for index, row in df[:4].iterrows():
        st.header(f"{row['first name'].capitalize()} {row['last name'].capitalize()}")
        st.write(row['role'])
        st.image(f"Assignments\Project1\images\{row['image']}")


with col2:
    for index, row in df[4:8].iterrows():
        st.header(f"{row['first name'].capitalize()} {row['last name'].capitalize()}")
        st.write(row['role'])
        st.image(f"Assignments\Project1\images\{row['image']}")

with col3:
    for index, row in df[8:].iterrows():
        st.header(f"{row['first name'].capitalize()} {row['last name'].capitalize()}")
        st.write(row['role'])
        st.image(f"Assignments\Project1\images\{row['image']}")

