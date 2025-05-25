import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

from config import APP_TITLE, DEFAULT_SLIDER_DAYS
from components import render_header, render_upload_section, render_plot_section

st.set_page_config(page_title=APP_TITLE, layout="wide")

render_header()

uploaded_file = render_upload_section()

if uploaded_file:
    df = pd.read_csv(uploaded_file, parse_dates=['date'])

    if 'generation' not in df.columns or 'date' not in df.columns:
        st.error("The CSV must contain 'date' and 'generation' columns.")
    else:
        df['day_of_year'] = df['date'].dt.dayofyear
        df['year'] = df['date'].dt.year

        render_plot_section(df)

        X = df[['day_of_year']]
        y = df['generation']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

        model = LinearRegression()
        model.fit(X_train, y_train)
        predictions = model.predict(X_test)

        st.write(f"Model MSE: {mean_squared_error(y_test, predictions):.2f}")

        forecast_days = st.slider("Days to Forecast", 1, 365, DEFAULT_SLIDER_DAYS)
        future = pd.DataFrame({'day_of_year': range(1, forecast_days + 1)})
        future['forecast'] = model.predict(future)

        st.subheader("Forecasted Solar Generation")
        plt.figure(figsize=(10, 4))
        plt.plot(future['day_of_year'], future['forecast'], label="Forecast")
        plt.xlabel("Day of Year")
        plt.ylabel("Predicted Generation (kWh)")
        plt.legend()
        st.pyplot(plt)