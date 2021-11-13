# Control order of programs.

import os
import sys
import logging
from typing import List

from pywinauto.application import Application

logging.basicConfig(level=logging.INFO)

# https://pywinauto.readthedocs.io/en/latest/getting_started.html#getting-started-guide
BACKEND_TYPE = "uia"


def onStart() -> None:
    logging.info("Starting Startup Manager")
    notepadApp = Application(backend=BACKEND_TYPE).start("notepad.exe")



if __name__ == "__main__":
    onStart()
