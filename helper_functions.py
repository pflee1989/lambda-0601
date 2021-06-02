import pandas as pd
# import matplotlib
import numpy as np

def null_count(df):
    count = df.isnull().sum().sum()
    return count


def train_test_split(df, frac):
    len23rd = int(round(len(df_main)*(1-frac),0))
    len13rd = int(round(len(df_main)*(frac),0))
    # assert len23rd + len13rd == len(df) or "redo"
    df_train = df_main.iloc[0:(len23rd+1)]
    df_val = df_main.iloc[0:(len13rd+1)]
    return df_train, df_val


def randomize(df):
    df = df_main.sample(frac=1).reset_index(drop=True)
    return df

def list_2_series(list_2_series, df):
    df = pd.DataFrame(list_2_series)
    return df


def addy_split(df):
    regex = r'(?P<City>[^,]+)\s*,\s*(?P<State>[^\s]+)\s+(?P<Zip>\S+)'
    df[["street2", "city2", "state2", "zip2"]] = df.address.str.extract('(.+)[ ]{3}(.+)\,[ ]([a-zA-z]{2})[ ]([0-9]{5})',expand=True)
    return df


def split_dates(date_series):
    X = date_series.copy()
    for col in X:
        if X[col].dtypes == '<M8[ns]':
            X[col+"year"] = X[col].dt.year
            X[col+"month"] = X[col].dt.month
            X[col+"day"] = X[col].dt.day
    return X

