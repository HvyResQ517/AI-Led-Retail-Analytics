import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

st.set_page_config(page_title="AI-Led Retail Analytics",layout="wide")
BASE=Path(__file__).parent
df=pd.read_csv(BASE/"data.csv",parse_dates=["sale_date","sale_datetime"])

st.title("AI-Led Retail Analytics Experiment")
st.caption("A synthetic retail analysis designed to compare an analyst-guided workflow with an AI-led workflow requiring minimal human intervention.")

page=st.sidebar.radio("Explore",["Executive Overview","Profit & Discount","Products & Stores","Model Results","AI vs Analyst Experiment","About"])

# filters
with st.sidebar:
    st.subheader("Filters")
    regions=st.multiselect("Region",sorted(df.region.unique()),default=sorted(df.region.unique()))
    channels=st.multiselect("Channel",sorted(df.channel.unique()),default=sorted(df.channel.unique()))
    cats=st.multiselect("Category",sorted(df.product_category.unique()),default=sorted(df.product_category.unique()))

f=df[df.region.isin(regions)&df.channel.isin(channels)&df.product_category.isin(cats)].copy()

def money(x): return f"${x:,.0f}"

if page=="Executive Overview":
    st.header("Executive Overview")
    c1,c2,c3,c4=st.columns(4)
    c1.metric("Net Sales",money(f.net_sales.sum()))
    c2.metric("Gross Profit",money(f.gross_profit.sum()))
    c3.metric("Gross Margin",f"{f.gross_profit.sum()/f.net_sales.sum():.1%}" if f.net_sales.sum() else "-")
    c4.metric("Transactions",f"{len(f):,}")
    monthly=f.groupby(f.sale_date.dt.to_period('M').astype(str),as_index=False).agg(net_sales=('net_sales','sum'),gross_profit=('gross_profit','sum'))
    st.plotly_chart(px.line(monthly,x='sale_date',y=['net_sales','gross_profit'],title='Monthly Sales and Gross Profit'),use_container_width=True)
    bycat=f.groupby('product_category',as_index=False).agg(net_sales=('net_sales','sum'),gross_profit=('gross_profit','sum'))
    st.plotly_chart(px.bar(bycat.sort_values('net_sales',ascending=False),x='product_category',y='net_sales',title='Net Sales by Product Category'),use_container_width=True)
    st.info("Headline: this dataset has strong predictive structure, but the clearest executive tradeoff is revenue versus margin as discount depth increases.")

elif page=="Profit & Discount":
    st.header("Profitability and Discounting")
    discount=f.groupby('discount_pct',as_index=False).agg(net_sales=('net_sales','sum'),gross_profit=('gross_profit','sum'),orders=('order_id','count'))
    discount['gross_margin_pct']=discount.gross_profit/discount.net_sales
    c1,c2,c3=st.columns(3)
    c1.metric("Negative-profit transactions",f"{(f.gross_profit<0).sum():,}")
    c2.metric("Sales on negative-profit transactions",money(f.loc[f.gross_profit<0,'net_sales'].sum()))
    c3.metric("Average discount",f"{f.discount_pct.mean():.1f}%")
    st.plotly_chart(px.line(discount,x='discount_pct',y='gross_margin_pct',markers=True,title='Gross Margin by Discount Level'),use_container_width=True)
    st.plotly_chart(px.bar(discount,x='discount_pct',y='net_sales',title='Net Sales by Discount Level'),use_container_width=True)
    st.caption("Association within synthetic data. These views do not establish causal effects of discounting.")

elif page=="Products & Stores":
    st.header("Products and Stores")
    prod=f.groupby(['product_category','product'],as_index=False).agg(net_sales=('net_sales','sum'),gross_profit=('gross_profit','sum'))
    prod['gross_margin_pct']=prod.gross_profit/prod.net_sales
    st.plotly_chart(px.scatter(prod,x='net_sales',y='gross_margin_pct',size='gross_profit',color='product_category',hover_name='product',title='Revenue vs Gross Margin by Product'),use_container_width=True)
    stores=f.groupby(['store_id','city','region'],as_index=False).agg(net_sales=('net_sales','sum'),gross_profit=('gross_profit','sum'))
    stores['gross_margin_pct']=stores.gross_profit/stores.net_sales
    st.dataframe(stores.sort_values('net_sales',ascending=False),use_container_width=True,hide_index=True)

