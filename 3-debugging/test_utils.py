import pandas as pd
from utils import dataframe_modifier


def test_dataframe_modifier():
    df = pd.DataFrame([[1, 2], [2, 3]], columns=["a", "b"])
    res = dataframe_modifier(df, 2)

    assert res.equals(df)
