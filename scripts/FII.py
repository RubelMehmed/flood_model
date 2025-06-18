import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ========== Step 1: Load Annual Discharge Data ==========
discharge_df = pd.read_excel('../data/flood_discharge.xlsx')

# Select major flood years
major_years = [1988, 1991, 1998, 2002, 2004, 2020]
discharge_df = discharge_df[discharge_df['Year'].isin(major_years)]

# ========== Step 2: Load Daily Flood Simulation Data ==========
flood_data = {}
for year in major_years:
    file_path = f"../data/model{year}.xlsx"
    if os.path.exists(file_path):
        df = pd.read_excel(file_path)
        df.columns = df.columns.str.strip()  # Clean column names
        flood_data[year] = df
    else:
        print(f"⚠️ File not found for year {year}: {file_path}")

# ========== Step 3: Calculate Peak and Duration ==========
threshold = 12.0
peak_discharges = {}
duration_above_threshold = {}

for year, df in flood_data.items():
    # Only consider columns A–E
    discharge_values = df[['A', 'B', 'C', 'D', 'E']]
    
    # Peak discharge across all stations
    peak = discharge_values.max().max()
    peak_discharges[year] = peak
    
    # Duration above threshold (average over stations)
    duration = (discharge_values > threshold).sum().mean()
    duration_above_threshold[year] = duration

# ========== Step 4: Calculate FII ==========
flood_intensity = {}
for year in major_years:
    peak = peak_discharges.get(year, 0)
    duration = duration_above_threshold.get(year, 0)
    FII = (peak * duration) / 100
    flood_intensity[year] = round(FII, 2)

# ========== Step 5: Plot FII ==========
plt.figure(figsize=(10, 6))
sns.barplot(x=list(flood_intensity.keys()), y=list(flood_intensity.values()), palette='magma')
plt.title('Flood Intensity Index (FII) for Major Flood Years', fontsize=14)
plt.xlabel('Year', fontsize=12)
plt.ylabel('FII Value', fontsize=12)
for i, (year, val) in enumerate(flood_intensity.items()):
    plt.text(i, val + 2, str(val), ha='center', va='bottom', fontsize=10)
plt.tight_layout()
plt.show()
