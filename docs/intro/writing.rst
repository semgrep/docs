Writing Analysis
================

For this tutorial, we're writing an analysis that reports **how much of each file in a project
is whitespace**. We'll use it to find which projects have checked in `minified JavaScript files`_.

.. _minified JavaScript files: https://en.wikipedia.org/wiki/Minification_(programming)

Setting up the Container
------------------------

We will write this analysis in the Python programming language. Though we are using Python for this
tutorial, **you can write analysis in any programming language** as each Docker container can have
different software installed.

Before we can write Python, we'll need to install it in our Docker container. To do this, add the
following line to the project's Dockerfile:

.. literalinclude:: samples/minifinder/Dockerfile
    :linenos:
    :language: dockerfile
    :emphasize-lines: 3

When we edit our code later, the container will automatically be rebuilt by ``r2c run``.

Writing the Code
----------------

We need to be able to count both whitespace and non-whitespace characters in a given file. We can do
this with a simple regular expression in Python. Create a file ``src/whitespace.py`` with the
following contents:

.. literalinclude:: samples/minifinder/src/whitespace.py
    :linenos:
    :language: python3

This file computes the number of whitespace characters and total characters in each file in its
input. When we run our analyzer, we want to run this file with all JavaScript input files as
arguments.

We write this object to ``/analysis/output/output.json`` because this is a JSON-type analyzer. r2c
also supports filesystem type analyzers, that modify or augment their input but want to preserve a
filesystem structure or output large binary data, e.g. neural net training results. Most analysis
eventually leads to JSON output, because JSON output is what gets consumed r2c's other tools.

To get just JavaScript files, we'll use the ``find`` program on our mounted source-code
directory. Change ``src/analyze.sh`` to look like this:

.. literalinclude:: samples/minifinder/src/analyze.sh
    :linenos:
    :language: bash
    :emphasize-lines: 6-8

First, we change to the directory our source code is checked out. That folder is
``/analysis/inputs/public/source-code/`` inside the Docker container. This location is a result of
minifinder depending on the ``source-code`` component (configured in ``analyzer.json``). For more
information about dependencies and locating their output, see :doc:`/api/index`.

Then, we use the ``find`` command to find all files that end in ``.js`` and use ``xargs`` to have it
pass all of those file paths as arguments to our python program.

.. note:: Though we wrote our python in a file ``src/whitespace.py``, inside of ``src/analyze.sh``
          we invoke it at the path ``/analyzer/whitespace.py``. This is because in line 12 of our
          Dockerfile, we copy the ``src`` folder to the ``/analyzer`` folder inside the container.

Now that we've written our code, let's try :doc:`running-locally`.
