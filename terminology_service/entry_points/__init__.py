import logging

verbosity_mapping = {
    0: logging.WARNING,  # Default to WARNING if -v is not provided
    1: logging.INFO,
    2: logging.DEBUG
}
