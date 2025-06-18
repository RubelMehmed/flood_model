import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

# Load data
df = pd.read_excel("../data/flood_discharge.xlsx")  # Replace with actual file name
df.columns = df.columns.str.strip()

# Sort data by year to ensure proper plotting
df = df.sort_values("Year")

# Normalize discharge for color mapping
norm = plt.Normalize(df["Discharge"].min(), df["Discharge"].max())
colors = cm.viridis(norm(df["Discharge"]))

# Create plot
fig, ax = plt.subplots(figsize=(14, 6))

# Line with gradient by segments
for i in range(len(df) - 1):
    ax.plot(df["Year"].iloc[i:i+2], df["Discharge"].iloc[i:i+2],
            color=colors[i], linewidth=3)

# Scatter points to show data points
sc = ax.scatter(df["Year"], df["Discharge"], c=df["Discharge"],
                cmap="viridis", edgecolor='k', s=60, zorder=3)

# Annotate extreme years
for year in [1988, 1998, 2004]:
    val = df[df["Year"] == year]
    if not val.empty:
        x = val["Year"].values[0]
        y = val["Discharge"].values[0]
        ax.annotate(f"{year}\n{y:.0f}", xy=(x, y), xytext=(x, y+200),
                    ha='center', fontsize=10,
                    arrowprops=dict(arrowstyle='->', color='black'))

# Styling
ax.set_title("Flood Discharge in Bangladesh (1988–2021)", fontsize=16)
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Discharge (m³/s)", fontsize=12)
plt.xticks(df["Year"], rotation=45)
plt.colorbar(sc, label='Discharge (m³/s)')
plt.tight_layout()
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()
