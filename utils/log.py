import logging
import os


def setup_custom_logger(name):
    formatter = logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(module)s - %(message)s')

    console = logging.StreamHandler()
    console.setFormatter(formatter)

    os.makedirs("log", exist_ok=True)

    debugLog = logging.FileHandler("log/debug.log")
    debugLog.setLevel(logging.DEBUG)
    debugLog.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    logger.addHandler(console)
    logger.addHandler(debugLog)
    return logger
