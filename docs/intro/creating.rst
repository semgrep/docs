Creating an analyzer
====================

Log in
------

.. highlight:: text

Before you create analyzers, you'll want to be logged in to your organization on ``r2c``. In
addition to giving you access to your collaborators` published analyzers, this sets up several
defaults for creating and publishing analysis containers. If somebody in your organization has
already added your Github account to the group, then logging in is as simple as running::

  $ r2c login

and following the instructions. If you don't have a group name, :email:`contact us<mailto:collaborate@returntocorp.com>`! 
We're happy to support new projects on the ``r2c`` platform.

Initialize your project
-----------------------

Make sure you are in a directory where you want to create analyzers. Then run::

  $ r2c init

The prompt will walk you through setting several options. For this tutorial, we're going to create a
simple analyzer that reports whitespace ratios in files; let's call it ``minifinder``, since it can
help us find minified files. If you have ``git`` configured, the author name and email properties
will be filled from your git configuration. For the rest of the values, let's accept the defaults by
pressing enter - we'll discuss what they mean later::

  $ r2c init
  Analyzer name [example]: minifinder
  Author name [Jav A. Script]:
  Author email [hello@example.com]:
  Run on (constant, commit, git) [commit]:
  Output type (filesystem, json, both) [json]:
  ✅ done. Your analyzer can be found in the minifinder directory
  
This created several files in the ``minifinder`` folder.

Important files
---------------

The ``Dockerfile`` is responsible for all of our container's setup and configuration. For some analyzers you
may need to edit it, installing dependencies to build and run your analysis. To learn more about Dockerfiles in general, see `Docker's tutorial <https://docs.docker.com/get-started/part2/#define-a-container-with-dockerfile>`_.

.. note:: Though it can be tempting to use images like ``node:latest``, most analyzers should be
          deterministic and therefore benefit from pinning their base image to a specific
          version. For more information, see :doc:`/best-practices`.

The ``analyzer.json`` file is the most important file in the analyzer. This defines how the analyzer
will interact with the ``r2c`` system and tools. Some important values in this file are:

``analyzer_name``
  This is our namespaced analyzer name. If you look inside the file, you can see that it has been
  combined with our organization name - this is because you can only develop analyzers within your
  organization. The only analyzers that exist outside of an organization are special analyzers built
  into the ``r2c`` platform.

``version``
  The version is very important. Versions should follow semantic versioning. ``r2c`` uses the
  analyzer name, version, and other parameters for caching: when running an analyzer at scale, all
  of these are used to determine if the analysis needs to be run again on a given input. The version
  is also used for other purposes, which we will cover later. All analyzers default to starting at
  version 0.0.1.

``dependencies``
  This is the main way our analysis can interact with other analysis components. This analyzer
  depends on the most basic component, ``source-code``. It specifies that it depends on any version
  of the ``source-code`` component by specifying ``"*"`` as the version. For more complicated
  analysis, we could depend on components such as ``r2c/transpiler`` with different options, or
  ``r2c/typeflow``, but those are beyond the scope of this tutorial.

For now, all these default values are good enough to get us started. We will spend most of our time
in the third file created in our project: ``analyze.sh``. This file is the entry point for our
analysis, and in it we can do whatever we'd like! Let's move on to :doc:`writing`.
