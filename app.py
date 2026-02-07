import streamlit as st
import pandas as pd
import plotly.express as px
from ai_engine import analyze_performance


# Page settings
st.set_page_config(page_title="AI Personalized Learning Assistant", layout="wide")

# Sidebar
st.sidebar.title("🎓 AI Learning Assistant")
menu = st.sidebar.selectbox(
    "Navigation",
    ["Dashboard", "Performance", "Recommendations", "Profile"]
)

# Main title
st.title("🎓 AI Personalized Learning Assistant")

# Student input
name = st.text_input("Enter Student Name")

python_marks = st.slider("Python Marks", 0, 100, 50)
dbms_marks = st.slider("DBMS Marks", 0, 100, 50)
ai_marks = st.slider("AI Marks", 0, 100, 50)

# Data
data = {
    "Subject": ["Python", "DBMS", "AI"],
    "Marks": [python_marks, dbms_marks, ai_marks]
}

df = pd.DataFrame(data)

# Dashboard
if menu == "Dashboard":

    st.subheader("Student Overview")

    col1, col2, col3 = st.columns(3)

    col1.metric("Python", python_marks)
    col2.metric("DBMS", dbms_marks)
    col3.metric("AI", ai_marks)

# Performance page
elif menu == "Performance":

    st.subheader("Performance Chart")

    fig = px.bar(df, x="Subject", y="Marks", color="Marks")
    st.plotly_chart(fig, use_container_width=True)

# Recommendation page
elif menu == "Recommendations":

    st.subheader("AI Learning Recommendations")

    results = analyze_performance(python_marks, dbms_marks, ai_marks)

    for subject, info in results.items():

        if info["level"] == "Weak":
            st.error(f"{subject}: Weak - {info['recommendation']}")

        elif info["level"] == "Average":
            st.warning(f"{subject}: Average - {info['recommendation']}")

        else:
            st.success(f"{subject}: Strong - {info['recommendation']}")



# Profile page
elif menu == "Profile":

    st.subheader("Student Profile")

    st.write("Name:", name)
    st.write("Course: MCA")
