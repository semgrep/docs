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
