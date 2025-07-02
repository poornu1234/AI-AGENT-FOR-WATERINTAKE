
import streamlit as st
import pandas as pd
from data_store import load_logs

st.title("💧 Daily Water Intake Tracker")

logs = load_logs()
if logs:
    df = pd.DataFrame(logs)
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df = df.sort_values("timestamp")

    st.line_chart(df.set_index("timestamp")["amount_ml"])
    st.write(f"Total intake today: {df['amount_ml'].sum()} ml")
else:
    st.write("No water intake logged yet.")
