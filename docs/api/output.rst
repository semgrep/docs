``output.json``
===============

The current version of the ``output.json`` specification is ``1.0.0``. This version supports the following fields in the top-level JSON object:

**results**: *[result]*
    Required field with an array of 0 or more result objects.

**errors**: *[error]*
    Optional field with an array of 0 or more error objects.

field, type, description, required

+-------+------+-------------+----------+
| field | type | description | required |
+=======+======+=============+==========+
| hello | test | test        | final    |
+-------+------+-------------+----------+

sample output

For analyzer's with json output.
results, what are they? when would you use or output this?


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
