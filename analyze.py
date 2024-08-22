import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.seasonal import seasonal_decompose
import os

# Assuming all CSV files are in the same directory
output_file = 'cleaned_nifty_fifty_data.csv'

# Check if the cleaned file already exists
if not os.path.exists(output_file):
    directory = 'Nifty Fifty Master Data'
    files = [f for f in os.listdir(directory) if f.endswith('.csv')]
    
    # Load all files into a single DataFrame
    df_list = []
    for file in files:
        df = pd.read_csv(os.path.join(directory, file))
        df['Source'] = file  # Optional: Add a column to identify the source file
        df_list.append(df)
    
    combined_df = pd.concat(df_list, ignore_index=True)
    columns_to_drop = ['Price', 'Adj Close.1', 'Close.1', 'High.1', 'Low.1', 'Open.1', 'Volume.1']
    combined_df = combined_df.drop(columns=columns_to_drop)
    
    # Step 2: Check for and drop duplicate rows (if any)
    combined_df = combined_df.drop_duplicates()
    
    # Step 3: Drop rows with missing values
    combined_df_cleaned = combined_df.dropna()
    
    # Step 4: Convert 'Date' column to datetime format 
    combined_df_cleaned['Date'] = pd.to_datetime(combined_df_cleaned['Date'])
    
    # Step 5: Inspect the cleaned DataFrame
    print(combined_df_cleaned.head())
    print(combined_df_cleaned.info())
    
    # Cleaned file
    combined_df_cleaned.to_csv('cleaned_nifty_fifty_data.csv', index=False)
