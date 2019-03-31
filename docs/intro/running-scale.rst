Running on r2c
==============

Pushing to r2c
--------------

Before we can run analysis at scale, we need to upload the analyzer to ``r2c``.

Uploading an analyzer is simple. In :doc:`creating`, we logged in to the r2c system, so we already
have our credentials to push analyzers to r2c. Once published, though, analyzer versions can't be
unpublished, so we should take a quick look at our analyzer to make sure everything is ready to
go. For larger analyzers, this would be the time to also run all of our unit tests and integration
test. For this tutorial analyzer, we'll just sanity-check the fields in ``analyzer.json``:

.. literalinclude:: samples/minifinder/analyzer.json
    :linenos:
    :language: json
   
Everything looks mostly good. However, to follow best practices, our analyzer should use `Semantic
Versioning`_. As this is our first release, but we're not yet sure if everything is production
ready, we should designate this release version ``0.1.0``:

.. code-block:: json

  "version": "0.1.0",

.. _Semantic Versioning: https://semver.org/

.. highlight:: text

Great! Now we're all set. We can push our analyzer to r2c by running the following command from
within the analyzer directory:

.. code-block:: console

  $ r2c push

That's it! Now let's head on over to :samp:`https://[YOUR-GROUP].massive.ret2.co/` to run your analyzer on the
top 1000 npm projects and dive right into the results.

Starting the Job
----------------

Once you've logged in with Github, your group's Jobs page might look something like this:

.. image:: images/r2c.png
   :alt: The r2c Jobs page

Click the "Create Job" button, which will pull up a menu letting you select the analyzer you've just
pushed!

.. image:: images/analyzer.png
   :alt: Selecting the analyzer to run

After that, we'll pick a data set to run our analyzer across. Let's use the top 1000 NPM packages as
of the start of 2019 for this tutorial.

.. image:: images/npm1k.png
   :alt: Choosing the data set for our run.

Click "Run Job" to start the analysis!
      
Viewing Results
---------------

The job we started in the previous section may take a little while to run. The first time you run
any job, it may take a while for the Docker image to reach all the machines running your
analysis. Once that happens, it should proceed quickly and you should be able to get results within
just a few minutes for your code. You can click on the job in the job list to see the output,
console logs, and errors coming in in real time.

Once the job has finished, click the "View results in notebook" button to be taken to your Jupyter
notebook where you can query the results. Currently, this documentation doesn't cover that part of
the r2c system. We're adding more documentation soon, bu for now, don't hesitate to :email:`reach
us<mailto:collaborate@returntocorp.com>` by email with any questions!  Once you've successfully
explored your analysis across 1000 projects, send us an email for access to larger and more powerful
data sets, including the entire history of hundreds of thousands of packages on npm.

Happy hacking!
