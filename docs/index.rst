pytoolkit Documentation
=======================

Welcome to pytoolkit's documentation!

**pytoolkit** is a collection of helper utilities for Python projects. It provides
small, composable building blocks instead of a heavy framework.

**GitHub Repository**: https://github.com/actobotics/pyToolkit

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   installation
   quickstart
   api/index
   contributing
   changelog

Features
--------

* **Configuration Management**: Load configs from JSON, YAML, TOML, and .env files
* **Logging**: Colored loggers with environment-based configuration
* **HTTP Client**: Sync and async HTTP clients with retry logic
* **Caching**: In-memory cache with TTL support
* **Retry Logic**: Decorator with exponential backoff
* **Validators**: Email, URL, UUID, IP address validation
* **String Tools**: Slugify, case conversion, random strings
* **Math Tools**: Moving average, normalization, scaling
* **Task Scheduler**: Simple in-process task scheduling
* **File Utilities**: Safe file operations with atomic writes
* **Crypto Utilities**: Hashing and secure token generation

Quick Example
-------------

.. code-block:: python

   from pytoolkit import ConfigLoader, get_logger, HttpClient
   
   # Configure logging
   logger = get_logger()
   
   # Load configuration
   config = ConfigLoader(env_file=".env", json_file="config.json")
   api_url = config.get("API_URL", "https://api.example.com")
   
   # Make HTTP request
   with HttpClient(base_url=api_url) as client:
       response = client.get("/users")
       data = client.json(response)
       logger.info("Fetched %d users", len(data))

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

