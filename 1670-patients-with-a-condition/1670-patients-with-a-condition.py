import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    
    return patients.loc[ patients['conditions'].str.contains(r'(^| )DIAB1') ]


    # find_patients_df = patients[ patients['conditions'].str.contains(r'\bDIAB1') ]
    # return find_patients_df




    # conditions = DskjdIashdABf4gsf1k

    # Line 8 will return the above conditions too if we do not use the '\b'. 
    # '\b' helps us to only return true if 'DIAB1' is present sequentially together.