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

A sample results field and entry from our whitepace finding analyzer in :ref:`running` is:

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

+----------+-------------+--------------------------------------------------------------------+----------+
| Field    | Type        | Description                                                        | Required |
+----------+-------------+--------------------------------------------------------------------+----------+
| check_id | ``string``  | The snake_case identifier for the check (e.g "whitespace")         |     Y    |
+----------+-------------+--------------------------------------------------------------------+----------+
| path     | ``string``  | The slash delineated path and filename where the result is located |     N    |
+----------+-------------+--------------------------------------------------------------------+----------+
| start    | ``point{}`` | The line and column the finding starts on. See point_ for details  |     N    |
+----------+-------------+--------------------------------------------------------------------+----------+
| end      | ``point{}`` | The line and column the finding ends on. See point_ for details    |     N    |
+----------+-------------+--------------------------------------------------------------------+----------+
| extra    | ``{}``      | A freeform catch-call object for extra data                        |     N    |
+----------+-------------+--------------------------------------------------------------------+----------+

errors: [error]
---------------
Optional field containing an array of 0 or more ``error`` objects with error messages and related data.

how to display? table with different sections? json blob with comments?

results (required)
    - array of result objects, can be empty array
    - result
        - check_id (required): string (conventions?)
        - start: point
        - end: point
        - path: string
        - extra: {} (conventions?)
    - point
        - line (required): integer
        - col: integer


errors (optional)
    - array of error objects
    - error
        - message (required): string
        - data: {}

.. code-block:: json

    {
        "results": [
            {"check_id": "hello_world"}
        ],
        "errors": []
    }
    [
