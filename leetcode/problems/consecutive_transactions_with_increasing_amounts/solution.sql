WITH consecutive_transactions AS (
    SELECT 
        a.customer_id, 
        a.transaction_date 
    FROM 
        Transactions a
    JOIN 
        Transactions b 
    ON 
        a.customer_id = b.customer_id 
        AND b.amount > a.amount 
        AND DATEDIFF(b.transaction_date, a.transaction_date) = 1
),
row_num_transactions AS (
    SELECT 
        customer_id, 
        transaction_date,
        ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY transaction_date) AS rn
    FROM 
        consecutive_transactions
),
group_row_nums AS (
    SELECT 
        customer_id, 
        transaction_date, 
        DATE_SUB(transaction_date, INTERVAL rn DAY) AS date_group
    FROM 
        row_num_transactions
),
group_size AS (
    SELECT 
        customer_id, 
        MIN(transaction_date) AS consecutive_start, 
        COUNT(*) AS cnt
    FROM 
        group_row_nums 
    GROUP BY 
        customer_id, date_group
)
SELECT 
    customer_id, 
    consecutive_start,
    DATE_ADD(consecutive_start, INTERVAL cnt DAY) AS consecutive_end 
FROM 
    group_size 
WHERE 
    cnt > 1 
ORDER BY 
    customer_id;