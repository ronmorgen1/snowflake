# Snowflake Connector

The purpose of this connector is to provide a simple way to connect to Snowflake. Currently, it is only used for
internal purposes.
___

## Installation

Clone the repository and go to the root directory:

```bash
git clone https://github.com/ronmorgen1/snowflake.git && cd snowflake
```

Run the setup script to install dependencies:

```bash
python setup.py install
```

___

## Basic Usage

create a python file named `snowflake.py` and import the connector, use your credentials to connect:
**Basic Query**:

```python
from Snowflake.snowflake import Snowflake

with Snowflake("<pagaya_email>", "<pagaya_password>") as conn:
    res = conn.execute_simple("SELECT * FROM LOANS LIMIT 100")
    print(res)
```

___
**Run a query that returns a pandas dataframe**:

```python
from Snowflake.snowflake import Snowflake

with Snowflake("<pagaya_email>", "<pagaya_password>") as conn:
    res = conn.execute_to_df("SELECT * FROM LOANS LIMIT 10;")
    print(res)
```

___
**From SQL File**:

Create a file named `query.sql` and write the query in it:

```sql
SELECT *
FROM LOANS
LIMIT 100;
```

Run the query from `snowflake.py`:

```python
from Snowflake.snowflake import Snowflake

with Snowflake("<pagaya_email>", "<pagaya_password>") as conn:
    res = conn.execute_file('./query.sql')
    print(res)
```




