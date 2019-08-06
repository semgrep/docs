Troubleshooting
===============

The ``/analysis`` directory is completely empty
-----------------------------------------------

If the ``/analysis`` directory doesn't even have ``inputs`` and ``output`` 
subdirectories, then Docker is probably having issues mounting those folders. To verify, run

.. code-block:: console

   $ tempdir=$(mktemp -d)
   $ touch $tempdir/data
   $ docker run --volume $tempdir:/dummy alpine:latest ls -l /dummy

You should see a single line of output:

.. code-block:: console

   total 0

If this is the case, then Docker can't mount folders inside /tmp. This can happen if you installed Docker via the snap package manager (i.e., ``which docker`` shows a path starting with ``/snap``). If you did that, you'll need to run ``sudo snap remove docker`` and then `reinstall Docker`_ via your package manager or a similar method.

.. _reinstall docker: https://docs.docker.com/install/

If you see two lines of output like

.. code-block:: console

    total 0
    -rw-r--r--    1 root     root             0 Apr 15 21:47 data

then the issue is something else. In that case, please contact us at `support@r2c.dev`_ and we'll be happy to assist.

.. _support@r2c.dev: support@r2c.dev


The ``r2c`` command is not found
--------------------------------

If you try to run ``r2c --help`` from the command line and receive a ``command not found`` error, then it’s possible you need to add something to your ``$PATH``.

First, get the appropriate location to be added from pip3 by running

.. code-block:: console

   $ pip3 show r2c-cli

Notice the output reports a field labeled ``Location``. For example, this might be something like:
``/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages``.

From the ``Location`` you can derive the appropriate ``bin`` directory that needs to be added to the ``$PATH``. In this example, that would be:
``/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/bin``.

In your shell of choice, add that directory to your path through an entry in your ``.bashrc``, ``.zshrc``, or similar (depending on your shell), for example:

.. code-block:: console

   export PATH="$PATH:/Library/Frameworks/Python.framework/Versions/3.7"
