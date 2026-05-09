import pandas as pd

REQUIRED_COLUMNS = ["age"]

class DataValidatorError(Exception):
    """
    Base class for data validation related errors.
    """
    pass 

class EmptyDatasetError(DataValidatorError):
    """
    Raised when the dataset is empty
    """
    pass 

class MissingColumnError(DataValidatorError):
    """
    Raised when required column is missing.
    """
    pass 


def load_csv(path: str) -> pd.DataFrame:
    """
    Load a CSV into a pandas DataFrame.

    Args:
        path (str): Path to the CSV file.
    
    Returns:
        pd.DataFrame: Loaded dataset.

    Raises:
        FileNotFoundError: If the file does not exist.
        pd.errors.EmptyDataError: if the file is empty.     
    
    Example:
        >>> load_csv("data/sample.csv")
        DataFrame with loaded data

    """
    return pd.read_csv(path)

def validate_dataframe(df: pd.DataFrame) -> None:
    """
    Validate the structure and integrity of the DataFrame.

    Args:
        df (pd.DataFrame): Input dataset.

    Raises:
        EmptyDatasetError: If the DataFrame is empty.
        MissingColumnError: If required columns are missing.
    
    Example:
        >>> validate_dataframe(dataframe)
        None
    """
    if df.empty:
        raise EmptyDatasetError("Dataset is empty")
    
    missing_cols = [col for col in REQUIRED_COLUMNS if col not in df.columns]

    if missing_cols:
        raise MissingColumnError(f"Missing columns: {missing_cols}")

def analyze_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """
    Generate descriptive statistics for numeric columns.

    Args:
        df (pd.DataFrame): Input dataset.

    Returns:
        pd.DataFrame: Statistical summary of the dataset.
    """
    return df.describe()

def process_data(path: str) -> pd.DataFrame:
    """
    Execute the full data processing pipeline:
    load → validate → analyze.

    Args:
        path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: Loaded dataset after validation.

    Raises:
        EmptyDatasetError: If dataset is empty.
        MissingColumnError: If required columns are missing.
    """
    df = load_csv(path)
    validate_dataframe(df)
    stats = analyze_dataframe(df)

if __name__ == "__main__":
    stats = process_data("path")
    print(stats)

