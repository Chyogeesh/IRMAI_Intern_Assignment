import streamlit as st
import pandas as pd

st.title("📊 AI-Powered Anomaly Detection Dashboard")

data = pd.read_csv("data/explained_anomalies.csv")

st.subheader("Detected Anomalies")
st.dataframe(data)

if st.button("Download CSV"):
    st.download_button("Download Results", data.to_csv(index=False), file_name="explained_anomalies.csv")
streamlit run app.py
