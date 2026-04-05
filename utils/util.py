import pandas as pd
import re

def fill_with_mean(df, cols):
    for col in cols:
        df[col] = df[col].fillna(df[col].mean())



def fill_with_median(df, cols):
    for col in cols:
        df[col] = df[col].fillna(df[col].median())

        

def convert_income(x):
    if pd.isna(x):
        return None
    
    if '-' in x:
        nums = list(map(int, re.findall(r'\d+', x)))
        return sum(nums) / len(nums) * 1000
    
    elif '<' in x:
        num = int(re.findall(r'\d+', x)[0])
        return (num / 2) * 1000
    
    elif '+' in x:
        num = int(re.findall(r'\d+', x)[0])
        return num * 1.2 * 1000
    
    return None