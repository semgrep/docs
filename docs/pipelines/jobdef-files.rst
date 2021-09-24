Job Definition Files
=========================

Often when repeatedly running an analyzer over different corpora, or when
iterating development on an analyzer, it can be useful to run essentially the same job but with some minor tweaks. Similarly, if your analyzer has parameters, you probably don't want to have to type out the parameters each time. This is where job definitions (also known as jobdefs) come in.


The Jobdef File Format
-----------------------

A jobdef is a YAML file that specifies the analyzer and the input set. For example,

.. literalinclude:: samples/jobdef.yaml
    :linenos:
    :language: yaml

The format is simple: we specify the analyzer's name and version using the
`analyzer` key, and similarly for the input set. All of these fields are required.

Running a job using a jobdef is exactly equivalent to running it via the
step-by-step web UI, and each job's results page has a 'download' button to
download its jobdef.


Specifying Parameters
-----------------------

Some analyzers can include parameters. Depending on the analyzer, you may not
have to include parameters; some analyzers will have some reasonable set of defaults. However, if you do want to include parameters in your jobdef, you can either use the multi-line YAML syntax for the parameters:

.. literalinclude:: samples/jobdef-with-yaml-parameters.yaml
    :linenos:
    :language: yaml

or the more JSON-like syntax:

.. literalinclude:: samples/jobdef-with-json-parameters.yaml
    :linenos:
    :language: yaml

Both are valid, and will be treated equivalently.
