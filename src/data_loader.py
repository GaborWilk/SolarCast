import pandas as pd


def load_energy_data(filepath: str) -> pd.DataFrame:
    df = pd.read_excel(filepath)
    df['utc_timestamp'] = pd.to_datetime(df['utc_timestamp'])
    return df


def load_weather_data(filepath: str) -> pd.DataFrame:
    df = pd.read_csv(filepath, sep=';')
    df['utc_timestamp'] = df['Date'].str.split('/').str[0]
    df['utc_timestamp'] = pd.to_datetime(df['utc_timestamp'])
    df.drop(columns=['Date'], inplace=True)
    return df


def merge_datasets(energy_df, weather_df) -> pd.DataFrame:
    df = energy_df.join(weather_df, how="inner")
    df = df.dropna()
    return df
