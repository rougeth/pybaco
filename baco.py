import logging

from pybaco import (
    base2,
    base8,
    base10,
    base16,
    base36,
    base62,
    Baco
)


logging.basicConfig(level=logging.WARNING)

logger = logging.getLogger(__name__)
logger.warning('Deprecated module name: use pybaco instead of baco')
