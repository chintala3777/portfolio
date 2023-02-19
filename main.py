import streamlit as st
import pandas

st.set_page_config(layout="wide")

photo_col, desc_col = st.columns(2)

with photo_col:
    st.image("images/profilephoto.png",width=300)

with desc_col:
    st.title("Chaitanya Chintala")
    desc_content = """
    Hi, I am Chaitanya! I am a Big Data Analyst, Python programmer, Oracle Apps R12 Developer, Oracle PLSQL Developer and so on. I graduated in 2003 with a Bachelor of Computer Applications from the Nagarjuna University,Guntur,Andhra Pradesh, India.
    I have worked with the various companies like Virtusa Corporation,HCL,Randstad India(Oracle India),CSS Technergy(Currently known as Cosyn) and so on. Working as Industrious Senior Consultant with excellent critical thinking and team-building talents. Familiar with the policies and procedures of product development and operations.
    """
    st.info(desc_content)

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




