from dataclasses import dataclass
from datetime import datetime
from typing import Sequence

@dataclass
class DataRecord:
    filename: str
    row_count: int 
    column_names: list[str]
    loaded_at: datetime


def get_row_count(data: Sequence[dict]) -> int:
    return len(data)

def get_column_names(data: Sequence[dict]) -> list[str]:
    if not data:
        return []
    return list(data[0].keys())

def get_null_counts(data: Sequence[dict]) -> dict[str, int]:
    if not data:
        return {}
    
    columns = data[0].keys()

    return {
        col: sum(1 for row in data if row.get(col) in (None, "", "null"))
        for col in columns 
    }

def print_summary(record: DataRecord, null_counts: dict[str, int]) -> None:
    print("----- DATA SUMMARY -----")
    print(f"File: {record.filename}")
    print(f"Rows: {record.row_count}")
    print(f"Columns: {', '.join(record.column_names)}")
    print(f"Loaded At: {record.loaded_at}")
    print("Null Counts:")
    for col, count in null_counts.items():
        print(f"  {col}: {count}")

if __name__ == "__main__":
    sample_data = [
        {"age": 25, "salary": 50000},
        {"age": None, "salary": 60000},
        {"age": 35, "salary": None},
    ]


    record = DataRecord(
        filename="sample.csv",
        row_count=get_row_count(sample_data),
        column_names=get_column_names(sample_data),
        loaded_at=datetime.now()
    )

    nulls = get_null_counts(sample_data)

    print_summary(record, nulls)