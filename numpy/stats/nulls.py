import numpy as np 
import pandas as pd 

def vectorized_null_profile(df: pd.DataFrame) -> dict:
    """
    Compute null percentage for each column using NumPy.

    Args:
        df (pd.DataFrame): Input DataFrame

    Returns:
        dict: Column-wise null percentages.
    """
    # Convert to numpy array
    arr = df.to_numpy()
    
    # Detect nulls
    null_mask = np.isnan(arr)
    
    # Count nulls column-wise
    null_counts = np.sum(null_mask, axis=0)

    # Total rows
    row_count = arr.shape[0]

    # Percentage
    null_percent = (null_counts / row_count) * 100

  # Map to column names
    return dict(zip(df.columns, map(float, null_percent)))


if __name__ == "__main__":
    df = pd.DataFrame({
    "A": [1, 2, np.nan, 4],
    "B": [np.nan, np.nan, 3, 4]
    })
    result = vectorized_null_profile(df)
    print(result)