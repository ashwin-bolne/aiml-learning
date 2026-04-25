from typing import Sequence 

def square_numbers(data: Sequence[int]) -> list[int]:
    """
    Return the list with square of each number from the sequnece.

    Args:
        data: Sequence of integer.

    Returns:
        list of square of each number from Sequence.
    """
    return [x * x for x in data]

def get_even_numbers(data: Sequence[int]) -> list[int]:
    """
    Return the list of even numbers from the sequence.

    Args:
        data: Sequence of integer.
    
    Returns:
        return the list of even numbers from the sequnece.
    """
    return [x for x in data if x % 2 == 0]

def map_to_square(data: Sequence[int]) -> dict[int, int]:
    return {x: x * x for x in data}

def unique_values(data: Sequence[int]) -> set[int]:
    return {x for x in data}

def label_numbers(data: Sequence[int]) -> list[str]:
    return ["even" if x % 2 == 0 else "odd" for x in data]

if __name__ == "__main__":
    data = [1, 2, 3, 4, 4]

    print(square_numbers(data))
    print(get_even_numbers(data))
    print(map_to_square(data))
    print(unique_values(data))
    print(label_numbers(data))