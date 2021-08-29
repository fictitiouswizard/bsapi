"""
Provides wrapper classes for interacting with the the BrowserStack REST api

Exports:
    Settings
    Api

Modules:
    app_automate.appium
"""
__version__ = "0.1.0"

from bsapi.settings import Settings
from bsapi.base import Api
from bsapi.config import BSAPIConf
