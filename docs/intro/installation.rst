Installation
============

Requirements
------------

.. note:: We currently support Ubuntu and Mac OSX for running ``r2c`` and developing analyzers. While not officially supported, some users have used Windows Subsystem for Linux (WSL) on Windows 10.

Before beginning, you'll need to install:

* `Docker`_, a tool for running software in isolated containers
* `Python 3`_, the programming language needed to run (but not develop analysis with) ``r2c``
* `pip`_, the package manager for Python used to install and obtain updates for ``r2c``.

.. _docker: https://docs.docker.com/install/
.. _Python 3: https://docs.python.org/3/using/index.html
.. _pip: 

Follow those links to get both of those set up on your operating system and come back here when you're ready to proceed. Chances are, your installation of python already comes with pip, so it should only be two steps! To check if everything works, you can run the following commands:

.. note:: You'll need to be able to run ``docker`` as the same user you want to run ``r2c``. For linux users: Rather than run ``r2c`` as a root or system administrator, we highly encourage `setting up Docker for regular users <https://docs.docker.com/install/linux/linux-postinstall/#manage-docker-as-a-non-root-user>`_.

.. attention:: Installing Docker via the ``snap`` installer is incompatible with ``r2c``. If you're not sure how it was installed, run ``which docker``. If the output starts with ``/snap`` or something similar, you'll need to uninstall it from snap via ``sudo snap remove docker`` and then install it via one of the other methods listed above.

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
