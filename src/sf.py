from Snowflake.queries import *
from Snowflake.snowflake import Snowflake


def main(queries_list: list, email: str, password: str):
    sf = Snowflake(email, password)
    sf.connect()
    sf_data = []
    for query in queries_list:
        df = sf.execute(query)
        sf_data.append(df)

    return sf_data


if __name__ == "__main__":
    # change the queries list to your own queries
    queries = [example_query_1, example_query_2]
    # change this to your pagaya email & password
    main(queries, "ron.morgenstern@pagaya.com", "p.zyuY4a")
