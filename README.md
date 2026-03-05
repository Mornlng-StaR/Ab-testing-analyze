# 🚀 A/B Testing Decision Engine
### *Statistical Framework for Product Optimization (SQL + Python)*

---

## 📈 1. Project Overview
This project is an end-to-end analytics pipeline designed to determine if a product change (Variant B) performs significantly better than the current version (Variant A). It automates the process of data aggregation, statistical validation, and business recommendation.

---

## 🏗️ 2. Project Architecture
The repository is organized to demonstrate a professional data science workflow:
* **`/sql`**: Performance queries for MySQL.
* **`/python`**: Statistical testing engine and data generation.
* **`/dashboard`**: Visualization of the conversion funnel.

---

## 📊 3. SQL Analysis Layer
I developed a modular SQL layer to extract key performance indicators (KPIs) directly from the MySQL database.

### **Variant Performance Analysis**
```sql
/* Goal: Compare Control (A) vs Treatment (B) */
SELECT 
    variant, 
    COUNT(user_id) AS total_users, 
    SUM(converted) AS total_conversions, 
    ROUND(AVG(converted), 4) AS conversion_rate 
FROM ab_testing_project.experiment_data
GROUP BY variant;
```
----
## 🧪 4. Statistical Testing Layer
To ensure the observed lift isn't due to random chance, the system employs a **Z-Test for Proportions** using Python.

* **Null Hypothesis ($H_0$):** No difference in conversion rates between A and B.
* **Alternative Hypothesis ($H_1$):** Variant B has a significantly different conversion rate.
* **Confidence Level:** 95% ($\alpha = 0.05$).



---

## 🤖 5. Automated Decision Engine
The engine processes SQL outputs through a logical gate to provide a final recommendation:

| Metric | Threshold | Result | Action |
| :--- | :--- | :--- | :--- |
| **P-Value** | < 0.05 | Statistically Significant | **Deploy Variant B** |
| **P-Value** | > 0.05 | Not Significant | **Keep Variant A** |

---

## 🛠️ 6. Core Skills Demonstrated
* **SQL**: Advanced aggregation, grouping, and funnel modeling.
* **Python**: Statistical hypothesis testing and database integration.
* **Analytics**: Experiment design, p-value interpretation, and data-driven decision making.

---

## 🚀 7. How to Reproduce
1. **Generate Data**: Run `python/generate_data.py` to create the initial dataset.
2. **Database Setup**: Import the `.csv` into **MySQL** (Database: `ab_testing_project`).
3. **Run Analysis**: Execute `python/stats_test.py` to generate the automated report.
---

**IMAGE**<img width="1000" height="600" alt="Figure_1" src="https://github.com/user-attachments/assets/1807f382-7e52-4e56-bef2-1d243fba47ae" />
