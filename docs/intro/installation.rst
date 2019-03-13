Installation
============

Requirements
------------

Before beginning, you'll need to install:

* `Docker`_, a tool for running software in isolated containers
* `Python 3`_, the programming language needed to run (but not develop analysis with) ``r2c``
* `pip`_, the package manager for Python used to install and obtain updates for ``r2c``.

.. _docker: https://docs.docker.com/install/
.. _Python 3: https://docs.python.org/3/using/index.html
.. _pip: 

Follow those links to get both of those set up on your operating system and come back here when you're ready to proceed. Chances are, your installation of python already comes with pip, so it should only be two steps! To check if everything works, you can run the following commands:

.. note:: You'll need to be able to run ``docker`` as the same user you want to run ``r2c``. For linux users: Rather than run ``r2c`` as a root or system administrator, we highly encourage `setting up Docker for regular users <https://docs.docker.com/install/linux/linux-postinstall/#manage-docker-as-a-non-root-user>`_.

.. highlight:: text

Checking that docker works:::

  $ docker run hello-world

Checking that python and pip work:::

  $ python3 --version
  $ pip3 --version
   
Get the R2C CLI
---------------

It's easy! Just run:

  $ pip3 install r2c-cli

If you already have ``r2c`` installed and want to upgrade, run ``pip3 install -U r2c-cli``. ``r2c`` is still in beta, so check back here and upgrade early and often - we're making it better every day.

To verify that your installation of ``r2c`` works, run:

  $ r2c --help

You should see:::
  
  Usage: r2c [OPTIONS] COMMAND [ARGS]...

  Options:
    --debug    Show extra output, error messages, and exception stack traces
    --version  Show current version of r2c cli.
    --help     Show this message and exit.

  Commands:
    init      Creates an example analyzer for analyzing JavaScript/TypeScript.
    login     Log into the R2C analysis platform.
    logout    Log out of the R2C analysis platform.
    push      Push the analyzer in the current directory to the R2C analysis...
    run       Run the analyzer in the current directory over a code directory.
    test      Locally run integration tests for the current analyzer...
    unittest  Locally unit tests for the current analyzer directory You can...

If everything looks good, you're ready to move on to :doc:`creating`.  

