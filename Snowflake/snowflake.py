import pandas as pd
import snowflake.connector


class Snowflake:
    def __init__(self, user, password):
        self.__user = user
        self.__password = password
        self.ctx = None
        self.cs = None
        self.is_connected = False

    def __enter__(self):
        if not self.is_connected:
            self.connect()
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self.is_connected:
            self.disconnect()

    def connect(self) -> None:
        """
        Initialize connection to Snowflake API
        """
        try:
            self.ctx = snowflake.connector.connect(
                user=self.__user,
                password=self.__password,
                account='pagaya-bi',
                warehouse='OPS_WH',
                database='PIPER_DB',
                schema='PIPERDB_PUBLIC',
                role='OPS_FOC',
                authenticator='externalbrowser'
            )
            self.cs = self.ctx.cursor()
            self.cs.execute("SELECT current_version()")
            check = self.cs.fetchone()
            if check:
                print("CONNECTION SUCCESS")
            self.is_connected = True
        except snowflake.connector.errors.DatabaseError as e:
            print("CONNECTION ERROR\n", e)

    def disconnect(self) -> None:
        """
        Disconnect from Snowflake API
        """
        self.ctx.close()
        self.is_connected = False

    def execute_to_df(self, query: str) -> pd.DataFrame:
        """
        Execute SQL query and return result as pandas dataframe
        """
        if not self.is_connected:
            self.connect()
        self.cs = self.ctx.cursor()
        try:
            self.cs.execute(query)
            return pd.DataFrame(self.cs.execute(query), columns=self.cs.description)
        except snowflake.connector.errors.DatabaseError as e:
            print("EXECUTE ERROR\n", e)
