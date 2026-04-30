import pandas as pd

def drop_high_null_columns(df: pd.DataFrame, thresold: float = 0.5) -> pd.DataFrame:
    """
    Drops columns where null percentage exceeds thresold
    """
    nulls_pct = df.isnull().mean()
    cols_to_drop = nulls_pct[nulls_pct > thresold].index
    return df.drop(columns=cols_to_drop)


def run_pipeline(df: pd.DataFrame) -> pd.DataFrame:
    """
    Runs full pandas transformation pipeline
    """
    return (
        df
        .pipe(drop_high_null_columns, thresold=0.5)
    )

if __name__ == "__main__":
    import seaborn as sns

    df = sns.load_dataset("titanic")
    df_clean = run_pipeline(df)

    print(df_clean.columns)