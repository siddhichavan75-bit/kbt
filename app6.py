import streamlit as st
from datetime import date

st.title("User Details Form")

with st.form("user_form"):
    
    first_name = st.text_input("First Name")
    last_name = st.text_input("Last Name")
    dob = st.date_input(
        "Date of Birth",
        value=None,   # No default date
        min_value=date(1900, 1, 1)
    )
    
    submit = st.form_submit_button("Submit")

if submit:
    if not first_name or not last_name or dob is None:
        st.error("Please fill all fields.")
    else:
        st.success("Form Submitted Successfully")
        st.write("First Name:", first_name)
        st.write("Last Name:", last_name)
        st.write("Date of Birth:", dob)