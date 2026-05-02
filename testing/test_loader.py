import pytest
from pathlib import Path 
from testing.loader import load_csv, load_json


@pytest.fixture
def data_dir():
    return Path("testing/data")


def test_load_valid_csv(data_dir):
    df = load_csv(data_dir / "sample_good.csv")

    assert df.shape == (2, 3)
    assert "age" in df.columns


def test_load_empty_csv(data_dir):
    with pytest.raises(ValueError, match="empty"):
        df = load_csv(data_dir / "sample_empty.csv")

def test_load_missing_file(data_dir):
    with pytest.raises(FileNotFoundError):
        load_csv(data_dir / "does_not_exist.csv")

def test_schema_mismatch(data_dir):
    df = load_csv(data_dir / "sample_bad.csv")

    expected_cols = {"name", "age", "fare"}

    assert not expected_cols.issubset(set(df.columns))

def test_load_json_valid(data_dir):
    df = load_json(data_dir / "sample_good.json")

    assert df.shape == (2, 3)
    assert "name" in df.columns

def test_load_json_empty(data_dir):
    with pytest.raises(ValueError, match="empty"):
        load_json(data_dir / "sample_empty.json")