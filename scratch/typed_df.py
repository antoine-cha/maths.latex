from typing import List, Type
from dataclasses import dataclass

import pandas as pd

from abc import ABC


class TypedDF(ABC):
    """Base class of the typed DataFrame.
    Do not use as is """
    INDEX: List[str] = []
    COLUMNS: List[str] = []

    def __init__(self, df: pd.DataFrame):
        self.df = df
        self.check_structure()

    def check_structure(self):
        # Check structure and dtypes of the DataFrame
        assert set(df.columns) == set(self.COLUMNS)
        assert set(df.index.names) == set(self.INDEX)




def create_typed_df_class(name, index, columns) -> Type[TypedDF]:
    tdf = type(name, (TypedDF,), {"INDEX": index, "COLUMNS": columns})
    return tdf

def index_level_dtypes(df):
    return [f"{df.index.names[i]}: {df.index.get_level_values(n).dtype}"
            for i, n in enumerate(df.index.names)]


if __name__ == "__main__":
    df = pd.DataFrame({"col1": range(10), "col2": range(10)}, index=pd.RangeIndex(name="index", stop=10))
    print(df)
    my_class = create_typed_df_class("mon_tableau", ["index"], ["col1", "col2"])
    print(my_class)
    tdf = my_class(df)
    print("-" * 80)
    print("original")
    print(tdf)
    print(tdf.df)
    print(tdf.df.dtypes)
    print(index_level_dtypes(tdf.df))
    tdf.df = tdf.df.reset_index().set_index("col1")
    print("-" * 80)
    print("1 index")
    print(tdf.df)
    print(tdf.df.dtypes)
    print(index_level_dtypes(tdf.df))
    print("-" * 80)
    print("2 index")
    tdf.df = tdf.df.reset_index().set_index(["col1", "col2"])
    print(tdf.df)
    print(tdf.df.dtypes)
    print(index_level_dtypes(tdf.df))
    print(pd.DataFrame)


