import hashlib
import json

from iota import Iota, ProposedTransaction, Address, TryteString, Tag, Transaction
from utils.configLoader import ConfigLoader


class GraphAPI:

    def __init__(self):
        self.api = None
        self.seed = None
        self.address = None
        self.host = None
        self.load_config()

    def load_config(self):
        self.host = ConfigLoader.getIotaNode()
        self.seed = ConfigLoader.getIotaSeed()
        self.address = ConfigLoader.getIotaAddress()
        self.api = Iota(self.host, self.seed)

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

    def clean_results(self, results):
        for element in results:
            if not element:
                results.remove(element)

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
            "responsible person": new_owner,
            "business unit": new_business_unit,
            "team": new_team,
            "date of the change": date}, indent=4
        )

    def register_equipment(self, type_equip, ID, brand, serial_number, purchase_date, business_unit, team, owner):
        """ Gets register transaction's information from the user """
        type_equip = type_equip.upper()
        type_equip = bytes(type_equip.encode('utf-8'))
        message = self.from_parameters_to_data_register(ID, brand, serial_number, purchase_date, business_unit, team,
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
        recipient_address = self.address
        recipient_address_bytes = bytes(recipient_address.encode('utf-8'))
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

    def get_streams(self):
        types = []
        address_as_bytes = [bytes(self.address.encode('utf-8'))]
        raw_transactions = self.api.find_transactions(addresses=address_as_bytes)
        transactions_to_check = raw_transactions["hashes"]
        for txn_hash in transactions_to_check:
            txn_hash_as_bytes = bytes(txn_hash)
            gt_result = self.api.get_trytes([txn_hash_as_bytes])
            trytes = str(gt_result['trytes'][0])
            txn = Transaction.from_tryte_string(trytes)
            tag = str(txn.tag).replace("9","")
            types.append(tag.capitalize())
        types = list(set(types))
        return types

    def get_id_by_type(self, type_equip):
        ids = []
        transactions = []
        if type_equip:
            transactions = self.get_transactions_by_type(type_equip)
        for tr in transactions:
            message = self.decode_message(str(tr.signature_message_fragment))
            if not isinstance(message, dict):
                if isinstance(message, str):
                    if len(message) == 0:
                        continue
                    if message[0] != '{':
                        continue
                    message = json.loads(message)
            if "id" in message:
                ids.append(message['id'])
        ids = list(set(ids))
        self.clean_results(ids)
        return ids

    def get_all_ids(self):
        ids = []
        address_as_bytes = [bytes(self.address.encode('utf-8'))]
        raw_transactions = self.api.find_transactions(addresses=address_as_bytes)
        transactions_to_check = []
        if raw_transactions:
            transactions_to_check = raw_transactions["hashes"]
        for txn_hash in transactions_to_check:
            txn_hash_as_bytes = bytes(txn_hash)
            gt_result = self.api.get_trytes([txn_hash_as_bytes])
            trytes = str(gt_result['trytes'][0])
            txn = Transaction.from_tryte_string(trytes)
            message = self.decode_message(str(txn.signature_message_fragment))
            if not isinstance(message, dict):
                if isinstance(message, str):
                    if len(message) == 0:
                        continue
                    if message[0] != '{':
                        continue
                    message = json.loads(message)
            if "id" in message:
                ids.append(message['id'])
        ids = list(set(ids))
        self.clean_results(ids)
        return ids

    def get_all_brands(self):
        results = []
        address_as_bytes = [bytes(self.address.encode('utf-8'))]
        raw_transactions = self.api.find_transactions(addresses=address_as_bytes)
        transactions_to_check = []
        if raw_transactions:
            transactions_to_check = raw_transactions["hashes"]
        for txn_hash in transactions_to_check:
            txn_hash_as_bytes = bytes(txn_hash)
            gt_result = self.api.get_trytes([txn_hash_as_bytes])
            trytes = str(gt_result['trytes'][0])
            txn = Transaction.from_tryte_string(trytes)
            message = self.decode_message(str(txn.signature_message_fragment))
            if not isinstance(message, dict):
                if isinstance(message, str):
                    if len(message) == 0:
                        continue
                    if message[0] != '{':
                        continue
                    message = json.loads(message)
            if "brand" in message:
                results.append(message['brand'])
        results = list(set(results))
        self.clean_results(results)
        return results

    def get_all_owners(self):
        results = []
        address_as_bytes = [bytes(self.address.encode('utf-8'))]
        raw_transactions = self.api.find_transactions(addresses=address_as_bytes)
        transactions_to_check = raw_transactions["hashes"]
        for txn_hash in transactions_to_check:
            txn_hash_as_bytes = bytes(txn_hash)
            gt_result = self.api.get_trytes([txn_hash_as_bytes])
            trytes = str(gt_result['trytes'][0])
            txn = Transaction.from_tryte_string(trytes)
            message = self.decode_message(str(txn.signature_message_fragment))
            if not isinstance(message, dict):
                if isinstance(message, str):
                    if len(message) == 0:
                        continue
                    if message[0] != '{':
                        continue
                    message = json.loads(message)
            if "owner" in message:
                results.append(message['owner'])
        results = list(set(results))
        return results
