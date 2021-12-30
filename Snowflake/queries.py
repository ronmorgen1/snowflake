from Snowflake.snowflake import Snowflake

set_query = """
SET (platform,start_date, end_date) = ('marlette_ep', '2021-10-01', '2021-10-31');
"""

amount_passed_th = """
WITH OFFERS_CTE AS
         (SELECT PAGAYA_ID, MEDIAN(OFFER_AMOUNT) AS MAX_OFFER_AMOUNT
          FROM OFFERS
          WHERE OFFER_STATUS IN ('PASSED_TH', 'ISSUED')
          GROUP BY PAGAYA_ID),
     APPS_CTE AS (
         SELECT SEEN_DATE::timestamp::date as SEEN_DATE,
                PAGAYA_ID,
                REQUESTED_AMOUNT,
                PLATFORM
         FROM APPLICATIONS
     ),
     PASSED_TH_OFFERS AS
         (SELECT SEEN_DATE,
                 IFF(OFFERS_CTE.MAX_OFFER_AMOUNT < APPS_CTE.REQUESTED_AMOUNT, OFFERS_CTE.MAX_OFFER_AMOUNT,
                     OFFERS_CTE.MAX_OFFER_AMOUNT) AS APPS_PASSED_TH
          FROM OFFERS_CTE
                   JOIN APPS_CTE ON APPS_CTE.PAGAYA_ID = OFFERS_CTE.PAGAYA_ID
          WHERE APPS_CTE.PLATFORM = $platform
            AND (SEEN_DATE BETWEEN $start_date
              AND $end_date))
SELECT SEEN_DATE,
       ROUND(SUM(APPS_PASSED_TH), 0) AS APPS_PASSED_TH
FROM PASSED_TH_OFFERS
GROUP BY 1
ORDER BY 1 DESC
"""

