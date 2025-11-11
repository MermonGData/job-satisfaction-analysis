import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import mean_absolute_error, root_mean_squared_error, r2_score


def evaluate_regression_metrics_df(y_true, y_pred, warn=True):
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)

    diffs = y_true - y_pred
    abs_diffs = np.abs(diffs)
    pct_diffs = abs_diffs / np.maximum(np.abs(y_true), 1e-8)
    pct_diff_squared = ((diffs / np.maximum(np.abs(y_true), 1e-8)) ** 2)

    if warn and np.any(np.abs(y_true) < 1e-6):
        print("Warning: `y_true` contains near-zero values - MAPE and RMSPE may be unstable.")

    mse = root_mean_squared_error(y_true, y_pred)
    mae = mean_absolute_error(y_true, y_pred)
    rmse = np.sqrt(mse)

    metrics = {
        "MSE": mse,
        "RMSE": rmse,
        "RMSPE [%]": np.sqrt(np.mean(pct_diff_squared)) * 100,
        "MAE": mae,
        "MAPE [%]": np.mean(pct_diffs) * 100, 
        "R²": r2_score(y_true, y_pred),
        "Korelacja Pearsona": np.corrcoef(y_true, y_pred)[0, 1]
    }

    df = pd.DataFrame(list(metrics.items()), columns=["Metryka", "Wartość"])
    return df.round(4)

def plot_residuals(y_true, y_pred):
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)

    residuals = y_true - y_pred

    # Histogram
    plt.figure(figsize=(6, 4))
    sns.histplot(residuals, kde=True, bins=30, color='steelblue')
    plt.axvline(0, color='red', linestyle='--', linewidth=1)
    plt.title("Residuals Distribution")
    plt.xlabel("Residual")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.show()

def plot_residuals_vs_fitted(model, X_test, y_true, title="Residuals vs Fitted"):
    y_pred = model.predict(X_test)
    residuals = y_true - y_pred
    
    plt.scatter(y_pred, residuals, alpha=0.6, edgecolor='k')
    plt.axhline(0, color='red', linestyle='--', linewidth=1)
    plt.xlabel("Fitted values (Predicted satisfaction)")
    plt.ylabel("Residuals")
    plt.title(title)