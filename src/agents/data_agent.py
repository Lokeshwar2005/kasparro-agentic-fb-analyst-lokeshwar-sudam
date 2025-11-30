import pandas as pd

class DataAgent:
    def __init__(self, df: pd.DataFrame, llm_config):
        self.df = df
        self.llm_config = llm_config
    
    def execute(self, user_query: str, data_summary: str) -> str:
        print("  - DataAgent: Generated targeted data slices.")
        # Generates a simple summary based on the sample data for the next agent
        low_roas_campaigns = self.df[self.df['roas'] < 3.0]['campaign_name'].unique()
        return f"Targeted Data Summary: Low ROAS campaigns: {', '.join(low_roas_campaigns)}. Data Agent observed Campaign A ROAS dropped from 5.0 to 2.4."
