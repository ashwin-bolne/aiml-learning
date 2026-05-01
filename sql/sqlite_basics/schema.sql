CREATE TABLE IF NOT EXISTS quality_runs (
    id INTEGER PRIMARY KEY,
    filename TEXT NOT NULL,
    row_count INTEGER,
    col_count INTEGER,
    quality_score REAL,
    null_rate REAL,
    run_at TIMESTAMP
)