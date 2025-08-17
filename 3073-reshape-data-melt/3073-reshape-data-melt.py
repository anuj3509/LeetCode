import pandas as pd

def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    
    melted_report = report.melt(
        id_vars = ['product'],  # column which we want to keep intact
        value_vars = ['quarter_1', 'quarter_2', 'quarter_3', 'quarter_4'],  # this line is optional though
        var_name = 'quarter',     # title of value_vars
        value_name = 'sales'
    )
    return melted_report