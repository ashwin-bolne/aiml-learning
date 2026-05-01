from database import get_connection, create_table, insert_quality_run
from datetime import datetime 

def main():
    conn = get_connection()
    create_table(conn)

    sample_data = {
        "filename": "sales.csv",
        "row_count": 1000,
        "col_count": 12,
        "quality_score": 0.85,
        "null_rate": 0.1,
        "run_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    insert_quality_run(conn, sample_data)

    conn.close()


if __name__ == "__main__":
    main()