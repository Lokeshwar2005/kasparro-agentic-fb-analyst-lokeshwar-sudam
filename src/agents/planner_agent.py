import json

class PlannerAgent:
    def __init__(self, llm_config):
        self.llm_config = llm_config
    
    def execute(self, user_query: str) -> dict:
        print("  - Planner: Decomposed query into subtasks.")
        # Simulates the Planner output structure
        return {
            "summary_of_request": f"Analysis of ROAS drop based on query: {user_query}",
            "task_sequence": ["DataAgent", "InsightAgent", "EvaluatorAgent", "CreativeGenerator", "ReportGenerator"]
        }
