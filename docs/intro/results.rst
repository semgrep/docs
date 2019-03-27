Analyzing Results
=================

.. note:: The following instructions are for analyzers with output type ``json``. See TODO to learn more.

When you run an analyzer on the r2c platform we store the results in a group or team specific SQL database. There are a few ways we prefer to interact with results that all ultimately rely on a SQL client of some kind. The most common tools we've used and seen are:

1. `psql <https://www.postgresql.org/docs/9.3/app-psql.html>`_, for raw querying
2. `Jupyter Notebook <https://jupyter.org/>`_ with Python sqlalchemy, for more in-depth analysis.

We'll use both in this tutorial to explore the available tables, data, and to find minified files. For your own projects, we encourage you to use what you're familiar with for working with SQL.

Using ``psql``
--------------

* great tool for quickly getting a feel for data through the use of counts and aggregations
* making sure you have it (brew install, apt install)
* connecting to the DB (psql postgres://<>:<>:<>)
 * table names
  * \dt
* how data relates to output.json format
 * schemas: \d results
 * closely matches output.json
* how do I get results for just my job?
  * We filter by corpus, analyzer, and version
  * why?? because results may be cached, so we don't use job_id as an identifier here

Using Jupyter Notebook with Python
---------------------------------

TODO
* more comprehensive data analysis and data science work. Recommend using docker here and running Jupyter locally.
* run docker
 * we've already set up for sqlalchemy
 * create a new notebook
 * run following query to show data
  * notice that this is basically just the psql commands we ran earlier
* do analysis to find minified files
* graph them?
