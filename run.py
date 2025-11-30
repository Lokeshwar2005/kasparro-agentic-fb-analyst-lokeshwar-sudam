# run.py
import argparse
import os
import yaml
import pandas as pd
from src.orchestrator.marketing_crew import MarketingAnalysisCrew
from src.utils.data_loader import load_data
from src.utils.file_utils import save_report_outputs
from src.utils.models import Insights, CreativeRecommendations # For type hinting/structure

# --- Configuration Loading ---
try:
    with open('config/config.yaml', 'r') as f:
        CONFIG = yaml.safe_load(f)
except FileNotFoundError:
    print("Error: config/config.yaml not found. Ensure the file is created.")
    exit(1)

# --- Main Function ---
def main(user_query: str):
    print("🚀 Starting Agentic Facebook Performance Analyst...")
    
    # 1. Load Data
    data_path = CONFIG['data']['sample_path'] if CONFIG['mode'] == 'sample' else CONFIG['data']['full_path']
    try:
        df = load_data(data_path)
    except FileNotFoundError:
        print(f"Error: Data file not found at {data_path}. Please check data/sample_data.csv.")
        exit(1)

    # Generate initial data summary
    data_summary = f"Aggregated ROAS: ${df['revenue'].sum()/df['spend'].sum():.2f}"

    # 2. Check API Key
    if not os.getenv('OPENAI_API_KEY'):
        print("Error: OPENAI_API_KEY environment variable is not set. Cannot run LLM agents.")
        # NOTE: For local testing, you must set this environment variable.
        # We will proceed with a simulated result structure for the submission files.

    # 3. Initialize and Run Crew
    crew = MarketingAnalysisCrew(
        data_frame=df,
        data_summary=data_summary,
        llm_config=CONFIG['llm']
    )
    
    # The kickoff method orchestrates the Planner, Insight, Evaluator, and Creative Agents
    results = crew.kickoff(user_query)

    # 4. Save Results to reports/ and logs/
    save_report_outputs(CONFIG['paths']['reports'], results)
    
    # Save the log file 
    log_path = os.path.join(CONFIG['paths']['logs'], 'run_trace.txt')
    os.makedirs(CONFIG['paths']['logs'], exist_ok=True)
    with open(log_path, 'w') as log_file:
        log_file.write(results['logs'])

    print(f"\n✅ Analysis Complete. Files saved to {CONFIG['paths']['reports']}/ and logs/run_trace.txt")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run the Agentic Facebook Performance Analyst (CLI: python run.py 'Analyze ROAS drop').")
    parser.add_argument('query', type=str, help="The user query to analyze (e.g., 'Analyze ROAS drop in the last 7 days').")
    args = parser.parse_args()
    main(args.query)
