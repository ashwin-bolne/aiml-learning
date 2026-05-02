import json

from pathlib import Path
import pandas as pd 

def load_csv(path: str) -> pd.DataFrame:
    """
    Load the csv file

    Args:
        path (str): path for the csv file
    
    Returns:
        pd.DataFrame: return the pandas dataframe
    """

    file_path = Path(path)

    if not file_path.exists():
        raise FileNotFoundError(f"file not found: {path}")
    
    df = pd.read_csv(file_path)

    if df.empty:
        raise ValueError("Dataset is empty")
    
    return df

def load_json(path: str) -> pd.DataFrame:
    """
    Load the json file

    Args:
        path (str): path for the json file
        
    Returns:
        pd.DataFrame: return the pandas dataframe
    """
    file_path = Path(path)

    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {path}")
    
    with open(file_path, "r") as f:
        data = json.load(f)

    if not data:
        raise ValueError("Empty dataset")
    
    df = pd.DataFrame(data)
    return df 