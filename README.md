# Job Satisfaction Analysis 

This project explores factors that shape **overall job satisfaction** based on survey data from **Biuro Kapitału Ludzkiego (Poland)**.  
The goal is to understand which aspects of work matter most for people's job satisfaction, and how these priorities differ across groups.

---
## Overview

The project analyzes self-reported survey data from employed individuals in Poland.  
Respondents include full-time and part-time employees under any type of contract.  
Excluded groups:
- People whose main job was **agricultural work (own/family farm)**  
- **Self-employed** or **business owners**, due to data irrelevance and missing responses

---
## Project Objectives

1. Identify key predictors of overall job satisfaction  
2. Assess how different satisfaction components (e.g., pay, work-life balance, management) contribute  
3. Explore differences between groups of employees using clustering  
4. Interpret results through explainable ML methods (e.g., SHAP)

---
## Objectives vs. Methods

| Objective | Method / Tool |
|-----------|---------------|
| Identify key predictors of overall job satisfaction | Regression models: Linear, Ridge, Lasso, Random Forest, XGBoost |
| Assess contributions of satisfaction components (pay, work-life balance, management) | SHAP feature importance and direction |
| Explore differences between employee groups | K-means clustering on SHAP-transformed features |
| Interpret results through explainable ML | SHAP visualizations and cluster summaries |
| Provide actionable HR insights | Notebook summaries and aggregated plots |

---
## Project Structure

### Notebooks
- `01_preprocessing_and_integrated_eda.ipynb` – data cleaning, preprocessing, and exploratory data analysis
- `02_modelling.ipynb` – model training, evaluation, and baseline predictions
- `03_advanced_analysis.ipynb` – SHAP interpretation, clustering, and advanced analyses

### Data (`data/`)
- `raw/` – original survey files (not included in repo, only `.gitkeep` placeholder)
- `processed/` – cleaned datasets used for analysis
- `metadata/` – data dictionaries and variable information

### Models (`models/`)
- `best_model.pkl` – trained final model
- Other `.pkl` files – intermediate train/test splits and scaled features

### Utilities (`utils/`)
- `data_io.py` – functions for loading data
- `evaluation.py` – functions for evaluating model performance
- `notebook_setup.py` – common notebook setup routines
- `viz_style.py` – visualization styling functions
- `__init__.py` – package initializer

---
## Data

- **Source:** Biuro Kapitału Ludzkiego survey data (Poland)
- **Scope:** Employed individuals (excluding agricultural and self-employed respondents)
- **Type:** Self-reported survey responses
- **Privacy:** Dataset not included in repo; only processed model and code are shared
- **Limitation:** Self-reporting bias and incomplete responses

---
## Methods & Tools

- Python (pandas, numpy, scikit-learn, matplotlib, seaborn, joblib)
- Modular notebook workflow (01_preprocessing_and_intergrated_eda → 02_modelling → 03_advanced_analysis)
- SHAP / clustering analysis for model interpretability

---
## Limitations

- **Self-reporting Bias**: As with any self-reported survey, responses may be influenced by recall bias, social desirability, or subjective interpretation of questions.
- **Data & Missingness**: Some survey responses were incomplete. For Likert-scale questions (j-variables), missingness was generally low (<8%), while salary-related questions (m-variables) had ~20% missing responses due to refusal to disclose. Missing data could affect model reliability, especially for salary-related analyses.
- **Sampling biases**: Potential sampling biases were not formally assessed. Future work could explore whether certain industries, job types, or demographic groups are over- or under-represented in the dataset. 
- **Modeling & Interpretability**: Multiple regression and tree-based models were tested (linear regression, ridge, lasso, Random Forest, XGBoost, SVR, KNN, GBR), with SHAP used for interpretability. The final model (ridge regression) achieved an R² of ~30%, which is typical for social science survey data but indicates substantial unexplained variation. Relationships were assumed linear; any underlying nonlinear interactions may not be fully captured.
- **Generality / External Validity**: Survey data were collected in 2021. The dataset covers employees in Poland only. While some findings may generalize to culturally similar Central European countries, results cannot be assumed to hold elsewhere without additional data. Findings may not generalize to post-COVID-19 labor market conditions, particularly for younger workers.
- **Unobserved Factors & Heterogeneity**: Some factors influencing job satisfaction may not have been captured in the survey. Additionally, job types and industries were not analyzed separately due to heterogeneity and classification challenges; factors driving satisfaction may differ across sectors.
- **Clustering / SHAP Limitations**: Clustering and SHAP interpretations are model-specific. Linear models may not capture nonlinear interactions, and cluster results may be sensitive to scaling and feature selection.

---
## Key Insights

### Top Predictors of Job Satisfaction
- **Personal satisfaction with earnings (j1_01)** is the strongest predictor, more important than actual income levels.
- Other strong positive predictors: **satisfaction with work tasks** and **employment security**.
- Strongest negative predictor: **desire to change jobs**.
- Other notable factors: positive impact from **learning opportunities**, negative impact from **excessive workload**.

### Cluster Patterns
- Seven clusters reveal distinct patterns of job satisfaction:
  1. **Financially anchored satisfaction** – satisfaction driven by pay and financial security (Clusters 4, 5, 6).
  2. **Stability/condition-based satisfaction** – comfort and balance drive satisfaction (Cluster 2).
  3. **Compensated dissatisfaction** – higher pay does not translate to happiness; these employees remain dissatisfied despite positive conditions (Clusters 0, 1, 3).
- Clustering metrics indicate **moderate separation** (Calinski-Harabasz index 70.96; Davies-Bouldin index 2.88).

### Generational Patterns
- **Gen Z** reports the highest overall satisfaction; **Baby Boomers** the lowest.
- **Millennials** report the easiest time making ends meet.
- **Gen X** shows mixed patterns: less satisfied with stability but more satisfied with learning opportunities.

### Other Notable Patterns
- **Earnings and job retention** sometimes have a negative SHAP impact in certain clusters (“compensated dissatisfaction”).
- **Learning and growth opportunities** differentiate clusters: highly valued in some, less in others.
- **Atmosphere and autonomy** matter most for the most dissatisfied cluster.
- **Variables with lowest satisfaction:** opportunities for promotion (j1_02), feeling tasks are too easy (j3_06), and overall job satisfaction.
- **Variables with highest satisfaction:** ease of making ends meet (m13), coworker relations (j1_04), and lack of workplace harassment (j3_09).

### Overall
Employees find satisfaction in very different ways—through pay and stability, through learning and growth, or even despite positive conditions—highlighting the heterogeneity of job satisfaction drivers.

---
## Project Status & Next Steps

**Status:**
Project is mostly complete.
Key components implemented:
- Modular notebook workflow (01_data_cleaning → 04_advanced_analysis)
- Data folder structure with privacy considerations
- Utilities (utils folder)
- Final trained model (best_model.pkl)
- Initial EDA, modelling, SHAP, and clustering analyses

**Remaining Work / Next Steps**:
- Review Notebook 01 clarity and consistency
- Refine plots for readability and consistency.
- Code review / final polish - especially for utilities and helper functions.
- Presentation & formatting: ensure notebooks and outputs are clean, clear, and well-documented.
- Assess potential sampling biases
- Unify Markdown and code comment style across notebooks and README for consistency and readability
- Optional: publishing a dashboard or interactive results outside GitHub