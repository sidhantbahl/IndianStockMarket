from statsmodels.tsa.seasonal import seasonal_decompose
import matplotlib.pyplot as plt
import os

def decompose_time_series(stock_data, graph_directory):
    # Ensure the graph directory exists
    if not os.path.exists(graph_directory):
        os.makedirs(graph_directory)
    
    for stock, df in stock_data.items():
        # Define the file name and path for the decomposition plot
        graph_file_name = f"{stock}_decomposition.png"
        graph_file_path = os.path.join(graph_directory, graph_file_name)
        
        # Check if the graph already exists
        if not os.path.exists(graph_file_path):
            decomposition = seasonal_decompose(df['Close'], model='additive', period=365)
            decomposition.plot()
            plt.suptitle(f'{stock} Time-Series Decomposition')
            plt.savefig(graph_file_path)  # Save the graph
            plt.close()  # Close the figure to free up memory
            print(f"Saved: {graph_file_name}")
        else:
            print(f"Graph already exists: {graph_file_name}")

if __name__ == "__main__":
    from preprocess_data import preprocess_data
    from load_data import load_data
    
    directory = 'Nifty Fifty Master Data'
    graph_directory = 'decomposition_graphs'
    
    stock_data = load_data(directory)
    stock_data = preprocess_data(stock_data)
    decompose_time_series(stock_data, graph_directory)