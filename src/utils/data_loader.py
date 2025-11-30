import pandas as pd
import numpy as np

def load_data(file_path: str) -> pd.DataFrame:
    """
    Loads the CSV file, preprocesses the date column, and calculates 
    ROAS and CTR to ensure consistency across the analysis.
    """
    df = pd.read_csv(file_path)
    df['date'] = pd.to_datetime(df['date'])
    
    # Calculate ROAS: Revenue divided by Spend (required metric)
    # Use np.where to handle division by zero (sets ROAS to 0 if spend is 0)
    df['roas'] = np.where(df['spend'] > 0, df['revenue'] / df['spend'], 0)
    
    # Calculate CTR: Clicks divided by Impressions (required metric)
    df['ctr'] = np.where(df['impressions'] > 0, df['clicks'] / df['impressions'], 0)
    
    return df

def summarize_data(df: pd.DataFrame) -> str:
    """
    Generates a high-level summary string used by the Data Agent 
    to provide context to the Insight Agent.
    """
    return f"""
    Overall Period: {df['date'].min().date()} to {df['date'].max().date()}
    Total Spend: \${df['spend'].sum():.2f}
    Aggregated ROAS: \${df['revenue'].sum()/df['spend'].sum():.2f}
    """
