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

That's it! Head on over to :samp:`https://[YOUR-GROUP].massive.ret2.co/` to run your analyzer on the
top 1000 npm projects and dive right into the results. These documents will be updated soon to cover
that part of the r2c workflow as well; for now, don't hesitate to :email:`reach
us<mailto:collaborate@returntocorp.com>` by email with any questions! Once you've successfully run
your analysis on 1000 projects and looked at the result, send us an email for access to larger and
more powerful data sets, including the entire history of hundreds of thousands of packages on npm.
               
Happy hacking!
