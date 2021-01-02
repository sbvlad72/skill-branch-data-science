import pandas as pd
from sklearn.model_selection import train_test_split

def split_data_into_two_samples(x):
    return train_test_split(x, random_state=42)

def prepare_data(x):
    #x.drop(columns=["id"], inplace=True)
    #del x["id"]
    s_dtypes = x.dtypes
    #print(s_dtypes.loc[s_dtypes == 'object'].index.to_list())
    for col in  s_dtypes.loc[s_dtypes == 'object'].index.to_list():
        #print(col)
        x.drop(columns=col, inplace=True)
    #x.drop(columns = [s_dtypes.loc[s_dtypes == 'object'].index], inplace=True)
    x.reset_index()
    x.drop(columns=["id"], inplace=True)
    x.dropna()
    x1 = x.pop("price_doc")
    return x, x1

