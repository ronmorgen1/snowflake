example_query_1 = """
SELECT
    *
FROM
LOANS LIMIT 10;
"""

example_query_2 = """
SELECT
    *
FROM
    OFFERS
WHERE
OFFER_STATUS IN ('PASSED_TH', 'ISSUED')
LIMIT 10;
"""
