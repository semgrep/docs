Creating an Analyzer
=====================

Creating the Boilerplate
------------------------

In a directory where you want to create your new analyzer, run:

.. code-block:: console

  $ r2c init

For the ``Analyzer name`` prompt, enter ``<YOUR-USERNAME>-minifinder``. A new subdirectory with that name will be created. For the rest of the prompts we'll use the defaults.

.. code-block:: console

  $ r2c init
  Analyzer name (can only contain lowercase letters, numbers or - and _): <YOUR-USERNAME>-minifinder
  Author name [Jav A. Script]:
  Author email [hello@example.com]:
  Will your analyzer produce:
  - output for a particular `git` repository
  - output for a particular git `commit` in a repo
  - the same `constant` output regardless of commit or repo? (git, commit, constant) [commit]:
  Does your analyzer output
  - a single schema-compliant JSON file
  - a full filesystem output? (json, filesystem) [json]:
  ✔ Done! Your analyzer can be found in the <YOUR-USERNAME>-minifinder directory

Check it out by changing to the new folder:

.. code-block:: console

   $ cd <YOUR-USERNAME>-minifinder/

Understanding Analyzer Files
----------------------------

The ``init`` command created several files in the directory you initialized:

.. code-block:: text

  .
  ├── Dockerfile
  ├── README.md
  ├── analyzer.json
  └── src
      ├── analyze.sh
      └── unittest.sh

Each of these files is used by the r2c system in a different way.
  
* ``analyzer.json`` defines how your analyzer will interact with the r2c system and tools. Some
  important values in this file are:

 * ``analyzer_name``: The namespaced analyzer name. For the beta, all analyzers must be namespaced with ``beta`` to be uploaded to the platform.

 * ``version``: The version of the analyzer. *Versions should follow semantic versioning*. r2c
   uses the analyzer name, version, and other parameters for caching: when running an analyzer at
   scale, all of these are used to determine if the analysis has already been run on that piece of
   code.

 * ``dependencies``: This analyzer depends on the most basic component, ``public/source-code``. It
   specifies that it depends on any version of the ``public/source-code`` component by specifying ``"*"``
   as the version. For more complicated analysis, we could depend on components such as
   ``r2c/transpiler`` or ``r2c/typed-ast``, which are beyond the scope of this tutorial.

* ``Dockerfile`` is responsible for the container's setup and configuration. In this file you can
  install dependencies to build and run your analysis. To learn more about Dockerfiles in general,
  see `Docker's tutorial
  <https://docs.docker.com/get-started/part2/#define-a-container-with-dockerfile>`_.

.. note:: Though it can be tempting to use images like ``node:latest``, most analyzers should be
          deterministic and therefore benefit from pinning their base image to a specific
          version. For more information, see :doc:`/best-practices`.

* ``src/analyze.sh`` is the main entry point. From this file, we'll run your program that performs
  analysis!

* ``src/unittest.sh`` run your analyzer's unit tests, if it has them, inside the container by
  caling them from this file.

Once you've checked out those files, let's move on to :doc:`writing`.
