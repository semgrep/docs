Installation
============

We'll start our journey with ``r2c-cli``, which is used to develop and test analyzers locally before pushing them to the platform to run at scale.

Requirements
------------

.. note:: We support Mac OSX and Ubuntu for local analyzer development.

Please install the following required software:

* `docker`_: a tool for running software in isolated containers
* `python3`_: the programming language needed to run (but not to develop) analyzers
* `pip3`_: the Python package manager used to install and update ``r2c-cli``

.. _docker: https://docs.docker.com/install/
.. _python3: https://docs.python.org/3/using/index.html
.. _pip3: https://pip.pypa.io/en/stable/

When installing ``docker``:

- Do not use ``snap``, it is incompatible with ``r2c-cli``
- For Ubuntu users we highly encourage `setting up Docker for regular users <https://docs.docker.com/install/linux/linux-postinstall/#manage-docker-as-a-non-root-user>`_. You need to run ``docker`` as the same user you'll run ``r2c-cli`` with, and we discourage running ``r2c-cli`` as a root or system administrator

Once you've installed ``docker``, ``python3``, and ``pip3``, run the following commands to ensure everything is installed properly:

.. highlight:: text

Checking that docker works:

.. code-block:: console

  $ docker run hello-world

Checking that python and pip work:

.. code-block:: console

  $ python3 --version
  $ pip3 --version
   
Getting the r2c CLI
-------------------

It's easy! Just run:

.. code-block:: console

  $ pip3 install r2c-cli

.. note:: If you already have ``r2c`` installed and want to upgrade, run ``pip3 install -U r2c-cli``. ``r2c`` is still in beta, so check back here and upgrade early and often - we're making it better every day.

To verify that your installation of ``r2c`` works, run:

.. code-block:: console

  $ r2c --help
  Usage: r2c [OPTIONS] COMMAND [ARGS]...
  
  Options:
    --debug                 Show extra output, error messages, and exception
                            stack traces
    --version               Show current version of r2c cli.
    --no-traverse-manifest  Don't attempt to find an analyzer.json if it doesn't
                            exist in the current or specified directory
    --help                  Show this message and exit.
  
  Commands:
    build     Builds an analyzer without running it.
    init      Creates an example analyzer for analyzing JavaScript/TypeScript.
    login     Log in to the R2C analysis platform.
    logout    Log out of the R2C analysis platform.
    push      Push the analyzer in the current directory to the R2C platform.
    run       Run the analyzer in the current directory over a code directory.
    test      Locally run integration tests for the current analyzer.
    unittest  Locally unit tests for the current analyzer directory.
  
If the help prompt successfully prints, you're ready to move on to :doc:`creating`.
