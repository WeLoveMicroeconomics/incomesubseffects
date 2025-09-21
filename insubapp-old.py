import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Income & Substitution Effects Visualizer", layout="wide")

st.title("Income & Substitution Effects Visualizer")

# Load your existing interactive HTML file
with open("IncomeSubEffects.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# Embed the HTML with interactive JS inside Streamlit
components.html(html_content, height=750, scrolling=True)
