import pandas as pd

def fraudulent_data_generator(file_path):
    df = pd.read_csv(file_path)
    for _, row in df.iterrows():
        yield row.to_dict()
