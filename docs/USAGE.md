# Usage guide

This document gives a quick overview of how to combine several helpers.

## Basic configuration and logging

```python
from pytoolkit.config_loader import ConfigLoader
from pytoolkit.logger import configure_from_env
from pytoolkit.env import get_environment

logger = configure_from_env()
env = get_environment()

config = ConfigLoader(env_file=".env", json_file="config.json", prefix="APP_")

logger.info("Environment: %s", env.name)
logger.info("Loaded config keys: %s", list(config.as_dict().keys()))
```

## HTTP client with retries and timing

```python
from pytoolkit.http_client import HttpClient
from pytoolkit.retry import retry
from pytoolkit.timer import time_function
from pytoolkit.logger import configure_from_env

logger = configure_from_env()

@retry(max_attempts=3)
@time_function(logger=logger)
def fetch_data():
    with HttpClient(base_url="https://httpbin.org") as client:
        response = client.get("/json")
        return client.json(response)
```
