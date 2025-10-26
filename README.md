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
to do: identified flaw in the modelling section -> correct

---
Data

- **Source:** Biuro Kapitału Ludzkiego survey data (Poland)
- **Scope:** Employed individuals (excluding agricultural and self-employed respondents)
- **Type:** Self-reported survey responses
- **Limitation:** Self-reporting bias and incomplete responses
---
Methods & Tools

TBD

---

Limitations & Next Steps

The current analysis is based on secondary survey data, which limits control over what variables were collected.  
As a result, the model may be affected by **omitted variable bias** — certain relevant factors (e.g., workplace culture, job autonomy, personal expectations) are not included in the dataset and cannot be added retroactively.  

The current regression model likely suffers from Omitted Variable Bias (OVB). Several potential predictors were explored (including ANOVA and feature importance checks), but some influences likely remain unobserved.  
These constraints are typical when working with real-world survey data and should be considered when interpreting the results.

Next steps focus on:
- Refining existing variables and model specification  
- Improving interpretability and communication of findings  
- Documenting assumptions and uncertainty transparently  

These limitations do not invalidate the results, but outline their **scope and reliability**.

---

Key Insights

TBD

---