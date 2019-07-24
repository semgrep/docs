Installation
============

We'll start our journey with ``r2c-cli``, which is used to develop and test analyzers locally before pushing them to the platform to run at scale.

Requirements
------------

.. note:: We support Mac OS X and Ubuntu for local analyzer development.

Please install the following required software:

* `Docker Engine - Community`_: a tool for running software in isolated containers
* `Python 3.6+`_: the programming language needed to run (but not to develop) analyzers
* `pip3`_: the Python package manager used to install and update ``r2c-cli`` (note pip3 will be installed by the Python 3.6+ installer)

.. _Docker Engine - Community: https://docs.docker.com/install/#supported-platforms
.. _Python 3.6+: https://docs.python.org/3/using/index.html
.. _pip3: https://pip.pypa.io/en/stable/

When installing ``docker``:

- Do not use ``snap``, it is incompatible with ``r2c-cli``
- For Ubuntu users we highly encourage `setting up Docker for non-root users <https://docs.docker.com/install/linux/linux-postinstall/#manage-docker-as-a-non-root-user>`_. You need to run ``docker`` as the same user you'll run ``r2c-cli`` with, and we discourage running ``r2c-cli`` as a root or system administrator

Run the following to test ``docker``, ``python3``, and ``pip3`` installation:

.. code-block:: console

  $ docker run hello-world
  $ python3 --version
  $ pip3 --version

Getting ``r2c-cli``
-------------------

It's easy! Just run:

.. code-block:: console

  $ pip3 install r2c-cli

To verify the ``r2c-cli`` installation, run:

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

If the help prompt prints, you're ready to move on to :doc:`creating`.
