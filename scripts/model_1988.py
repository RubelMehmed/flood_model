import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Excel file
model1988 = pd.read_excel("../data/model1988.xlsx")

# Convert 'time' column to datetime (ensure day-first format)
model1988['time'] = pd.to_datetime(model1988['time'], dayfirst=True)

# Set seaborn style
sns.set_theme(style="whitegrid")

# Initialize plot
plt.figure(figsize=(14, 6))

# Plot each series with updated, meaningful colors
plt.plot(model1988['time'], model1988['A'], label="Observed", color="orange")
plt.scatter(model1988['time'], model1988['A'], color="orange")

plt.plot(model1988['time'], model1988['B'], label="1D without modification", color="purple")
plt.scatter(model1988['time'], model1988['B'], color="purple")

plt.plot(model1988['time'], model1988['C'], label="2D without modification", color="blue")
plt.scatter(model1988['time'], model1988['C'], color="blue")

plt.plot(model1988['time'], model1988['D'], label="1D with modification", color="navy")
plt.scatter(model1988['time'], model1988['D'], color="navy")

plt.plot(model1988['time'], model1988['E'], label="2D with modification", color="green")
plt.scatter(model1988['time'], model1988['E'], color="green")

# Set x-axis limits to match only the available data range
plt.xlim(model1988['time'].min(), model1988['time'].max())

# Format x-axis
plt.xticks(rotation=45)
plt.xlabel("Date")
plt.ylabel("Water Level (m)")
plt.title("Flood Simulation – July 1988", fontsize=16)

# Legend
plt.legend(title="Legend", loc='lower center', bbox_to_anchor=(0.5, -0.3), ncol=2)

# Layout
plt.tight_layout()
plt.show()
