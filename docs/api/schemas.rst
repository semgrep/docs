Database Schemas
================

.. note::

    We recommend `psql <https://www.postgresql.org/docs/9.3/app-psql.html>`_ for raw querying and exploration of data or the Python library `sqlalchemy <https://www.sqlalchemy.org/>`_ for data analysis in environments like `Jupyter Notebook <https://jupyter.org/>`_. See :doc:`../intro/results` for more details and connection strings.

Analyzers with output type ``json`` (discussed in :doc:`manifest`) are stored in group specific SQL databases. There are two primary tables: 

1. ``result``
2. ``commit_corpus``

``result``
----------

The schema for the ``result`` table closely follows the format of :doc:`output`.

.. code-block:: console

          Column      |  Type   
    ------------------+---------
     id               | integer 
     analyzer_name    | text    
     analyzer_version | text    
     commit_hash      | text    
     check_id         | text    
     path             | text    
     start_line       | integer 
     start_col        | integer 
     end_line         | integer 
     end_col          | integer 
     extra            | jsonb   

``commit_corpus``
-----------------

.. code-block:: console

       Column    | Type 
    -------------+------
     commit_hash | text 
     repo_url    | text 
     corpus_name | text 
