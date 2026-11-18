# AI-Led Retail Analytics Experiment

## Purpose
This project tests how much of an end-to-end analytics workflow can be completed by AI when the analyst provides only a raw fictional dataset and minimal intervention.

## Dataset
- 20,000 fictional retail transactions
- 22 original variables
- 12 stores, 4 regions, 5 product categories, 20 products
- 2024-01-01 through 2025-12-31
- No missing values or duplicate rows detected in the initial audit

## Primary Business Question
**What factors explain retail sales and profitability, and where does the business appear to be trading revenue for margin?**

## Headline Findings
- Net sales: $3,487,529
- Gross profit: $959,789
- Aggregate gross margin: 27.5%
- Negative-profit transactions: 505
- Aggregate gross margin falls from roughly 34.0% at 0% discount to -15.4% at 35% discount.
- Random Forest was the strongest tested gross-profit model, with cross-validated R² of 0.911.

## Experiment Design
The earlier Drive Time project used a highly collaborative, analyst-guided workflow. This project deliberately reverses that model. AI performs the production work first; the analyst intervenes only when human judgment, context, credentials, or publication actions are required.

## Human Input Through Initial Build
1. Defined the experiment.
2. Provided the raw CSV.
3. Saved requested outputs.

## AI Work Through Initial Build
- Data audit and arithmetic reconciliation
- Business framing
- Descriptive and segmented analysis
- Correlation and discount comparison analysis
- Predictive model comparison
- Feature-importance analysis
- Executive visualizations
- Streamlit application source
- Documentation and experiment tracking

## Limitations
All data are fictional and synthetic. Findings are associations within the dataset and should not be interpreted as evidence about any real retailer or as proof of cause and effect.
