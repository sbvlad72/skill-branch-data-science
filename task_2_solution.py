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

def calculate_cheap_apartment(x):
    return x[x['price_doc'] <= 1000000]['price_doc'].count()

def calculate_squad_in_cheap_apartment(x):
    return round(x[x['price_doc'] <= 1000000]['full_sq'].mean(), 0)

def calculate_mean_price_in_new_housing(x):
    return round(x[(x.num_room == 3) & (x.build_year >= 2010)]['price_doc'].mean(), 0)

def calculate_mean_squared_by_num_rooms(x):
    return round(x.groupby(['num_room'])['full_sq'].mean(), 2)

def calculate_squared_stats_by_material(x):
    res = round(x.groupby(['material'])['full_sq'].aggregate({'min', 'max'}), 2)
    return res.rename(columns = {'max': 'amax', 'min': 'amin'})

def calculate_crosstab(x):
    return round(x.pivot_table('price_doc', index = ('sub_area'), columns=('product_type'), aggfunc = 'mean', fill_value=None), 2)
