import pandas as pd


def load(path: str):
    """
    Loads a dataset from a csv file in path
    """
    try:
        data = pd.read_csv(path)
        print(f"Loading dataset of dimensions {data.shape}")
        return data

    except ValueError as e:
        print(f"Error: {e}")
        return None
