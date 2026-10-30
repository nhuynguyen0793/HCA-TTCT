from pathlib import Path

import streamlit as st
from streamlit.components.v1 import html


st.set_page_config(
    page_title="HCA - Trung tâm Chính trị",
    page_icon="🗺️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
    html, body {
        overflow: hidden !important;
        height: 100vh !important;
        margin: 0 !important;
        padding: 0 !important;
    }
    #MainMenu, header, footer,
    [data-testid="stHeader"],
    [data-testid="stToolbar"],
    [data-testid="stStatusWidget"] {
        display: none !important;
        height: 0 !important;
    }
    [data-testid="stAppViewContainer"],
    [data-testid="stMain"] {
        height: 100vh !important;
        max-height: 100vh !important;
        overflow: hidden !important;
    }
    [data-testid="stMain"] {
        padding: 0 !important;
    }
    [data-testid="stMainBlockContainer"] {
        width: 100vw !important;
        max-width: none !important;
        height: 100vh !important;
        padding: 0 !important;
        margin: 0 !important;
    }
    [data-testid="stVerticalBlock"],
    [data-testid="stVerticalBlockBorderWrapper"],
    [data-testid="stElementContainer"],
    [data-testid="stIFrame"] {
        width: 100vw !important;
        height: 100vh !important;
        max-height: 100vh !important;
        margin: 0 !important;
        padding: 0 !important;
        gap: 0 !important;
    }
    [data-testid="stIFrame"] iframe,
    iframe {
        width: 100vw !important;
        height: 100vh !important;
        max-height: 100vh !important;
        border: 0 !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

html_template = Path(__file__).with_name("index.html")
html(html_template.read_text(encoding="utf-8"), height=0, scrolling=False)
