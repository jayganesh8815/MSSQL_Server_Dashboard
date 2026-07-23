# queries.py

# Query 1: Get total active vs running sessions
ACTIVE_SESSIONS_QUERY = """
SELECT 
    COUNT(session_id) AS TotalSessions,
    SUM(CASE WHEN status = 'running' THEN 1 ELSE 0 END) AS RunningQueries,
    SUM(CASE WHEN status = 'sleeping' THEN 1 ELSE 0 END) AS SleepingSessions
FROM sys.dm_exec_sessions 
WHERE is_user_process = 1;
"""

# Query 2: Get top 5 long-running queries
LONG_RUNNING_QUERIES = """
SELECT TOP 5
    r.session_id AS [Session ID],
    r.status AS [Status],
    r.cpu_time AS [CPU Time (ms)],
    CAST(r.total_elapsed_time / 1000.0 AS DECIMAL(10,2)) AS [Elapsed (s)],
    SUBSTRING(st.text, (r.statement_start_offset/2)+1,
        ((CASE r.statement_end_offset
            WHEN -1 THEN DATALENGTH(st.text)
            ELSE r.statement_end_offset
            END - r.statement_start_offset)/2) + 1) AS [SQL Query]
FROM sys.dm_exec_requests r
CROSS APPLY sys.dm_exec_sql_text(r.sql_handle) st
WHERE r.session_id > 50
ORDER BY r.total_elapsed_time DESC;
"""