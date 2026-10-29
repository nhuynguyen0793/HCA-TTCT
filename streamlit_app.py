from pathlib import Path

import streamlit as st
from streamlit.components.v1 import html


st.set_page_config(
    page_title="HCA - Trung tâm Chính trị",
    layout="wide",
)

st.markdown(
    """
    <style>
    #MainMenu, header, footer { visibility: hidden; }
    [data-testid="stHeader"] { height: 0; }
    [data-testid="stToolbar"] { display: none; }
    [data-testid="stAppViewContainer"] { overflow: hidden; }
    [data-testid="stMain"] { padding: 0; }
    [data-testid="stMainBlockContainer"] {
        max-width: none;
        width: 100vw;
        padding: 0;
        margin: 0;
    }
    [data-testid="stVerticalBlock"] { gap: 0; }
    [data-testid="stIFrame"] {
        width: 100vw !important;
        height: 100vh !important;
        max-height: 100vh !important;
    }
    [data-testid="stIFrame"] iframe {
        width: 100vw !important;
        height: 100vh !important;
        border: 0 !important;
    }
    iframe { border: 0 !important; }
    </style>
    """,
    unsafe_allow_html=True,
)

html_template = Path(__file__).with_name("index.html")
html(html_template.read_text(encoding="utf-8"), height=900, scrolling=False)
