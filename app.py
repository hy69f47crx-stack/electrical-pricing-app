import streamlit as st
from pathlib import Path

# Set page config - remove all padding
st.set_page_config(
    page_title="برنامج التسعير الكهربائي",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Hide streamlit UI elements and remove padding/margins
hide_streamlit_style = """
<style>
    /* Hide Streamlit elements */
    #MainMenu {visibility: hidden; display: none !important;}
    footer {visibility: hidden; display: none !important;}
    header {visibility: hidden; display: none !important;}

    /* Hide all Streamlit toolbars and controls */
    [data-testid="stToolbar"] {display: none !important;}
    [data-testid="stDecoration"] {display: none !important;}
    [data-testid="stStatusWidget"] {display: none !important;}
    .stStatusWidget {display: none !important;}

    /* Hide manage app button specifically */
    button[kind="secondary"]:last-of-type {display: none !important;}
    [data-testid="toolbarButtonContainer"] {display: none !important;}

    /* Hide any element with text 'manage' or 'Manage' */
    button[title*="anage"], button[aria-label*="anage"] {display: none !important;}

    /* Remove Streamlit padding and margins */
    .stMain {
        padding: 0 !important;
        margin: 0 !important;
    }

    .stMainBlockContainer {
        padding: 0 !important;
        margin: 0 !important;
        max-width: 100% !important;
        width: 100% !important;
    }

    /* Remove iframe padding */
    iframe {
        margin: 0 !important;
        padding: 0 !important;
    }

    /* Remove body padding */
    body {
        margin: 0 !important;
        padding: 0 !important;
    }

    /* Full width container */
    .element-container {
        padding: 0 !important;
        margin: 0 !important;
    }

    /* Hide any fixed/absolute positioned elements at bottom-right */
    [style*="bottom"], [style*="right"] {
        z-index: 0 !important;
    }

    /* Hide any tooltip or popup at bottom-right */
    .stToast, .stNotification {display: none !important;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Read the HTML file
try:
    html_content = Path("pricing-app.html").read_text(encoding="utf-8")
    # Display the app with full height and no scrolling
    st.components.v1.html(html_content, height=1080, scrolling=False)
except FileNotFoundError:
    st.error("❌ Error: pricing-app.html file not found!")
    st.info("Make sure pricing-app.html is in the same directory as app.py")
