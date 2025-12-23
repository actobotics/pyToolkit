"""Example using the HttpClient."""

from pytoolkit.http_client import HttpClient
from pytoolkit.logger import configure_from_env

logger = configure_from_env()


def main() -> None:
    with HttpClient() as client:
        response = client.get("https://httpbin.org/json")
        data = client.json(response)
    logger.info("Received keys: %s", list(data.keys()))


if __name__ == "__main__":
    main()
