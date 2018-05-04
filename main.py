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

        # TEST 1
        # print("Register a new equipment :")
        # type_stream = input("Type (computer, table, microwave ...) : ")
        # brand = input("Brand : ")
        # serial_number = input("Serial number : ")
        # purchase_date = input("Date of purchase (dd-mm-yyyy format) : ")
        # business_unit = input("Business unit : ")
        # team = input("Team : ")
        # owner = input("Person in charge : ")
        # api.registerEquipment(type_stream, brand, serial_number, purchase_date, business_unit, team, owner)

        # TEST 2
        print("Look for an equipment by ID :")
        id_equip = input("ID : ")
        object = api.getByID(id_equip)
        api.printResults(object)

        # TEST 3
        # print("Move a registered equipement :")
        # id_equip = input("Equipment's ID : ")
        # type_stream = input("Type : ")
        # new_business_unit = input("New business unit : ")
        # new_team = input("New team : ")
        # new_owner = input("New person in charge : ")
        # date = input("Date of this change : ")
        # api.moveEquipment(id_equip, type_stream, new_owner, new_business_unit, new_team, date)

        # TEST 4
        # print("Look for equipments by type :")
        # type_stream = input("Type : ")
        # myobjects = api.getByType(type)
        # api.printResults(myobjects)



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Lancement du logiciel en mode daemon/gui')
    parser.add_argument('--daemon', help='Lancement du logiciel en mode daemon', action='store_true')
    args = parser.parse_args()
    if args.daemon:
        program = MainDaemon()
    else:
        program = MainProgram()

