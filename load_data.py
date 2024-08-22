import os
import pandas as pd

def load_data(directory):
    data_frames = {}
    for file_name in os.listdir(directory):
        if file_name.endswith('.csv'):
            stock_name = file_name.split('.')[0]
            df = pd.read_csv(os.path.join(directory, file_name))
            df['Source'] = stock_name
            data_frames[stock_name] = df
    return data_frames

if __name__ == "__main__":
    directory = 'Nifty Fifty Master Data'
    stock_data = load_data(directory)
    print(f"Loaded {len(stock_data)} files.")