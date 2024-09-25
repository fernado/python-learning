import requests

# from sklearn.datasets import load_boston
import pandas as pd
# from sklearn.model_selection import train_test_split
# import matplotlib.pyplot as plt
# from sklearn import metrics
import numpy as np

# from sklearn.linear_model import LinearRegression

# inputNames = {'CRIM','ZN','INDUS','CHAS','NOX','RM','AGE','DIS','RAD','TAX','PTRATIO','B','LSTAT'};
# outputNames = {'MEDV'};
# housingAttributes = [inputNames,outputNames];


# url_data = "http://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data"
# url_names = "http://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.names"
#
# response = requests.get(url_names)

data_url = "http://lib.stat.cmu.edu/datasets/boston"
raw_df = pd.read_csv(data_url, sep="\s+", skiprows=22, header=None)
data = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])
target = raw_df.values[1::2, 2]


print(type(target))
print(target.shape)
print(target.data.shape)