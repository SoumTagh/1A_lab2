import pandas as pd
import streamlit as st

# display widgets
st.title("Streamlit Widgets Test")
st.header("Testing core capabilities")
st.markdown(
    "Here's a test of different types of interactive elements !"
)

st.divider()  # this adds a visual line separator

# input widgets
st.subheader("Interactive Input Testing")

# setting up two columns side-by-side to organize elements cleanly
col1, col2 = st.columns(2)

with col1:
    user_text = st.text_input("Type something here :", "Hello Streamlit!")
    user_number = st.number_input(
        "Select a number:", min_value=0, max_value=100, value=26
    )
    is_checked = st.checkbox("Enable premium visualizations")

with col2:
    app_genre = st.selectbox(
        "Choose an app category:",
        ["Productivity", "Finance", "Medical", "Developer Tools"],
    )
    rating_slider = st.slider(
        "Filter by minimum rating:", min_value=1.0, max_value=5.0, value=4.0
    )
    is_toggled = st.toggle("Dark mode simulation")

st.divider()

# streamlit magic
st.subheader("Streamlit Magic commands")

# creating a small dataframe to simulate a scraped data
data = {
    "title": ["App A", "App B", "App C"],
    "rating": [4.5, 3.8, rating_slider],  # this connects dynamically to the slider above
    "type": ["Free", "Paid", "Free"],
}
df = pd.DataFrame(data)


"#### Live Dataframe Output (Magic):"
df

"#### Live Inputs Summary (Magic):"
f"You typed: **{user_text}** | Selected Category: **{app_genre}** | Min Rating: **{rating_slider}**"