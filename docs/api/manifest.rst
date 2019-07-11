..  _analyzer_json_manifest_spec:

``analyzer.json``
=================

The current version of the ``analyzer.json`` specification is ``1.0.0``. This version supports the
following fields in the top-level JSON object:

**analyzer_name** : *string*
   The name of the analyzer. All analyzers must belong to an org, e.g. ``r2c/transpiler``.

**author_name** : *string*
   The name of the author.

**author_email** : *string*
   A contact address for the author.

**version** : *string*
   The `semantic version string`_ representing the current analyzer version.

.. _semantic version string: https://semver.org/

.. note:: Analyzer versions are used for caching and result correctness. A given version of a
          deterministic analyzer run on the same input is expected to always produce the same
          result. One consequence of this is that you cannot overwrite or push multiple of the same
          version for a given analyzer.

**spec_version** : *string*
   The version of the analyzer specification this analyzer is compatible with. To match the version
   of the documented on this page, this should always be ``1.0.0``.
   
**dependencies** : *object*
   This is the main mechanism by which analyzers interact with other analysis components in the r2c
   system.  Each key in this object is the name of another analyzer, such as
   ``r2c/transpiler``. Each value is the version of the analyzer you want to use. An analyzer's
   output for the same input (commit or repository) appears under its name in ``/analysis/inputs`` when your
   container runs, e.g. ``/analysis/inputs/r2c/transpiler``. 

   Analyzers are expected to follow `semantic versioning <https://semver.org/>`. You can depend on a 
   specific version, or on ``*`` to keep up to date with the latest. To keep your analyzer deterministic, we 
   highly recommend depending on a specific version. Semver caret and tilde ranges like ``~1.1.0`` or ``^1.1.0``
   are allowed, but discouraged.

**type** : *"constant", "commit", or "git"*
   The type of input for which this analyzer produces a unique output.

   * A ``constant`` analyzer always produces the same output. This can be useful for the trained
     data for a machine learning based analysis, by having the analyzer depend on its trained
     weights separately from the actual analysis.
   * A ``commit`` analyzer produces output for a JavaScript project at a specific point in its
     history, a single instance of code. This analyzer should not expect to make use of any version
     control features. Most analyzers are ``commit`` anlayzers.
   * A ``git`` analyzer understands the evolution and history of a repository. It produces unique
     outputs for an entire commit graph or bare git checkout. These analyzers can directly compare
     trends in a project.

**output** : *"json", "filesystem", or "both"*
   The type of output this analyzer produces.

   * ``json`` output is the most common output format. For the structure of the resulting JSON, see
     :doc:`output`.
   * ``filesystem`` output allows the analyzer to output an arbitrary directory and file
     structure. Hard links are not supported. These analyzers may do such things as transpile code,
     install dependencies, or produce binary or other data from an analysis that would not be
     serializable as JSON. They lose the benefit of parts of the r2c toolchain that understand the
     JSON format, so most analysis should eventually end up as JSON.
   * The ``both`` value indicates that both ``json`` and ``filesystem`` output appear together. This
     is useful for describing properties of the filesystem output to query the results.

**deterministic** : *boolean*
   The current version of the r2c platform does not support non-deterministic analyzers. However,
   this feature is a part of the analyzer specifciation version ``1.0.0`` and will be implemneted
   soon.

