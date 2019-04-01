Analyzing Results
=================

.. note:: The following instructions are for analyzers with output type ``json``. See :doc:`../api/manifest` to learn more about this and other output types.

When you run an analyzer on the r2c platform we store the results in a group or team specific PostgreSQL database. There are a few ways we prefer to interact with results that all ultimately rely on a SQL client. The most common tools we've used and seen are:

1. `psql <https://www.postgresql.org/docs/9.3/app-psql.html>`_, for raw querying
2. `Jupyter Notebook <https://jupyter.org/>`_ with Python `sqlalchemy <https://www.sqlalchemy.org/>`_, for more in-depth analysis.

We'll use both in this tutorial to explore the available tables, data, and to find minified files.

Using ``psql``
--------------

First, install ``psql`` on your terminal.

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

When SQL queries aren't sufficient, or we want to programatically interact with the data, we recommend `Jupyter Notebook <https://jupyter.org/>`_.

To standup a Jupyter Notebook instance locally using docker [#jupyter-tut]_:

.. code-block:: console

  $ docker run -p 8888:8888 jupyter/scipy-notebook:latest
  Unable to find image 'jupyter/scipy-notebook:latest' locally
  latest: Pulling from jupyter/scipy-notebook
  a48c500ed24e: Already exists
  ...
  b1ae2d961bf6: Download complete
  Digest: sha256:3abebd0ed8ba4f6c6c3c92c0294ce3f0379e4db363c621411af6f9efcb7d97e8
  Status: Downloaded newer image for jupyter/scipy-notebook:latest
  Executing the command: jupyter notebook
  [I 04:01:37.656 NotebookApp] Writing notebook server cookie secret to /home/jovyan/.local/share/jupyter/runtime/  notebook_cookie_secret
  [I 04:01:38.835 NotebookApp] JupyterLab extension loaded from /opt/conda/lib/python3.7/site-packages/jupyterlab
  [I 04:01:38.836 NotebookApp] JupyterLab application directory is /opt/conda/share/jupyter/lab
  [I 04:01:38.838 NotebookApp] Serving notebooks from local directory: /home/jovyan
  [I 04:01:38.838 NotebookApp] The Jupyter Notebook is running at:
  [I 04:01:38.838 NotebookApp] http://(5d73df7e3877 or 127.0.0.1):8888/?token=<TOKEN>
  [I 04:01:38.838 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
  
Following the instructions printed out to your terminal, navigate to Jupyter in your browser.

<image of jupyter>

.. code-block:: console

  $ pip install psycopg2-binary
  Collecting psycopg2-binary
  Downloading https://files.pythonhosted.org/packages/04/c3/fbf0ec416151ce082087bfbb42f236ec42c2c74d2d9f7a5b5cdf49cfc517/psycopg2_binary-2.7.7-cp37-cp37m-manylinux1_x86_64.whl (2.7MB)
    100% |████████████████████████████████| 2.7MB 3.5MB/s
  Installing collected packages: psycopg2-binary
  Successfully installed psycopg2-binary-2.7.7



 * install psycopg2
 * create a new notebook
 * do analysis to find minified files
 * graph them?

.. [#jupyter-tut] `Jupyter Docker Stacks, Running a Container <https://jupyter-docker-stacks.readthedocs.io/en/latest/using/running.html#running-a-container>`_