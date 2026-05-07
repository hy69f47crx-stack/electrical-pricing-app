import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="برنامج التسعير الكهربائي",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ── CSS: hide Streamlit chrome (safe, targeted selectors only) ───────────────
st.markdown("""
<style>
  /* Core chrome */
  #MainMenu  { visibility: hidden !important; display: none !important; }
  footer     { visibility: hidden !important; display: none !important; }
  header     { visibility: hidden !important; display: none !important; }

  /* Toolbars */
  [data-testid="stToolbar"]              { display: none !important; }
  [data-testid="stDecoration"]           { display: none !important; }
  [data-testid="stStatusWidget"]         { display: none !important; }
  [data-testid="stToolbarButton"]        { display: none !important; }
  [data-testid="toolbarButtonContainer"] { display: none !important; }
  [data-testid="stHeader"]               { display: none !important; }

  /* Deploy / Manage-app buttons */
  .stDeployButton                        { display: none !important; }
  [data-testid="manage-app-button"]      { display: none !important; }
  [data-testid="stAppToolbar"]           { display: none !important; }
  .stAppToolbar                          { display: none !important; }
  button[title="Manage app"]             { display: none !important; }
  button[aria-label="Manage app"]        { display: none !important; }

  /* Community Cloud badge */
  .viewerBadge                           { display: none !important; }
  [data-testid="stHostedBadge"]          { display: none !important; }
  #badge-container                       { display: none !important; }

  /* Layout – remove padding */
  .stMain               { padding: 0 !important; margin: 0 !important; }
  .stMainBlockContainer { padding: 0 !important; margin: 0 !important;
                          max-width: 100% !important; width: 100% !important; }
  .element-container    { padding: 0 !important; margin: 0 !important; }
  iframe                { margin: 0 !important; padding: 0 !important; }
  body                  { margin: 0 !important; padding: 0 !important; }
  .stSidebar            { display: none !important; }
  .stAppViewContainer   { overflow: hidden !important; }
</style>
""", unsafe_allow_html=True)

# Read and render the app
try:
    html_content = Path("pricing-app.html").read_text(encoding="utf-8")
    st.components.v1.html(html_content, height=1080, scrolling=False)
except FileNotFoundError:
    st.error("❌ pricing-app.html not found")

# ── JS: hide "Manage app" by text content, safely ───────────────────────────
# Only hides elements whose EXACT visible text is "Manage app" or "Manage App".
# Does NOT walk up ancestors (avoids accidentally hiding the app iframe wrapper).
# Uses MutationObserver so it catches dynamically injected elements.
st.markdown("""
<script>
(function () {
  function hideManageApp() {
    document.querySelectorAll(
      'button, a, [role="button"], [class*="stActionButton"]'
    ).forEach(function (el) {
      // Skip anything inside an iframe (can't reach anyway, but be safe)
      if (el.closest('iframe')) return;

      var txt   = (el.textContent || '').trim().toLowerCase();
      var label = (el.getAttribute('aria-label') || '').toLowerCase();
      var title = (el.title || '').toLowerCase();

      if (
        txt   === 'manage app' ||
        label === 'manage app' ||
        title === 'manage app'
      ) {
        el.style.setProperty('display', 'none', 'important');

        // Hide the immediate wrapper ONLY if it contains no iframe
        var p = el.parentElement;
        if (p && !p.querySelector('iframe') && p !== document.body) {
          p.style.setProperty('display', 'none', 'important');
        }
      }
    });

    // Also hide the bottom-right panel that wraps the button (Streamlit Cloud)
    // Strategy: find any fixed/absolute element whose ONLY visible text is
    // "Manage app" (the whole panel, not just the button).
    document.querySelectorAll('div, section, aside').forEach(function (el) {
      if (el.closest('iframe')) return;
      try {
        var s = window.getComputedStyle(el);
        if (s.position !== 'fixed' && s.position !== 'absolute') return;
        var rect = el.getBoundingClientRect();
        // Must be in the bottom-right corner, small, not the app iframe
        if (
          rect.top  > window.innerHeight * 0.7 &&
          rect.left > window.innerWidth  * 0.6 &&
          rect.height < 120 &&
          rect.width  < 300 &&
          !el.querySelector('iframe')
        ) {
          el.style.setProperty('display', 'none', 'important');
        }
      } catch (e) {}
    });
  }

  hideManageApp();
  setInterval(hideManageApp, 800);

  var obs = new MutationObserver(hideManageApp);
  function startObs() {
    obs.observe(document.body, { childList: true, subtree: true });
  }
  if (document.body) { startObs(); }
  else { document.addEventListener('DOMContentLoaded', startObs); }
})();
</script>
""", unsafe_allow_html=True)
