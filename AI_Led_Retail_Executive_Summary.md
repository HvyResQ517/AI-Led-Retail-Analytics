# AI-Led Retail Analytics: Executive Summary

## Objective
Determine what factors explain sales and gross profitability in a fictional retail transaction dataset, with the analytical workflow led by AI and minimal analyst intervention.

## Data
- 20,000 unique transactions
- 22 original variables
- January 1, 2024 through December 31, 2025
- 12 stores across 4 regions
- 5 product categories and 20 products
- No missing values or duplicate rows in the supplied data

## Executive Findings
1. **Revenue and profit:** Net sales total $3,487,529; gross profit totals $959,789; aggregate gross margin is 27.5%.
2. **Discounting is the clearest margin risk:** aggregate gross margin declines from about 34.0% at 0% discount to -15.4% at 35% discount. The transaction-level correlation between discount percent and gross-margin percent is Pearson -0.369 and Spearman -0.317.
3. **Loss-making transactions matter:** 505 transactions produce negative gross profit.
4. **Revenue leadership is not the same as margin leadership:** high-revenue technology products such as Tablet and Monitor carry lower aggregate margins than several lower-revenue product groups.
5. **Predictive structure is strong:** Random Forest was the best tested gross-profit model, with 3-fold cross-validated R² 0.911, MAE $6.91, and RMSE $16.87.
6. **Primary predictive drivers:** permutation importance ranks unit price, quantity, discount percentage, product category, and product as the strongest tested features.

## Interpretation
The most actionable synthetic-data story is a revenue-margin tradeoff. Discounting can support transaction revenue while rapidly compressing gross margin, and the most important gross-profit predictors are transactional and merchandising variables rather than geography or payment method.

## Limitations
- The data are fictional and synthetic.
- Relationships are associative and do not establish causation.
- Gross profit is mechanically related to sale economics, so strong prediction should not be interpreted as discovery of an independent causal mechanism.
- The model intentionally excludes cost of goods sold and derived gross margin to reduce obvious target leakage.

## AI vs Analyst Experiment
The analyst defined the experiment, supplied the dataset, and preserved requested outputs. AI independently performed data audit, business framing, descriptive analysis, hypothesis testing, model comparison, feature importance, documentation, and Streamlit application development through this checkpoint.
