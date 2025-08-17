import pandas as pd

def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    
    return pd.concat([df1, df2], axis = 0)
    
    # axis = 0 is for vertical join (i.e., same number of columns, increased rows)
    # axis = 1 is for horizontal join (i.e., same number of rows, increased columns)