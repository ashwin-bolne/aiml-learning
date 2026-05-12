from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer

numeric_pipeline = Pipeline(
    steps=[
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler()),
    ]
)

categorical_pipeline = Pipeline(
    steps=[
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("encoder", OneHotEncoder(handle_unknown="ignore")),
    ]
)

def make_preprocessor(
        numeric_cols: list[str],
        categorical_cols: list[str],
) -> ColumnTransformer:
    """
    Create a preprocessing pipeline for numeric and categorical features.

    Args:
        numeric_cols: List of numeric column names.
        categorical_cols: List of categorical column names.

    Returns:
        Configured sklearn ColumnTransformer object.
    """
    preprocessor = ColumnTransformer(
        transformers=[
            ("num", numeric_pipeline, numeric_cols),
            ("cat", categorical_pipeline, categorical_cols),
        ]
    )

    return preprocessor