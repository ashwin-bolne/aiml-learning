from typing import Sequence 

def add(a: int, b: int) -> int:
    """
    Add two integers.

    Args:
        a: First integer
        b: Second integer
    
    Returns:
        Sum of a and b
    """
    return a + b

def is_even(n: int) -> bool:
    """
    Check if number is even.

    Args:
        n: Integer input
    
    Returns:
        True if even, False otherwise
    """
    return n % 2 == 0

def find_max(values: Sequence[int]) -> int:
    """
    Find the maximum value in a non-empty sequence.

    Args:
        values: Sequence of integers (must not be empty)

    Returns:
        Maximum integer in the sequence

    Raises:
        ValueError: If values is empty
    """
    if not values:
        raise ValueError("values cannot be empty")
    
    max_value = values[0]
    for value in values:
        if value > max_value:
            max_value = value
    return max_value

def calculate_average(values: Sequence[float]) -> float:
    """
    Calculate the arithmetic mean.

    Args:
        values: Sequence of floats (must not be empty)

    Returns:
        Average of values
    
    Raises:
        ValueError: If values is empty
    """
    if not values:
        raise ValueError("Values cannot be empty")
    
    total = 0.0
    for value in values:
        total += value 
    return total / len(values)

if __name__ == "__main__":
    print(add(2, 3))
    print(is_even(4))
    print(find_max([1, 5, 2]))
    print(calculate_average([10.0, 20.0, 30.0]))