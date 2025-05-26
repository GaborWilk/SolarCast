import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="☀️ SolarCast", layout="wide")

st.title("SolarCast: Solar Power Forecasting in Hungary")


@st.cache_data
def load_data():
    return pd.read_csv("data/processed/merged_data.csv", parse_dates=["utc_timestamp"])


df = load_data()
st.line_chart(df.set_index("utc_timestamp")["HU_solar_generation_actual"])

st.markdown("---")

if st.button("Run Forecast"):
    model = joblib.load("models/solarcast_model.pkl")
    last_row = df.iloc[-1:]
    forecast = model.predict(last_row.drop(columns=["HU_solar_generation_actual"]))
    st.metric("Predicted Solar Output (next step)", f"{forecast[0]:.2f} MW")