import os
import matplotlib.pyplot as plt

def create_graph_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def save_time_series_graphs(stock_data, graph_directory):
    create_graph_directory(graph_directory)
    
    for stock, df in stock_data.items():
        try:
            # Check if 'Date' column exists
            if 'Date' not in df.columns:
                raise KeyError(f"'Date' column not found in {stock} data.")

            # Define the file name and path for the graph
            graph_file_name = f"{stock}_time_series.png"
            graph_file_path = os.path.join(graph_directory, graph_file_name)
            
            # Check if the graph already exists
            if not os.path.exists(graph_file_path):
                plt.figure(figsize=(10, 6))
                plt.plot(df['Date'], df['Close'], label=f'{stock} Close Price')
                plt.title(f'Time-Series of {stock}')
                plt.xlabel('Date')
                plt.ylabel('Close Price')
                plt.legend()
                plt.savefig(graph_file_path)  # Save the graph
                plt.close()  # Close the figure to free up memory
                print(f"Saved: {graph_file_name}")
            else:
                print(f"Graph already exists: {graph_file_name}")
        
        except KeyError as e:
            print(f"Error with {stock}: {e}")
        except Exception as e:
            print(f"An unexpected error occurred with {stock}: {e}")

if __name__ == "__main__":
    from preprocess_data import preprocess_data
    from load_data import load_data
    
    directory = 'Nifty Fifty Master Data'
    graph_directory = 'time_series_graphs'
    
    stock_data = load_data(directory)
    stock_data = preprocess_data(stock_data)
    save_time_series_graphs(stock_data, graph_directory)