# Flood Simulation Model

### 1. Flood Intensity Index (FII)

Interactive visualization of FII values computed from peak discharge and flood duration (above 12.0m threshold) for major flood years: **1988, 1991, 1998, 2002, 2004, 2020**.

📌 _FII Formula:_  
\[
\text{FII} = \frac{\text{Peak Discharge} \times \text{Duration Above Threshold}}{100}
\]

🔗 **Code**: [`fii_plotly.py`](scripts/fii.py)

![FII Plot](plot/fii_plot.png)

---

### 2. Annual Flood Discharge Trend (1988–2021)

Line chart showing yearly peak discharges, with extreme years highlighted for context.

🔗 **Code**: [`trend_analysis.py`](scripts/trend_analysis.py)

![Discharge Trend](plot/trend_afd.png)

---

### 3. Flood Simulation Time Series (Daily)

Daily model outputs (columns A–E) plotted for each major flood year.

🔗 **Code**: [`discharge_plot.py`](scripts/fds.py)

#### 📆 1988 Flood Model Simulation

![Model 1988](plot/fms_1988.png)

#### 📆 1991 Flood Model Simulation

![Model 1991](plot/fms_1991.png)

#### 📆 1998 Flood Model Simulation

![Model 1998](plot/fms_1998.png)

#### 📆 2002 Flood Model Simulation

![Model 2002](plot/fms_2002.png)

#### 📆 2004 Flood Model Simulation

![Model 2004](plot/fms_2004.png)

#### 📆 2020 Flood Model Simulation

![Model 2020](plot/fms_2020.png)

---

### 3. Flood Simulation Time Series (by Year)

Daily simulation plots for selected major flood years, based on model outputs for stations A–E.

🔗 **Code**: [`discharge_plot.py`](scripts/fds.py)

## 📌 Data Source

**Title:** Validation of 1D and 2D Model Results with the Observed Data of the Old Brahmaputra River at Mymensingh Gauge Station  
**Type:** Daily discharge data, model simulations, annual discharge records  
**Source Format:** Excel (.xlsx)

---

## ⚙️ Environment Setup

```bash
# Create conda environment
conda create -n flood_model python=3.10
conda activate flood_model

# Install required packages
pip install pandas plotly seaborn matplotlib openpyxl
```
