``output.json``
===============

The JSON results produced by your analysis must conform to the ``output.json`` specification. As of ``1.0.0``, there are two top-level fields: ``results`` (required) and ``errors`` (optional):

.. code-block:: json

    {
        "results": [],
        "errors": []
    }

results
-----------------
The ``results`` key is a required top-level field containing an array of 0 or more ``result`` objects that specify the type of result and its location (if applicable).

A sample results response from our whitepace finding analyzer in :ref:`running` is:

    .. code-block:: json

        {
            "results":[
                {
                    "check_id":"whitespace",
                    "path":"./perf/O(n).js",
                    "extra":{
                        "whitespace":77,
                        "total":241
                    }
                }
            ]
        }

Each result object supports the following fields:

+----------+---------+--------------------------------------------------------------------+----------+
| Field    | Type    | Description                                                        | Required |
+==========+=========+====================================================================+==========+
| check_id | string  | The snake_case identifier for the check (e.g "whitespace")         |     Y    |
+----------+---------+--------------------------------------------------------------------+----------+
| path     | string  | The slash delineated path and filename where the result is located |     N    |
+----------+---------+--------------------------------------------------------------------+----------+
| start    | point   | The line and column the finding starts on. See point_ for details  |     N    |
+----------+---------+--------------------------------------------------------------------+----------+
| end      | point   | The line and column the finding ends on. See point_ for details    |     N    |
+----------+---------+--------------------------------------------------------------------+----------+
| extra    | {}      | A freeform catch-all object for extra data                         |     N    |
+----------+---------+--------------------------------------------------------------------+----------+

Each point object supports the following fields:

.. _point:

+-------+---------+-----------------------------------+----------+
| Field | Type    | Description                       | Required |
+=======+=========+===================================+==========+
| line  | integer | The line number of the result     |     Y    |
+-------+---------+-----------------------------------+----------+
| col   | integer | The column position of the result |     N    |
+-------+---------+-----------------------------------+----------+

errors
---------------
Optional field containing an array of 0 or more ``error`` objects with error messages and related data.

A sample error response looks like:

    .. code-block:: json

        {
            "results":[],
            "errors": [
                {
                    "message": "Cyclomatic complexity limit reached.",
                    "data": {
                        "path": "./foobar.js"
                    }
                }
            ]
        }

Each error object supports the following fields:

+---------+--------+--------------------------------------------+----------+
| Field   | Type   | Description                                | Required |
+=========+========+============================================+==========+
| message | string | A string describing the error              |     Y    |
+---------+--------+--------------------------------------------+----------+
| data    | {}     | A freeform catch-all object for error data |     N    |
+---------+--------+--------------------------------------------+----------+
