import pandas as pd 

from sklearn.model_selection import train_test_split
from src.preprocessor import make_preprocessor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import root_mean_squared_error


df = pd.read_csv("data/employees.csv")

print(f"Dataset: \n{df.head()}")

X = df.drop(columns=["target"])
y = df["target"]

print(f"\nFeatures: \n{X.head()}")
print(f"\nTarget: \n{y.head()}")

X_train, X_val, y_train, y_val = train_test_split(
    X, 
    y,
    test_size=0.2,
    random_state=42,
)

print("\nTrain shape: ", X_train.shape)
print("Validation shape: ", X_val.shape)

numeric_cols = X_train.select_dtypes(
    include=["int64", "float64"]
).columns.tolist()

categorical_cols = X_train.select_dtypes(
    include=["str"]
).columns.tolist()

print(f"\nNumeric Columns: \n{numeric_cols}")
print(f"\nCategorical Columns; \n{categorical_cols}")

preprocessor = make_preprocessor(
    numeric_cols=numeric_cols,
    categorical_cols=categorical_cols,
)

X_train_processed = preprocessor.fit_transform(X_train)
X_val_processed = preprocessor.transform(X_val)

print("\nProcessed Train Shape: ", X_train_processed.shape)
print("Processed Validation Shape: ", X_val_processed.shape)

correct_model = LinearRegression()

correct_model.fit(X_train_processed, y_train)

correct_predictions = correct_model.predict(X_val_processed)

correct_rmse = root_mean_squared_error(
    y_val,
    correct_predictions,
)

print(f"\nCorrect workflow RMSE: \n{correct_rmse}")

leaky_preprocessor = make_preprocessor(
    numeric_cols=numeric_cols,
    categorical_cols=categorical_cols,
)

X_full_processed = leaky_preprocessor.fit_transform(X)

X_train_leaky = X_full_processed[X_train.index]
X_val_leaky = X_full_processed[X_val.index]

leaky_model = LinearRegression()

leaky_model.fit(X_train_leaky, y_train)

leaky_predictions = leaky_model.predict(X_val_leaky)

leaky_rmse = root_mean_squared_error(
    y_val,
    leaky_predictions,
)

print("\nLeaky workflow RMSE: ")
print(leaky_rmse)