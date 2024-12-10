# -*- coding: utf-8 -*-
import pandas as pd

# Loading the file
file_path = '/Users/tejuskhandelwal/Desktop/UGP/GWQ_2010-2018.xlsx'
df = pd.read_excel(file_path, engine='openpyxl')
print(df.head)

"""# Data Preprocessing
This section includes handling missing values, cleaning, and preparing data for analysis.
"""

# Separating important columns
columns_to_extract = ['PH', 'TH', 'CA', 'MG', 'CHLORIDE', 'SULPHATE', 'NITRATE', 'FLUORIDE', 'TDS']
new_df = df[columns_to_extract]

print(new_df.head)

# Handling non numeric types
new_df.replace(['ND', 'BDL'], 0, inplace=True)

print((new_df == 'ND').sum())

print((new_df == 'BDL').sum())

print(new_df.isnull().sum())

# Converting data to numeric
new_df = new_df.apply(pd.to_numeric, errors='coerce')

print(new_df.isnull().sum())

print((new_df == 0).sum())

new_df.dropna(inplace=True)

# print(new_df.head)
print(new_df.shape[0])

# These are the standards as defined by Bureau of Indian Standards
bis_standards = {
    'PH': (6.5, 8.5),        # Acceptable range for pH
    'TH': (0, 200),          # Total Hardness in mg/L
    'CA': (0, 75),           # Calcium in mg/L
    'MG': (0, 30),           # Magnesium in mg/L
    'CHLORIDE': (0, 250),    # Chloride in mg/L
    'SULPHATE': (0, 200),    # Sulphate in mg/L
    'NITRATE': (0, 45),      # Nitrate in mg/L
    'FLUORIDE': (0, 1),    # Fluoride in mg/L
    'TDS': (0, 500)          # Total Dissolved Solids in mg/L
}

# Based on whether the data is within the limits we set if water is healthy or unhealthy
def check_health(row):
    for param, (low, high) in bis_standards.items():
        if pd.isna(row[param]) or not (low <= row[param] <= high):
            return 0
    return 1

print((new_df == 0).sum())

new_df['Health_Status'] = new_df.apply(check_health, axis=1)

print(new_df.head)

print((new_df['Health_Status']==1).sum())

print((new_df['Health_Status']==0).sum())

# Exporting
output_file_path = '/Users/tejuskhandelwal/Desktop/UGP/training_data.csv'
new_df.to_csv(output_file_path, index=False)
