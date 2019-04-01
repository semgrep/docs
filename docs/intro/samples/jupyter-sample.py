import os
import pandas as pd
import psycopg2
from sqlalchemy import create_engine

###################################
# START OF EDITABLE CONSTANTS
###################################

GROUP = "YOUR-GROUP"
DB_PASSWORD = "YOUR-DB-PASSWORD"

ANALYZER_NAME = f"{GROUP}/minifinder"
ANALYZER_VERSION = "0.1.0"
CORPUS_NAME = "npm-1000-2019-01-01"

###################################
# END OF EDITABLE CONSTANTS
###################################

ANALYZER_SPECIFIC_QUERY = """
SELECT result.commit_hash
FROM  result,
      commit_corpus
WHERE corpus_name = %(corpus_name)s
      AND analyzer_name = %(analyzer_name)s
      AND analyzer_version = %(analyzer_version)s
      AND commit_corpus.commit_hash = result.commit_hash
GROUP BY result.commit_hash;
"""

QUERY_PARAMS = {
    "corpus_name": CORPUS_NAME,
    "analyzer_name": ANALYZER_NAME,
    "analyzer_version": ANALYZER_VERSION
}

engine = create_engine(f'postgresql://notebook_user:{DB_PASSWORD}@{GROUP}-db.massive.ret2.co/postgres')
analyzer_specific_df = pd.read_sql(analyzer_specific_query, engine, params=QUERY_PARAMS)
analyzer_specific_df
