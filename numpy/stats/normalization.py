import numpy as np 

def normalize_column(arr: np.ndarray) -> np.ndarray:
    """
    Perform min-max normalization on a 1D array.

    Args:
        arr (np.ndarray): Input numeric array.

    Returns:
        np.ndarray: Normalized array in range [0, 1]
    """
    min_val = np.min(arr)
    max_val = np.max(arr)

    if max_val == min_val:
        return np.zeros_like(arr, dtype=float)

    normalized = (arr - min_val) / (max_val - min_val)
    return normalized


if __name__ == "__main__":
    # Case 1: normal data
    arr1 = np.array([10, 20, 30, 40])
    print("Input:", arr1)
    print("Normalized:", normalize_column(arr1))
    # Expected: [0.0, 0.333..., 0.666..., 1.0]

    print("-" * 40)

    # Case 2: identical values (edge case)
    arr2 = np.array([5, 5, 5, 5])
    print("Input:", arr2)
    print("Normalized:", normalize_column(arr2))
    # Expected: [0.0, 0.0, 0.0, 0.0]

    print("-" * 40)

    # Case 3: negative values
    arr3 = np.array([-10, 0, 10])
    print("Input:", arr3)
    print("Normalized:", normalize_column(arr3))
    # Expected: [0.0, 0.5, 1.0]