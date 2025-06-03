import streamlit as st
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("mutual_funds_india.csv")
df.columns = df.columns.str.replace(" ", "")  # Clean column names

# Title
st.title("Mutual Fund Analysis in India")

# Dropdown for category
category = st.selectbox("Select Mutual Fund Category", df['category'].dropna().unique())

# Filter by category
filtered_df = df[df['category'] == category]

# Dropdown for AMC name
amc = st.selectbox("Select AMC Name", filtered_df['AMC_name'].dropna().unique())

# Filter by AMC name
final_df = filtered_df[filtered_df['AMC_name'] == amc]

# Display dataframe
st.write("### Filtered Mutual Funds", final_df)

# Plotting
st.write("### 1-Year Return Comparison")
plt.figure(figsize=(15, 8))
sb.barplot(data=final_df, x='MutualFundName', y='return_1yr', palette='ocean')
plt.xticks(rotation=90)
plt.tight_layout()
st.pyplot(plt)
