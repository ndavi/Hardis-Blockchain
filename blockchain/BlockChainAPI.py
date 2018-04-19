import os
from utils.configLoader import ConfigLoader
from Savoir import Savoir
import logging


class BlockChainAPI:
    def __init__(self):
        self.loginInfo = {}
        self.loadRpcInfo()
        self.api = None

    def loadRpcInfo(self):
        logger = logging.getLogger('root')
        logger.info("Récupération des informations de connexion")
        drive = os.getenv("SystemDrive")
        user = os.getlogin()
        chain = ConfigLoader.getChainName()
        with open(drive + "\\Users\\" + user + "\AppData\Roaming\MultiChain\\" + chain + "\\multichain.conf") as multichainconfig:
            for line in multichainconfig:
                name, var = line.partition("=")[::2]
                self.loginInfo[name.strip()] = var.strip()
        with open(drive + "\\Users\\" + user + "\AppData\Roaming\MultiChain\\" + chain + "\\params.dat") as params:
            for line in params:
                name, var = line.partition("=")[::2]
                if name.strip() == "default-rpc-port":
                    self.loginInfo["rpcport"] = var.strip()[:4]
        login = self.loginInfo["rpcuser"]
        password = self.loginInfo["rpcpassword"]
        port = self.loginInfo["rpcport"]
        logger.info("Affichage du noeud")
        self.api = Savoir(login,password,"localhost",port,chain)
        print(self.api.getinfo())