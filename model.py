import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

def train_model(X_train, y_train):
    model = RandomForestRegressor(n_estimators=80, random_state=42, n_jobs=-1)
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    r2 = r2_score(y_test, y_pred)
    print(f"📊 MAE: {mae:.2f}, RMSE: {rmse:.2f}, R2: {r2:.3f}")
    return mae, rmse, r2, y_pred

def save_model(model, path):
    joblib.dump(model, path)
    print(f"✅ Model saved at {path}")
