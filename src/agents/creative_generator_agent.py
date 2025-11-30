import pandas as pd
import json

class CreativeGeneratorAgent:
    def __init__(self, df: pd.DataFrame, llm_config):
        self.df = df
        self.llm_config = llm_config
        self.CTR_LOW_THRESHOLD = 0.008 # Example from config

    def execute(self, validated_insights_json: str) -> str:
        print("  - CreativeGenerator: Proposed new messaging (JSON).")
        # Filter low CTR campaigns based on the threshold
        low_ctr_df = self.df[self.df['ctr'] < self.CTR_LOW_THRESHOLD]
        low_campaigns = low_ctr_df['campaign_name'].unique().tolist()
        
        # Simulation of generating creative ideas
        recommendations = [
            {
                "campaign_name": name,
                "original_message_theme": "Generic 10% Off",
                "new_headline": "Last Chance: Save Now!",
                "new_primary_message": "Injecting urgency based on high fatigue insight.",
                "new_cta": "Shop Now",
                "reasoning": "Using urgency to fight audience fatigue."
            } for name in low_campaigns
        ]

        # Returns a JSON string conforming to the CreativeRecommendations model
        return json.dumps({"low_ctr_campaigns_analyzed": low_campaigns, "recommendations": recommendations}, indent=2)
