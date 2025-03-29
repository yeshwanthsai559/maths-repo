import streamlit as st

def main():
    st.title("Simple Addition App")
    
    # User input for two numbers
    num1 = st.number_input("Enter 1st number", value=0.0, step=1.0)
    num2 = st.number_input("Enter second number", value=0.0, step=1.0)
    
    # Perform addition
    result = num1 + num2

    # User input for two numbers
    num1 = st.number_input("Enter first number", value=0.0, step=1.0)
    num2 = st.number_input("Enter second number", value=0.0, step=1.0)
    
    # Perform addition
    result1 = num1 - num2
    
    # Display result
    if st.button("Add"):
        st.success(f"The sum is: {result}")

        # Display result
    if st.button("subtract"):
        st.success(f"The difference is: {result1}")

if __name__ == "__main__":
    main()
