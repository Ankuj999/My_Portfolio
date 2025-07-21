import streamlit as st
from PIL import Image
import base64

# Set up page configuration
st.set_page_config(page_title="Ankuj Saha Portfolio", page_icon="💼", layout="centered")

def set_bg_from_local(image_path):
    with open(image_path, "rb") as img_file:
        encoded = base64.b64encode(img_file.read()).decode()
    bg_image = f"""
    <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded}");
            background-size: cover;
            background-attachment: fixed;
            background-repeat: no-repeat;
            background-position: center;
        }}
    </style>
    """
    st.markdown(bg_image, unsafe_allow_html=True)

set_bg_from_local("background.png")

# Load image
img = Image.open(r"Ankuj.jpg")  # Use raw string for Windows paths

# Custom CSS
custom_css = """
<style>
    .custom-name {
        font-family: 'Algerian', cursive;
        font-size: 48px;
        font-weight: bold;
        color: #222222;
        text-align: center;
    }
    .custom-title {
        font-family: 'Algerian', cursive;
        font-size: 24px;
        color: #555555;
        text-align: center;
        margin-top: -10px;
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# Center layout using columns
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image(img, width=330)
    st.markdown("<div class='custom-name'>Ankuj Saha</div>", unsafe_allow_html=True)

# Full-width centered container to show entire line
st.markdown("""
<div style='
    font-family: Algerian, cursive;
    font-size: 18px;
    text-align: center;
    margin-top: -15px;
'>
    Emerging Data Analyst | Python&#8201;•&#8201;SQL&#8201;•&#8201;Power BI&#8201;•&#8201;Machine Learning
</div>
""", unsafe_allow_html=True)
st.markdown("""
<div style='
    font-family: Calibri, sans-serif;
    font-size: 16px;
    text-align: justify;
    text-justify: inter-word;
    color: #444444;
    margin-top: 33px;
    line-height: 1.6;
    max-width: 700px;
    margin-left: auto;
    margin-right: auto;
'>
    <span style='color: #003333; font-weight: bold;'>
    " Hello! I’m Ankuj Saha, currently residing in Agartala, Tripura(W). I come from an academic foundation in Electronics and Communication Engineering and have a keen interest in the field of Data Analytics. With hands-on experience in Python, SQL, Power BI, and Machine Learning, I focus on leveraging data to uncover insights and support informed decision-making. My goal is to apply structured problem-solving approaches and statistical techniques to solve real-world challenges. I am actively exploring opportunities that will allow me to grow as a Data Analyst and contribute meaningfully to data-driven projects in collaborative environments "
    </span>
</div>
""", unsafe_allow_html=True)


st.markdown("<br><br>", unsafe_allow_html=True)
st.title("📄 Portfolio Navigation")

# Custom styled buttons
button_css = """
<style>
div.stButton > button {
    width: 90%;
    height: 70px;
    margin: 10px 0;
    font-size: 20px;
    background-color: white !important;
    color: black !important;
    border: 2px solid #ccc;
    border-radius: 12px;
    font-family: Calibri, sans-serif;
}
</style>
"""
st.markdown(button_css, unsafe_allow_html=True)

# Navigation buttons using switch_page (Streamlit 1.25+)
if st.button("🎓 Education"):
    st.switch_page("pages/Education.py")

if st.button("💻 Projects"):
    st.switch_page("pages/Projects.py")    

if st.button("📌 Experience"):
    st.switch_page("pages/Experience.py")

if st.button("📜 Certifications"):
    st.switch_page("pages/Certifications.py")

if st.button("🌐 Contact & Links"):
    st.switch_page("pages/Social_Media.py")



st.markdown("<hr>", unsafe_allow_html=True)
st.markdown(
    """
    <div style='text-align: center; color: #6c757d; font-size: 24px; margin-top: 20px;'>
        Designed & Developed by <b>Ankuj Saha</b> | © 2025
    </div>
    """,
    unsafe_allow_html=True
)
