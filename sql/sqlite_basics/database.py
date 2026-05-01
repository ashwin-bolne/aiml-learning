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
    

