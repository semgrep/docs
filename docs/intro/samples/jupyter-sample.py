import os
import pandas as pd
import psycopg2
from sqlalchemy import create_engine
import matplotlib.pyplot as plt

###################################
# EDIT THESE CONSTANTS
###################################

GROUP = "YOUR-GROUP"
DB_PASSWORD = "YOUR-DB-PASSWORD"

ANALYZER_NAME = f"{GROUP}/minifinder"
ANALYZER_VERSION = "0.1.0"
CORPUS_NAME = "r2c-1000"

###################################
# END EDIT SECTION
###################################

# Canonical SQL query to get job-specific results back.
JOB_QUERY = """
SELECT * 
FROM   result, 
       commit_corpus 
WHERE  result.commit_hash = commit_corpus.commit_hash 
       AND analyzer_name = %(analyzer_name)s 
       AND analyzer_version = %(analyzer_version)s
       AND corpus_name = %(corpus_name)s
"""

QUERY_PARAMS = {
    "corpus_name": CORPUS_NAME,
    "analyzer_name": ANALYZER_NAME,
    "analyzer_version": ANALYZER_VERSION
}

# Connect to PostgreSQL host and query for job-specific results
engine = create_engine(f'postgresql://notebook_user:{DB_PASSWORD}@{GROUP}-db.massive.ret2.co/postgres')
job_df = pd.read_sql(JOB_QUERY, engine, params=QUERY_PARAMS)

# Print pandas dataframe to stdout for debugging
print("Raw job dataframe:")
print(job_df[1:10])

# Helper method to compute % whitespace from the num_whitespace and size fields in our 'extra' column
def get_percent_whitespace(row):
    size = row.extra['size']
    # Avoid 'division by zero' exceptions.
    return row.extra['num_whitespace'] / size if size else 0

# Add 'percent_whitespace' column
job_df['percent_whitespace'] = job_df.apply(get_percent_whitespace, axis=1)

# Create a histogram of our data using the `percent_whitespace` column
job_df.hist(column="percent_whitespace", bins=100)
plt.show()
