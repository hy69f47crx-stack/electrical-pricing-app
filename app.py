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
    /* ── Core Streamlit chrome ── */
    #MainMenu {visibility: hidden !important; display: none !important;}
    footer {visibility: hidden !important; display: none !important;}
    header {visibility: hidden !important; display: none !important;}

    /* ── Toolbars & decorations ── */
    [data-testid="stToolbar"]               {display: none !important;}
    [data-testid="stDecoration"]            {display: none !important;}
    [data-testid="stStatusWidget"]          {display: none !important;}
    [data-testid="stToolbarButton"]         {display: none !important;}
    [data-testid="toolbarButtonContainer"]  {display: none !important;}
    [data-testid="manage-app-button"]       {display: none !important;}
    [data-testid="stActionButton"]          {display: none !important;}
    [data-testid="stActionButtonIcon"]      {display: none !important;}

    /* ── Manage App / Deploy buttons (Streamlit Cloud) ── */
    .stDeployButton                         {display: none !important;}
    .stActionButton                         {display: none !important;}
    button[title="Manage app"]              {display: none !important;}
    button[aria-label="Manage app"]         {display: none !important;}
    button[title*="anage"]                  {display: none !important;}
    button[aria-label*="anage"]             {display: none !important;}
    a[href*="/manage"]                      {display: none !important;}

    /* ── Code / source viewer ── */
    button[aria-label="Code"]               {display: none !important;}
    button[title="Code"]                    {display: none !important;}
    button[aria-label*="code"]              {display: none !important;}
    button[title*="code"]                   {display: none !important;}
    div[data-testid="stCode"]               {display: none !important;}
    .streamlit-code-viewer                  {display: none !important;}

    /* ── Community Cloud badge / watermark ── */
    .viewerBadge                            {display: none !important;}
    .css-5rimss                             {display: none !important;}
    .ef3psqc11                              {display: none !important;}
    #badge-container                        {display: none !important;}
    [data-testid="stHostedBadge"]           {display: none !important;}
    [data-testid="community-cloud-badge"]   {display: none !important;}
    a[href*="streamlit.io"]                 {display: none !important;}
    a[href*="share.streamlit"]              {display: none !important;}

    /* ── Remove all padding / margin ── */
    .stMain                  {padding: 0 !important; margin: 0 !important;}
    .stMainBlockContainer    {padding: 0 !important; margin: 0 !important; max-width: 100% !important; width: 100% !important;}
    .element-container       {padding: 0 !important; margin: 0 !important;}
    iframe                   {margin: 0 !important; padding: 0 !important;}
    body                     {margin: 0 !important; padding: 0 !important;}

    /* ── Sidebar / misc ── */
    .stSidebar               {display: none !important;}
    .stAppViewContainer      {overflow: hidden !important;}
    .stToast, .stNotification{display: none !important;}
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

# JS — continuously hide any Streamlit chrome that loads dynamically
st.markdown("""
<script>
(function() {
  function hideStreamlitChrome() {
    const selectors = [
      '[data-testid="stToolbar"]',
      '[data-testid="stStatusWidget"]',
      '[data-testid="stToolbarButton"]',
      '[data-testid="manage-app-button"]',
      '[data-testid="stActionButton"]',
      '[data-testid="stHostedBadge"]',
      '[data-testid="community-cloud-badge"]',
      '.stDeployButton',
      '.viewerBadge',
      '#badge-container',
    ];
    selectors.forEach(sel => {
      document.querySelectorAll(sel).forEach(el => el.style.setProperty('display','none','important'));
    });
    // Buttons by text / title
    document.querySelectorAll('button').forEach(btn => {
      const t = (btn.textContent + (btn.title || '') + (btn.getAttribute('aria-label') || '')).toLowerCase();
      if (t.includes('manage') || t.includes('code') || t.includes('deploy')) {
        btn.style.setProperty('display','none','important');
      }
    });
    // Links to streamlit.io / share.streamlit
    document.querySelectorAll('a').forEach(a => {
      if (a.href && (a.href.includes('streamlit.io') || a.href.includes('share.streamlit'))) {
        a.style.setProperty('display','none','important');
      }
    });
  }
  // Run on load and periodically
  document.addEventListener('DOMContentLoaded', hideStreamlitChrome);
  setInterval(hideStreamlitChrome, 800);
})();
</script>
""", unsafe_allow_html=True)
