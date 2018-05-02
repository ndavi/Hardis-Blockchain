import os
from utils.configLoader import ConfigLoader
from Savoir import Savoir
import logging


class BlockChainAPI:
    def __init__(self):
        self.api = None
        self.loginInfo = {}
        self.loadRpcInfo()

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

    # Helpful fonctions

    def generateID(self,type):
        number = random.randint(0, 9999)
        return type + str(number)

    def fromParametersToData(self,brand, serial_number, purchase_date, business_unit, team, owner):
        return json.dumps({"brand": brand,
                           "serial number": serial_number,
                           "date of purchase": purchase_date,
                           "business unit": business_unit,
                           "team": team,
                           "responsible person": owner}, indent=4)

    def fromDataToHexa(self,data):
        data_hexa = hex(int.from_bytes(data.encode('utf-8'), 'big'))
        return data_hexa.replace('0x', "")

    def fromHexaToData(self,data_hexa):
        return codecs.decode(data_hexa, "hex").decode('utf-8')

    # Transactions

    def registerEquipment(self,type, brand, serial_number, purchase_date, business_unit, team, owner):
        id = generateID(type)
        data = fromParametersToData(brand, serial_number, purchase_date, business_unit, team, owner)
        data_hexa = fromDataToHexa(data)
        self.api.publish(type, id, data_hexa)
        return "New equipment properly registered"

    def moveEquipment(self,id, type, new_owner, new_business_unit, new_team, limit_date=None):
        data = fromParametersToData(new_owner, new_business_unit, new_team, limit_date)
        data_hexa = fromDataToHexa(data)
        self.api.publish(type, id, data_hexa)
        return "Moved equipment properly registered"

    # Queries

    def getByType(self,type):
        return self.api.liststreamitems(type, True, 100000)

    def getByBrand(self,type, brand):
        time_start = time.time()
        transactions = getByType(type)
        for tr in transactions:
            data_hexa = tr['data']
            data_txt = fromHexaToData(data_hexa)
            if "'brand':'" + brand + "'" in data_txt:
                print(data_txt)
                print("\n")
        time_end = time.time()
        print("Time spent : ")
        print(time_end - time_start)

    def getByOwner(self,type, owner):
        time_start = time.time()
        transactions = getByType(type)
        for tr in transactions:
            data_hexa = tr['data']
            data_txt = fromHexaToData(data_hexa)
            if "'proprio':'" + owner + "'" in data_txt:
                print(data_txt)
                print("\n")
        time_end = time.time()
        print("Time spent : ")
        print(time_end - time_start)

    def getByID(self,type, ID):
        return self.api.liststreamkeyitems(type, ID)
