.. _running:

Running and testing
===================

.. highlight:: text

Let's test our analyzer! First we'll need a target javascript project to test it on. Let's use the popular ``left-pad`` project. Let's make a folder to keep our test projects in and clone that project to the folder::

  $ mkdir ~/test-repos
  $ git clone https://github.com/stevemao/left-pad ~/test-repos/left-pad

Now we can run our analyzer::

  $ r2c run --code ~/test-repos/left-pad

We get the following output:

.. code-block:: json
                
   {
     "results": [
       {
         "check_id": "whitespace",
         "path": "perf/O(n).js",
         "extra": {
           "whitespace": 77,
           "total": 241
         }
       },
       {
         "check_id": "whitespace",
         "path": "perf/perf.js",
         "extra": {
           "whitespace": 213,
           "total": 1442
         }
       },
       {
         "check_id": "whitespace",
         "path": "perf/es6Repeat.js",
         "extra": {
           "whitespace": 61,
           "total": 216
         }
       },
       {
         "check_id": "whitespace",
         "path": "test.js",
         "extra": {
           "whitespace": 714,
           "total": 4005
         }
       },
       {
         "check_id": "whitespace",
         "path": "index.js",
         "extra": {
           "whitespace": 436,
           "total": 1469
         }
       }
     ]
   }

This is helpful! We don't see any minified files, but it'd be nice to understand what *percentage* of the file is whitespace. Let's add a percentage field; we can compute this using the program ``bc``. First, we'll add the program to our Dockerfile:

.. code-block:: Dockerfile
   :emphasize-lines: 3

   FROM ubuntu:17.10
                
   RUN apt update && apt install -y jq gawk bc

   RUN groupadd -r analysis && useradd --no-log-init --system --gid analysis analysis

Now let's add the percentage computation to our whitespace function:

.. code-block:: bash
   :emphasize-lines: 4,10,11
                     
   whitespace () {
       num_ws=$(gawk -v RS='[[:space:]]' 'END{print NR}' "$1")
       total=$(wc -c $1 | cut -d ' ' -f 1)
       path=$(echo "{$1}" |  cut -c 2-)
       pct=$(echo "scale = 4; $num_ws / $total * 100" | bc)
       echo -e "{ \n\
       \"check_id\": \"whitespace\", \n\
       \"path\": \"${path}\", \n\
       \"extra\": { \n\
         \"whitespace\": ${num_ws}, \n\
         \"total\": ${total}, \n\
         \"percentage\": ${pct} \n\
         } \n\
       }"
   }
                                
And run again:

.. code-block:: bash

  $ r2c run --code ~/test-repos/left-pad/



.. code-block:: json
   
   {
     "results": [
       {
         "check_id": "whitespace",
         "path": "perf/O(n).js",
         "extra": {
           "whitespace": 77,
           "total": 241,
           "percentage": 31.95
         }
       },
       {
         "check_id": "whitespace",
         "path": "perf/perf.js",
         "extra": {
           "whitespace": 213,
           "total": 1442,
           "percentage": 14.77
         }
       },
       {
         "check_id": "whitespace",
         "path": "perf/es6Repeat.js",
         "extra": {
           "whitespace": 61,
           "total": 216,
           "percentage": 28.24
         }
       },
       {
         "check_id": "whitespace",
         "path": "test.js",
         "extra": {
           "whitespace": 714,
           "total": 4005,
           "percentage": 17.82
         }
       },
       {
         "check_id": "whitespace",
         "path": "index.js",
         "extra": {
           "whitespace": 436,
           "total": 1469,
           "percentage": 29.68
         }
       }
     ]
   }

Cool! Now we can hunt for minified files. All of these files look reasonable; though we don't know exactly what our threshold should be, minified files will probably be less than 5 to 10 percent whitespace. To find minified files in top projects and get a sense of what cut-off point to use, we'll want to run this analyzer at scale against npm packages - perhaps the top 1000 to start. To get started, head on over to :doc:`uploading`.
