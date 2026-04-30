import seaborn as sns
import pandas as pd

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


def run_pipeline(df: pd.DataFrame) -> pd.DataFrame:
    """
    Runs full pandas transformation pipeline
    """
    return (
        df
        .pipe(drop_high_null_columns, thresold=0.5)
        .pipe(fill_numeric_nulls, strategy="median")
    )

if __name__ == "__main__":
    
    df = sns.load_dataset("titanic")
    df_clean = run_pipeline(df)

    print(df_clean.isnull().sum())