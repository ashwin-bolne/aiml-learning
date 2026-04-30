import seaborn as sns
import pandas as pd

AGE_BINS = [0, 18, 60, 100]
AGE_LABELS = ["child", "adult", "senior"]


def drop_high_null_columns(df: pd.DataFrame, thresold: float = 0.5) -> pd.DataFrame:
    """
    Drops columns where null percentage exceeds thresold
    """
    nulls_pct = df.isnull().mean()
    cols_to_drop = nulls_pct[nulls_pct > thresold].index
    return df.drop(columns=cols_to_drop)

def fill_numeric_nulls(df: pd.DataFrame, strategy: str = "median") -> pd.DataFrame:
    """
    Fill missing values in numeric columns using a given strategy. 
    """
    num_cols = df.select_dtypes(include="number").columns

    if strategy == "median":
        fill_values = {col: df[col].median() for col in num_cols}
    elif strategy == "mean":
        fill_values = {col: df[col].mean() for col in num_cols}
    else:
        raise ValueError("Unsupported strategy")
    
    return df.fillna(fill_values)


def fill_categorical_nulls(df: pd.DataFrame) -> pd.DataFrame:
    """
    Fill missing values in categorical columns using mode.
    """
    cat_cols = df.select_dtypes(include=["object", "category", "string"]).columns

    fill_values = {
        col: df[col].mode()[0]
        for col in cat_cols
        if df[col].isnull().any()
    }

    return df.fillna(fill_values)

def add_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add engineered features:
    - family_size
    - age_group 
    """

    return (
        df
        .assign(
            family_size=lambda x: x["sibsp"] + x["parch"],
            age_group=lambda x: pd.cut(
                x["age"],
                bins=AGE_BINS,
                labels=AGE_LABELS
            )
        )
    )
   
def encode_categoricals(df: pd.DataFrame) -> pd.DataFrame:
    """
    one-hot encode categorical columns
    """
    cat_cols = df.select_dtypes(include=["object", "category", "string"]).columns
    df_encoded = pd.get_dummies(df, columns=cat_cols, drop_first=True)

    return df_encoded.astype(int, errors="ignore")

def drop_redundant_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Drop columns that leak target information or are redundant
    """
    cols_to_drop = ["alive_yes"]
    return df.drop(columns=[col for col in cols_to_drop if col in df.columns])

def run_pipeline(df: pd.DataFrame) -> pd.DataFrame:
    """
    Runs full pandas transformation pipeline
    """
    return (
        df
        .pipe(drop_high_null_columns, thresold=0.5)
        .pipe(fill_numeric_nulls, strategy="median")
        .pipe(fill_categorical_nulls)
        .pipe(add_features)
        .pipe(encode_categoricals)
        .pipe(drop_redundant_columns)
    )

if __name__ == "__main__":

    df = sns.load_dataset("titanic")
    df_clean = run_pipeline(df)

    print(df_clean.head())
    print("\nColumns:\n", df_clean.columns)