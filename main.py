from src.preprocess import load_and_prepare
from src.model import train_model, evaluate_model, save_model
from src.visualize import plot_results, feature_importance_plot
from src.report import generate_report

def main():
    X_train, X_test, y_train, y_test, feature_cols, df = load_and_prepare("data/traffic_data.csv")

    model = train_model(X_train, y_train)
    mae, rmse, r2, y_pred = evaluate_model(model, X_test, y_test)

    save_model(model, "artifacts/traffic_model.joblib")
    plot_results(y_test, y_pred)
    feature_importance_plot(model, feature_cols)
    generate_report(mae, rmse, r2)

    print("✅ Pipeline complete. Check artifacts and report.")

if __name__ == "__main__":
    main()
