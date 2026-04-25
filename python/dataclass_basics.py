from dataclasses import dataclass
from datetime import datetime

@dataclass
class DataRecord:
    """
    Represents metadata of loaded dataset.
    """
    filename: str
    row_count: int
    column_names: list[int]
    loaded_at: datetime

    def summary(self) -> str:
        return f"{self.filename} has {self.row_count} rows"
        
    def __post_init__(self):
        if self.row_count < 0:
            raise ValueError("row_count cannot be negative")
        

if __name__ == "__main__":
    from datetime import datetime

    record = DataRecord(
        filename="sample.csv",
        row_count=50,
        column_names=["age", "salary"],
        loaded_at=datetime.now()
    )

    print(record)
    print(record.summary())