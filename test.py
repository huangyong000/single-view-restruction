#coding:utf-8
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
items= pd.read_excel(".\\items.csv")
signup= pd.read_excel(".\\signup.csv")
items_dataset = items[["item_id", "item_name"]]
signup_dataset = items[["item_id"]]
