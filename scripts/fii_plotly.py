import pandas as pd
import plotly.express as px
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
        df.columns = df.columns.str.strip()
        flood_data[year] = df
    else:
        print(f"⚠️ File not found for year {year}: {file_path}")

# ========== Step 3: Calculate Peak and Duration ==========
threshold = 12.0
peak_discharges = {}
duration_above_threshold = {}

for year, df in flood_data.items():
    discharge_values = df[['A', 'B', 'C', 'D', 'E']]
    peak = discharge_values.max().max()
    peak_discharges[year] = peak
    duration = (discharge_values > threshold).sum().mean()
    duration_above_threshold[year] = duration

# ========== Step 4: Calculate FII ==========
fii_data = []
for year in major_years:
    peak = peak_discharges.get(year, 0)
    duration = duration_above_threshold.get(year, 0)
    fii = round((peak * duration) / 100, 2)
    fii_data.append({
        'Year': year,
        'Peak Discharge': round(peak, 2),
        'Duration > Threshold': round(duration, 2),
        'FII': fii
    })

fii_df = pd.DataFrame(fii_data)

# ========== Step 5: Interactive Plotly Bar Chart ==========
fig = px.bar(
    fii_df,
    x='Year',
    y='FII',
    text='FII',
    color='FII',
    color_continuous_scale='magma',
    labels={'FII': 'Flood Intensity Index'},
    title='Flood Intensity Index (FII) for Major Flood Years'
)

fig.update_traces(
    texttemplate='%{text}',
    textposition='outside',
    marker_line_color='black',
    marker_line_width=1
)

fig.update_layout(
    title_x=0.5,
    yaxis=dict(title='FII Value'),
    xaxis=dict(type='category'),
    uniformtext_minsize=8,
    uniformtext_mode='hide',
    margin=dict(t=80, b=40, l=50, r=50),
    height=500
)

# ========== Show the Plot ==========
fig.show()
