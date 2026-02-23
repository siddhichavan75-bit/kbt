import streamlit as st

st.title("simple chatbot")

que=st.text_input("Ask me anything")

if st.button("send"):
    st.write("you asked",que)
    st.write("i will reply soon")