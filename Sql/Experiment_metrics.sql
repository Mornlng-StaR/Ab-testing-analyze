/* 1. VARIANT PERFORMANCE ANALYSIS 
Goal: Calculate the primary conversion metric to compare Version A and Version B.
*/
SELECT 
    variant,
    COUNT(user_id) AS total_users,
    SUM(converted) AS total_conversions,
    ROUND(AVG(converted), 4) AS conversion_rate
FROM ab_testing_project.experiment_data
GROUP BY variant;

/* 2. FUNNEL ANALYSIS 
Goal: Track user progression through the lifecycle (Visitors -> Clicks -> Conversions). [cite: 37, 38, 92]
*/
SELECT 
    variant,
    SUM(visited) AS visitors,
    SUM(clicked) AS clicks,
    SUM(converted) AS conversions,
    ROUND(SUM(clicked) * 1.0 / SUM(visited), 4) AS ctr -- [cite: 26]
FROM ab_testing_project.experiment_data
GROUP BY variant;
