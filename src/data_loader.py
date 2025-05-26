import pandas as pd


def load_energy_data(filepath: str) -> pd.DataFrame:
    df = pd.read_csv(filepath, parse_dates=["utc_timestamp"])
    df = df[df["HU_solar_generation_actual"] > 0]  # Trim zeros
    df = df.set_index("utc_timestamp").sort_index()
    return df


def load_weather_data(filepath: str) -> pd.DataFrame:
    df = pd.read_csv(filepath, comment="#", parse_dates=[0])
    df.columns = [
        "timestamp", "TOA", "ClearSky_GHI", "ClearSky_BHI", "ClearSky_DHI",
        "ClearSky_BNI", "GHI", "BHI", "DHI", "BNI", "Reliability"
    ]
    df = df.set_index("timestamp").sort_index()
    return df


def merge_datasets(energy_df, weather_df) -> pd.DataFrame:
    df = energy_df.join(weather_df, how="inner")
    df = df.dropna()
    return df
