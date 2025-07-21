import streamlit as st

st.markdown("## 📱 Connect with Me")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <a href="https://www.linkedin.com/in/ankuj-saha-700260218/" target="_blank">
        <div style="background-color:#0077B5;padding:15px;border-radius:10px;text-align:center;">
            <span style="color:white;font-size:18px;font-weight:bold;">🔗 LinkedIn</span>
        </div>
    </a>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <a href="https://github.com/Ankuj999" target="_blank">
        <div style="background-color:#333;padding:15px;border-radius:10px;text-align:center;">
            <span style="color:white;font-size:18px;font-weight:bold;">💻 GitHub</span>
        </div>
    </a>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <a href="mailto:ankujsaha920@gmail.com">
        <div style="background-color:#34A853;padding:15px;border-radius:10px;text-align:center;">
            <span style="color:white;font-size:16px;font-weight:bold;">📧 Email</span>
        </div>
    </a>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <a href="tel:+91 9863123537">
        <div style="background-color:#F4B400;padding:15px;border-radius:10px;text-align:center;">
            <span style="color:white;font-size:16px;font-weight:bold;">📞 Phone</span>
        </div>
    </a>
    """, unsafe_allow_html=True)