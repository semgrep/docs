.. _running:

Running Analysis Locally
========================

Let's test our analyzer! First we'll need a target JavaScript project to test it on. Let's use the
popular `left-pad <https://github.com/stevemao/left-pad>`_ project. Make a folder to keep our test projects in and clone ``left-pad`` to the folder:

.. code-block:: console

  $ mkdir ~/test-repos
  $ git clone https://github.com/stevemao/left-pad ~/test-repos/left-pad

Now we can run our analyzer:

.. code-block:: console

  $ r2c run ~/test-repos/left-pad

We get the following output:

.. literalinclude:: samples/minifinder/output/console.log
    :language: console

Notice how the ``print`` statements in our Python code appear as if we were running the program
outside of r2c. This makes it easy to debug programs normally. The full JSON output of the program
should look something like this:

.. literalinclude:: samples/minifinder/output/leftpad.json
    :linenos:
    :language: json

Cool! Now we can hunt for minified files. All of these files look reasonable; though we don't know
exactly what our threshold should be, minified files will probably be less than 5 to 10 percent
whitespace. To find minified files in top projects and get a sense of what cut-off point to use,
we'll want to run this analyzer at scale against npm packages. 

To get started, head on over to :doc:`running-scale`.
