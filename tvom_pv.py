import streamlit as st

def time_value_money(FV, interest_rate, period):
    PV = FV / ((1 + interest_rate) ** period)
    return PV

# Streamlit app
st.title("Present Value Calculator")

# Description
st.write("""
This app calculates the Present Value (PV) of a future sum using the Time Value of Money principle.

The Time Value of Money (TVM) concept recognizes that a dollar today is worth more than a dollar in the future due to its potential earning capacity.

This calculator uses the formula:
PV = FV / (1 + r)^n

Where:
- PV is the Present Value (what we're calculating)
- FV is the Future Value
- r is the interest rate per period (as a decimal)
- n is the number of periods
""")

st.write("---")  # Adds a horizontal line for better separation

# Input fields
FV = st.number_input("Future Value (FV)", min_value=0.0, value=1000.0, step=100.0)
interest_rate = st.number_input("Interest Rate (as a decimal)", min_value=0.0, max_value=1.0, value=0.05, step=0.01)
period = st.number_input("Number of Periods", min_value=1, value=10, step=1)

# Calculate Present Value
if st.button("Calculate Present Value"):
    PV = time_value_money(FV, interest_rate, period)
    st.write(f"The present value is: ${PV:.2f}")
    st.markdown(f"This means that ${FV:.2f} in {period} periods from now is worth ${PV:.2f} today, assuming an interest rate of **{interest_rate:.2%}** per period.")

# Additional information
st.write("---")
st.write("""
**Note**: 
- The interest rate should be entered as a decimal (e.g., 0.05 for 5%).
- This calculation assumes interest is compounded once per period.
- Make sure the interest rate and number of periods use the same time frame (e.g., both annual or both monthly).
- The Present Value (PV) represents the amount you would need to invest today to reach the specified Future Value (FV) given the interest rate and time period.
""")
