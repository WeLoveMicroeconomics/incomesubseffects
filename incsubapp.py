import streamlit as st
import streamlit.components.v1 as components
import time

st.set_page_config(page_title="Income & Substitution Effects Visualizer", layout="wide")

st.title("Income & Substitution Effects Visualizer")

with st.spinner("Loading visualization..."):
    with open("income_visualizer.html", "r", encoding="utf-8") as f:
        html_content = f.read()
    # simulate tiny delay if needed
    time.sleep(0.5)

components.html(html_content, height=750, scrolling=True)

st.success("Ready!")
