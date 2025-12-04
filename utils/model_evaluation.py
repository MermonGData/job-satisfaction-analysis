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

    df = pd.DataFrame(list(metrics.items()), columns=["Metric", "Value"])
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

def plot_residuals_grid(trained_models_dict, comparison_df, dataset_name, y_test, 
                        n_models=4, figsize=(14, 10)):
    #Create a grid of residual plots for top models in a specific dataset
    dataset_models = comparison_df[comparison_df["Dataset"] == dataset_name].head(n_models)

    models_dict = trained_models_dict[dataset_name]
    
    n_rows = int(np.ceil(n_models / 2))
    n_cols = 2 if n_models > 1 else 1
    fig, axes = plt.subplots(n_rows, n_cols, figsize=figsize)
    
    #Flattening axes
    if n_models > 1:
        axes = axes.flatten()
    else:
        axes = [axes]
    
    for i in range(len(dataset_models), len(axes)):
        axes[i].set_visible(False)
    
    for ax, (_, row) in zip(axes, dataset_models.iterrows()):
        model_name = row["Model"]
        
        entry = models_dict[model_name]
        model = entry["model"]
        
        if "y_pred" in entry:
            y_pred = entry["y_pred"]
        else:
            X_test = entry["X_test"]
            y_pred = model.predict(X_test)
        
        residuals = y_test.values - y_pred
        
        ax.scatter(y_pred, residuals, alpha=0.6, edgecolor='k', s=50)
        ax.axhline(0, color='red', linestyle='--', linewidth=2)
        ax.set_xlabel("Fitted values", fontsize=11)
        ax.set_ylabel("Residuals", fontsize=11)
        ax.set_title(f"{model_name}\n({dataset_name})", fontsize=12, fontweight='bold')
        
        r2 = r2_score(y_test, y_pred)
        rmse = np.sqrt(np.mean(residuals**2))
        ax.text(0.05, 0.95, f"R² = {r2:.3f}\nRMSE = {rmse:.3f}", 
                transform=ax.transAxes, verticalalignment='top',
                bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))
    
    plt.tight_layout()
    return fig, axes