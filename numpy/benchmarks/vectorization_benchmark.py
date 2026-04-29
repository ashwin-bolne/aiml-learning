import time
from typing import List

import numpy as np 


def python_loop_sum(arr: List[float]) -> float:
    """
    Compute sum of elements using a python loop.

    Args:
        arr (List[float]): Input list of floats
    
    Returns:
        float: Sum of elements.
    """
    total = 0.0
    for item in arr:
        total += item 
    return total 

def numpy_sum(arr: np.ndarray) -> float:
    """
    Compute the sum of elements using NumPy array.

    Args:
        arr (np.ndarray): Input NumPy array
    
    Returns:
        float: Sum of elements.
    """
    return float(np.sum(arr))

def run_benchmark(size: int = 1_000_000) -> dict:
    """
    Benchmark python loop vs NumPy sum.

    Args:
        size (int): Number of elements.
    
    Returns:
        dict: Benchmark results including timings and speedup.
    """
    py_list: List[float] = [float(i) for i in range(size)]
    np_array: np.ndarray = np.array(py_list)

    python_loop_sum(py_list)
    numpy_sum(np_array)

    # Python loop timing
    start: float = time.perf_counter()
    python_loop_sum(py_list)
    loop_time: float = time.perf_counter() - start 

    # NumPy timing 
    start = time.perf_counter()
    numpy_sum(np_array)
    numpy_time: float = time.perf_counter() - start

    speedup: float = loop_time / numpy_time

    return {
        "loop_time": loop_time,
        "numpy_time": numpy_time,
        "speedup": speedup
    }


def main() -> None:
    """
    Entry point for running the benchmarks.
    """
    results = run_benchmark()
    print(f"Python loop time: {results['loop_time']:.6f} sec")
    print(f"NumPy time:       {results['numpy_time']:.6f} sec")
    print(f"Speedup:          {results['speedup']:.2f}x")


if __name__ == "__main__":
    main()