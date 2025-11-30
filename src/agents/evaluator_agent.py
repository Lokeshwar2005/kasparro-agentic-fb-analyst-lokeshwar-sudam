import pandas as pd
import json

class EvaluatorAgent:
    def __init__(self, df: pd.DataFrame, llm_config):
        self.df = df
        self.llm_config = llm_config
        self.ROAS_THRESHOLD = 3.5 # Example from config

    def execute(self, insights_json: str) -> str:
        print("  - Evaluator: Validated hypotheses quantitatively and updated confidence.")
        # Simulation of quantitative check and confidence update
        insights = json.loads(insights_json)
        
        for hyp in insights['hypotheses']:
            # Example quantitative check
            roas_avg = self.df['roas'].mean()
            if roas_avg < self.ROAS_THRESHOLD:
                hyp['validation_evidence'] = f"Average campaign ROAS is {roas_avg:.2f}, confirming underperformance."
                hyp['final_confidence'] = 0.95
            else:
                hyp['validation_evidence'] = f"Average ROAS is acceptable ({roas_avg:.2f}), hypothesis rejected."
                hyp['final_confidence'] = 0.1
        
        return json.dumps(insights, indent=2)
