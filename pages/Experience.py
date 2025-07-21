import streamlit as st

st.set_page_config(page_title="Experience")

st.title("💼 Experience")

# Internship at NIT Rourkela
st.subheader("📌 Summer Internship – National Institute of Technology Rourkela")
st.image("images/NITR.jpg", caption="Research Intern", width=300)
st.markdown("""
**Topic**: Intrusion Detection using Machine Learning  
**Duration**: 16th May'25 - 4th July'25  
**Description**: Worked on Intrusion detection using supervised ML models on IoMT Network.  
[🔗 Research Paper Link](https://example.com/your-research-paper-link)
""")

st.markdown("---")

# AAI Internship
st.subheader("✈️ Training Cum Internship – Airports Authority of India (AAI)")
st.image("images/AAI.jpg", caption="AAI Agartala Airport", use_container_width=True)
st.markdown("""
**Domain**: Air Traffic Services and Radar Communication  
**Duration**: June'24 – July'24  
**Description**: Learned about airport radar communication, navigational aids, and control tower operations.
""")

st.markdown("---")

# BIS Workshop
st.subheader("📚 Workshop – Bureau of Indian Standards (BIS)")
st.image("images/BIS.jpg", caption="BIS One-Day Workshop", use_container_width=True)
st.markdown("""
**Event**: 1-Day Awareness Workshop on Standardization & Quality Practices  
**Date**: 10th January'24  
**Takeaway**: Gained insights into national standards, certification processes, and quality benchmarking.
""")
