Docker Containers
=================

The Dockerfile for r2c analyzers allows you to customize your operating system, software, and
filesystem as much as you like. However, r2c expects a few things of these containers to be able to
run analysis, and a few more things for a smooth experience when developing analysis on your local
machine.

Filesystem Structure
--------------------

Dependencies for analyzers are mounted into the container at ``/analysis/inputs``. For more on
specifying dependencies, see :ref:`the manifest spec <analyzer_json_manifest_spec>`.

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

Above we allude to ``/analysis/output/``; this is the folder where analyzers are expected to write
their output. For filesystem type analyzers, the contents of the folder ``/analysis/output/output/``
will be saved. For JSON type analyzers, the contents of ``/analysis/output/output.json`` will be
saved.

Entry Point Behavior
--------------------

Analyzers may specify any entry point (default Docker CMD) they wish. By default, the r2c init
template sets this to ``/analyzer/analyze.sh``. However, this command could instead be a ``java
-jar`` command, a python program, or any other valid command. The only expectation r2c has of this
command is that if it exits **with a non-zero return code**, the analysis is considered to have
failed and output will not be saved.

User Permissions
----------------

It is considered bad practice to run inside of Docker containers as the root user. It is also
considered bad practice when running locally to develop r2c analyzers as root. This leads to one
complication: files created in the container as the user inside the container may have different
user permissions that prevent the local user running r2c from cleaning up the temporary files.

To avoid this, the default r2c template takes arguments that create a user with the same ID as the
current user on the host machine. This happens once at build time, and does not affect the ability
of the analyzer to run at scale on r2c infrastructure, but avoids files being created that require
extra permission to clean up when running locally. If you need to, you may have analysis inside the
Docker container run as any user you like, though it is often not good practice to do so.
