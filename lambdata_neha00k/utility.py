#Train/validate/test split function for a dataframe
import pandas as pd
import sklearn
from sklearn.model_selection import train_test_split

import numpy as np

df = pd.DataFrame(np.random.randn(100, 4), columns=list('ABCD'))
def split_data(df):

    train, test =train_test_split(df, test_size = 20, random_state = 42)
    train, val = train_test_split(train, test_size = 20, random_state = 42)
    print("Splitting done")
    return train, test, val
