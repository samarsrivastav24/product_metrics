import pandas as pd
import numpy as np

# -------------------------
# LOAD DATA
# -------------------------
def load_data(path):
    df = pd.read_csv(path)
    return df

# -------------------------
# PRODUCT METRICS
# -------------------------
def get_product_metrics(df):
    metrics = {
        "Total Rows": len(df),
        "Total Columns": df.shape[1],
        "Missing Values": df.isna().sum().sum(),
        "Duplicates": df.duplicated().sum(),
        "Column-wise Missing": df.isna().sum().to_dict(),
        "Data Types": df.dtypes.astype(str).to_dict()
    }
    return metrics

# -------------------------
# GUESSTIMATE
# -------------------------
def get_guesstimates(df):
    current_rows = len(df)
    growth_rate = 0.10  # 10%

    g = {
        "Current Rows": current_rows,
        "Next Month": int(current_rows * (1 + growth_rate)),
        "In 6 Months": int(current_rows * (1 + growth_rate)**6),
        "Growth Rate (%)": 10
    }
    return g

# -------------------------
# RCA (ROOT CAUSE ANALYSIS)
# -------------------------
def get_rca(df):
    rca = {}

    # Missing values
    missing = df.isna().sum()
    rca["Missing Values"] = missing[missing > 0].to_dict()

    # Duplicates
    rca["Duplicate Rows"] = df.duplicated().sum()

    # Outliers (Numerical)
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    outliers = {}
    for col in numeric_cols:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        outlier_count = df[(df[col] < Q1 - 1.5*IQR) | (df[col] > Q3 + 1.5*IQR)].shape[0]
        outliers[col] = outlier_count

    rca["Outliers"] = outliers

    return rca
