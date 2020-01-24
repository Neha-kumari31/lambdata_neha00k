#function to take a list, turn it into a series and add it to a dataframe as a new column
import pandas as pd
def list_to_column(df, mylist):
    """
    function to add mylist into a dataframe as a new column
    """
    new_col = pd.Series(mylist)
    df['new_col'] = new_col.values
    return df


df = pd.DataFrame({"A":[1,7,45, 9,10], "B": [5, 7, 4, 9, 70]})
list_to_column(df,[9,56, 9,45, 6] )
print(df.head())