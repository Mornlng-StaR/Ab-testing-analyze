import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
import os

# 1. Connection (Update 'YOUR_PASSWORD' with your actual MySQL password)
engine = create_engine('mysql+mysqlconnector://root:Lucifer666$@localhost/ab_testing_project')

def generate_funnel_chart():
    # 2. SQL Analysis Layer: Fetching Funnel Data
    query = """
    SELECT 
        variant,
        SUM(visited) AS Visitors,
        SUM(clicked) AS Clicks,
        SUM(converted) AS Conversions
    FROM experiment_data
    GROUP BY variant;
    """
    df = pd.read_sql(query, con=engine)
    
    # 3. Setup Visualization Layer
    stages = ['Visitors', 'Clicks', 'Conversions']
    colors = ['#2ecc71', '#3498db'] # Green for Variant A, Blue for Variant B
    
    plt.figure(figsize=(10, 6))
    
    for i, variant in enumerate(['A', 'B']):
        # Extract the values for each variant
        values = df[df['variant'] == variant][stages].values[0]
        plt.barh(stages, values, label=f'Variant {variant}', color=colors[i], alpha=0.7)

    # 4. Formatting for the Portfolio
    plt.xlabel('Number of Users')
    plt.title('A/B Test Funnel Visualization')
    plt.legend()
    plt.gca().invert_yaxis() # Puts 'Visitors' at the top
    plt.grid(axis='x', linestyle='--', alpha=0.6)
    
    # 5. Fix for Directory Error: Create folder if missing
    output_dir = 'dashboard'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # 6. Save the Chart
    file_path = os.path.join(output_dir, 'funnel_chart.png')
    plt.tight_layout()
    plt.savefig(file_path)
    print(f"Success! Funnel chart saved to {file_path}")
    plt.show()

if __name__ == "__main__":
    generate_funnel_chart()
