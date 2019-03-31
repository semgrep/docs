Analyzing Results
=================

.. note:: The following instructions are for analyzers with output type ``json``. See :doc:`../api/manifest` to learn more about this and other output types.

When you run an analyzer on the r2c platform we store the results in a group or team specific PostgreSQL database. There are a few ways we prefer to interact with results that all ultimately rely on a SQL client. The most common tools we've used and seen are:

1. `psql <https://www.postgresql.org/docs/9.3/app-psql.html>`_, for raw querying
2. `Jupyter Notebook <https://jupyter.org/>`_ with Python `sqlalchemy <https://www.sqlalchemy.org/>`_, for more in-depth analysis.

We'll use both in this tutorial to explore the available tables, data, and to find minified files.

Using ``psql``
--------------

First, install ``psql``.

.. code-block:: console

  # Mac OSX
  $ brew install postgresql

  # Ubuntu
  $ apt install psql

After installation, confirm it's available on your path.

.. code-block:: console

  $ psql

  psql: could not connect to server: No such file or directory
	Is the server running locally and accepting
	connections on Unix domain socket "/tmp/.s.PGSQL.5432"?

Next, log in to your group or team's database, replacing ``$DB_PASSWORD`` and ``$GROUP`` (contact us if you don't know these values).

.. code-block:: console

  $ psql postgresql://notebook_user:$DB_PASSWORD@$GROUP-db.massive.ret2.co/postgres

  psql (10.6 (Ubuntu 10.6-0ubuntu0.18.04.1), server 9.6.8)
  SSL connection (protocol: TLSv1.2, cipher: ECDHE-RSA-AES256-GCM-SHA384, bits: 256, compression: off)
  Type "help" for help.
  
  postgres=>

To see results:

.. code-block:: console

  postgres=> select * from result;

At this stage you should see results! If you do not, confirm that you've run an analyzer and that it has reported success within the web UI.

Now that we've selected all results (``select *``), we'll limit the search with a more complicated query to just the results relevant to your analyzer, the selected version, and the corpus you ran against.

.. code-block:: console

  select result.commit_hash from result, commit_corpus where corpus_name = $CORPUS and analyzer_name = $ANALZYER and analyzer_version = $ANALYZER_VERSION and commit_corpus.commit_hash = result.commit_hash group by result.commit_hash

Using Jupyter Notebook with Python
----------------------------------

TODO
* more comprehensive data analysis and data science work. Recommend using docker here and running Jupyter locally.
* run docker
 * we've already set up for sqlalchemy
 * create a new notebook
 * run following query to show data
  * notice that this is basically just the psql commands we ran earlier
* do analysis to find minified files
* graph them?
