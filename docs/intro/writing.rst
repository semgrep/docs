Writing the analysis
====================

For this tutorial, we're going to write an analysis that reports how much of each file in a project
is whitespace. We'll use it to find which projects have checked in minified Javascript files, so
we've called it minifinder. At this point we have our ``minifinder`` folder containing
``analyzer.json``, a ``Dockerfile``, and the ``src`` directory containing ``analyze.sh``.

The environment
---------------

.. highlight:: text

For the sake of expediency, we'll write this simple analyzer in bash with basic unix tools -
gawk, find, xargs, wc, and echo. We'll use an additional tool, jq, to format the
output as ``r2c``-compliant JSON.

Before we can use these tools, we'll need to install them in our Docker container. Our default base image already includes most of the programs we need, but we'll need to install gawk and jq. To do this, add the following line to the project's Dockerfile:

.. code-block:: dockerfile
   :emphasize-lines: 3

   FROM ubuntu:17.10

   RUN apt update && apt install -y jq gawk

   RUN groupadd -r analysis && useradd --no-log-init --system --gid analysis analysis

When we run our code later, the container will automatically be rebuilt.

.. note:: Analyzers can be written in any programming language, compiled as part of the Docker
          container build process, and executed by ``analyze.sh``. Only trivial analyzers should be
          written in languages like ``bash``! For more information, see
          :doc:`/best-practices`.

The code
--------

We need to be able to count both whitespace and non-whitespace characters in a given
file. We can do this with GNU ``awk`` and the following command [#f1]_::

  gawk -v RS='[[:space:]]' 'END{print NR}' <some-file>

We'll want to run that command on all Javascript files in our input. Because we depend on the
``source-code`` component for our input, the input will be located in
``/analysis/inputs/public/source-code/``. For more information on specifying dependencies and locating
their data, see :doc:`/api/index`.

To run that command over all files in our input, we can use the ``find`` program. Let's add it into our analyze.sh so that the file looks like this:

.. code-block:: bash
   :linenos:
   :emphasize-lines: 6-17,19,21,23-26

   #!/bin/bash

   set -e
   CODE_DIR="/analysis/inputs/public/source-code"

   whitespace () {
       num_ws=$(gawk -v RS='[[:space:]]' 'END{print NR}' "$1")
       total=$(wc -c $1 | cut -d ' ' -f 1)
       echo -e "{ \n\
       \"check_id\": \"whitespace\", \n\
       \"path\": \"$1\", \n\
       \"extra\": { \n\
         \"whitespace\": ${num_ws}, \n\
         \"total\": ${total} \n\
         } \n\
       }"
   }

   export -f whitespace

   cd ${CODE_DIR}

   find . -name '*.js' | \
     xargs -n 1 -I {} bash -c 'whitespace "$@"' _ {} | \
     jq -s '{results: .}' | \
     tee /analysis/output/output.json

There's a lot going on there, so we'll take it line by line.

First, we declare this as a function that can produce one r2c JSON result object per file. In line
7, we use GNU awk to find the number of whitespace characters. In line 8, we use wc to find the
total number of characters in the file; this will be helpful later for determining *how much* of the
file is whitespace. Then, we use echo to log the result as a single instance of an r2c JSON
result. The ``check_id`` field is necessary; it tells R2C what this result indicates. The rest of
the fields are optional, and will help us later to match results to code locations in other r2c
tools and to run our computations.

In line 19, we make this function available to other bash shells; this is needed for the arcane
``xargs`` instance to follow. Most analyses either discover Javascript files on their own, or can
run with command line arguments outside of bash, so this line won't be needed for most other
analyses.

In line 21, we change the working directory to the folder of our input. This is to make the paths we
output relative to the input source; it's easier than using absolute paths and removing the input
directory portion later.

In line 23, we:

* Use ``find`` to locate all ``js`` files in the project
* Use ``xargs`` to run bash with our ``whitespace`` function for all those files
* Use ``jq`` to gather all the individual results into a single, nicely formatted JSON object
* Write this object to ``/analysis/output/output.json``

We write this object to ``/analysis/output/output.json`` because this is a JSON-type analyzer. r2c
also supports filesystem type analyzers, that modify or augment their input but want to preserve a
filesystem structure or output large binary data, e.g. neural net training results. Most analyses
eventually lead to JSON output, because JSON output is what gets used by all of the other r2c tools.

Now that we've written our code, it's time for :doc:`running`.

.. [#f1] https://unix.stackexchange.com/questions/212859/how-can-i-count-the-number-of-whitespace-characters-in-a-file

