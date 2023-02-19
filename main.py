import streamlit as st

st.set_page_config(layout="wide")

photo_col, desc_col = st.columns(2)

with photo_col:
    st.image("images/profilephoto.jpg")

with desc_col:
    st.title("Chaitanya Chintala")
    content = """
    Hi, I am Chaitanya Chintala! I am a Big Data Analyst, Python programmer, Oracle Apps R12 Developer, Oracle PLSQL Developer and so on. I graduated in 2003 with a Bachelor of Computer Applications from the Nagarjuna University,Guntur,Andhra Pradesh, India.
    I have worked with the various companies like Virtusa Corporation,HCL,Randstad India(Oracle India),CSS Technergy(Currently known as Cosyn) and so on. Working as Industrious Senior Consultant with excellent critical thinking and team-building talents. Familiar with the policies and procedures of product development and operations.
    """
    st.info(content)





