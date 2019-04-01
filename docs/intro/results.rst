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

  $ export $DB_PASSWORD=[YOUR-DB-PASSWORD]
  $ export $GROUP=[YOUR-GROUP]
  $ psql postgresql://notebook_user:$DB_PASSWORD@$GROUP-db.massive.ret2.co/postgres

  psql (10.6 (Ubuntu 10.6-0ubuntu0.18.04.1), server 9.6.8)
  SSL connection (protocol: TLSv1.2, cipher: ECDHE-RSA-AES256-GCM-SHA384, bits: 256, compression: off)
  Type "help" for help.
  
  postgres=>

To see results:

.. code-block:: console

  postgres=> SELECT * FROM result;

At this stage you should see results! If you do not, confirm that you've run an analyzer and that it has reported success within the web UI.

Now that we've selected all results (``select *``), we'll limit the search with a more complicated query to just the results relevant to your analyzer, the selected version, and the corpus you ran against.

Replace ``$CORPUS_ID``, ``$ANALYZER_NAME``, ``$ANALYZER_VERSION`` (e.g. ``npm-1000-2019-01-01``, ``r2c/minifinder``, ``0.1.0``):

.. code-block:: console

  postgres=> SELECT result.commit_hash 
  FROM  result, 
        commit_corpus 
  WHERE corpus_name = $CORPUS_ID 
        AND analyzer_name = $ANALYZER_NAME 
        AND analyzer_version = $ANALYZER_VERSION
        AND commit_corpus.commit_hash = result.commit_hash 
  GROUP BY result.commit_hash;

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
