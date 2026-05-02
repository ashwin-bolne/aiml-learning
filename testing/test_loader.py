import pytest

from testing.loader import load_csv

def test_load_valid_csv():
    df = load_csv("testing/data/sample_good.csv")

    assert df.shape == (2, 3)

def test_load_empty_csv():
    with pytest.raises(ValueError, match="empty"):
        df = load_csv("testing/data/sample_empty.csv")

def test_load_missing_file():
    with pytest.raises(FileNotFoundError):
        load_csv("testing/data/does_not_exist.csv")