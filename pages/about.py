import streamlit as st

st.subheader("This is about my consultancy about QNA")

if "shared" not in st.session_state:
   st.session_state["shared"] = True