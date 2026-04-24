from typing import Sequence

def calculate_sum(values: Sequence[float]) -> float:
    """
    Calculate the sum of numeric values.

    Args:
        values: Sequence of numbers
    
    Returns:
        Sum of values
    
    Raises:
        ValueError: If values is empty
    """
    if not values:
        raise ValueError("values cannot be empty")
    total = 0.0
    for value in values:
        total += value 
    
    return total 

def calculate_mean(values: Sequence[float]) -> float:
    """
    Calculate mean (average) of values.

    Args:
        values: Sequence of numbers

    Returns:
        Mean value
    
    Raises:
        ValueError: If values is empty
    """
    total = calculate_sum(values)
    return total / len(values)

def get_summary_stats(values: Sequence[float]) -> dict:
    """
    Generate summary stastics for numeric data.

    Args:
        values: Sequence of numbers

    Returns:
        Dictionary containing summary stats:
            - count
            - sum 
            - mean
            - min 
            - max 
    
    Raises:
        ValueError: If values is empty
    """
    if not values: 
        raise ValueError("values cannot be empty")

    return {
        "count": len(values),
        "sum": calculate_sum(values),
        "mean": calculate_mean(values),
        "min": min(values),
        "max": max(values),
    } 

if __name__ == "__main__":
    sample = [10, 20, 30, 40]

    print(calculate_sum(sample))
    print(calculate_mean(sample))
    print(get_summary_stats(sample))