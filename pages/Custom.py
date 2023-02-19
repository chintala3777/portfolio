import streamlit as st
import pandas

contact_content = """
Below you can find some of apps i have built in python. Feel free to contact me!
"""
st.subheader(contact_content)

py_proj1, empty_col, py_proj2 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")

with py_proj1:
    for index, row in df[:10].iterrows():
        st.subheader(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with py_proj2:
    for index, row in df[10:].iterrows():
        st.subheader(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")
