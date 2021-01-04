import pandas as pd
from sklearn.model_selection import train_test_split

def split_data_into_two_samples(x):
    return train_test_split(x, test_size=0.3, random_state=42)

def prepare_data(x):
    #x.drop(columns=["id"], inplace=True)
    #del x["id"]
    s_dtypes = x.dtypes
    #print(s_dtypes.loc[s_dtypes == 'object'].index.to_list())
    for col in  s_dtypes.loc[s_dtypes == 'object'].index.to_list():
        #print(col)
        x.drop(columns=col, inplace=True)
    #x.drop(columns = [s_dtypes.loc[s_dtypes == 'object'].index], inplace=True)
    #x = x.reset_index(drop=True)
    if "id" in x.columns: 
        x.drop(columns=["id"], inplace=True)
    x1 = x.dropna(axis=1)
    x2 = x1.pop("price_doc")
    return x1, x2

def skale_data(x, scaleMeth):
    scaler = scaleMeth()
    return scaler.fit_transform(x)
