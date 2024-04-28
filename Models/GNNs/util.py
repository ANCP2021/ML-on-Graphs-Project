import pandas as pd
import torch
from sklearn.preprocessing import StandardScaler


def readFile(path, columnNames):
    # Read csv
    df = pd.read_csv(path, usecols=columnNames)
    x, y = [], []
    
    # Create lag attributesd
    for col in columnNames:
        df[f'{col}_lag1'] = df[col].shift(1)
        
    df.dropna(inplace=True) # Drop because of Nan values

    df = df.drop(['DATE', 'DATE_lag1'], axis=1) # Drop 'DATE' and 'DATE_lag1' and  column

    # Define x and y variables for lag and current populations
    x_columns = [col for col in df.columns if '_lag' in col]
    y_columns = [col for col in df.columns if '_lag' not in col]

    x = df[x_columns].values
    y = df[y_columns].values

    return x, y


def splitDataset(x, y, split_percent):
    split_idx = int(len(x) * split_percent)
    x_train, x_test = x[:split_idx], x[split_idx:]
    y_train, y_test = y[:split_idx], y[split_idx:]

    scaler = StandardScaler()
    x_train = scaler.fit_transform(x_train)
    x_test = scaler.transform(x_test)

    scaler = StandardScaler()
    y_train = scaler.fit_transform(y_train)
    y_test = scaler.transform(y_test)

    # Convert to PyTorch tensors
    x_train = torch.tensor(x_train, dtype=torch.float)
    x_test = torch.tensor(x_test, dtype=torch.float)
    y_train = torch.tensor(y_train, dtype=torch.float)
    y_test = torch.tensor(y_test, dtype=torch.float)

    return x_train, x_test, y_train, y_test


def r_squared(y_true, y_pred):
    y_true_mean = torch.mean(y_true)
    ss_res = torch.sum((y_true - y_pred) ** 2)
    ss_tot = torch.sum((y_true - y_true_mean) ** 2)

    return 1 - ss_res / ss_tot