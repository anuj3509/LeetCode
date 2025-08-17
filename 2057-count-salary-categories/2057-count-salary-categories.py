import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    
    conditions = [
        accounts["income"] < 20000,
        accounts["income"].between(20000, 50000, inclusive="both"),
        accounts["income"] > 50000
    ]
    choices = ["Low Salary", "Average Salary", "High Salary"]

    accounts["category"] = np.select(conditions, choices)

    # count by category
    counts = accounts["category"].value_counts().reset_index()
    counts.columns = ["category", "accounts_count"]

    # if there are no salary in any category, we use default as 0
    all_categories = ["Low Salary", "Average Salary", "High Salary"]
    result = (
        counts.set_index("category")
              .reindex(all_categories, fill_value=0)
              .reset_index()
    )
    return result

