# 🛡️ MS SQL Server Health Check Dashboard

An automated, real-time database performance and health monitoring dashboard built for **Microsoft SQL Server**. This tool queries Dynamic Management Views (DMVs) to track active sessions, identify blocking/long-running queries, and visualize performance bottlenecks in real time.

---

## 📸 Overview

The **SQL Health Check Dashboard** provides a lightweight, pure-Python solution for Database Administrators (DBAs) and Engineers to monitor database health without heavy third-party agent installations.

### Key Features
* 📊 **Real-time Session Tracking:** Monitor total user sessions, active running queries, and sleeping processes.
* ⚠️ **Long-Running Query Detection:** Capture top resource-intensive queries along with CPU time, elapsed execution duration, and full SQL query text.
* 📈 **Interactive Visualizations:** Interactive charts powered by Plotly to quickly spot elapsed time spikes across session IDs.
* 🔄 **On-Demand Refresh:** Quickly trigger manual telemetry updates.

---

## 🛠️ Tech Stack

* **Database Engine:** Microsoft SQL Server
* **Backend Scripting & Data Wrangling:** Python, Pandas
* **Database Driver:** `pyodbc` (ODBC Driver 17 for SQL Server)
* **Frontend / Dashboard Framework:** Streamlit
* **Data Visualization:** Plotly Express

---

## 📁 Project Structure

```text
sql-health-check-dashboard/
│
├── app.py              # Main Streamlit application UI & connection handler
├── queries.py          # T-SQL DMV queries for metrics collection
├── requirements.txt    # Python dependency specifications
└── README.md           # Project documentation
