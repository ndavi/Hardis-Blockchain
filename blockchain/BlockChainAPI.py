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

    def from_parameters_to_data_register(self, brand, serial_number, purchase_date, business_unit, team, owner):
        return json.dumps({
            "brand": brand,
            "serial number": serial_number,
            "date of purchase": purchase_date,
            "business unit": business_unit,
            "team": team,
            "responsible person": owner}, indent=4
        )

    def from_parameters_to_data_move(self, new_owner, new_business_unit, new_team, date):
        return json.dumps({
            "responsible person": new_owner,
            "business unit": new_business_unit,
            "team": new_team,
            "date of the change": date}, indent=4
        )

    def from_data_to_hexa(self, data):
        data_hexa = hex(int.from_bytes(data.encode('utf-8'), 'big'))
        return data_hexa.replace('0x', "")

    def from_hexa_to_data(self, data_hexa):
        return codecs.decode(data_hexa, "hex").decode('utf-8')

    def clean_results(self, results):
        for element in results:
            if not element:
                results.remove(element)

    def print_results(self, results):
        data = []
        if results:
            for transaction in results:
                data.append("ID : " + transaction['key'] +
                            "\nData : " + self.from_hexa_to_data(transaction['data']))
        else:
            data.append("No result found")
        return data

    # Transactions

    def register_equipment(self, type_stream, id_equip, brand, serial_number, purchase_date, business_unit, team, owner):
        data = self.from_parameters_to_data_register(brand, serial_number, purchase_date, business_unit, team, owner)
        data_hexa = self.from_data_to_hexa(data)
        try:
            self.api.publish(type_stream, id_equip, data_hexa)
            print("New equipment properly registered with id " + str(id_equip))
        except:
            print("Error : something occurred. Are you sure you subscribed the right stream ?")
        return id_equip

    def move_equipment(self, id_equip, type_stream, new_owner, new_business_unit, new_team, date):
        data = self.from_parameters_to_data_move(new_owner, new_business_unit, new_team, date)
        data_hexa = self.from_data_to_hexa(data)
        try:
            self.api.publish(type_stream, id_equip, data_hexa)
            print("Equipment with id " + str(id_equip) + " properly moved")
        except:
            print("Error : something occurred. Are you sure you subscribed the right stream ?")

    # Queries

    def get_transactions_by_type(self, type_stream):
        results = []
        streams = self.api.liststreams()
        for stream in streams:
            if stream['name'] == type_stream and stream['subscribed']:
                results = self.api.liststreamitems(type_stream, True, 100000)
        results_number = len(results)
        print(str(results_number)+" results found in stream " + str(type_stream))
        return results

    def get_transactions_by_type_by_brand(self, type_stream, brand):
        results = []
        time_start = time.time()
        transactions = self.get_transactions_by_type(type_stream)
        if len(transactions) == 0:
            return results
        for tr in transactions:
            data_hexa = tr['data']
            data_txt = self.from_hexa_to_data(data_hexa)
            if "\"brand\": \"" + brand + "\"" in data_txt:
                results.append(tr)
        time_end = time.time()
        self.clean_results(results)
        results_number = len(results)
        print(str(results_number) + " results found for brand " + str(brand) + " in stream " + str(type_stream))
        print("Time spent : ")
        print(time_end - time_start)
        return results

    def get_transactions_by_brand(self, brand):
        results = []
        streams = self.api.liststreams()
        for stream in streams:
            if stream['subscribed']:
                results.extend(self.get_transactions_by_type_by_brand(stream['name'], brand))
        results_number = len(results)
        print(str(results_number) + " results found for brand " + str(brand))
        return results

    def get_transactions_by_type_by_owner(self, type_stream, owner):
        results = []
        time_start = time.time()
        transactions = self.get_transactions_by_type(type_stream)
        for tr in transactions:
            data_hexa = tr['data']
            data_txt = self.from_hexa_to_data(data_hexa)
            if "\"responsible person\": \"" + owner + "\"" in data_txt:
                results.append(tr)
        time_end = time.time()
        results_number = len(results)
        print(str(results_number) + " results found in stream " + str(type_stream) + " for user " + str(owner))
        print("Time spent : ")
        print(time_end - time_start)
        return results

    def get_transactions_by_owner(self, owner):
        results = []
        streams = self.api.liststreams()
        for stream in streams:
            if stream['subscribed']:
                results.extend(self.get_transactions_by_type_by_owner(stream['name'], owner))
        results_number = len(results)
        print(str(results_number) + " results found for user " + str(owner))
        return results

    def get_transactions_by_type_by_id(self, type_stream, id_equip):
        results = self.api.liststreamkeyitems(type_stream, id_equip)
        results_number = len(results)
        print(str(results_number) + " results found in stream " + str(type_stream) + " for ID " + str(id_equip))
        return results

    def get_transactions_by_id(self, id_equip):
        results = []
        streams = self.api.liststreams()
        for stream in streams:
            if stream['subscribed']:
                results.extend(self.get_transactions_by_type_by_id(stream['name'], id_equip))
        results_number = len(results)
        print(str(results_number) + " results found for ID " + str(id_equip))
        return results
