import hashlib
import json
import random
import os

from iota import Iota, ProposedTransaction, Address, TryteString, Tag, Transaction
from iota.crypto.addresses import AddressGenerator
from utils import configLoader


class GraphAPI:

    def __init__(self):
        self.api = None
        self.seed = None
        self.iota_node = None
        self.file_name = None
        self.raw_account_data = None
        self.settings = None
        self.address_data = None
        self.fal_balance = None
        self.transfers_data = None
        self.host = "https://walletservice.iota.community:443"
        #self.host = "https://field.carriota.com:443"
        self.load_config()

    def load_config(self):
        self.seed = "MXNORIXDL9FHQERMCURRETWCGOCJMOJFTLDWHEBJOFUQJALJMGCTVFTCTTAAKWVEKBIIAXUTQZ9FUGHXS"
        #self.seed = configLoader.getSeed()

        self.file_name = self.create_file_name()

        self.raw_account_data = self.read_account_data()
        self.settings = self.raw_account_data['account_data'][0]['settings']
        self.address_data = self.raw_account_data['account_data'][0]['address_data']
        self.address = str(self.address_data[0]['address']) + str(self.address_data[0]['checksum'])
        self.fal_balance = self.raw_account_data['account_data'][0]['fal_balance']
        self.transfers_data = self.raw_account_data['account_data'][0]['transfers_data']

        #self.iota_node = self.settings[0]['host']
        self.iota_node = "https://walletservice.iota.community:443"
        self.api = Iota(self.iota_node, self.seed)

    def create_seed_hash(self, seed):
        """ Returns a sha256 hash of the seed """
        s = hashlib.sha256(seed.encode('utf-8'))
        return s.hexdigest()

    def create_file_name(self):
        seed_hash = self.create_seed_hash(self.seed)
        file_name = seed_hash[:12]
        file_name += ".txt"
        return file_name

    def read_account_data(self):
        """ Will try to open the account file.
        In case the file doesn't exist it will create a new account file. """
        try:

            with open(self.file_name, 'r') as account_data:
                data = json.load(account_data)
                return data
        except:
            with open(self.file_name, 'w') as account_data:
                data = {}
                data['account_data'] = []
                data['account_data'].append({
                    'settings': [{'host': self.host, 'min_weight_magnitude': 14, 'units': "i"}],
                    'address_data': [{"address": "KGCKNRJDFDHBGKFMMEBFEXLIRUWGEDGZGMIHULJDQUGMJSXLXPECBQRO9ERGKDLDEXCVONWENYPKCCSJD", "checksum": "GUTBGOKBA"}],
                    'fal_balance': [{'f_index': 0, 'l_index': 0}],
                    'transfers_data': []
                })
                json.dump(data, account_data)
                print("Created new account file!")
                return data

    def print_results(self, results):
        """ Prints the given data """
        data = []
        # hash = str(txn.hash)
        # tag = str(txn.tag)
        # print("Type : "+tag.strip('9'))
        if results:
            for transaction in results:
                data.append(self.decode_message(str(transaction.signature_message_fragment)))
        else:
            data.append("No result to print")
        return data

    # def decode_message(self, message):
    #     values = "9ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    #     if len(message) % 2 != 0:
    #         return "Invalid data"
    #     output = ""
    #     for i in range(0, len(message), 2):
    #         first_value = message[i]
    #         second_value = message[i+1]
    #         decimal_value = values.index(first_value) + values.index(second_value)*27
    #         character = chr(decimal_value)
    #         output = output + character
    #     return output

    def decode_message(self, message):
        """ Decode trytes message in unicode string """
        try:
            msg = TryteString(message).encode('utf-8')
            msg = msg.decode('utf-8')
            msg_string = str(msg)
            msg_string = msg_string[:len(msg_string) - 1]
            nice_string = msg_string.replace('\x00', '')
            return nice_string
        except UnicodeDecodeError:
            print("Invalid data")


    def generate_id(self, type_stream):
        random_id = random.randint(0, 99999)
        return type_stream + str(random_id)

    def from_parameters_to_data_register(self, id_equip, brand, serial_number, purchase_date, business_unit, team, owner):
        return json.dumps({
            "id": id_equip,
            "brand": brand,
            "serial number": serial_number,
            "date of purchase": purchase_date,
            "business unit": business_unit,
            "team": team,
            "responsible person": owner}, indent=4)

    def from_parameters_to_data_move(self, id_equip, new_owner, new_business_unit, new_team, date):
        return json.dumps({
            "id": id_equip,
            "owner": new_owner,
            "business unit": new_business_unit,
            "team": new_team,
            "date of the change": date}, indent=4
        )

    def register_equipment(self, type_equip, brand, serial_number, purchase_date, business_unit, team, owner):
        """ Gets register transaction's information from the user """
        id_equip = self.generate_id(type_equip)
        type_equip = type_equip.upper()
        type_equip = bytes(type_equip.encode('utf-8'))
        message = self.from_parameters_to_data_register(id_equip, brand, serial_number, purchase_date, business_unit, team,
                                                owner)
        self.register_transaction(type_equip, message)

    def move_equipment(self, id_equip, type_equip, new_owner, new_business_unit, new_team, date):
        """ Gets move transaction's information from the user """
        type_equip = type_equip.upper()
        type_equip = bytes(type_equip.encode('utf-8'))
        message = self.from_parameters_to_data_move(id_equip, new_owner, new_business_unit, new_team, date)
        self.register_transaction(type_equip, message)

    def register_transaction(self, type_equip, user_message):
        """ Prepares the transaction to be sent and uses IOTA API to send it into the public Tangle """
        print("Sending transfer, this can take a while...")
        transfer_value = 0
        recipient_address = "KGCKNRJDFDHBGKFMMEBFEXLIRUWGEDGZGMIHULJDQUGMJSXLXPECBQRO9ERGKDLDEXCVONWENYPKCCSJDGUTBGOKBA"
        recipient_address_bytes = bytes(recipient_address.encode('utf-8'))
        #deposit_address = self.get_deposit_address()
        bundle = []
        txn = \
            ProposedTransaction(
                address=Address(recipient_address_bytes),
                message=TryteString.from_string(user_message),
                tag=Tag(type_equip),
                value=transfer_value,
            )
        bundle.append(txn)
        deposit_address = str(recipient_address)
        self.api.send_transfer(
            depth=7,
            transfers=bundle,
            change_address=deposit_address,
            #min_weight_magnitude=18,
        )

    # ---------------------------------------- Queries ------------------------------------

    def get_transactions_by_type(self, type_equipment):
        """ Returns transactions with wanted type as a tag """
        results = []

        address_as_bytes = [bytes(self.address.encode('utf-8'))]
        raw_transfers = self.api.find_transactions(addresses=address_as_bytes)
        transactions_to_check = raw_transfers["hashes"]
        for txn_hash in transactions_to_check:
            txn_hash_as_bytes = bytes(txn_hash)
            gt_result = self.api.get_trytes([txn_hash_as_bytes])
            trytes = str(gt_result['trytes'][0])
            txn = Transaction.from_tryte_string(trytes)
            tag = str(txn.tag)
            tag = tag.strip('9')
            if type_equipment.upper() in tag:
                results.append(txn)
        return results

    def get_transactions_by_brand(self, brand):
        """ Returns transactions with wanted brand in message """
        results = []
        address_as_bytes = [bytes(self.address.encode('utf-8'))]
        raw_transfers = self.api.find_transactions(addresses=address_as_bytes)
        transactions_to_check = raw_transfers["hashes"]
        for txn_hash in transactions_to_check:
            txn_hash_as_bytes = bytes(txn_hash)
            gt_result = self.api.get_trytes([txn_hash_as_bytes])
            trytes = str(gt_result['trytes'][0])
            txn = Transaction.from_tryte_string(trytes)
            message = self.decode_message(str(txn.signature_message_fragment))
            if "\"brand\": \"" + brand + "\"" in message:
                results.append(txn)
        return results

    def get_transactions_by_owner(self, owner):
        """ Returns transactions with wanted owner in message """
        results = []
        address_as_bytes = [bytes(self.address.encode('utf-8'))]
        raw_transfers = self.api.find_transactions(addresses=address_as_bytes)
        transactions_to_check = raw_transfers["hashes"]
        for txn_hash in transactions_to_check:
            txn_hash_as_bytes = bytes(txn_hash)
            gt_result = self.api.get_trytes([txn_hash_as_bytes])
            trytes = str(gt_result['trytes'][0])
            txn = Transaction.from_tryte_string(trytes)
            message = self.decode_message(str(txn.signature_message_fragment))
            if "\"responsible person\": \"" + owner + "\"" in message:
                results.append(txn)
        return results

    def get_transactions_by_id(self, id_equip):
        """ Returns transactions with wanted id in message """
        results = []
        address_as_bytes = [bytes(self.address.encode('utf-8'))]
        raw_transfers = self.api.find_transactions(addresses=address_as_bytes)
        transactions_to_check = raw_transfers["hashes"]
        for txn_hash in transactions_to_check:
            txn_hash_as_bytes = bytes(txn_hash)
            gt_result = self.api.get_trytes([txn_hash_as_bytes])
            trytes = str(gt_result['trytes'][0])
            txn = Transaction.from_tryte_string(trytes)
            message = self.decode_message(str(txn.signature_message_fragment))
            if "\"id\": \"" + id_equip + "\"" in message:
                results.append(txn)
        return results