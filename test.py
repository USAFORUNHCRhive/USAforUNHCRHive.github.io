def testFunctionWithBadFormatting():
    # This function has bad formatting
    print("Hello, World!")
    print("This is a test function with bad formatting.")
    for i in range(10):
        print(i)
    print("Done.")

testFunctionWithBadFormatting()

import pandas as pd
import numpy as np
import os

query = """
SELECT
    id, o.closedate
, SUM(o.amount) AS amount
 FROM raw_salesforce.opportunity AS o
 group by id, o.closedate
 LIMIT 10
"""

# put the above in a function
def fetchData(query):
    import pandas_gbq
    import pydata_google_auth
    SCOPES = ['https://www.googleapis.com/auth/cloud-platform']
    credentials = pydata_google_auth.get_user_credentials(SCOPES, auth_local_webserver=True)

# Update the in-memory credentials cache (added in pandas-gbq 0.7.0).
    pandas_gbq.context.credentials = credentials
    pandas_gbq.context.project = "u4u-ds-prod-00"

    df = pandas_gbq.read_gbq(query)
    return df

test2 = fetchData(query)  # Call the function with the query

for i in test2:
    print(i)