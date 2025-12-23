Quick Start
===========

This guide will help you get started with pytoolkit.

Configuration and Logging
--------------------------

Load configuration from multiple sources and set up logging:

.. code-block:: python

   from pytoolkit import ConfigLoader, get_logger
   
   # Create a logger
   logger = get_logger("myapp", level=logging.INFO)
   
   # Load configuration from .env and config.json
   config = ConfigLoader(
       env_file=".env",
       json_file="config.json",
       prefix="APP_"
   )
   
   # Get configuration values
   api_key = config.require("API_KEY")
   timeout = config.get_int("TIMEOUT", default=30)
   debug = config.get_bool("DEBUG", default=False)
   
   logger.info("Configuration loaded successfully")

HTTP Client
-----------

Make HTTP requests with automatic retries:

.. code-block:: python

   from pytoolkit import HttpClient
   
   # Create a client
   with HttpClient(
       base_url="https://api.example.com",
       timeout=10.0,
       max_retries=3,
       default_headers={"Authorization": "Bearer token"}
   ) as client:
       # Make requests
       response = client.get("/users")
       users = client.json(response)
       
       # POST data
       new_user = {"name": "Alice", "email": "alice@example.com"}
       response = client.post("/users", json=new_user)

Async HTTP Client
~~~~~~~~~~~~~~~~~

For async operations:

.. code-block:: python

   from pytoolkit import AsyncHttpClient
   import asyncio
   
   async def fetch_data():
       async with AsyncHttpClient(base_url="https://api.example.com") as client:
           response = await client.get("/data")
           return await client.json(response)
   
   data = asyncio.run(fetch_data())

Caching
-------

Cache expensive function results:

.. code-block:: python

   from pytoolkit import cached
   import time
   
   @cached(ttl=300)  # Cache for 5 minutes
   def expensive_computation(x, y):
       time.sleep(2)  # Simulate expensive operation
       return x + y
   
   # First call takes 2 seconds
   result = expensive_computation(10, 20)
   
   # Second call returns immediately from cache
   result = expensive_computation(10, 20)

Retry Logic
-----------

Automatically retry failed operations:

.. code-block:: python

   from pytoolkit.retry import retry
   import requests
   
   @retry(max_attempts=3, initial_delay=1.0, backoff_factor=2.0)
   def fetch_url(url):
       response = requests.get(url)
       response.raise_for_status()
       return response.json()
   
   # Will retry up to 3 times with exponential backoff
   data = fetch_url("https://api.example.com/data")

Validators
----------

Validate common data types:

.. code-block:: python

   from pytoolkit.validators import (
       is_email,
       is_url,
       is_uuid,
       is_ipv4,
       min_length,
   )
   
   # Email validation
   if is_email("user@example.com", strict=True):
       print("Valid email")
   
   # URL validation
   if is_url("https://example.com", require_tld=True):
       print("Valid URL")
   
   # UUID validation
   if is_uuid("550e8400-e29b-41d4-a716-446655440000"):
       print("Valid UUID")

String Tools
------------

Common string operations:

.. code-block:: python

   from pytoolkit.string_tools import (
       slugify,
       to_snake_case,
       to_camel_case,
       random_string,
       truncate,
   )
   
   # Create URL-friendly slugs
   slug = slugify("Hello World!")  # "hello-world"
   
   # Case conversion
   snake = to_snake_case("MyClassName")  # "my_class_name"
   camel = to_camel_case("my_function_name")  # "MyFunctionName"
   
   # Random strings
   token = random_string(length=32)
   
   # Truncate with ellipsis
   short = truncate("Long text here", max_length=10)  # "Long te..."

Timing Functions
----------------

Measure execution time:

.. code-block:: python

   from pytoolkit import time_function, Timer
   
   # As a decorator
   @time_function(label="slow_operation")
   def slow_operation():
       time.sleep(2)
       return "done"
   
   result = slow_operation()  # Logs: slow_operation took 2.0000 seconds
   
   # As a context manager
   with Timer("block_operation") as timer:
       time.sleep(1)
   
   print(f"Took {timer.duration:.2f} seconds")

Task Scheduler
--------------

Schedule recurring tasks:

.. code-block:: python

   from pytoolkit.task_scheduler import TaskScheduler
   
   def cleanup_task():
       print("Running cleanup...")
   
   def report_task():
       print("Generating report...")
   
   # Create scheduler
   scheduler = TaskScheduler(tick=1.0)
   
   # Add tasks
   scheduler.add_task("cleanup", interval=300, function=cleanup_task)
   scheduler.add_task("report", interval=3600, function=report_task)
   
   # Start scheduler
   scheduler.start()
   
   # ... your application runs ...
   
   # Stop scheduler when done
   scheduler.stop()

File Utilities
--------------

Safe file operations:

.. code-block:: python

   from pytoolkit.file_utils import (
       read_text,
       write_text,
       atomic_write,
       file_hash,
   )
   
   # Read and write text files
   content = read_text("input.txt")
   write_text("output.txt", content.upper())
   
   # Atomic write (safe for concurrent access)
   atomic_write("important.txt", "critical data")
   
   # Compute file hash
   hash_value = file_hash("document.pdf", algorithm="sha256")

Math Tools
----------

Numeric utilities:

.. code-block:: python

   from pytoolkit.math_tools import (
       moving_average,
       normalize,
       percentage_change,
       scale_value,
   )
   
   # Moving average
   data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
   smoothed = moving_average(data, window=3)
   
   # Normalize to 0-1 range
   normalized = normalize([10, 20, 30, 40, 50])
   
   # Calculate percentage change
   change = percentage_change(old=100, new=120)  # 20.0%
   
   # Scale value between ranges
   scaled = scale_value(5, old_min=0, old_max=10, new_min=0, new_max=100)

Next Steps
----------

* Read the :doc:`api/index` for detailed API documentation
* Check out the `examples <https://github.com/actobotics/pyToolkit/tree/main/examples>`_ directory
* Learn how to contribute in :doc:`contributing`

