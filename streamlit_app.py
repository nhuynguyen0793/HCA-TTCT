from pathlib import Path

import streamlit as st
from streamlit.components.v1 import html


st.set_page_config(
    page_title="HCA - Trung tâm Chính trị",
    layout="wide",
)

html_template = Path(__file__).with_name("index.html")
html(html_template.read_text(encoding="utf-8"), height=900, scrolling=True)
