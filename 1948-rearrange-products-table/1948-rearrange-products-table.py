import pandas as pd

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    
    result_df = products.melt(
        id_vars = ['product_id'],
        value_vars = ['store1', 'store2', 'store3'],
        var_name = 'store',
        value_name = 'price'
    )

    result_df = result_df.dropna()

    return result_df