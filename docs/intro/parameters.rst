Parameterized Analyzers
===========================

In some cases, you may want your analyzer to have behavior that's configurable
at runtime. For example, an analyzer that looks for uses of a certain function
would want the user to be able to specify the name of the function, as opposed
to having to make a new version of the analyzer each time the user wants to look
for a separate function.

This is what **parameterized analyzers** are for. An analyzer can receive a
parameter object, which is an arbitrary JSON dict, from where it was invoked
(either the local r2c tool or the analysis platform), and the parameters will
be present inside the Docker image at ``/analysis/input/parameters.json``.

.. warning::

    Currently, if an analyzer doesn't have any explicitly-passed parameters, it
    will get an empty object (i.e., ``{}``) as parameters. In the
    future, this will change so that the parameters file will contain ``null``
    instead. Therefore, any analyzers you write should be able to handle both
    cases with the same semantics.

If you have version 0.0.24b0 or later of the r2c tool, you can try it out for
yourself. Run your test analyzer as follows:

.. code-block:: console

    $ r2c run --interactive \
              --parameters '{"hello": "world"}' \
              ~/test-repos/left-pad

The ``--interactive`` option means that, instead of running the analyzer, it will
drop us into a shell running inside the analyzer's Docker image. From here, you
can see the parameters:

.. code-block:: console

   $ cat /analysis/input/parameters.json
   {"hello": "world"}

The meaning of the parameters is up to the analysis author; for our whitespace
analyzer, you could imagine passing ``{"tabsAsSpaces": 2}`` to indicate that tabs
should be counted as two spaces.

When running an analyzer on the platform, the results page will have a
'parameters' tab contianing a YAML representation of the parameters as passed to
the analyzer, and the job list will have a trimmed-down preview of the
parameters, so you can distinguish jobs with different parameters easily.

Parameters and Determinism
==============================

A note for analysis authors: this means that your analyzer should behave
*deterministically* with respect to its parameters: the same version of an
analyzer run over a given input with the same parameters should always
produce the same output.

If you want to embed an resource via its URL, you should include a URL whose
contents will never change and also include a hash of the resource's
contents in your parameters. You should also *fail* if the hash doesn't
validate, so that if a user includes a URL that changes, they'll notice
instead of silently getting cached results.

However, we may in the future disable or heavily restrict analyzers' network
access, so we would prefer you avoid fetching URLs in the first place. If you
want to do this, please contact us!
