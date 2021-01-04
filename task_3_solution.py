import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

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

def scale_data(x, scaleMeth):
    scaler = scaleMeth()
    return scaler.fit_transform(x)

def prepare_data_for_model(x, scaleMeth):
    x, y = prepare_data(x)
    x = scale_data(x, scaleMeth)
    return x, y

def fit_first_linear_model(x, y):
    return LinearRegression().fit(x, y)

def evaluate_model(m, x, y):
    y_pred = m.predict(x)
    mse = mean_squared_error(y, y_pred)
    mae = mean_absolute_error(y, y_pred)
    r2 = r2_score(y, y_pred)
    return round(mse, 2), round(mae, 2), round(r2, 2)
