# Job Satisfaction Analysis (Work in Progress)

This project explores factors that shape **overall job satisfaction** based on survey data from **Biuro Kapitału Ludzkiego (Poland)**.  
The goal is to understand which aspects of work matter most for people's job satisfaction, and how these priorities differ across groups.

---
Overview

The project analyzes self-reported survey data from employed individuals in Poland.  
Respondents include full-time and part-time employees under any type of contract.  
Excluded groups:
- People whose main job was **agricultural work (own/family farm)**  
- **Self-employed** or **business owners**, due to data irrelevance and missing responses
---
Project Objectives

1. Identify key predictors of overall job satisfaction  
2. Assess how different satisfaction components (e.g., pay, work-life balance, management) contribute  
3. Explore differences between groups of employees using clustering  
4. Interpret results through explainable ML methods (e.g., SHAP)
---
Project Structure

`job_satisfaction_analysis.ipynb` | Combined draft notebook – will be split and refined

---
Current Status

**Status:** Work in progress

Completed:
1. Split monolithic notebook into modular notebooks:
01_data_cleaning.ipynb
02_eda.ipynb
03_modelling.ipynb
04_advanced_analysis.ipynb (SHAP / clustering ready)

2. Implemented data/ folder structure (raw/, processed/, metadata/) with privacy considerations
3. Created utils/ folder with reusable functions (helpers.py, data_prep.py)
4. Trained and saved final model (best_model.pkl)
5. Improved code modularity and clarity in notebooks
6. Ongoing / Next Steps:
Refining plots and visualizations for readability and consistency
Finalizing README documentation to reflect current workflow and insights

---
Data

- **Source:** Biuro Kapitału Ludzkiego survey data (Poland)
- **Scope:** Employed individuals (excluding agricultural and self-employed respondents)
- **Type:** Self-reported survey responses
- **Privacy:** Dataset not included in repo; only processed model and code are shared
- **Limitation:** Self-reporting bias and incomplete responses

---
Methods & Tools

- Python (pandas, numpy, scikit-learn, matplotlib, seaborn, joblib)
- Modular notebook workflow (01_data_cleaning → 02_eda → 03_modelling → 04_advanced_analysis)
- SHAP / clustering analysis for model interpretability

---

Limitations 

TBD

---

Next Steps
- Refine visualizations for clarity and consistency
- Improving interpretability and communication of findings  
- Complete final README documentation and project narrative
- Optional: future dashboard or interactive results outside GitHub
- Prepare for public release  

---

Key Insights

TBD

---