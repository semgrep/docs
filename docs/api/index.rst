API Reference
=============

The r2c analysis API has three main parts - the ``analyzer.json`` manifest file which specifies how the analyzer interacts with the rest of the r2c system, the Docker container in which the analyzer runs and how r2c expects programs in the container to behave, and the final output formats of the analysis that go on to be used by other parts of the r2c toolchain.

.. toctree::

   manifest
   schemas
   containers
   output
