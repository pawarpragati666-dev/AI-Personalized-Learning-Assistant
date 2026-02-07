import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="AI Learning Assistant", layout="wide")

st.title("🎓 AI Personalized Learning Assistant")

name = st.text_input("Enter Student Name")

python_marks = st.slider("Python Marks", 0, 100, 50)
dbms_marks = st.slider("DBMS Marks", 0, 100, 50)
ai_marks = st.slider("AI Marks", 0, 100, 50)

if st.button("Analyze Performance"):

    data = {
        "Subject": ["Python", "DBMS", "AI"],
        "Marks": [python_marks, dbms_marks, ai_marks]
    }

    df = pd.DataFrame(data)

    st.subheader("Performance Chart")
    fig = px.bar(df, x="Subject", y="Marks", color="Marks")
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("AI Recommendations")

    if python_marks < 50:
        st.warning("Improve Python skills")

    if dbms_marks < 50:
        st.warning("Improve DBMS skills")

    if ai_marks < 50:
        st.warning("Improve AI skills")

    if python_marks >= 50 and dbms_marks >= 50 and ai_marks >= 50:
        st.success("Excellent performance!")
