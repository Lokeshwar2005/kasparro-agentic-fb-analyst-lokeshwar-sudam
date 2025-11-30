import json
import pandas as pd
from src.agents.planner_agent import PlannerAgent
from src.agents.data_agent import DataAgent
from src.agents.insight_agent import InsightAgent
from src.agents.evaluator_agent import EvaluatorAgent
from src.agents.creative_generator_agent import CreativeGeneratorAgent
from src.utils.data_loader import summarize_data # Helper

class MarketingAnalysisCrew:
    def __init__(self, data_frame: pd.DataFrame, data_summary: str, llm_config: dict):
        self.df = data_frame
        self.data_summary = data_summary
        self.llm_config = llm_config
        # Initialize agents (simulated)
        self.planner = PlannerAgent(llm_config)
        self.data_agent = DataAgent(data_frame, llm_config)
        self.insight_agent = InsightAgent(llm_config)
        self.evaluator = EvaluatorAgent(data_frame, llm_config)
        self.creative_generator = CreativeGeneratorAgent(data_frame, llm_config)

    def kickoff(self, user_query: str) -> dict:
        print("\n--- Agent Workflow Start ---")
        
        # 1. Plan the analysis
        plan_output = self.planner.execute(user_query)
        print(f"Plan: {plan_output.get('task_sequence', ['Planning successful.'])[0]}...")

        # 2. Data Preparation
        data_slices = self.data_agent.execute(user_query, self.data_summary)
        
        # 3. Insight Generation
        initial_insights_json = self.insight_agent.execute(data_slices)
        
        # 4. Hypothesis Validation (Planner-Evaluator Loop)
        validated_insights_json = self.evaluator.execute(initial_insights_json)
        
        # 5. Creative Recommendations
        creatives_json = self.creative_generator.execute(validated_insights_json)

        # 6. Report Generation
        report_md = self._generate_final_report(validated_insights_json, creatives_json)
        
        print("--- Agent Workflow Complete ---")

        return {
            'report_md': report_md,
            'insights_json': validated_insights_json,
            'creatives_json': creatives_json,
            'logs': 'Full execution log trace stored here: Planner executed -> Data Summarized -> Insights Formed -> Hypotheses Validated -> Creatives Proposed.'
        }

    def _generate_final_report(self, insights_json: str, creatives_json: str) -> str:
        # A simplified method to combine JSON outputs into a Markdown report
        try:
            insights = json.loads(validated_insights_json)
            creatives = json.loads(creatives_json)
        except json.JSONDecodeError:
             return "# Final Report Error: Could not parse agent outputs."

        report = "# Final ROAS Performance Analysis Report\n\n"
        report += "## 💡 Executive Summary\n"
        report += insights.get('summary_of_change', 'Analysis complete.') + "\n\n"
        
        report += "## 📈 Diagnosed Drivers (Validated Insights)\n"
        for hyp in insights.get('hypotheses', []):
            report += f"### {hyp['driver']} (Confidence: {hyp['final_confidence']:.2f})\n"
            report += f"* **Evidence**: {hyp['validation_evidence']}\n"
            
        report += "## ✍️ Creative Recommendations\n"
        for rec in creatives.get('recommendations', []):
            report += f"### For Campaign: {rec['campaign_name']}\n"
            report += f"* **New Headline**: **{rec['new_headline']}**\n"
            report += f"* **Reasoning**: {rec['reasoning']}\n\n"
            
        return report
