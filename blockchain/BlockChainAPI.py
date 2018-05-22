import os
import platform
from utils.configLoader import ConfigLoader
from Savoir import Savoir
import logging
import random
import json
import codecs
import time


class BlockChainAPI:
    def __init__(self):
        self.api = None
        self.loginInfo = {}
        self.loadRpcInfo()

    def loadRpcInfo(self):
        logger = logging.getLogger('root')
        logger.info("Récupération des informations de connexion")
        chain = ConfigLoader.getChainName()
        if platform.system() == "Windows":
            drive = os.getenv("SystemDrive")
            user = os.getlogin()
            config_path = drive + "\\Users\\" + user + "\AppData\Roaming\MultiChain\\" + chain + "\\multichain.conf"
            param_path = drive + "\\Users\\" + user + "\AppData\Roaming\MultiChain\\" + chain + "\\params.dat"
        else:
            home_user = os.path.expanduser('~')
            config_path = home_user + "/.multichain/" + chain + "/multichain.conf"
            param_path = home_user + "/.multichain/" + chain + "/params.dat"
        with open(config_path) as multichainconfig:
            for line in multichainconfig:
                name, var = line.partition("=")[::2]
                self.loginInfo[name.strip()] = var.strip()
        with open(param_path) as params:
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
        print("\n")

    # Helpful functions

    def generateID(self, type_stream):
        random_id = random.randint(0, 99999)
        return type_stream + str(random_id)

    def fromParametersToDataRegister(self, brand, serial_number, purchase_date, business_unit, team, owner):
        return json.dumps({
            "brand": brand,
            "serial number": serial_number,
            "date of purchase": purchase_date,
            "business unit": business_unit,
            "team": team,
            "responsible person": owner}, indent=4
        )

    def fromParametersToDataMove(self, new_owner, new_business_unit, new_team, date):
        return json.dumps({
            "owner": new_owner,
            "business unit": new_business_unit,
            "team": new_team,
            "date of the change": date}, indent=4
        )

    def fromDataToHexa(self, data):
        data_hexa = hex(int.from_bytes(data.encode('utf-8'), 'big'))
        return data_hexa.replace('0x', "")

    def fromHexaToData(self, data_hexa):
        return codecs.decode(data_hexa, "hex").decode('utf-8')

    def cleanResults(self, results):
        for element in results:
            if not element:
                results.remove(element)


    def printResults(self, results):
        print("\n")
        print()
        if results:
            for transaction in results:
                print("ID : " + transaction['key'])
                print("Data : " + self.fromHexaToData(transaction['data']))
        else:
            print("No result to print")

    # Transactions

    def registerEquipment(self, type_stream, brand, serial_number, purchase_date, business_unit, team, owner):
        id_equip = self.generateID(type_stream)
        data = self.fromParametersToDataRegister(brand, serial_number, purchase_date, business_unit, team, owner)
        data_hexa = self.fromDataToHexa(data)
        self.api.publish(type_stream, id_equip, data_hexa)
        print("New equipment properly registered with id " + str(id_equip))
        return id_equip

    def moveEquipment(self, id_equip, type_stream, new_owner, new_business_unit, new_team, date):
        data = self.fromParametersToDataMove(new_owner, new_business_unit, new_team, date)
        data_hexa = self.fromDataToHexa(data)
        print(data_hexa)
        print(type(data_hexa))
        self.api.publish(type_stream, id_equip, data_hexa)
        print("Equipment with id " + str(id_equip) + " properly moved")

    # Queries

    def getByType(self, type_stream):
        results = self.api.liststreamitems(type_stream, True, 100000)
        results_number = len(results)
        print(str(results_number)+" results found in stream " + str(type_stream))
        return results

    def getByBrand(self, type_stream, brand):
        results = []
        time_start = time.time()
        transactions = self.getByType(type_stream)
        for tr in transactions:
            data_hexa = tr['data']
            data_txt = self.fromHexaToData(data_hexa)
            if "'brand':'" + brand + "'" in data_txt:
                results.extend(tr)
        time_end = time.time()
        self.cleanResults(results)
        results_number = len(results)
        print(str(results_number) + " results found for brand  " + str(brand) + " in stream " + str(type_stream))
        print("Time spent : ")
        print(time_end - time_start)
        return results

    def getByTypeByOwner(self, type_stream, owner):
        results = []
        time_start = time.time()
        transactions = self.getByType(type_stream)
        for tr in transactions:
            data_hexa = tr['data']
            data_txt = self.fromHexaToData(data_hexa)
            if "\"responsible person\": \"" + owner + "\"" in data_txt:
                results.extend(tr)
        time_end = time.time()
        results_number = len(results)
        print(str(results_number) + " results found in stream " + str(type_stream) + " for user " + str(owner))
        print("Time spent : ")
        print(time_end - time_start)
        return results

    def getByOwner(self, owner):
        results = []
        streams = self.api.liststreams()
        for stream in streams:
            if stream['subscribed']:
                results.extend(self.getByTypeByOwner(stream['name'], owner))
        results_number = len(results)
        print(str(results_number) + " results found for user " + str(owner))
        return results

    def getByTypeByID(self, type_stream, id_equip):
        results = self.api.liststreamkeyitems(type_stream, id_equip)
        results_number = len(results)
        print(str(results_number) + " results found in stream " + str(type_stream) + " for ID " + str(id_equip))
        return results

    def getByID(self, id_equip):
        results = []
        streams = self.api.liststreams()
        for stream in streams:
            if stream['subscribed']:
                results.extend(self.getByTypeByID(stream['name'], id_equip))
        results_number = len(results)
        print(str(results_number) + " results found for ID " + str(id_equip))
        return results
