import streamlit as st
import pandas as pd
import joblib
import os

DATA_PATH = os.path.join("data", "processed")

st.set_page_config(page_title="SolarCast", layout="wide")
st.title("☀️ SolarCast: Solar Power Forecasting in Hungary")


@st.cache_data
def load_data():
    return pd.read_csv(os.path.join(DATA_PATH, "merged_data.csv"), parse_dates=["utc_timestamp"])


df = load_data()
st.line_chart(df.set_index("utc_timestamp")["generation_actual"])

st.markdown("---")

if st.button("Run Forecast"):
    model = joblib.load("models/solarcast_model.pkl")
    last_row = df.iloc[-1:]
    forecast = model.predict(last_row.drop(columns=["generation_actual"]))
    st.metric("Predicted Solar Output (next step)", f"{forecast[0]:.2f} MW")