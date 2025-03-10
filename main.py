import streamlit as st

st.set_page_config(page_title="Homepage", page_icon="🏠")

st.title("Python for JS Developers")
st.write("A personal notes.")

st.divider()

st.page_link("pages/introduction-to-python.py", label="Introduction to Python", icon="1️⃣")
st.page_link("pages/functions-and-control-flow.py", label="Functions and Control Flow in Python", icon="2️⃣")
st.page_link("pages/working-with-files.py", label="Working with Files in Python", icon="3️⃣")
st.page_link("pages/oop.py", label="OOP in Python", icon="4️⃣")
st.page_link("pages/django-installation.py", label="Django Installation", icon="5️⃣")
