import streamlit as st
import matplotlib.pyplot as plt

def render_header():
    st.title("🔆 Solar Generation Forecasting App")
    st.markdown("Upload your data and forecast solar energy generation.")

def render_upload_section():
    st.sidebar.header("Upload CSV")
    return st.sidebar.file_uploader("Upload a file with 'date' and 'generation' columns", type="csv")

def render_plot_section(df):
    st.subheader("Historical Generation Data")
    plt.figure(figsize=(10, 4))
    plt.plot(df['date'], df['generation'], label='Actual')
    plt.xlabel("Date")
    plt.ylabel("Generation (kWh)")
    plt.title("Solar Generation Over Time")
    st.pyplot(plt)