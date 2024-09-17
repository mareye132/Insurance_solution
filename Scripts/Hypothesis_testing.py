import pandas as pd
from scipy.stats import ttest_ind, chi2_contingency
import numpy as np

# Load dataset
data_path = 'C:/Users/user/Desktop/Github/Insurance_solution/data/MachineLearningRating_v3.txt'
data = pd.read_csv(data_path, delimiter='|')

# Ensure column names are stripped of extra spaces
data.columns = data.columns.str.strip()

# Example of hypothesis testing
def hypothesis_testing(data):
    # 1. Risk Differences Across Provinces
    provinces = data['Province'].unique()
    province_risks = [data[data['Province'] == p]['Risk'] for p in provinces]
    _, p_value_provinces = f_oneway(*province_risks)
    
    # 2. Risk Differences Between Zip Codes
    zip_codes = data['PostalCode'].unique()
    zip_code_risks = [data[data['PostalCode'] == z]['Risk'] for z in zip_codes]
    _, p_value_zip_codes = f_oneway(*zip_code_risks)
    
    # 3. Margin Difference Between Zip Codes
    zip_code_margins = [data[data['PostalCode'] == z]['Margin'] for z in zip_codes]
    _, p_value_margins = f_oneway(*zip_code_margins)
    
    # 4. Risk Differences Between Women and Men
    genders = data['Gender'].unique()
    gender_risks = [data[data['Gender'] == g]['Risk'] for g in genders]
    _, p_value_genders = ttest_ind(*gender_risks)
    
    # Print results
    print(f"P-value for risk differences across provinces: {p_value_provinces}")
    print(f"P-value for risk differences between zip codes: {p_value_zip_codes}")
    print(f"P-value for margin differences between zip codes: {p_value_margins}")
    print(f"P-value for risk differences between women and men: {p_value_genders}")

if __name__ == "__main__":
    hypothesis_testing(data)
