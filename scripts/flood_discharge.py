import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_excel("../data/flood_discharge.xlsx") 
df.columns = df.columns.str.strip()  # Clean column names

# Plot
sns.set_theme(style="whitegrid")
plt.figure(figsize=(14, 6))
sns.lineplot(data=df, x='Year', y='Discharge', marker='o', color='royalblue', linewidth=2.5)
plt.title("Annual Flood Discharge (1988–2021)", fontsize=16)
plt.xlabel("Year")
plt.ylabel("Discharge (m³/s)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