elif page=="Model Results":
    st.header("Gross Profit Model Results")
    models=pd.DataFrame([
        ['Random Forest',0.9106,6.91,16.87],['Gradient Boosting',0.9041,8.41,17.46],['Linear Regression',0.6778,18.99,32.04],['Ridge',0.6771,18.94,32.07]
    ],columns=['Model','CV R²','CV MAE','CV RMSE'])
    st.dataframe(models,use_container_width=True,hide_index=True)
    imp=pd.read_csv(BASE/'feature_importance.csv')
    st.plotly_chart(px.bar(imp.head(10).sort_values('importance_mean'),x='importance_mean',y='feature',orientation='h',title='Random Forest Permutation Importance'),use_container_width=True)
    st.caption("The model excludes cost of goods sold and derived gross margin to avoid obvious outcome leakage.")

elif page=="AI vs Analyst Experiment":
    st.header("AI vs Analyst Experiment")
    st.markdown("""### Experimental question\nHow much of an end-to-end analytics project can AI complete when given only a raw fictional dataset, with the analyst deliberately providing minimal direction?""")
    st.markdown("""### Human input so far\n- Defined the experiment and requested a comparable portfolio project.\n- Supplied the raw fictional CSV.\n- Saved the outputs when instructed.\n\n### AI work so far\n- Inferred the data structure and business framing.\n- Audited data quality and reconciled calculated fields.\n- Selected analytical outcomes and predictors.\n- Ran descriptive, segmented, correlation, hypothesis, and predictive analyses.\n- Created project artifacts and this Streamlit application.\n\n### Why this comparison matters\nThe earlier Drive Time project was analyst-guided and intentionally educational. This project tests the opposite workflow: AI handles production work first, while the analyst intervenes only where judgment, context, credentials, or publication actions require a human.""")
    st.warning("This is a process experiment, not a claim that human analysts are unnecessary. Final interpretation, business relevance, accountability, and decisions remain human responsibilities.")
    st.markdown("""### What the experiment showed
A large share of the repeatable production workflow could be delegated to AI: data audit, business framing, exploratory analysis, statistical testing, model comparison, feature importance, documentation, coding, and presentation design. Human involvement became necessary for purpose, account ownership, publication, verification, and ultimately deciding whether the output is meaningful and trustworthy.

### Comparison with Drive Time
The earlier Drive Time project was analyst-guided and intentionally educational. The analyst worked through the tools, questioned results, made design choices, and learned through iteration. The AI-led project prioritized speed and autonomy. That difference matters: the first workflow developed analyst judgment, while the second demonstrated how much production work that judgment can later supervise.

### Important comparison limitation
The two datasets are not equivalent. Drive Time used broad daily operational measures and produced relatively weak predictive relationships. This project uses transaction-level price, quantity, discount, sales, cost, and profit measures with much stronger structural relationships. Differences in model performance therefore should not be attributed to AI autonomy versus analyst guidance alone.

### Bottom line
The experiment suggests that AI is strongest as an accelerator rather than a replacement for the analyst. AI can compress much of the production cycle, while the analyst shifts toward framing, context, skepticism, validation, accountability, and decision-making.""")

else:
    st.header("About")
    st.markdown("""This application uses a fictional retail transaction dataset containing 20,000 orders across 2024 and 2025. The project is intentionally AI-led: the dataset was provided without a data dictionary or business explanation, and the analytical workflow was generated with minimal analyst intervention.\n\n**Data disclaimer:** All data and findings are fictional and are intended for learning, portfolio development, and experimentation with AI-assisted analytics. They do not describe a real retailer, store, customer, or employee.""")
