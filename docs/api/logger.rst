Logger
======

.. automodule:: pytoolkit.logger
   :members:
   :undoc-members:
   :show-inheritance:

Example Usage
-------------

.. code-block:: python

   from pytoolkit.logger import get_logger, configure_from_env
   import logging
   
   # Basic logger
   logger = get_logger("myapp")
   logger.info("Application started")
   
   # Logger with file output
   logger = get_logger(
       "myapp",
       level=logging.DEBUG,
       to_file="app.log"
   )
   
   # Configure from environment
   import os
   os.environ["LOG_LEVEL"] = "DEBUG"
   logger = configure_from_env()

