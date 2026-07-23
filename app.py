# app.py
import streamlit as st
import pyodbc
import pandas as pd
import plotly.express as px
from queries import ACTIVE_SESSIONS_QUERY, LONG_RUNNING_QUERIES

# Page Configuration
st.set_page_config(page_title="MSSQL Health Dashboard", layout="wide")
st.title("🛡️ MS SQL Server Health Check Dashboard")

# 1. Database Connection Function
def get_db_connection():
    conn_str = (
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=localhost;"            # or localhost\SQLEXPRESS
        "DATABASE=master;"
        "Trusted_Connection=yes;"      # Uses your current Windows login
    )
    return pyodbc.connect(conn_str)

# 2. Fetch Data Helper
def fetch_data(query):
    conn = get_db_connection()
    df = pd.read_sql(query, conn)
    conn.close()
    return df

# Auto-refresh button / Sidebar controls
st.sidebar.header("Controls")
if st.sidebar.button("🔄 Refresh Data"):
    st.rerun()

# --- DASHBOARD LAYOUT ---

try:
    # Metric Section
    sessions_df = fetch_data(ACTIVE_SESSIONS_QUERY)
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Total User Sessions", sessions_df["TotalSessions"].iloc[0])
    col2.metric("Running Queries", sessions_df["RunningQueries"].iloc[0])
    col3.metric("Sleeping Sessions", sessions_df["SleepingSessions"].iloc[0])

    st.markdown("---")

    # Long Running Queries Section
    st.subheader("⚠️ Long-Running Queries")
    long_queries_df = fetch_data(LONG_RUNNING_QUERIES)

    if not long_queries_df.empty:
        # Visualizing CPU Time using Plotly Bar Chart
        fig = px.bar(
            long_queries_df, 
            x="Session ID", 
            y="Elapsed (s)", 
            title="Execution Elapsed Time by Session ID (Seconds)",
            color="Elapsed (s)",
            color_continuous_scale="Reds"
        )
        st.plotly_chart(fig, use_container_width=True)

        # Show Table
        st.dataframe(long_queries_df, use_container_width=True)
    else:
        st.success("No long-running queries detected.")

except Exception as e:
    st.error(f"Error connecting to SQL Server: {e}")