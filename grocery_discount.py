import streamlit as st

def grocery(order):
    discount = 25 if order > 200 else 0
    disc_amt = discount * order / 100
    tax = 0.07 * (order - disc_amt)
    return disc_amt, tax

# Streamlit app
st.title("Grocery Discount Calculator")

# Description
st.write("""
This app calculates the discount and tax for your grocery order.

- Orders above $200 receive a 25% discount.
- A 7% tax is applied to the discounted amount.
""")

st.write("---")  # Adds a horizontal line for better separation

# Input for order amount
order = st.number_input("Enter the amount of your order ($)", min_value=0.0, step=0.01, value=0.0)

# Calculate Discount and Tax
if order > 0:
    discount, tax = grocery(order)
    total = order - discount + tax
    st.write(f"**Order Amount**: ${order:.2f}")
    st.write(f"**Discount**: ${discount:.2f}")
    st.write(f"**Tax**: ${tax:.2f}")
    st.write(f"**Total Amount**: ${total:.2f}")
else:
    st.write("Please enter a valid order amount.")

# Additional Information
st.write("---")
st.write("""
**Note**: 
- The discount is applied only to orders above $200.
- The tax is calculated on the amount after the discount is applied.
""")
