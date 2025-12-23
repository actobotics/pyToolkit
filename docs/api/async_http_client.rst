Async HTTP Client
=================

.. automodule:: pytoolkit.async_http_client
   :members:
   :undoc-members:
   :show-inheritance:

Example Usage
-------------

.. code-block:: python

   import asyncio
   from pytoolkit.async_http_client import AsyncHttpClient
   
   async def fetch_users():
       async with AsyncHttpClient(
           base_url="https://api.example.com",
           max_retries=3
       ) as client:
           response = await client.get("/users")
           return await client.json(response)
   
   users = asyncio.run(fetch_users())

Note: Requires aiohttp. Install with: ``pip install pytoolkit[async]``

