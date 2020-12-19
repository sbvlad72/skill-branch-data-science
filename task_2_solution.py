import pandas as pd

def calculate_data_shape(x):
    return x.shape

def take_columns(x):
    pd.set_option('display.max_rows', 100500)
    return x.columns

def calculate_target_ratio(x, pColumn):
    return round(x[pColumn].mean(), 2)

def calculate_data_dtypes(x):
    iNum = 0
    iObj = 0
    for column in x.dtypes:
        if column == "int64" or column == "float64":
            iNum +=1
        elif column == "object":
            iObj +=1
    return iNum, iObj
