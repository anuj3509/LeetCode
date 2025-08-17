import pandas as pd

def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    
    products['quantity'].fillna(0, inplace = True)  # inplace checks if we have to return in a new dataframe or modify the same dataframe
    return products