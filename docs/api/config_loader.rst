Configuration Loader
====================

.. automodule:: pytoolkit.config_loader
   :members:
   :undoc-members:
   :show-inheritance:

Example Usage
-------------

.. code-block:: python

   from pytoolkit.config_loader import ConfigLoader
   
   # Load from multiple sources
   config = ConfigLoader(
       env_file=".env",
       json_file="config.json",
       yaml_file="config.yaml",
       prefix="APP_"
   )
   
   # Get values with type conversion
   api_key = config.require("API_KEY")
   port = config.get_int("PORT", default=8000)
   debug = config.get_bool("DEBUG", default=False)
   
   # Get all config as dict
   all_config = config.as_dict()

