import streamlit as st

st.title("Basic Calculator")

num1 = st.number_input("Enter your first number")
num2 = st.number_input("Enter your second number")

operation = st.selectbox("Choose Operation", ["add", "sub", "mul", "div"])

if st.button("Calculate"):
    if operation == "add":
        st.write("Result:", num1 + num2)
    elif operation == "sub":
        st.write("Result:", num1 - num2)
    elif operation == "mul":
        st.write("Result:", num1 * num2)
    elif operation == "div":
        if num2 != 0:
            st.write("Result:", num1 / num2)
        else:
            st.error("Cannot divide by zero")