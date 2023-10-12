"""Establish the logger functionality."""
import logging
import os

# Logger config parameters.
log_level = "DEBUG"
log_file_path = "/var/log"


def set_logger() -> logging.Logger:
    # Set the logger.
    logging.basicConfig(
        level=log_level,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    # Create the logger.
    logger = logging.getLogger(__name__)

    # Configure the logger console handler and set the level.
    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level)

    # Set the logger file path.
    does_path_exist = os.path.exists(log_file_path)
    if not does_path_exist:
        try:
            os.makedirs(log_file_path)
        except Exception as e:
            print(str(e))

    # Add the handler to the logger.
    file_handler = logging.FileHandler(f"{log_file_path}/logger.log")
    file_handler.setLevel(log_level)

    # Configure the logger as will be printed in the console & log file.
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    # Add log handlers.
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger


logger = set_logger()
