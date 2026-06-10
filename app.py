import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title
st.title("Business Data Analytics Dashboard")
st.write("Welcome to the Business Analytics Project Dashboard.")

# File Uploader
uploaded_file = st.file_uploader("Kripya analysis shuru karne ke liye ek CSV file upload karein.", type=["csv"])

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.success("File successfully upload ho gayi hai!")
    
    # Data Preview
    st.subheader("Data Preview")
    st.dataframe(data.head())
    
    # Description
    st.subheader("Data Summary Statistics")
    st.write(data.describe())
    
    # Interactive Chart
    st.subheader("Interactive Data Chart")
    columns = data.columns.tolist()
    selected_col = st.selectbox("Chart ke liye column chunein:", columns)
    
    # Bar Chart plot
    if st.button("Generate Chart"):
        fig, ax = plt.subplots()
        data[selected_col].value_counts().plot(kind='bar', ax=ax)
        plt.title(f"{selected_col} ka Distribution")
        plt.ylabel("Count")
        st.pyplot(fig)