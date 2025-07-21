import streamlit as st


st.subheader("📜 Certifications")

col1, col2 = st.columns(2)

with col1:
    st.image("images/FG.jpg", caption="Flipkart Grid 6.0", use_container_width=True)
    st.markdown("**Flipkart Grid 5.0 - Software Development Challenge**")

with col2:
    st.image("images/Deloitte.jpg", caption="Forage Virtual Internship", use_container_width=True)
    st.markdown("**Data Analyst Virtual Internship – Forage (Deloitte)**")
