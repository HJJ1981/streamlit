import streamlit as st

def fare(d):
    book = 2.0
    start = 3.0
    cost = 1.0
    fare = book + start + d * cost
    return fare

# Streamlit app
st.title("Fare Calculator")

# Description
st.write("""
This app calculates the fare for a journey based on the distance traveled.

The fare is calculated using the following components:
- Booking Fee: $2.00
- Starting Fee: $3.00
- Cost per Kilometer: $1.00

The total fare is given by the formula:
**Fare = Booking Fee + Starting Fee + (Distance * Cost per Kilometer)**
""")

st.write("---")  # Adds a horizontal line for better separation

# Dropdown List for Distance Selection
distance_options = list(range(11))  # Generates a list of distances from 0 to 10 km
selected_distance = st.selectbox("Select the distance (in km)", distance_options)

# Calculate Fare
calculated_fare = fare(selected_distance)

# Display Result
st.write(f"The fare for a distance of {selected_distance} km is **${calculated_fare:.2f}**")

# Additional Information
st.write("---")
st.write("""
**Note**: 
- The fare calculation includes a fixed booking fee and a starting fee.
- The cost per kilometer is added based on the selected distance.
""")
