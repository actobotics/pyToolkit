"""Example showing the ConfigLoader."""

from pytoolkit.config_loader import ConfigLoader
from pytoolkit.logger import configure_from_env

logger = configure_from_env()


def main() -> None:
    config = ConfigLoader(
        env_file=".env",
        json_file="config.json",
        yaml_file="config.yaml",
        toml_file="config.toml",
        prefix="APP_",
    )
    logger.info("Configuration values: %s", config.as_dict())
    logger.info("Example typed value: APP_PORT as int: %s", config.get_int("APP_PORT"))


if __name__ == "__main__":
    main()
