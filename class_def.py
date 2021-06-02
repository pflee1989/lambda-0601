import pandas as pd
        
class Data_Clean:
    def __init__(self,df):
        self.df = df    
    def clean_data(self):
        return self.df.isnull().sum().sum()
    def __repr__(self): 
        return 'data_clean'

class Data_Frame_Constructor:
    def __init__(self,series):
        self.series = series    
    def clean_data(self):
        return pd.DataFrame(self.series)
    def __repr__(self): 
        return 'Data_Frame_Constructor'
    
class Date_Time:
    def __init__(self,datetime):
        self.series = datetime
    def year(self):
        return pd.to_datetime(self.series, infer_datetime_format=True).dt.year 
    def month(self):
        return pd.to_datetime(self.series, infer_datetime_format=True).dt.month
    def day(self):
        return pd.to_datetime(self.series, infer_datetime_format=True).dt.day 
    def __repr__(self): 
        return 'Date_Time'

class split_all_datetime:
    def __init__(self,datetime):
        self.series = datetime    
    def split_dates(datetime):
        X = datetime.copy()
        for col in X:
            if X[col].dtypes == '<M8[ns]':
                X[col+"year"] = X[col].dt.year
                X[col+"month"] = X[col].dt.month
                X[col+"day"] = X[col].dt.day
        return X
    def __repr__(self): 
        return 'split_all_datetime'
