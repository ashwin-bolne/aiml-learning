import numpy as np 

def detect_outliers_zscore(arr: np.ndarray, thresold: float = 1.0) -> np.ndarray:
    """
    Detect outliers using Z-score.

    Args:
        arr (np.ndarray): Input 1D numeric array
        thresold (float): Z-score thresold for outlier detection

    Returns:
        np.ndarray: Indices of outlier values
    """
    mean = np.mean(arr)
    std = np.std(arr)

    # edge case: no variation
    if std == 0:
        return np.array([], dtype=int)

    z_scores = (arr - mean) / std
    mask = np.abs(z_scores) > thresold
  
    return np.where(mask)[0]


if __name__ == "__main__":
    arr = np.array([10, 12, 14, 15, 100])

    result = detect_outliers_zscore(arr)
    print(result)