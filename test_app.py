import pandas as pd
import streamlit as st
from datetime import date, time

st.set_page_config(page_title="Streamlit Widgets", page_icon="🧪", layout="wide")

# display widgets
st.title("Streamlit Widgets")
st.header("Display Widgets")
st.subheader("Subheader")
st.text("hello streamlit")
st.markdown("**Bold**, *italic*, `code`, [link](https://streamlit.io)")
st.code("print('hello')", language="python")
st.latex(r"E = mc^2")
st.divider()

# input widgets 
st.header("Input Widgets")
col1, col2, col3 = st.columns(3)

with col1:
    user_text = st.text_input("Text input", "Hello Streamlit!")
    user_area = st.text_area("Text area", "Today, I feel...")

with col2:
    user_number = st.number_input("Number input", min_value=0, max_value=100, value=26)
    user_date = st.date_input("Date input", value=date.today())
    user_time = st.time_input("Time input", value=time(9, 0))

with col3:
    uploaded_file = st.file_uploader("File uploader", type=["csv"])
    camera_snap = st.camera_input("Camera input")

st.divider()

# filter widgets 
st.header("Filter Widgets")
col4, col5 = st.columns(2)

with col4:
    is_checked = st.checkbox("Checkbox")
    is_toggled = st.toggle("Toggle")
    payment = st.radio("Radio", ["Free", "Paid"])
    app_genre = st.selectbox("Selectbox", ["Productivity", "Finance", "Medical"])
    rating_min = st.slider("Slider", min_value=1.0, max_value=5.0, value=4.0, step=0.1)

with col5:
    selected_genres = st.multiselect("Multiselect", ["Productivity", "Finance", "Medical"], default=["Productivity"])
    install_range = st.select_slider("Select slider", options=["<1K", "1K–10K", "10K–100K", "1M+"], value=("<1K", "10K–100K"))

st.divider()

# button widgets 
st.header("Button Widgets")
col6, col7, col8 = st.columns(3)

with col6:
    st.button("Click on this button")

with col7:
    st.download_button("Download a csv file", data="title,rating\nApp A,4.5", file_name="sample.csv", mime="text/csv")

with col8:
    st.link_button("Streamlit link", "https://streamlit.io")

st.divider()

# data widgets
st.header("Data Widgets")

df = pd.DataFrame({
    "Title":    ["App A", "App B", "App C"],
    "Rating":   [4.5, 3.8, rating_min],
    "Type":     [payment, "Paid", "Free"],
    "Installs": [500_000, 1_200_000, 80_000],
})

st.dataframe(df, use_container_width=True)
st.table(df[["Title", "Rating"]])
st.data_editor(df, num_rows="dynamic")
st.color_picker("Color picker", "#008CFF")

st.divider()

# Streamlit Magic 
st.header("Streamlit Magic")

df

f"Text: {user_text} | Genre: {app_genre} | Rating: {rating_min}"

st.divider()

# layouts & containers 
st.header("Layouts & Containers")

tab1, tab2 = st.tabs(["Table", "Chart"])
with tab1:
    st.dataframe(df)
with tab2:
    st.bar_chart(df.set_index("Title")["Rating"])

with st.expander("Show raw data"):
    st.json(df.to_dict())

with st.container(border=True):
    st.write("This is a container")

main_col, side_col = st.columns([2, 1])
with main_col:
    st.bar_chart(df.set_index("Title")["Installs"])
with side_col:
    st.metric("Total apps", len(df))
    st.metric("Avg rating", f"{df['Rating'].mean():.2f}")

# sidebar 
st.sidebar.title("Sidebar")
st.sidebar.selectbox("Filter by type", ["All", "Free", "Paid"])
st.sidebar.slider("Max results", 5, 50, 10)