import pandas as pd
import seaborn as sns

def load_data():
    df = sns.load_dataset("titanic")
    return df 


if __name__ == "__main__":
    df = load_data()
    print(df.head())