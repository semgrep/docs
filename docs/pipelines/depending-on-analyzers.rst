Depending on Other Analyzers
============================

So you've looked around and identified an analyzer you'd like to depend on: great!
The next step is to add it as a dependency of your analyzer.

Declaring the Dependency
------------------------

In this example, we'll write an analyzer that uses a type-annotated AST produced by ``r2c/typed-ast`` and build some rules that use the type annotations.

We'll initialize an analyzer with ``r2c init`` and call it *typed-ast-rules-example*. Then we edit the ``analyzer.json`` to include ``r2c/typed-ast`` as a dependency:

.. literalinclude:: samples/typed-ast-rules-example/analyzer.json
    :linenos:
    :language: json

Analyzers are expected to follow `semantic versioning <https://semver.org/>`_.
You can depend on a specific version, or on the latest with ``*``. For more details, see see :ref:`api/manifest`.


Using the Dependency
--------------------

We've declared the dependency--how do we actually use it?

The output of the previous analyzer stage (or stages--you can have multiple dependencies in your analyzer)
will be mounted into your container automatically. 

As a reminder, dependencies for analyzers are mounted into the container at ``/analysis/inputs``.

All dependency names must also be valid Linux filesystem paths; this enables r2c to mount each
dependency in a subfolder matching the org and analyzer name. For example, for the ``transpiler``
analyzer published by ``r2c-cli``, specified in the dependency object as ``"r2c/transpiler": "1.0.0"``,
its output will appear under ``/analysis/inputs/r2c/transpiler``.

This behavior is slightly different for filesystem type analyzers and JSON type analyzers. For
filesystem type analyzers, their input appears at that path. If ``r2c/transpiler`` is of type
filesystem and writes a file named ``foo.bin`` to ``/analysis/output/output/``, then when depending
on ``r2c/tranpsiler``, that file would exist at ``/analysis/inputs/r2c/transpiler/foo.bin``. If on
the other hand, ``r2c/transpiler`` is of type JSON and writes its output to
``/analysis/output/output.json``, that JSON file would exist at
``/analysis/inputs/r2c/transpiler.json``.

In our case, ``r2c/typed-ast`` is a filesystem analyzer, so we can look for its input at ``/analysis/inputs/r2c/typed-ast``. 
Our ``analyze.sh`` entrypoint specifies this and passes it to a program that will iterate over all of the input ASTs and perform matching on them:

.. literalinclude:: samples/typed-ast-rules-example/src/analyze.sh
    :linenos:
    :language: bash

If you're interested in using *typed-ast-rules-example* specifically, you can continue cloning https://github.com/returntocorp/typed-ast-rules-example