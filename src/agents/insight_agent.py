class InsightAgent:
    def __init__(self, llm_config):
        self.llm_config = llm_config
    
    def execute(self, data_slices: str) -> str:
        print("  - InsightAgent: Formulated hypotheses (JSON).")
        # Returns a JSON string conforming to the Insights model (unvalidated)
        return '{"summary_of_change": "ROAS fluctuation detected.", "hypotheses": [{"driver": "Audience Fatigue", "hypothesis": "The ROAS drop is due to audience fatigue.", "confidence": 0.8, "validation_evidence": "", "final_confidence": 0.0}]}'
