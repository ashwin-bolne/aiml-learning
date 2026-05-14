from pathlib import Path 

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import (
    LinearRegression,
    Lasso,
    Ridge,
    )
from metrics_practice import evaluate_regression

import matplotlib.pyplot as plt


def main() -> None:

    plots_dir = Path("plots")
    plots_dir.mkdir(exist_ok=True)

    # 1. Load dataset
    data_path = Path("data/house_prices.csv")
    df = pd.read_csv(data_path)

    # 2. Basic dataset inspection
    print(f"\nDataset Shape: {df.shape}")

    print(f"\nDataset head: \n{df.head()}")

    print(f"\nDataset Columns: \n{df.columns.tolist()}")

    print(f"\ndtypes: \n{df.dtypes}")

    print(f"\nMissing Values: \n{df.isnull().sum()}")
   
    # Preprocessing 
    
    # 3. Define target column
    target_column = "SalePrice"

    print(f"\nTarget Column: {target_column}")

    # 4. Select numeric columns only
    numeric_df = df.select_dtypes(include=["number"])


    # dropping missing values 
    numeric_df = numeric_df.dropna()
    print(f"\nDataset shape after dropping missing values rows: {numeric_df.shape}")

    # 5 Create Target vector (y)
    y = numeric_df[target_column]

    # 6. Create feature matrix (X)
    X = numeric_df.drop(columns=[target_column])

    # 7. Final verification
    print(f"\nFeature Matrix shape: {X.shape}")

    print(f"Target vecoter shape: {y.shape}")

    print(f"Number of Features: {X.shape[1]}")

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
    )

    print(f"X_train shape: {X_train.shape}")

    print(f"X_test shape: {X_test.shape}")

    print(f"y_train shape: {y_train.shape}")

    print(f"y_test shape: {y_test.shape}")

    model = LinearRegression()

    model.fit(X_train, y_train)

    train_predictions = model.predict(X_train)
    test_predictions = model.predict(X_test)

    train_r2 = model.score(X_train, y_train)
    test_r2 = model.score(X_test, y_test)

    print(f"\ntrain_r2: {train_r2}")
    print(f"test_r2: {test_r2}")

    train_metrics = evaluate_regression(
        y_true=y_train,
        y_pred=train_predictions,
        n_features=X_train.shape[1],
    )

    test_metrics = evaluate_regression(
    y_true=y_test,
    y_pred=test_predictions,
    n_features=X_test.shape[1],
    )

    print("\nTraining Metrics")
    print("-" * 40)

    for metric_name, metric_value in train_metrics.items():
        print(f"{metric_name}: {metric_value:.4f}")

    print("\nTest Metrics")
    print("-" * 40)

    for metric_name, metric_value in test_metrics.items():
        print(f"{metric_name}: {metric_value:.4f}")

    plt.figure(figsize=(8, 6))

    plt.scatter(
        y_test,
        test_predictions,
        alpha=0.7
    )

    plt.plot(
    [y_test.min(), y_test.max()],
    [y_test.min(), y_test.max()],
    linestyle="--",
    )

    plt.xlabel("Actual Prices")
    plt.ylabel("Predicted Prices")
    plt.title("Actual vs Predicted Prices")

    plot_path = plots_dir / "actual_vs_predicted.png"

    plt.savefig(plot_path)

    plt.show()

    residuals = y_test - test_predictions
    plt.figure(figsize=(8, 6))

    plt.scatter(
        test_predictions,
        residuals,
        alpha=0.7,
    )

    plt.axhline(
        y=0,
        linestyle="--"
    )

    plt.xlabel("Predicted Prices")
    plt.ylabel("Residuals")
    plt.title("Residuals vs Predicted Prices")

    plot_path = plots_dir / "residual_plot.png"

    plt.savefig(plot_path)
    
    plt.show()

    coefficients_df = pd.DataFrame({
    "feature": X_train.columns,
    "coefficient": model.coef_,
    })

    coefficients_df = coefficients_df.sort_values(
    by="coefficient",
    )

    plt.figure(figsize=(10, 12))

    plt.barh(
    coefficients_df["feature"],
    coefficients_df["coefficient"],
    )

    plt.xlabel("Coefficient Value")
    plt.ylabel("Features")
    plt.title("Linear Regression Feature Coefficients")
    plt.tight_layout()

    plot_path = plots_dir / "feature_coefficients.png"

    plt.savefig(plot_path)
    plt.show()


    ridge_model = Ridge(alpha=1.0)

    ridge_model.fit(X_train, y_train)

    ridge_predictions = ridge_model.predict(X_test)
   
    ridge_metrics = evaluate_regression(
    y_true=y_test,
    y_pred=ridge_predictions,
    n_features=X_test.shape[1],
    )

    print("\nRidge Regression Metrics")
    print("-" * 40)

    for metric_name, metric_value in ridge_metrics.items():
        print(f"{metric_name}: {metric_value:.4f}")


    lasso_model = Lasso(alpha=1.0)

    lasso_model.fit(X_train, y_train)

    lasso_predictions = lasso_model.predict(X_test)

    lasso_metrics = evaluate_regression(
    y_true=y_test,
    y_pred=lasso_predictions,
    n_features=X_test.shape[1],
    )

    print("\nLasso Regression Metrics")
    print("-" * 40)

    for metric_name, metric_value in lasso_metrics.items():
        print(f"{metric_name}: {metric_value:.4f}")




if __name__ == "__main__":
    main()