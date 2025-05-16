import pandas as pd

def load_data(csv_path):
    df = pd.read_csv(csv_path)
    df.columns = ['ICDCode', 'Description']
    # print(df)
    return df

data_csv = "../data/ICDCodeSet.csv"

load_data(data_csv)