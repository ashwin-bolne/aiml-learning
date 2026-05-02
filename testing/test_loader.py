from testing.loader import load_csv

def test_load_valid_csv():
    df = load_csv("testing/data/sample_good.csv")

    assert df.shape == (2, 3)