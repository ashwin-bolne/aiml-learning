from pathlib import Path
import csv

def read_text_file(file_path: Path) -> str:
    """
    Read content of a text file.

    Args:
        file_path: path object

    Returns:
        File content as string
    """
    if not file_path.exists():
        raise FileNotFoundError(f"{file_path} does not exist.")
    
    with file_path.open("r") as f:
        return f.read
    
def write_text_file(file_path: Path, content: str) -> None:
    """
    Write content to file.

    Args:
        file_path: Path object
        content: Text to write
    """
    with file_path.open("w") as f:
        f.write(content)

def read_csv_basic(file_path: Path) -> list[dict[str, str]]:
    """
    Read CSV into list of dictionaries

    Args:
        file_path: Path to CSV

    Returns:
        List of rows as dictionaries
    """
    if not file_path.exists():
        raise FileNotFoundError(f"{file_path} not found")
    
    with file_path.open("r") as f:
        reader = csv.DictReader(f)
        return [row for row in reader]
    
if __name__ == "__main__":
    
    path = Path("test.txt")

    write_text_file(path, "Hello Ashwin")
    print(read_text_file(path))