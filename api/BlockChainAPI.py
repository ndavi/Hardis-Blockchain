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
        chain = ConfigLoader.getBlockChainName()
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
            "responsible person": owner,
            "action": "register"}, indent=4
        )

    def from_parameters_to_data_move(self, new_owner, new_business_unit, new_team, date):
        return json.dumps({
            "responsible person": new_owner,
            "business unit": new_business_unit,
            "team": new_team,
            "date of the change": date,
            "action": "move"}, indent=4
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
        data_to_print = []
        if results:
            for transaction in results:
                data = self.from_hexa_to_data(transaction['data'])
                data_json = json.loads(data)
                if data_json['action'] == "register":
                    data_to_print.append("Enregistrement ID : " + transaction['key'] +
                                         "\nMarque : " + data_json['brand'] +
                                         "\nNuméro de série : " + data_json['serial number'] +
                                         "\nDate d'achat : " + data_json['date of purchase'] +
                                         "\nBusiness unit : " + data_json['business unit'] +
                                         "\nEquipe : " + data_json['team'] +
                                         "\nResponsable : " + data_json['responsible person'] +
                                         "\n"
                                         )
                elif data_json['action'] == "move":
                    data_to_print.append("Déplacement ID : " + transaction['key'] +
                                         "\nDate du déplacement : " + data_json['date of the change'] +
                                         "\nNouvelle business unit : " + data_json['business unit'] +
                                         "\nNouvelle équipe : " + data_json['team'] +
                                         "\nNouveau responsable : " + data_json['responsible person'] +
                                         "\n"
                                         )
        else:
                data_to_print.append("Aucun résultat")
        return data_to_print

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

    def add_new_type(self, type_equip):
        self.api.create("stream", str(type_equip), True)
        self.api.subscribe(type_equip)

    # Queries

    def get_streams(self):
        results = []
        streams = self.api.liststreams()
        for stream in streams:
            if stream['name'] != 'root':
                if not stream['subscribed']:
                    self.api.subscribe(stream['name'])
                results.append(stream['name'])
        results.sort()
        return results

    def get_id_by_type(self, type_stream):
        ids = []
        transactions = []
        if type_stream:
            transactions = self.api.liststreamitems(type_stream, True, 100000)
        for tr in transactions:
            ids.append(tr['key'])
        ids = list(set(ids))
        self.clean_results(ids)
        ids.sort()
        return ids

    def get_all_ids(self):
        results = []
        streams = self.get_streams()
        for stream in streams:
            results.extend(self.get_id_by_type(stream))
        results = list(set(results))
        self.clean_results(results)
        results.sort()
        return results

    def get_all_brands(self):
        results = []
        streams = self.get_streams()
        for stream in streams:
            transactions = self.api.liststreamitems(stream, True, 100000)
            for tr in transactions:
                data_hexa = tr['data']
                data_txt = self.from_hexa_to_data(data_hexa)
                data_json = json.loads(data_txt)
                if "brand" in data_json:
                    results.append(data_json['brand'])
        results = list(set(results))
        self.clean_results(results)
        results.sort()
        return results

    def get_all_owners(self):
        results = []
        streams = self.get_streams()
        for stream in streams:
            transactions = self.api.liststreamitems(stream, True, 100000)
            for tr in transactions:
                data_hexa = tr['data']
                data_txt = self.from_hexa_to_data(data_hexa)
                data_json = json.loads(data_txt)
                if "responsible person" in data_json:
                    results.append(data_json['responsible person'])
        results = list(set(results))
        self.clean_results(results)
        results.sort()
        return results

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
