import streamlit as st
import pandas as pd

# Load dataset
df = pd.read_csv("synthetic_transactions.csv")

st.title("Fraud Detection Dashboard")
st.write("Explore synthetic transactions and fraud predictions.")

st.dataframe(df.head(20))
