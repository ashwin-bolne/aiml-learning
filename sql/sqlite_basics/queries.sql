SELECT 
    filename,
    quality_score,
    ROW_NUMBER() OVER (ORDER BY quality_score DESC) as rank
FROM quality_runs;


SELECT 
    filename,
    quality_score,
    RANK() OVER (ORDER BY quality_score DESC) as rank
FROM quality_runs;

SELECT 
    filename,
    quality_score,
    ROW_NUMBER() OVER (
        PARTITION BY filename
        ORDER BY quality_score DESC
    ) AS rank
FROM quality_runs;

SELECT 
    filename,
    quality_score,
    run_at,
    LAG(quality_score) OVER (
        PARTITION BY filename
        ORDER BY run_at
    ) AS prev_score
FROM quality_runs;

SELECT 
    filename,
    quality_score,
    run_at,
    SUM(quality_score) OVER (
        PARTITION BY filename
        ORDER BY run_at
    ) AS cumulative_score
FROM quality_runs;

SELECT *
FROM (
    SELECT 
        *,
        ROW_NUMBER() OVER (
            PARTITION BY filename
            ORDER BY quality_score DESC
        ) AS rank
    FROM quality_runs
) t
WHERE rank = 1;