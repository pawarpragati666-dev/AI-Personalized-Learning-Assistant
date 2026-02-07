import streamlit as st
import pandas as pd
import plotly.express as px
from ai_engine import analyze_performance, predict_performance
from quiz_data import quiz_questions

from data_manager import load_data, save_data

# Custom CSS styling
st.markdown("""
<style>
.main {
    background-color: #f5f7fb;
}

.stButton>button {
    background-color: #4CAF50;
    color: white;
    font-weight: bold;
    border-radius: 8px;
}

.stTextInput>div>div>input {
    border-radius: 8px;
}

.stSidebar {
    background-color: #1e3a8a;
    color: white;
}

h1, h2, h3 {
    color: #1e3a8a;
}
</style>
""", unsafe_allow_html=True)

# Page settings
st.set_page_config(page_title="AI Personalized Learning Assistant", layout="wide")

# Sidebar
st.sidebar.title("🎓 AI Learning Assistant")
menu = st.sidebar.selectbox(
    "Navigation",
    ["Dashboard", "Performance", "Recommendations", "Roadmap", "Quiz", "Student Data", "Profile"]
)




# Main title
st.title("🎓 AI Personalized Learning Assistant")

# Student input
name = st.text_input("Enter Student Name")

python_marks = st.slider("Python Marks", 0, 100, 50)
dbms_marks = st.slider("DBMS Marks", 0, 100, 50)
ai_marks = st.slider("AI Marks", 0, 100, 50)

# ✅ Save button MUST come AFTER inputs
if st.button("Save Student Data"):

    if name.strip() == "":
        st.error("Please enter student name")

    else:
        save_data(name, python_marks, dbms_marks, ai_marks)
        st.success("Student data saved successfully!")

# Data for charts
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
            st.error(f"{subject}: Weak - {info['roadmap']}")

        elif info["level"] == "Average":
            st.warning(f"{subject}: Average - {info['roadmap']}")

        else:
            st.success(f"{subject}: Strong - {info['roadmap']}")

elif menu == "Roadmap":

    st.subheader("AI Learning Roadmap")

    results = analyze_performance(python_marks, dbms_marks, ai_marks)

    for subject, info in results.items():

        st.write(f"### {subject}")
        st.write(f"Level: {info['level']}")
        st.write(f"Roadmap: {info['roadmap']}")

    st.subheader("Performance Prediction")

    prediction = predict_performance(python_marks, dbms_marks, ai_marks)

    st.info(prediction)

# Student Data page
elif menu == "Student Data":

    st.subheader("Student Records")

    df_students = load_data()

    st.dataframe(df_students)

# Profile page
elif menu == "Profile":

    st.subheader("Student Profile")

    st.write("Name:", name)
    st.write("Course: MCA")

elif menu == "Quiz":

    st.subheader("AI Knowledge Quiz")

    score = 0

    for i, q in enumerate(quiz_questions):

        st.write(f"Q{i+1}: {q['question']}")

        answer = st.radio(
            "Select answer:",
            q["options"],
            key=i
        )

        if answer == q["answer"]:
            score += 1

    if st.button("Submit Quiz"):
        st.success(f"Your Score: {score}/{len(quiz_questions)}")

        if score == len(quiz_questions):
            st.balloons()
