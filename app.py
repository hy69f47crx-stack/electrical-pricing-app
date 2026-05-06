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

    /* Hide manage app button and code button specifically */
    button[kind="secondary"]:last-of-type {display: none !important;}
    [data-testid="toolbarButtonContainer"] {display: none !important;}
    [data-testid="stToolbarButton"] {display: none !important;}
    button[aria-label*="code"] {display: none !important;}
    button[title*="code"] {display: none !important;}

    /* Hide Streamlit's code viewer and code button */
    div[data-testid="stCode"] {display: none !important;}
    .streamlit-code-viewer {display: none !important;}
    .streamlit-container code {display: none !important;}

    /* Hide code/source button from Streamlit */
    button[aria-label="Code"] {display: none !important;}
    button[title="Code"] {display: none !important;}
    a[href*="code"] {display: none !important;}

    /* Hide any element with 'code' text */
    button:nth-child(n) {
        visibility: visible !important;
    }

    /* Specifically target and hide the code snippet viewer */
    .streamlit-expanderContent {display: none !important;}
    [role="dialog"] {display: none !important;}

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

    /* Universal bottom-right element hiding */
    *[style*="bottom:"] {display: none !important;}
    *[style*="right:"] {display: none !important;}
    *[style*="bottom"] {display: none !important;}
    *[style*="right"] {display: none !important;}

    /* Hide any fixed/absolute positioned elements at bottom-right */
    [style*="bottom"], [style*="right"] {
        display: none !important !important;
        visibility: hidden !important;
        z-index: 0 !important;
    }

    /* Aggressive hiding of all bottom-right positioned elements */
    div[style*="position"], div[style*="bottom"], div[style*="right"],
    button[style*="bottom"], button[style*="right"] {
        display: none !important;
    }

    /* Hide any tooltip or popup at bottom-right */
    .stToast, .stNotification {display: none !important;}

    /* Hide Streamlit sidebar and controls */
    .stSidebar {display: none !important;}
    .stAppViewContainer {overflow: hidden !important;}

    /* Hide watermark and branding */
    .css-5rimss {display: none !important;}
    .ef3psqc11 {display: none !important;}
    .viewerBadge {display: none !important;}
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

# Add JavaScript to hide any code buttons or panels
st.markdown("""
<script>
// Remove code button and any code-related UI from Streamlit
document.addEventListener('DOMContentLoaded', function() {
    // Hide any button with code-related text or attributes
    document.querySelectorAll('button').forEach(btn => {
        if (btn.textContent.toLowerCase().includes('code') ||
            btn.getAttribute('aria-label')?.toLowerCase().includes('code') ||
            btn.getAttribute('title')?.toLowerCase().includes('code')) {
            btn.style.display = 'none';
        }
    });

    // Hide code dialogs/modals
    document.querySelectorAll('[role="dialog"]').forEach(dialog => {
        dialog.style.display = 'none';
    });
});

// Also check periodically for any dynamically added elements
setInterval(() => {
    document.querySelectorAll('button').forEach(btn => {
        if (btn.textContent.toLowerCase().includes('code')) {
            btn.style.display = 'none';
        }
    });
}, 500);
</script>
""", unsafe_allow_html=True)
