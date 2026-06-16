# 🌡️ Germany's Climate Bill
### Data Bootcamp Capstone · Spiced Academy · June 2026

An interactive climate impact analysis dashboard exploring the relationship between Germany's changing climate, insured weather losses, and emissions reduction progress.

---

## 🔍 Research Questions

| RQ | Question | Method |
|---|---|---|
| RQ1 | Is Germany's climate measurably changing? | Mann-Kendall trend tests · DWD 1881–2025 |
| RQ2 | Are insured losses from natural hazards growing? | Mann-Kendall · nominal, real, GVA-normalised |
| RQ3 | What climate variable drives insured losses? | OLS regression · 6 variables tested |
| RQ4 | What is Germany doing — and is it enough? | UBA KSG sectors · CAT projections · cost scenarios |

---

## 📊 Dashboard

Built with Streamlit + Plotly. Run locally:

```bash
cd notebooks
streamlit run streamlit_app.py
```

---

## 🗂️ Project Structure
CAPSTONE-CLIMATE-GERMANY/

├── notebooks/

│   ├── 00_data_acquisition.ipynb

│   ├── 01_eda_cleaning.ipynb

│   ├── 02_rq1.ipynb

│   ├── 03_rq2_rq4.ipynb

│   ├── 04_rq3.ipynb

│   └── streamlit_app.py

├── data/

│   ├── raw/

│   ├── processed/

│   └── figures/          # gitignored

└── README.md

---

## 📦 Data Sources

| Source | Data | Coverage |
|---|---|---|
| **DWD** | National temperature, extreme events, precipitation | 1881–2025 |
| **GDV** | Insured losses from natural hazards | 1973–2024 |
| **Destatis** | Consumer Price Index, Gross Value Added | 1991–2024 |
| **UBA** | GHG emissions by KSG sector | 1990–2025 |
| **CAT** | Climate Action Tracker projections | July 2025 |

---

## 🛠️ Stack

- **Python** · pandas · statsmodels · pymannkendall
- **Visualisation** · Plotly Express · Plotly Graph Objects
- **Dashboard** · Streamlit
- **Other** · Jupyter · VS Code · GitHub · PostgreSQL · dbt

---

## 🔑 Key Findings

- 🌡️ **All four climate indicators** show statistically significant trends (p < 0.001)
- 💶 **Nominal insured losses** are growing (p = 0.0007) — but not in real terms or as % of GVA
- 📉 **Heavy rain days** are the only climate variable significantly correlated with losses (p = 0.020, 1991–2024)
- ⚠️ **Germany's emissions** are falling (Tau = −0.940) but transport and buildings are critically off track
- 💸 Each extra heavy rain day costs an estimated **+€0.394bn** in insured losses

---

## ⚠️ Limitations

- Insured losses only — uninsured damage not captured
- OLS model explains 16% of variance (R² = 0.158) — other drivers exist
- Heavy rain days trend not yet statistically significant (p = 0.874) — small n, high variability
- CPI restricted to 1991–2024 due to reunification index break

---

## 👤 Author

**Erick Burgueño Salas**  
Environmental Researcher · Data Analytics · Berlin  
[LinkedIn](https://linkedin.com/in/) · [GitHub](https://github.com/)

---

*Spiced Academy Data Analytics Bootcamp · Berlin · 2026*