from typing import Sequence, Optional

def get_row_count(data: Sequence[int]) -> int:
    """
    Return number of elements in the sequence.

    Args:
        data: Sequence of integers
    
    Returns:
        Number of elements
    """
    return len(data)

def get_dtype_map(data: dict[str, str]) -> dict[str, str]:
    """
    Return same mapping (simulting dtype mapping).

    Args:
        data: Dictionary mapping column name -> dtype
    
    Returns:
        Same dictionary
    """
    return data 

def find_max(values: Sequence[int]) -> Optional[int]:
    """
    Return max value or None if empty.

    Args:
        values: Sequence of integers
    
    Returns:
        Maximum value or None
    """
    if not values:
        return None 

    return max(values)


if __name__ == "__main__":
    print(get_row_count([1, 2, 3]))
    print(get_dtype_map({"age": "int", "salary": "float"}))
    print(find_max([1, 5, 2]))
    print(find_max([]))