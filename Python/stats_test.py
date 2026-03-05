import pandas as pd
from sqlalchemy import create_engine
from statsmodels.stats.proportion import proportions_ztest, confint_proportions_2indep

# Connect to your MySQL database
# Replace 'YOUR_PASSWORD' with your actual root password
engine = create_engine('mysql+mysqlconnector://root:Lucifer666$@localhost/ab_testing_project')

def run_decision_engine():
    # Fetch aggregated data from MySQL [cite: 31]
    query = "SELECT variant, converted FROM experiment_data"
    df = pd.read_sql(query, con=engine)
    
    # Aggregate for Z-test [cite: 32, 33]
    results = df.groupby('variant')['converted'].agg(['sum', 'count'])
    conv_a, n_a = results.loc['A', 'sum'], results.loc['A', 'count']
    conv_b, n_b = results.loc['B', 'sum'], results.loc['B', 'count']
    
    # 1. Z-Test for proportions [cite: 40]
    z_stat, p_val = proportions_ztest([conv_a, conv_b], [n_a, n_b])
    
    # 2. 95% Confidence Intervals [cite: 48]
    ci_low, ci_high = confint_proportions_2indep(conv_b, n_b, conv_a, n_a)

    # 3. Decision Logic [cite: 61, 62]
    # Decision rule: p-value < 0.05 is significant [cite: 46]
    is_significant = p_val < 0.05
    status = "SUCCESS" if is_significant and (conv_b/n_b > conv_a/n_a) else "FAIL"
    recommendation = "Deploy Variant B" if status == "SUCCESS" else "Keep Variant A"

    # Final Summary [cite: 64, 65, 66]
    print(f"--- Experiment Result: {status} ---")
    print(f"Recommended Action: {recommendation}")
    print(f"P-Value: {p_val:.4f}")
    print(f"Confidence: 95%")
    print(f"Confidence Interval: ({ci_low:.2%}, {ci_high:.2%})")

if __name__ == "__main__":
    run_decision_engine()
