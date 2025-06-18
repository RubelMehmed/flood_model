import pandas as pd
from scipy.stats import linregress
import matplotlib.pyplot as plt

# Load the data
df = pd.read_excel('../data/flood_discharge.xlsx')

# Clean column names
df.columns = df.columns.str.strip()

# Print column names to confirm
print("Columns in the file:", df.columns.tolist())

# Proceed with analysis after confirming correct column names
if 'Discharge' in df.columns and 'Year' in df.columns:
    # Linear regression
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['Discharge'])

    # Plot
    plt.figure(figsize=(10, 6))
    plt.plot(df['Year'], df['Discharge'], marker='o', label='Discharge')
    plt.plot(df['Year'], intercept + slope * df['Year'], 'r--', label='Trend line')
    plt.title('Trend in Annual Flood Discharge')
    plt.xlabel('Year')
    plt.ylabel('Discharge (m³/s)')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    print(f"Slope: {slope:.2f}, Intercept: {intercept:.2f}")
    print(f"R-squared: {r_value**2:.4f}, P-value: {p_value:.4f}")
else:
    print("Error: 'Year' or 'Discharge' column not found.")
