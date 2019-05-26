Creating an Analyzer
=====================

Logging in to r2c
-----------------

.. note:: This section requires you to be a member of the ``r2c`` beta. Please skip it if you're doing local only development and/or are not currently part of the beta.

To download and publish analyzers you'll need to log in to the ``r2c`` platform.

.. code-block:: console

  $ r2c login
  Please enter your org name, or to use the common r2c platform, press enter [wildwest]:
  Opening web browser to get login token. Do you want to continue? [Y/n]:
  trying to open https://app.r2c.dev/settings/token in your browser...
  Please enter the API token: ...

Follow the on-screen instructions, accepting the default ``wildwest`` org name (which is tied to the beta).

Creating the Boilerplate
------------------------

In a directory where you want to create your new analyzer, run:

.. code-block:: console

  $ r2c init

For the ``Analyzer name`` prompt, enter **minifinder**. For the rest of the prompts we'll use
the defaults by pressing enter.

.. code-block:: console

  $ r2c init
  Analyzer name [example]: minifinder
  Author name [Jav A. Script]:
  Author email [hello@example.com]:
  Will your analyzer produce:
  - output for a particular `git` repository
  - output for a particular git `commit` in a repo
  - the same `constant` output regardless of commit or repo? (git, commit, constant) [commit]:
  Does your analyzer output
  - a single schema-compliant JSON file
  - a full filesystem output? (json, filesystem) [json]:
  ✅ Done! Your analyzer can be found in the minifinder directory

Check it out by changing to the new folder:

.. code-block:: console

   $ cd minifinder/

Understanding Analyzer Files
----------------------------

The ``init`` command created several files in the ``minifinder`` folder:

.. code-block:: text

  .
  ├── analyzer.json
  ├── Dockerfile
  └── src
      ├── analyze.sh
      └── unittest.sh

Each of these files is used by the ``r2c`` system in a different way.
  
* ``analyzer.json`` defines how the analyzer will interact with the ``r2c`` system and tools. Some
  important values in this file are:

 * ``analyzer_name``: The namespaced analyzer name. The name you entered has been combined with your
   org name - this is because you can only develop analyzers within your org.

 * ``version``: The version of the analyzer. *Versions should follow semantic versioning*. ``r2c``
   uses the analyzer name, version, and other parameters for caching: when running an analyzer at
   scale, all of these are used to determine if the analysis has already been run on that piece of
   code.

 * ``dependencies``: This analyzer depends on the most basic component, ``source-code``. It
   specifies that it depends on any version of the ``source-code`` component by specifying ``"*"``
   as the version. For more complicated analysis, we could depend on components such as
   ``r2c/transpiler`` or ``r2c/typeflow``, but those are beyond the scope of this tutorial.

* ``Dockerfile`` is responsible for the container's setup and configuration. In this file you can
  install dependencies to build and run your analysis. To learn more about Dockerfiles in general,
  see `Docker's tutorial
  <https://docs.docker.com/get-started/part2/#define-a-container-with-dockerfile>`_.

.. note:: Though it can be tempting to use images like ``node:latest``, most analyzers should be
          deterministic and therefore benefit from pinning their base image to a specific
          version. For more information, see :doc:`/best-practices`.

* ``src/analyze.sh`` is the main entry point. From this file, we'll run the programs that perform our
  analysis!

* ``src/unittest.sh`` lets us run our analyzer's unit tests, if it has them, inside the container by
  caling them from this file.

Once you've checked out those files, let's move on to :doc:`writing`.
