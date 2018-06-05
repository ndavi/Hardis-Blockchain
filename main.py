import os
import argparse

import sys
from PyQt5.QtWidgets import QApplication

from ui.controllers.ChooseWindow import ChooseWindow
from utils import log
from utils.configLoader import ConfigLoader
from blockchain.BlockChainAPI import BlockChainAPI

logger = log.setup_custom_logger('root')


class MainDaemon:
    def __init__(self):
        logger.info("Démarrage du programme")
        logger.debug("Appel à multichaind")
        os.system("multichaind " + ConfigLoader.getBlockChainAddress())

class MainProgram:
    def __init__(self):
        api = BlockChainAPI()

def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)
    exit(-100)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Lancement du logiciel en mode daemon/gui')
    parser.add_argument('--daemon', help='Lancement du logiciel en mode daemon', action='store_true')
    args = parser.parse_args()

    if args.daemon:
        program = MainDaemon()
    else:
        sys.excepthook = except_hook
        app = QApplication(sys.argv)
        program = ChooseWindow()
        program.start(app)



