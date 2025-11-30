import os

def save_report_outputs(output_dir: str, results: dict):
    """Saves the final report outputs (report.md, insights.json, creatives.json) to the designated directory."""
    
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    # Save the final summarized report
    with open(os.path.join(output_dir, 'report.md'), 'w') as f:
        f.write(results.get('report_md', '# Error: Report content missing.'))
    
    # Save the structured insights
    with open(os.path.join(output_dir, 'insights.json'), 'w') as f:
        f.write(results.get('insights_json', '{}'))
        
    # Save the generated creative recommendations
    with open(os.path.join(output_dir, 'creatives.json'), 'w') as f:
        f.write(results.get('creatives_json', '{}'))

    print(f"Reports saved successfully to {output_dir}/")
