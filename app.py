import streamlit as st
from utils import extract_text_from_pdf
from model import predict_role, skill_gap, jd_match
import plotly.express as px

st.set_page_config(page_title="Resume AI", layout="wide")

st.title("AI Resume Screening System")

jd = st.text_area("Paste Job Description")

uploaded_file = st.file_uploader("Upload Resume", type=["pdf"])

if uploaded_file:

    text = extract_text_from_pdf(uploaded_file)

    role, scores = predict_role(text)

    matching, missing, score = skill_gap(text, role)

    if jd:
        match = jd_match(text, jd)
        st.write("JD Match Score:", match,"%")

    st.subheader("Prediction")
    st.write("Predicted Role:", role)
    st.write("Resume Score:", score,"%")

    st.progress(score/100)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Matching Skills")
        st.write(matching)

    with col2:
        st.subheader("Missing Skills")
        st.write(missing)

    fig = px.bar(
        x=list(scores.keys()),
        y=list(scores.values()),
        title="Role Prediction Confidence"
    )

    st.plotly_chart(fig)