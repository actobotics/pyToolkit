"""Basic usage example that combines multiple helpers."""

from pytoolkit.logger import configure_from_env
from pytoolkit.timer import time_function
from pytoolkit.string_tools import slugify
from pytoolkit.math_tools import moving_average


logger = configure_from_env()


@time_function(logger=logger)
def main() -> None:
    text = "Hello World"
    slug = slugify(text)
    logger.info("Slug: %s", slug)

    values = [1, 2, 3, 4, 5]
    ma = moving_average(values, window=3)
    logger.info("Moving average: %s", ma)


if __name__ == "__main__":
    main()
