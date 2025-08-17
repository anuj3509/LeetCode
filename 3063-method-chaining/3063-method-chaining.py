import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    
    # Option 1: using query()
    # df = animals.query('weight > 100')
    # df = animals.sort_values(by = 'weight', ascending = False)

    # return df.filter(['name'])


    # Option 2: using loc()
    df = df = animals.sort_values(by = ['weight'], ascending = False)
    df = df.loc[df['weight'] > 100, ['name']]
    return df