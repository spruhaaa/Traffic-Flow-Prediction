import pandas as pd
from sklearn.model_selection import train_test_split

def make_lags(data, col="speed_kph", lags=[1,2,3]):
    for lag in lags:
        data[f"{col}_lag{lag}"] = data[col].shift(lag)
    return data

def load_and_prepare(path):
    df = pd.read_csv(path, parse_dates=["timestamp"])

    df = df.groupby("segment_id", group_keys=False).apply(make_lags, col="speed_kph", lags=[1,2,3])
    df = df.dropna().reset_index(drop=True)

    feature_cols = [
        "length_km","temp_c","rain_mm","is_event","is_holiday","is_weekend",
        "occupancy","flow","incidents","dayofweek","hour",
        "speed_kph_lag1","speed_kph_lag2","speed_kph_lag3"
    ]

    X = df[feature_cols]
    y = df["speed_kph"]

    return train_test_split(X, y, test_size=0.2, shuffle=False) + (feature_cols, df)
