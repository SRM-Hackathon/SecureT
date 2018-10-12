# Train the dataset to give if the person deserves to get the loan or not
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
plt.rc("font", size = 14)
from sklearn.linear_model import LogisticRegression
from sklearn import preprocessing
import seaborn as sns
sns.set(style = "white")
sns.set(style = "whitegrid", color_codes = True)
from sklearn.model_selection import train_test_split
loan_status = pd.read_csv("/home/bhavani/data_sets_secureT/credit_train.csv", header = 0)
loan_status = loan_status.dropna()
loan_status.shape
