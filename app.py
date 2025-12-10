#!/usr/bin/env python
# coding: utf-8

# In[5]:


import streamlit as st
import pandas as pd
from backend import load_data, get_product_metrics, get_guesstimates, get_rca

# -------------------------------------
# Page Config
# -------------------------------------
st.set_page_config(
    page_title="Product Metrics Dashboard",
    page_icon="📊",
    layout="wide",
)

# -------------------------------------
# Sidebar
# -------------------------------------
st.sidebar.title("📌 Dashboard Info")
st.sidebar.success(
    "Upload any CSV file to instantly get:\n"
    "- Product Metrics\n"
    "- Growth Guesstimates\n"
    "- Root Cause Analysis (RCA)"
)

# Sample CSV download button
sample_df = pd.DataFrame({"A":[1,2,3], "B":[4,5,6]})
st.sidebar.download_button(
    "Download Sample CSV",
    sample_df.to_csv(index=False),
    file_name="sample.csv",
    mime="text/csv"
)

# -------------------------------------
# Header Section
# -------------------------------------
st.markdown("""
<div style="text-align:center;">
    <h1>📊 Product Metrics Dashboard</h1>
    <h3>📈 Guesstimate • 🔍 RCA • 📁 Data Quality Insights</h3>
</div>
""", unsafe_allow_html=True)

st.write("---")

# -------------------------------------
# File Upload Section
# -------------------------------------
uploaded = st.file_uploader("📥 Upload your CSV file", type=["csv"])

if not uploaded:
    st.info("⬆ Please upload a CSV file to begin analysis.")
    st.stop()

# Load data
df = load_data("data.csv")

# Tabs for cleaner organization
tab1, tab2, tab3 = st.tabs(["📊 Product Metrics", "📈 Guesstimate", "🔍 Root Cause Analysis"])

# -------------------------------------
# TAB 1: Product Metrics
# -------------------------------------
with tab1:
    st.subheader("📊 Product Metrics")
    st.caption("Automated dataset quality analysis")

    metrics = get_product_metrics(df)

    # Show key metrics as cards
    row1 = st.columns(3)
    row1[0].metric("Total Rows", metrics.get("Total Rows", "-"))
    row1[1].metric("Total Columns", metrics.get("Total Columns", "-"))
    row1[2].metric("Missing Values", metrics.get("Missing Values", "-"))

    st.json(metrics)

# -------------------------------------
# TAB 2: Guesstimate
# -------------------------------------
with tab2:
    st.subheader("📈 Growth Guesstimate")
    st.caption("Predict dataset size using historical patterns")

    g = get_guesstimates(df)

    row2 = st.columns(3)
    row2[0].metric("Current Rows", g.get("Current Rows", "-"))
    row2[1].metric("Next Month", g.get("Next Month", "-"))
    row2[2].metric("In 6 Months", g.get("In 6 Months", "-"))

    st.json(g)

# -------------------------------------
# TAB 3: RCA
# -------------------------------------
with tab3:
    st.subheader("🔍 Root Cause Analysis")
    st.caption("Find the cause of missing data")

    rca = get_rca(df)

    st.json(rca)

# -------------------------------------
# Footer
# -------------------------------------
st.write("---")
st.markdown(
    "<p style='text-align:center;color:gray;'>Built with ❤️ using Streamlit</p>",
    unsafe_allow_html=True
)


# In[ ]:





# In[ ]:




