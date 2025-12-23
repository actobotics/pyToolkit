Installation
============

Basic Installation
------------------

Install pytoolkit using pip:

.. code-block:: bash

   pip install pytoolkit

From Source
-----------

To install from source:

.. code-block:: bash

   git clone https://github.com/actobotics/pyToolkit.git
   cd pyToolkit
   pip install -e .

Optional Dependencies
---------------------

pytoolkit has several optional dependency groups:

Development Dependencies
~~~~~~~~~~~~~~~~~~~~~~~~

For development, testing, and linting:

.. code-block:: bash

   pip install pytoolkit[dev]

This includes:

* pytest and pytest-cov for testing
* black and ruff for code formatting
* mypy for type checking
* pre-commit for git hooks

Async Support
~~~~~~~~~~~~~

For async HTTP client functionality:

.. code-block:: bash

   pip install pytoolkit[async]

This includes:

* aiohttp for async HTTP requests
* aiofiles for async file operations

Documentation
~~~~~~~~~~~~~

To build documentation locally:

.. code-block:: bash

   pip install pytoolkit[docs]

This includes:

* sphinx and sphinx-rtd-theme
* sphinx-autodoc-typehints

All Optional Dependencies
~~~~~~~~~~~~~~~~~~~~~~~~~~

To install everything:

.. code-block:: bash

   pip install pytoolkit[all]

Requirements
------------

* Python 3.9 or higher
* requests >= 2.31.0
* python-dotenv >= 1.0.0
* PyYAML >= 6.0.0

Platform Support
----------------

pytoolkit is tested on:

* Linux (Ubuntu)
* macOS
* Windows

All major Python versions (3.9, 3.10, 3.11, 3.12) are supported.

