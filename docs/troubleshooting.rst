Troubleshooting
===============


Upgrading to CLI version ``0.0.16``
---------------

For ``CLI`` versions ``>=0.0.12 <0.0.16``, the expected Dockefile for analysis projects was expected to look like.
.. literalinclude:: samples/minifinder_deprecated/Dockerfile
    :linenos:
    :language: dockerfile
    :emphasize-lines:

Starting with version ``0.0.16``, the Dockerfile for analyzers should looks like the following.
.. literalinclude:: samples/minifinder/Dockerfile
    :linenos:
    :language: dockerfile
    :emphasize-lines: