HTTP Client
===========

.. automodule:: pytoolkit.http_client
   :members:
   :undoc-members:
   :show-inheritance:

Example Usage
-------------

.. code-block:: python

   from pytoolkit.http_client import HttpClient
   
   # Basic usage
   with HttpClient(base_url="https://api.example.com") as client:
       response = client.get("/users")
       users = client.json(response)
   
   # With authentication and custom headers
   client = HttpClient(
       base_url="https://api.example.com",
       timeout=30.0,
       max_retries=3,
       default_headers={"User-Agent": "MyApp/1.0"},
       auth=("username", "password")
   )
   
   try:
       response = client.post("/data", json={"key": "value"})
       result = client.json(response)
   finally:
       client.close()

