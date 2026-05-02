import pytest

from testing.loader import load_csv, load_json

def test_load_valid_csv():
    df = load_csv("testing/data/sample_good.csv")

    assert df.shape == (2, 3)

def test_load_empty_csv():
    with pytest.raises(ValueError, match="empty"):
        df = load_csv("testing/data/sample_empty.csv")

def test_load_missing_file():
    with pytest.raises(FileNotFoundError):
        load_csv("testing/data/does_not_exist.csv")

def test_schema_mismatch():
    df = load_csv("testing/data/sample_bad.csv")

    expected_cols = {"name", "age", "fare"}

    assert not expected_cols.issubset(set(df.columns))

def test_load_json_valid():
    df = load_json("testing/data/sample_good.json")

    assert df.shape == (2, 3)
    assert "name" in df.columns

def test_load_json_empty():
    with pytest.raises(ValueError, match="empty"):
        load_json("testing/data/sample_empty.json")