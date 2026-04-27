import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

# custom exception classes 
class EmptyDatasetError(Exception):
    """Raised when the dataset is empty."""
    pass 

class InvalidFileFormatError(Exception):
    """Raised when the file format is not supported."""
    pass 

class SchemaMismatchError(Exception):
    """Raised when dataset schema does not match expected strucutre."""
    pass


def load_data_simulator(data: list) -> str:
    """
    Simulates loading a dataset

    Args:
        data: input dataset 
    
    Returns:
       success message 
    
    Raises:
        InvalidFileFormatError: If input is not a list
        EmptyDatasetError: If dataset is empty
    """
    logger.info("Starting data load process")

    if not isinstance(data, list):
        logger.error("Invalid data format detected")
        raise InvalidFileFormatError("Data must be a list.")
    
    if len(data) == 0:
        logger.error("Empty dataset detected")
        raise EmptyDatasetError("Dataset is empty")
    
    logger.info("Data loaded successfully")
    return "Data loaded successfully"

def run_test(data):
    """
    Executes data loading and handles exceptions.

    Args:
        data: Input dataset
    """
    try:
        result = load_data_simulator(data)
        print(result)

    except EmptyDatasetError as e:
        logger.error(f"Handled EmptyDatasetError: {e}")
        print(f"Error: {e}")

    except InvalidFileFormatError as e:
        logger.error(f"Handled InvalidFileFormatError: {e}")
        print(f"Error: {e}")


if __name__ == "__main__":
    print("---- Test Case 1: Empty List ----")
    run_test([])

    print("\n---- Test Case 2: Invalid Format ----")
    run_test("abc")

    print("\n---- Test Case 3: Valid Data ----")
    run_test([1, 2, 3])
    