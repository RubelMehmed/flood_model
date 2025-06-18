import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Excel file
model1991 = pd.read_excel("../data/model1991.xlsx")

# Convert 'time' column to datetime (ensure day-first format)
model1991['time'] = pd.to_datetime(model1991['time'], dayfirst=True)

# Set seaborn style
sns.set_theme(style="whitegrid")

# Initialize plot
plt.figure(figsize=(14, 6))

# Plot lines and points for each model
plt.plot(model1991['time'], model1991['A'], label="Observed", color="purple")
plt.scatter(model1991['time'], model1991['A'], color="purple")

plt.plot(model1991['time'], model1991['B'], label="1D without modification", color="cyan")
plt.scatter(model1991['time'], model1991['B'], color="cyan")

plt.plot(model1991['time'], model1991['C'], label="2D without modification", color="blue")
plt.scatter(model1991['time'], model1991['C'], color="blue")

plt.plot(model1991['time'], model1991['D'], label="1D with modification", color="green")
plt.scatter(model1991['time'], model1991['D'], color="green")

plt.plot(model1991['time'], model1991['E'], label="2D with modification", color="red")
plt.scatter(model1991['time'], model1991['E'], color="red")

# Set x-axis limits to match only the dates in the file
plt.xlim(model1991['time'].min(), model1991['time'].max())

# Format x-axis labels
plt.xticks(rotation=45)
plt.xlabel("Date")
plt.ylabel("Water Level (m)")
plt.title("Flood Simulation – July 1991", fontsize=16)

# Add legend
plt.legend(title="Legend", loc='lower center', bbox_to_anchor=(0.5, -0.3), ncol=2)

# Adjust layout to prevent clipping
plt.tight_layout()
plt.show()
