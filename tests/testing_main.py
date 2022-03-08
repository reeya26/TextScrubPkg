import sys,os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import csv
import pandas as pd

#from textscrub import clean

df = pd.read_csv("tests\\testing_dataset.csv")
# print(df.head())

