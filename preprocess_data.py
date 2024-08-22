def preprocess_data(stock_data):
    columns_to_drop = ['Price', 'Adj Close.1', 'Close.1', 'High.1', 'Low.1', 'Open.1', 'Volume.1']
    
    for stock, df in stock_data.items():
        df.drop(columns=columns_to_drop, inplace=True, errors='ignore')
        df.drop_duplicates(inplace=True)
        df.dropna(inplace=True)
        stock_data[stock] = df
    
    return stock_data

if __name__ == "__main__":
    from load_data import load_data
    
    directory = 'Nifty Fifty Master Data'
    stock_data = load_data(directory)
    stock_data = preprocess_data(stock_data)
    print("Preprocessing complete.")