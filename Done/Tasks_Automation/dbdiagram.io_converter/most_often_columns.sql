SELECT
    c.name AS 'ColumnName',
    count(c.name) AS 'Amount'
FROM
    sys.columns c
WHERE
    c.name LIKE '%%'
GROUP BY
    c.name
ORDER BY
    Amount DESC