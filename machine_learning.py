from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import os

def train_model(stock_data, graph_directory):
    # Ensure the graph directory exists
    if not os.path.exists(graph_directory):
        os.makedirs(graph_directory)
    
    results = []

    for stock, df in stock_data.items():
        df['Lag_1'] = df['Close'].shift(1)
        df['MA_10'] = df['Close'].rolling(window=10).mean()
        df['MA_50'] = df['Close'].rolling(window=50).mean()
        df.dropna(inplace=True)

        X = df[['Lag_1', 'MA_10', 'MA_50']]
        y = df['Close']
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)
        
        model = RandomForestRegressor(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)
        
        y_pred = model.predict(X_test)
        mse = mean_squared_error(y_test, y_pred)
        results.append({'Stock': stock, 'MSE': mse})

        # Define the file name and path for the prediction plot
        graph_file_name = f"{stock}_prediction.png"
        graph_file_path = os.path.join(graph_directory, graph_file_name)
        
        # Check if the graph already exists
        if not os.path.exists(graph_file_path):
            plt.figure(figsize=(10, 6))
            plt.plot(df['Date'].iloc[-len(y_test):], y_test, label='Actual')
            plt.plot(df['Date'].iloc[-len(y_test):], y_pred, label='Predicted')
            plt.title(f'{stock} Actual vs Predicted Close Price')
            plt.xlabel('Date')
            plt.ylabel('Close Price')
            plt.legend()
            plt.savefig(graph_file_path)  # Save the graph
            plt.close()  # Close the figure to free up memory
            print(f"Saved: {graph_file_name}")
        else:
            print(f"Graph already exists: {graph_file_name}")
    
    return results

if __name__ == "__main__":
    from preprocess_data import preprocess_data
    from load_data import load_data
    
    directory = 'Nifty Fifty Master Data'
    graph_directory = 'prediction_graphs'
    
    stock_data = load_data(directory)
    stock_data = preprocess_data(stock_data)
    results = train_model(stock_data, graph_directory)
    
    print("Model training complete. Results:")
    for result in results:
        print(result)
