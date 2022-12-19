import pandas as pd

data = pd.read_csv('list.csv')
data = data[data['City']=="London"]

data.to_csv('london_list.csv')