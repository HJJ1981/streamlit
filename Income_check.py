import streamlit as st

st.title("Income Level Checker")

# Description
st.write("""
This app helps you determine your income level based on your monthly income.
Enter your income below to see which category you fall into.
""")

# Input for income with a minimum value of 0
income = st.number_input("Enter your monthly income ($)", min_value=0.0, step=100.0, value=2000.0)

# Button to trigger the check
if st.button("Check Income Level"):
    if income > 8000:
        result = "High income"
        color = "green"
    elif income > 4000:
        result = "Medium high income"
        color = "lightgreen"
    elif income > 2000:
        result = "Medium income"
        color = "yellow"
    elif income > 1000:
        result = "Medium low income"
        color = "orange"
    else:
        result = "Low income"
        color = "red"

    # Display result with color
    st.markdown(f"Based on your income of ${income:.2f}, your income level is: "
                f"<span style='color:{color};font-weight:bold;'>{result}</span>", 
                unsafe_allow_html=True)

    # Additional information
    st.write("""
    Income Levels:
    - Low income: $0 - $1,000
    - Medium low income: $1,001 - $2,000
    - Medium income: $2,001 - $4,000
    - Medium high income: $4,001 - $8,000
    - High income: $8,001 and above
    """)

# Disclaimer
st.write("---")
st.write("""
**Disclaimer**: This is a simplified income level categorization and may not reflect official economic classifications. 
It's meant for illustrative purposes only.
""")
