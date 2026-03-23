import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide", page_title="ARC - Aspect Ratio Calculator", initial_sidebar_state="collapsed")

st.markdown("""
<style>
/* Remove Streamlit default paddings */
.block-container {
    padding-top: 0rem;
    padding-bottom: 0rem;
    max-width: 100%;
}
</style>
""", unsafe_allow_html=True)

try:
    with open("index.html", "r", encoding="utf-8") as f:
        html_data = f.read()
    
    # Render the HTML/JS dashboard
    components.html(html_data, height=1300, scrolling=True)
    
except FileNotFoundError:
    st.error("Error: index.html not found. Make sure the file exists in the same directory as app.py.")
