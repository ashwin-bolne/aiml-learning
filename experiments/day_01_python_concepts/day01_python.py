from dataclasses import dataclass
from typing import (List, Dict)
from datetime import datetime

import pandas as pd


@dataclass
class DataRecord:
    filename: str 
    row_count: int 
    column_names: List[str]
    loaded_at: datetime 


def load_csv(path: str) -> pd.DataFrame:
    """
    Load a CSV file into a pandas DataFrame.

    Args:
        path (str): path to the csv file.
    
    Returns:
        pd.DataFrame: Loaded dataset.

    Raises:
        FileNotFoundError: If the file does not exist.
    """
    return pd.read_csv(path)


def print_summary(df: pd.DataFrame) -> None:
    """
    Print the summary (shape, Dtype, Null counts per column) about dataset.

    Args:
        df (pd.DataFrame): pandas dataset.
    """
    print(f"\n------------ DATA SUMMARY ------------\n")

    print(f"Shape: \n{df.shape}")
    
    print(f"\nData Types: \n{df.dtypes.to_string()}")
    
    print(f"\nNull Counts: \n{df.isnull().sum()}")


def get_null_counts(df: pd.DataFrame) -> Dict[str, int]:
    """
    Return null counts for each column in the dataset.

    Args:
        df (pd.DataFrame): pandas dataframe.

    Returns:
        Dict[str, int]: returns a dictionary with columns name as key and null counts as value
    """
    return {
        col: int(df[col].isnull().sum())
        for col in df.columns
    }


def get_dtypes_map(df: pd.DataFrame) -> Dict[str, str]:
    """
    Return the dtypes for each column in the dataset.

    Args:
        df (pd.DataFrame): pandas dataframe.

    Returns:
        Dict[str, str]: returns a dictionary with columns name as key and dtypes as value
    """
    return {
        col: str(df[col].dtype)
        for col in df.columns
        
    }


def get_row_count(df: pd.DataFrame) -> int:
    """
    Returns the total rows in dataframe.

    Args:
        df (pd.DataFrame): pandas dataframe.

    Returns:
        int: total rows in dataframe.
    """
    return df.shape[0]



if __name__ == "__main__":
    df = load_csv("data/sample.csv")
    
    record = DataRecord(
        filename="sample.csv",
        row_count=get_row_count(df),
        column_names=df.columns.tolist(),
        loaded_at=datetime.now()
    )

    print(record)

    print_summary(df)

    print("\nDtype Map:")
    print(get_dtypes_map(df))

    print("\nNull Counts:")
    print(get_null_counts(df))