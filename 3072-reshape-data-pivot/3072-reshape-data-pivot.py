import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    pivoted_df = weather.pivot(
        index = 'month',
        columns = 'city',
        values = 'temperature'
    )
    # pivoted_df = pivoted_df.reset_index()   -> this will change the first column which is the index from month to serial numbers
    return pivoted_df