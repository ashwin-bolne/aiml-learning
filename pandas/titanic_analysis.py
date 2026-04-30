import json 

import pandas as pd
import seaborn as sns

AGE_BINS = [0, 18, 60, 100]
AGE_LABELS = ["child", "adult", "senior"]

def load_data() -> pd.DataFrame:
    """
    Load the titanic dataset

    Returns:
        pd.DataFrame: returns the titanic dataset

    """
    return sns.load_dataset("titanic")

def analyze_titanic(df: pd.DataFrame) -> dict:
    """
    Performs exploratory data analysis on the Titanic dataset
    and returns key statistical insights as a dictionary.

    Args:
        df (pd.Dataframe): input dataset

    Returns:
        dict: analysis result in dictionary format 
    """
    
    # 1. survival percentage calculation
    survival_pct = df["survived"].mean() * 100

    # 2. survival rate by passenger class
    survival_by_class = df.groupby("pclass")["survived"].mean() * 100
    
    # 3. Average age by class AND sex
    avg_age_raw = df.groupby(["pclass", "sex"])["age"].mean()

    avg_age_by_class_sex = {
        f"{pclass}_{sex}": value 
        for (pclass, sex), value in avg_age_raw.items()
    }

    # 4. embarkation port with highest survival
    survival_by_port = df.groupby("embarked")["survived"].mean()
    best_port = survival_by_port.idxmax()

    # 5. Null count per column
    null_counts = df.isnull().sum()

    # 6. Drop rows where age is null
    remaining_rows = df.dropna(subset=["age"]).shape[0]

    # 7. Create age_group using pd.cut()
    age_group_counts = (
        pd.cut(
            df["age"],
            bins=AGE_BINS,
            labels=AGE_LABELS
        )
        .value_counts()
    )

    # 8. one-hot encode embarked
    embarked_encoded = pd.get_dummies(df["embarked"], prefix="embarked")
    embarked_counts = embarked_encoded.sum()

    # 9. Correlation matrix of numeric columns
    numeric_df = df.select_dtypes(include="number")
    correlation_matrix = numeric_df.corr().round(3)

    # 10. Top 5 most common values in a categorical column - embark_town 
    top_embark_town = df["embark_town"].value_counts().head(5)

    return {
        "survival_pct": float(survival_pct),
        "survival_by_class": survival_by_class.to_dict(),
        "avg_age_by_class_sex": avg_age_by_class_sex,
        "best_embark_port": best_port,
        "null_counts": null_counts.to_dict(),
        "remaining_rows_after_age_drop": remaining_rows,
        "age_group_counts": age_group_counts.to_dict(),
        "embarked_one_hot_counts": embarked_counts.to_dict(),
        "correlation_matrix": correlation_matrix.to_dict(),
        "top_embark_town": top_embark_town.to_dict()
    }

  

if __name__ == "__main__":
    df = load_data()
    # print(df.head())
    # print("\nColumns:\n", df.columns)
    # print("\nData types:\n", df.dtypes)
    # print("\nNull values:\n", df.isnull().sum())

    result = analyze_titanic(df)
    print(json.dumps(result, indent=4))
 