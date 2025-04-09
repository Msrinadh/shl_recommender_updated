import streamlit as st
from extract import extract_text_from_url
from recommend_core import get_recommendations

st.title("🔍 SHL Assessment Recommendation Engine")

input_type = st.radio("Input type", ["Job Description Text", "Job Description URL"])

if input_type == "Job Description Text":
    user_input = st.text_area("Paste Job Description", height=200)
else:
    url_input = st.text_input("Paste JD URL")
    user_input = extract_text_from_url(url_input)
    st.text_area("Extracted JD", value=user_input, height=200)

if st.button("Get Recommendations"):
    if user_input.strip():
        results = get_recommendations(user_input)
        st.success(f"Top {len(results)} Recommendations:")
        for _, row in results.iterrows():
            st.markdown(f"""
            ### [{row['assessment_name']}]({row['url']})
            - 🕒 Duration: {row['duration']}
            - 🧪 Type: {row['test_type']}
            - 💻 Remote Testing: {row['remote_testing']}
            - 🧠 Adaptive/IRT: {row['adaptive_support']}
            - 📝 Description: {row['description']}
            """)
    else:
        st.warning("Please enter valid input.")