import pandas as pd
from sklearn.model_selection import train_test_split
import yaml

def main():
    with open("configs/config.yaml", "r") as file:
        config = yaml.safe_load(file)

    dataset_path = config["dataset"]["path"]
    df = pd.read_csv(dataset_path)

    # print(df.head())
    # print(f"\nDataset Shape: {df.shape}")
    # print(f"\nDataset columns: {df.columns}")
    # print(f"\nDataset Data Types: \n{df.dtypes}")
    # print(f"\nStastical Summary: \n{df.describe()}")

    missing_values = df.isnull().sum()
    missing_values = missing_values[missing_values > 0]
    missing_values = missing_values.sort_values(
        ascending = False 
    )

    #print(f"\nColumns With Missing Values: \n{missing_values}")

    target_col = config["dataset"]["target"]
    y = df[target_col]

    #print(f"\nTarget variable summary: \n{y.describe()}")

    X = df.drop(columns=[target_col])

    #print(f"\nFeature matrix shape: \n{X.shape}")
    #print(f"\nTarget Vector shape: \n{y.shape}")

    X_train_val, X_test, y_train_val, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    #print(f"\nTrain + Validation feature shape: \n{X_train_val.shape}")
    #print(f"\nTest Feature shape: \n{X_test.shape}")

    X_train, X_val, y_train, y_val = train_test_split(
        X_train_val,
        y_train_val,
        test_size=0.125,
        random_state=42
    )

    #print(f"\nTrain feature shape: \n{X_train.shape}")
    #print(f"\nvalidation feature shape: \n{X_val.shape}")

    #print("\nTarget Split Shapes:")
    #print(f"y_train shape: {y_train.shape}")
    #print(f"y_val shape: {y_val.shape}")
    #print(f"y_test shape: {y_test.shape}")

    print("\nFirst Training Row:")
    print(X_train.head(1))


if __name__ == "__main__":
    main()