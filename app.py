import streamlit as st
import pandas
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Personal Portfolio", layout="wide")

selected = option_menu(
    menu_title=None,
    options=["Home", "Custom Projects", "Contact Me"],
    orientation="horizontal",
)

hide_st_style = """
                <style>
                 #MainMenu {visibility: hidden;}
                 footer {visibility: hidden;}
                 header {visibility: hidden;}
                 </style>   
                """

st.markdown(hide_st_style, unsafe_allow_html=True)

if selected == "Home":
    photo_col, desc_col = st.columns(2)
    with photo_col:
        st.image("images/profilephoto.png", width=380)
    with desc_col:
        st.title("Chaitanya Chintala")

        st.download_button(label='Download Resume',
                           data=open('images/Chaitanya_Chintala_Resume.pdf', 'rb').read(),
                           file_name='images/Chaitanya_Chintala_Resume.pdf',
                           mime='images/Chaitanya_Chintala_Resume.pdf')

        desc_content = """
        Hi, I am Chaitanya! 4 years Working experience as Industrious Senior Consultant with excellent critical thinking and team-building talents.Having total 18 years of IT experience in Multi-tasking Consultant well-known for successfully taking projects from beginning stages to completion. I am a Big Data Analyst, Python programmer, Oracle Apps R12 Developer, Oracle PLSQL Developer and so on. I graduated in 2003 with a Bachelor of Computer Applications from the Nagarjuna University,Guntur,Andhra Pradesh, India.
        I have worked with the various companies like Virtusa Corporation (Current Company),HCL,Randstad India (Client : Oracle India),CSS Technergy Limited (Currently known as Cosyn)
        """
        st.info(desc_content)

    st.subheader("Work History")

    year_vir, desc_vir = st.columns(2)

    with year_vir:
        st.subheader("Mar-2017 - Currently Working")
        st.subheader("Company : [Virtusa Corporation](https://virtusa.com)")

    with desc_vir:
        st.subheader("Desination : Senior Consultant")
        st.write(
            """
            - ✔️ Analyzed problematic areas to provide recommendations and solutions.
            - ✔️ Determined areas for improvement and implemented processes to alleviate problems.
            - ✔️ Monitored technology use and program functionality, updating programs and making changes to enhance output.
            - ✔️ Assessed needs for projects and made proposals to senior executives.
            - ✔️ Exceeded customer requirements with accurate and deliverable solutions.
            """
        )

    year_hcl, desc_hcl = st.columns(2)

    with year_hcl:
        st.subheader("Apr-2014 - Feb-2017")
        st.subheader("Company : [HCL Technologies](https://www.hcltech.com/)")

    with desc_hcl:
        st.subheader("Desination : Senior Developer")
        st.write(
            """
            - ✔️ Produced robust, accurate code that minimized production issues.
            - ✔️ Designed updates to existing software to meet changing customer demands.
            - ✔️ Developed programs from ground up using measured, market-focused approach to eliminate waste and streamline implementation cycle.
            - ✔️ Worked with users to gather requirements and evaluate ease of use.
            - ✔️ Evaluated project requirements and specifications and developed software applications that surpassed client expectations.
            - ✔️ Discussed project progress with customers, collected feedback on different stages and directly addressed concerns.
            """
        )
    year_ora, desc_ora = st.columns(2)

    with year_ora:
        st.subheader("Jul-2012 - Feb-2014")
        st.subheader("Company : [Ranstad India](https://www.randstad.in/)")

    with desc_ora:
        st.subheader("Desination : PL/SQL Developer")
        st.write(
            """
            - ✔️ Analyzed existing SQL queries to identify opportunities for improvements.
            - ✔️ Created optimal technical solutions to user needs with in-depth system analysis.
            - ✔️ Maintained complex Oracle-SQL queries, views and stored procedures in multi-database environment with little supervision.
            - ✔️ Documented analysis results and provided performance improvement feedback.
            - ✔️ Designed and implemented Oracle queries for reporting and complex solution development.
            - ✔️ Analyzed business reports for prompt communication, follow-up and ongoing support.
            - ✔️ Developed, implemented and optimized stored procedures and functions using PL/SQL.
            - ✔️ Resolved complex business issues, proposing long-term solutions to avoid repeat problems.
            - ✔️ Followed standard practices for migrating changes to test and production environments.
            """
        )
    year_cs, desc_cs = st.columns(2)

    with year_cs:
        st.subheader("Oct-2004 - Jun-2012")
        st.subheader("Company : [CSS Technergy Limited](http://cosyn.in/)")

    with desc_cs:
        st.subheader("Desination : Programmer")
        st.write(
            """
            - ✔️ Worked with software development and testing team members to design and develop robust solutions to meet client requirements for functionality, scalability, and performance.
            - ✔️ Tested server code to validate code changes.
            - ✔️ Improved software efficiency by creating automated scripts and tools.
            - ✔️ Created databases, data entry systems, and other applications for diverse uses.
            - ✔️ Analyzed, reviewed and revised programs to increase operating efficiency.
            """
        )
if selected == "Custom Projects":
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

if selected == "Contact Me":
    st.header("hhhhhhhhh")