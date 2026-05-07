import streamlit as st
from pathlib import Path

# Set page config - remove all padding
st.set_page_config(
    page_title="برنامج التسعير الكهربائي",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ── CSS: hide every known Streamlit chrome element ──────────────────────────
hide_streamlit_style = """
<style>
    /* Core chrome */
    #MainMenu                               { visibility: hidden !important; display: none !important; }
    footer                                  { visibility: hidden !important; display: none !important; }
    header                                  { visibility: hidden !important; display: none !important; }

    /* Headers / toolbars */
    [data-testid="stHeader"]                { display: none !important; }
    [data-testid="stToolbar"]               { display: none !important; }
    [data-testid="stDecoration"]            { display: none !important; }
    [data-testid="stStatusWidget"]          { display: none !important; }
    [data-testid="stToolbarButton"]         { display: none !important; }
    [data-testid="toolbarButtonContainer"]  { display: none !important; }

    /* Manage App button — every known testid / class */
    [data-testid="manage-app-button"]       { display: none !important; }
    [data-testid="stActionButton"]          { display: none !important; }
    [data-testid="stActionButtonIcon"]      { display: none !important; }
    [data-testid="stAppToolbar"]            { display: none !important; }
    .stAppToolbar                           { display: none !important; }
    .stDeployButton                         { display: none !important; }
    .stActionButton                         { display: none !important; }
    button[title="Manage app"]              { display: none !important; }
    button[aria-label="Manage app"]         { display: none !important; }
    button[title*="anage"]                  { display: none !important; }
    button[aria-label*="anage"]             { display: none !important; }
    a[href*="/manage"]                      { display: none !important; }

    /* Streamlit emotion-cache — targets fixed/absolute Streamlit overlays
       (class names are hashed but always start with st-emotion-cache) */
    [class^="st-emotion-cache"][style*="position: fixed"]  { display: none !important; }
    [class^="st-emotion-cache"][style*="position:fixed"]   { display: none !important; }
    [class*="st-emotion-cache"][data-testid]               { display: none !important; }

    /* Community Cloud badge / watermark */
    .viewerBadge                            { display: none !important; }
    .css-5rimss                             { display: none !important; }
    .ef3psqc11                              { display: none !important; }
    #badge-container                        { display: none !important; }
    [data-testid="stHostedBadge"]           { display: none !important; }
    [data-testid="community-cloud-badge"]   { display: none !important; }
    a[href*="streamlit.io"]                 { display: none !important; }
    a[href*="share.streamlit"]              { display: none !important; }

    /* Code viewer */
    button[aria-label="Code"]               { display: none !important; }
    button[title="Code"]                    { display: none !important; }
    button[aria-label*="code"]              { display: none !important; }
    div[data-testid="stCode"]               { display: none !important; }

    /* Layout — remove all padding */
    .stMain                { padding: 0 !important; margin: 0 !important; }
    .stMainBlockContainer  { padding: 0 !important; margin: 0 !important; max-width: 100% !important; width: 100% !important; }
    .element-container     { padding: 0 !important; margin: 0 !important; }
    iframe                 { margin: 0 !important; padding: 0 !important; }
    body                   { margin: 0 !important; padding: 0 !important; }
    .stSidebar             { display: none !important; }
    .stAppViewContainer    { overflow: hidden !important; }
    .stToast, .stNotification { display: none !important; }
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Read the HTML file
try:
    html_content = Path("pricing-app.html").read_text(encoding="utf-8")
    st.components.v1.html(html_content, height=1080, scrolling=False)
except FileNotFoundError:
    st.error("❌ Error: pricing-app.html file not found!")
    st.info("Make sure pricing-app.html is in the same directory as app.py")

# ── JS: position-aware + text-aware Streamlit chrome remover ────────────────
# Runs on load, every 600 ms, AND on every DOM mutation.
# Three strategies so it works regardless of Streamlit version:
#   1. Known data-testid / class selectors
#   2. Button text / title matching ("Manage app", "Deploy", "Code")
#   3. Position scan: any fixed element that sits in the bottom portion of
#      the viewport and is small enough to be a floating badge/button
st.markdown("""
<script>
(function () {
  'use strict';

  var TESTIDS = [
    'stHeader','stToolbar','stDecoration','stStatusWidget',
    'stToolbarButton','manage-app-button','stActionButton',
    'stActionButtonIcon','stAppToolbar','stHostedBadge',
    'community-cloud-badge','toolbarButtonContainer'
  ];

  var CLASSES = [
    '.stDeployButton','.stAppToolbar','.stActionButton',
    '.viewerBadge','#badge-container'
  ];

  function hide(el) {
    if (el) el.style.setProperty('display', 'none', 'important');
  }

  function nukeChrome() {
    // 1. data-testid
    TESTIDS.forEach(function(id) {
      document.querySelectorAll('[data-testid="' + id + '"]').forEach(hide);
    });

    // 2. class / id selectors
    CLASSES.forEach(function(sel) {
      try { document.querySelectorAll(sel).forEach(hide); } catch(e) {}
    });

    // 3. Buttons / links by text or title
    document.querySelectorAll('button, a').forEach(function(el) {
      var text  = (el.textContent  || '').toLowerCase().trim();
      var label = (el.getAttribute('aria-label') || '').toLowerCase();
      var title = (el.title        || '').toLowerCase();
      var href  = (el.href         || '');
      if (
        text  === 'manage app' ||
        label.includes('manage') || title.includes('manage') ||
        label.includes('deploy') || title.includes('deploy') ||
        href.includes('streamlit.io') || href.includes('share.streamlit')
      ) {
        hide(el);
        // Also hide up to 4 ancestor wrappers
        var p = el.parentElement;
        for (var i = 0; i < 4 && p && p !== document.body; i++) {
          hide(p);
          p = p.parentElement;
        }
      }
    });

    // 4. Position scan — any fixed element in the bottom 35% of viewport
    //    that is small (badge / toolbar sized), not our iframe
    var vh = window.innerHeight;
    document.querySelectorAll('div, section, aside, nav').forEach(function(el) {
      if (el.tagName === 'IFRAME') return;
      try {
        var s = window.getComputedStyle(el);
        if (s.position === 'fixed') {
          var r = el.getBoundingClientRect();
          if (r.top > vh * 0.65 && r.height < 200 && r.width < 500) {
            hide(el);
          }
        }
      } catch(e) {}
    });
  }

  // Run immediately and every 600 ms
  nukeChrome();
  setInterval(nukeChrome, 600);

  // MutationObserver: catches elements injected after initial render
  var observer = new MutationObserver(nukeChrome);
  function startObserver() {
    observer.observe(document.body, { childList: true, subtree: true });
  }
  if (document.body) {
    startObserver();
  } else {
    document.addEventListener('DOMContentLoaded', startObserver);
  }
})();
</script>
""", unsafe_allow_html=True)
