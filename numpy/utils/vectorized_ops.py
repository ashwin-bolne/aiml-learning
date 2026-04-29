import numpy as np 

def replace_less_than(arr: np.ndarray, thresold: float = 10) -> np.array:
    """
    Replace values less than thresold with 0 using vectorized operation.

    Args:
        arr (np.ndarray): Input array
        thresold (float): Thresold value

    Returns:
        np.ndarray: Trasfomred array
    """
    return np.where(arr < thresold, 0, arr)

if __name__ == "__main__":
    arr = np.array([5, 12, 7, 20, 3])
    print(replace_less_than(arr))