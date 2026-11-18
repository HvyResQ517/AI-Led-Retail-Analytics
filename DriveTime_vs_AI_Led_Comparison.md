# Drive Time vs AI-Led Retail Analytics

## Experiment Question
How much of an end-to-end analytics project can AI complete when given only a raw fictional dataset and minimal analyst intervention, and what changes when compared with an analyst-guided workflow?

## Project A: Drive Time Analytics
The Drive Time project was intentionally collaborative and educational. The analyst defined the retail concept, worked through the tools step by step, made repeated design and analytical decisions, reviewed unexpected results, and participated directly in Excel, Orange, Python, Tableau, GitHub, and Streamlit work.

## Project B: AI-Led Retail Analytics
The analyst defined the experiment, supplied the raw CSV, preserved requested files, performed account-authenticated GitHub and Streamlit publication steps, and verified that the published application opened correctly. AI independently inferred the dataset structure, selected the business framing, audited the data, chose analytical outcomes and predictors, ran exploratory and statistical analysis, compared predictive models, selected the executive story, created the application, and prepared documentation.

## What AI Completed Without Analytical Direction
- Data structure inference and quality audit
- Arithmetic reconciliation
- Business-question framing
- Selection of outcomes and predictors
- Descriptive and segmented analysis
- Pearson and Spearman correlation analysis
- Discount profitability comparison
- Negative-profit risk analysis
- Predictive model comparison
- Feature-importance analysis
- Statistical diagnostics
- Executive interpretation
- Streamlit application source
- README, executive summary, and experiment documentation
- GitHub-ready publication package

## Where the Human Was Still Required
- Defining the purpose of the experiment
- Providing the fictional dataset
- Saving selected artifacts locally
- Creating and authenticating to the GitHub repository
- Uploading/committing prepared files under the analyst's account
- Authenticating to Streamlit Community Cloud
- Deploying the prepared application
- Verifying the published pages opened successfully

## Analytical Outcome of the AI-Led Project
The AI-led project identified a clear revenue-margin tradeoff. The synthetic dataset contains $3.49 million in net sales and approximately $960 thousand in gross profit, with a 27.5% aggregate gross margin. Discount depth is negatively associated with gross-margin percentage, and the negative-profit transaction rate rises sharply at the deepest discounts. Random Forest was the strongest tested gross-profit model, with cross-validated R² of approximately 0.91. Permutation importance identified unit price, quantity, discount percentage, product category, and product as the strongest tested predictors.

## Key Difference in the Two Workflows
The Drive Time workflow maximized analyst learning, business-context discussion, manual review, and incremental decision-making. The AI-led workflow maximized production speed and autonomy by allowing AI to make most analytical and presentation decisions before asking for human intervention.

The experiment did not show that the analyst is unnecessary. It showed that a large share of the repeatable production workflow can be delegated. The human remained essential for purpose, accountability, account ownership, publication, business-context validation, and deciding whether the result is worth trusting or acting on.

## Important Limitation of the Comparison
The two datasets are not equivalent. Drive Time was a deliberately broad daily operational dataset with relatively weak predictive relationships, while the second dataset is transaction-level and contains strong structural relationships among price, quantity, discount, sales, cost, and profit. Differences in model performance therefore cannot be attributed to AI autonomy versus analyst guidance alone.

## Bottom Line
The strongest use of AI appears to be acceleration rather than replacement. AI can compress data audit, exploratory analysis, modeling, documentation, coding, and presentation into a much shorter production cycle. The analyst's role shifts toward framing the problem, supplying context, challenging assumptions, validating whether conclusions make business sense, controlling publication, and taking responsibility for decisions.
