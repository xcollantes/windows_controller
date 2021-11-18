# Control order of programs.

import os
import sys
import time
import subprocess
import logging
from pywinauto import Desktop
from pywinauto.application import Application


logging.basicConfig(level=logging.DEBUG)
# Needed for elevated access.
os.environ.update({"__COMPAT_LAYER": "RUnAsInvoker"})

MINING_BATCH_PATH = (
    "C:\\Users\\colla\\Documents\\cryptomining\\trex\\xavier-eth.bat")


def startTrexMiner(pathExe: os.path) -> None:
    """Start Ethereum script.

    Args:
        pathExe: Full escaped path of script to run.
    """
    logging.info("Starting Trex Miner")


def isRunning(programPattern: str) -> bool:
    """Check if a given program is active.

    Args:
        programPattern: String of window title; may not be complete.
                        Ex: to find Spotify, "Spo" or "Spotif" will work.

    Returns:
        True if program is active, False otherwise.
    """
    logging.debug("Looking for program with pattern %s", programPattern)
    desktopApps = Desktop().windows()

    for program in desktopApps:
        if programPattern in program.window_text():
            logging.debug("%s running", program.window_text())
            return True
    logging.warn("None found with pattern: %s", programPattern)
    return False


def startMiningOperation() -> None:
    """Start up overclocking software to regulate GPU, start Ethereum script.
    """
    logging.info("Starting mining ops")
    if not isRunning("MSI A"):
        logging.info("MSI not running, starting up")
        msiClock = Application().start(
            "C:\\Program Files (x86)\\MSI Afterburner\\MSIAfterburner.exe")

    # time.sleep(5)  # Make sure MSI is running

    if not isRunning("xavier-eth") and isRunning("MSI A"):
        callFile = os.path.basename(MINING_BATCH_PATH)
        callDir = os.path.dirname(MINING_BATCH_PATH)
        logging.debug(f"Running command: `cd {callDir} && {callFile}`")

        os.system(f"""
            cd {callDir} && {callFile}
        """)
        logging.info(os.getcwd())


if __name__ == "__main__":
    startMiningOperation()
