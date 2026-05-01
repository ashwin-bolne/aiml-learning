"""
Database module for SQLite operations.

Responsibilites:
    - connection management
    - Table creation
    - Data insertion
    - Querying
"""
import sqlite3
from typing import Optional


def get_connection(db_path: str = "quality_results.db") -> sqlite3.Connection:
    """
    Create and return a database connection.

    Args:
        db_path (str): Path to SQLite database file.

    Returns:
        sqlite3.connection: Active database connection.
    """
    return sqlite3.connect(db_path)
    
def create_table(conn: sqlite3.Connection) -> None:
    """
    Create quality_runs table using schema.sql.

    Args:
        conn (sqlite3.connection): Active database connection.
    """
    with open("sql/sqlite_basics/schema.sql", "r") as file:
        sql_script = file.read()

    cursor = conn.cursor()
    cursor.executescript(sql_script)
    
    conn.commit()

def insert_quality_run(conn: sqlite3.Connection, result: dict) -> None:
    """
    Insert a single quality run record into a database.

    Args:
        conn (sqlite3.connection): Active database connection
        result (dict): Dictionary containing dataset qualit details
    """

    query = """
    INSERT INTO quality_runs (
        filename,
        row_count,
        col_count,
        quality_score,
        null_rate,
        run_at
    ) VALUES (?, ?, ?, ?, ?, ?)
    """

    values = (
        result["filename"],
        result["row_count"],
        result["col_count"],
        result["quality_score"],
        result["null_rate"],
        result["run_at"]
    )

    cursor = conn.cursor()
    cursor.execute(query, values)
    
    conn.commit()