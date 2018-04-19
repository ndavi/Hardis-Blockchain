import os
import argparse
from utils import log
from utils.configLoader import ConfigLoader
from blockchain.BlockChainAPI import BlockChainAPI

logger = log.setup_custom_logger('root')


class MainDaemon:
    def __init__(self):
        logger.info("Démarrage du programme")
        logger.debug("Appel à multichaind")
        os.system("multichaind " + ConfigLoader.loadBlockChainAddress())

class MainProgram:
    def __init__(self):
        api = BlockChainAPI()





if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Lancement du logiciel en mode daemon/gui')
    parser.add_argument('--daemon', help='Lancement du logiciel en mode daemon', action='store_true')
    args = parser.parse_args()
    if args.daemon:
        program = MainDaemon()
    else:
        program = MainProgram()

