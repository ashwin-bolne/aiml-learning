from datetime import datetime

class DataRecord:
    """
    Represents metadata of loaded dataset.
    """

    def __init__(
            self,
            filename: str,
            row_count: int,
            column_names: list[int],
            loaded_at: datetime,
    ) -> None:
        self.filename = filename
        self.row_count = row_count
        self.column_names = column_names
        self.loaded_at = loaded_at

    def __repr__(self) -> str:
        return (
            f"DataRecord(filename={self.filename}), "
            f"rows={self.row_count}, "
            f"columns={self.column_names}, "
            f"loaded_at={self.loaded_at})"
        )
    
    def __str__(self) -> str:
        return (
            f"File: {self.filename}\n"
            f"Rows: {self.row_count}\n"
            f"Columns: {','.join(self.column_names)}\n"
            f"Loaded At: {self.loaded_at}"
        )
    

if __name__ == "__main__":
    record = DataRecord(
        filename="sample.csv",
        row_count=100,
        column_names=["age", "salary"],
        loaded_at=datetime.now()
    )

    print(record)
    print(repr(record))