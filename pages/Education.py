import streamlit as st

st.set_page_config(page_title="Education", page_icon="🎓", layout="centered")

# Title and header
st.title("🎓 Education Background")

# Spacer
st.markdown("<br>", unsafe_allow_html=True)

# College Section
st.subheader("🏫 National Institute of Technology Agartala")
st.image("images/NIT Agartala.jpg", caption="NIT Agartala Campus", use_container_width=True)

st.markdown("""
**Degree**: B.Tech in Electronics and Communication Engineering  
**University**: NIT Agartala (Central Government Institute)  
**Year of Study**: 2022 – 2026  
**Current CGPA**: 7.34   
""")

# Spacer
st.markdown("---")

# School Section
st.subheader("🏫 Pranavananda Vidya Mandir")
st.image("images/PVM.jpg", caption="Pranavananda Vidya Mandir", use_container_width=True)

st.markdown("""
**Board**: CBSE (Central Board of Secondary Education)

- **Matriculation (Class X)**  
  **Year**: 2020  
  **Percentage**: 86.4%

- **Higher Secondary (Class XII)**  
  **Year**: 2022  
  **Percentage**: 91.8%  
  **Stream**: Science (PCM with Informatics Practices(Python,Sql,Basic Networking))
""")
