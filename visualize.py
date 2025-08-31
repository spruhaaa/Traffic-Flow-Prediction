import matplotlib.pyplot as plt
import pandas as pd

def plot_results(y_test, y_pred):
    plt.figure(figsize=(6,6))
    plt.scatter(y_test, y_pred, alpha=0.5)
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], "r--")
    plt.xlabel("Actual Speed"); plt.ylabel("Predicted Speed")
    plt.title("Actual vs Predicted (Test Set)")
    plt.tight_layout()
    plt.savefig("artifacts/fig_scatter.png")
    plt.close()

def feature_importance_plot(model, feature_cols):
    imp = pd.Series(model.feature_importances_, index=feature_cols).sort_values(ascending=False)
    plt.figure(figsize=(8,4))
    imp.plot(kind="bar")
    plt.title("Feature Importance")
    plt.ylabel("Importance")
    plt.tight_layout()
    plt.savefig("artifacts/fig_feature_importance.png")
    plt.close()
