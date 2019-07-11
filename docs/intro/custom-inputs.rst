Custom Inputs
=============

As of r2c-cli version 0.0.20, you can upload your own input sets to r2c
infrastructure to run your analyzer at scale on repositories or packages
that you specified.

The command ``r2c upload-inputset <filename>`` can be use upload a file in the following format:

    .. code-block:: json
    
        {
            "name": "STRING",
            "version": "SEMVER_STRING",
            "description": "OPTIONAL_STRING",
            "readme": "OPTIONAL_MARKDOWN_README",
            "inputs": [INPUT, ...],
        }

``INPUT`` is an interface with multiple types; as an example:

.. literalinclude:: samples/custom-inputset.json
    :linenos:
    :language: json

For details on generating an input set that specifies packages, rather than git repositories, please contact r2c!
