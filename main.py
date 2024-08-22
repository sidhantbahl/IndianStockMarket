from load_data import load_data
from preprocess_data import preprocess_data
from eda import save_time_series_graphs
from time_series_analysis import decompose_time_series
from machine_learning import train_model

if __name__ == "__main__":
    directory = 'Nifty Fifty Master Data'
    graph_directory = 'time_series_graphs'
    decompose_time_series_graph_directory = 'decomposition_graphs'
    
    # Step 1: Load data
    stock_data = load_data(directory)

    # Step 2: Preprocess data
    stock_data = preprocess_data(stock_data)
    
    # Step 3: Perform EDA
    save_time_series_graphs(stock_data, graph_directory)
    
    decomposition_graph_directory = 'decomposition_graphs'
    decompose_time_series(stock_data, decomposition_graph_directory)
    
    # Step 5: Machine Learning (Save prediction graphs)
    prediction_graph_directory = 'prediction_graphs'
    results = train_model(stock_data, prediction_graph_directory)
    
    print("All steps completed. Results:")
    for result in results:
        print(result)