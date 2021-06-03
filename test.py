"""Test for the Classes"""
import pytest as pyt
import pandas as pd
import numpy as np
from test_data import df_empty, df_test
from class_def import Data_Clean



def test_clean_data(df_empty):
   data = Data_Clean(df_empty)
   return data
   assert Data_Clean(df) == 0
   
def test_clean_data_null(df_test):
    return Data_Clean.clean_data(df_test)
    assert Data_Clean.clean_data(df_test) == 4