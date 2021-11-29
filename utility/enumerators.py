"""
This module present Enumerators which will used by `tests` and `services` packages.
"""
from enum import Enum, auto


class STRATEGY(Enum):
    """
    Enumerator for finding element Strategy .
    """
    XPATH = auto()
    ID = auto()


class ENV(Enum):
    """
    Enumerator for Environment flavor.<br>All `services.*.pages*` will inject `url`
    and other parameter for each page based on this `ENV.*` value
    """
    DEV = (1, "DEV", 'dev_config' )
    STAGE = (2, "STAGE", 'stage_config')
    PROD = (3, "PROD", "prod_config")

    def __init__(self, id, title, config):
        self.id = id
        self.title = title
        self.config = config


class BROWSERS(Enum):
    """
    Enumerator for Browsers flavor.
    """
    CHROME = (1, "Chrome")
    FIREFOX = (1, "Firefox")

    def __init__(self, id, title):
        self.id = id
        self.title = title

