import pandas as pd
import seaborn as sns

def load_data() -> pd.DataFrame:
    """
    Load the titanic dataset

    Returns:
        pd.DataFrame: returns the titanic dataset

    """
    df = sns.load_dataset("titanic")
    return df 

def analyze_titanic(d: pd.DataFrame) -> dict:
    survival_pct = df["survived"].mean() * 100

    return {
        "survival_pct": float(survival_pct)
    }

if __name__ == "__main__":
    df = load_data()
    # print(df.head())
    # print("\nColumns:\n", df.columns)
    # print("\nData types:\n", df.dtypes)
    # print("\nNull values:\n", df.isnull().sum())

    result = analyze_titanic(df)
    print(result)