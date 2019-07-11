Running on r2c
==============

.. note:: The following sections require you to be a member of the r2c beta.

Logging in to r2c
-----------------

To publish and download analyzers you'll need to log in to the r2c platform.

.. code-block:: console

  $ r2c login
  Please enter your org name, or to use the common r2c platform, press enter [wildwest]:
  Opening web browser to get login token. Do you want to continue? [Y/n]:
  trying to open https://app.r2c.dev/settings/token in your browser...
  Please enter the API token: ...

Follow the on-screen instructions, accepting the default ``wildwest`` org name (which is tied to the beta).

Pushing to r2c
--------------

Before uploading our analyzer, let's take a quick look at it to make sure everything is ready. **Once published, analyzer versions can't be
unpublished**. For larger analyzers, this would also be the time to run unit and integration
tests. 

For this tutorial analyzer, we'll just sanity-check the fields in ``analyzer.json``:

.. literalinclude:: samples/minifinder/analyzer.json
    :linenos:
    :language: json
   
Everything looks mostly good. However, to follow best practices, our analyzer should use `Semantic
Versioning`_. As this is our first release, but we're not yet sure if everything is production
ready, we should designate this release version ``0.1.0``:

.. code-block:: text

  "version": "0.1.0",

.. _Semantic Versioning: https://semver.org/

.. highlight:: text

Great! Now we're all set. We can push our analyzer to r2c by running the following command from
within the analyzer directory:

.. code-block:: console

  $ r2c push

That's it! Head on over to `app.r2c.dev <https://app.r2c.dev>`_ to run your analyzer on an npm input set and dive into the results.

Starting the Job
----------------

Once you've logged in to the platform you'll be taken to the Jobs page, which will look similar to this:

.. image:: images/r2c.png
   :alt: The r2c Jobs page

Click the "Create Job" button, which will pull up a menu letting you select the analyzer you've just
pushed!

.. image:: images/analyzer.png
   :alt: Selecting the analyzer to run

Now we'll select an input set to run our analyzer on: ``r2c npm 1000, 2019-04-01``.

.. image:: images/npm1k.png
   :alt: Choosing the input set to run your analyzer on.

Click "Run Job" to start the analysis! Your job will be added to the jobs list, where you can click on it to see output, console logs, and errors coming in in real time!

See :doc:`results` for next steps.
      
.. note:: When a job is first kicked off, the infrastructure may need to "warm up"; idle machines will start processing your job and new machines will be brought online to handle the demand. Once warmed up a job should proceed quickly and you'll get results within just a few minutes for quick analyzers like the tutorial.

.. note:: We currently limit your container to running for 5 minutes with 1.5 GB of memory. Most analyzers don't hit this limit, however, if you believe you're running into them please let us know and we can adjust them for your research.
