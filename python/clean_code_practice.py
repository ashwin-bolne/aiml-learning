import pandas as pd

class BaseDataError(Exception):
    """
    Base class for all custom exceptionas for clean_code_practice file code exceptions
    """
    pass 

class EmptyDatasetError(BaseDataError):
    """
    Raised when the dataset is empty
    """
    
    pass 

class MissingColumnError(BaseDataError):
    """
    Raised when required column is missing.
    """
    pass 


def load_csv(path: str) -> pd.DataFrame:
    """
    Load a CSV into a pandas DataFrame.

    Args:
        path (str): path to the CSV file.
    
    Returns:
        pd.DataFrame: Loaded dataset.

    Raises:
        FileNotFoundError: If the file does not exist.
        pd.errors.EmptyDataError: if the file is empty.     

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
    """
    if df.empty:
        raise EmptyDatasetError("Dataset is empty")
    
    if "age" not in df.columns:
        raise MissingColumnError("Column 'age' is missing.")

def analyze_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """
    Generate descriptive statistics for the dataset.

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
    print(stats)
    return df

