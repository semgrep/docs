.. _running:

Running Locally
===============

.. highlight:: text

Let's test our analyzer! First we'll need a target JavaScript project to test it on. Let's use the popular ``left-pad`` project. Let's make a folder to keep our test projects in and clone that project to the folder:

.. code-block:: console

  $ mkdir ~/test-repos
  $ git clone https://github.com/stevemao/left-pad ~/test-repos/left-pad

Now we can run our analyzer:

.. code-block:: console

  $ r2c run ~/test-repos/left-pad

We get the following output:

.. literalinclude:: samples/minifinder/examples/leftpad.json
    :linenos:
    :language: json
    :lines: 5-44

This is helpful! We don't see any minified files, but it'd be nice to understand what *percentage* of the file is whitespace. Let's add a percentage field; we can compute this using the program ``bc``. First, we'll add the program to our Dockerfile:

.. literalinclude:: samples/minifinder2/Dockerfile
    :linenos:
    :language: dockerfile
    :emphasize-lines: 3

Now let's add the percentage computation to our whitespace function:

.. literalinclude:: samples/minifinder2/src/analyze.sh
    :linenos:
    :language: bash
    :emphasize-lines: 10,16,17
    
                                
And run again:

.. code-block:: console

  $ r2c run ~/test-repos/left-pad/

.. literalinclude:: samples/minifinder2/examples/leftpad.json
    :linenos:
    :language: json
    :lines: 5-49

Cool! Now we can hunt for minified files. All of these files look reasonable; though we don't know exactly what our threshold should be, minified files will probably be less than 5 to 10 percent whitespace. To find minified files in top projects and get a sense of what cut-off point to use, we'll want to run this analyzer at scale against npm packages - perhaps the top 1000 to start. To get started, head on over to :doc:`uploading`.