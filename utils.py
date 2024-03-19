import pandas as pd

def load_train_data() :
  df = pd.read_csv('train.csv')
  x_train = df.iloc[:,:-1].to_numpy()
  y_train = df.iloc[:,-1].to_numpy()
  return (x_train, y_train)