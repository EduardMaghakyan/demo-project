# use e.g. pinject lib for managing application dependencies
import logging
from functools import cache

_LOG = logging.getLogger(__name__)


def setup_logger():
    handler = logging.StreamHandler()
    formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(name)s | %(message)s")
    handler.setFormatter(formatter)
    level = logging.DEBUG

    logging.root.addHandler(handler)
    logging.root.setLevel(logging.INFO)

    logger = logging.getLogger("demo_setup")
    logger.setLevel(level)


@cache
class Application:
    def __init__(self) -> None:
        setup_logger()
        _LOG.debug("Application logger configured")
