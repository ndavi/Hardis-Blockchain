from unittest import TestCase
from blockchain.BlockChainAPI import BlockChainAPI
import json


class TestBlockChainAPI(TestCase):

    def setUp(self):
        self.api = BlockChainAPI()

    def test_from_parameters_to_data_register(self):
        brand = "Ikea"
        serial_number = "3648"
        purchase_date = "20-04-2013"
        business_unit = "Business Apps"
        team = "Salesforce"
        owner = "person"
        expected_result = json.dumps({
            "brand": brand,
            "serial number": serial_number,
            "date of purchase": purchase_date,
            "business unit": business_unit,
            "team": team,
            "responsible person": owner}, indent=4
        )
        self.assertEqual(self.api.from_parameters_to_data_register(brand, serial_number, purchase_date, business_unit, team, owner), expected_result)

    def test_from_parameters_to_data_move(self):
        date = "20-04-2013"
        new_business_unit = "Business Apps"
        new_team = "Salesforce"
        new_owner = "person"
        expected_result = json.dumps({
            "owner": new_owner,
            "business unit": new_business_unit,
            "team": new_team,
            "date of the change": date}, indent=4
        )
        self.assertEqual(self.api.from_parameters_to_data_move(new_owner, new_business_unit, new_team, date), expected_result)

    def test_from_data_to_hexa(self):
        data = "hello world"
        data_hexa = "68656c6c6f20776f726c64"
        self.assertEqual(self.api.from_data_to_hexa(data), data_hexa)

    def test_from_hexa_to_data(self):
        data = "hello world"
        data_hexa = "68656c6c6f20776f726c64"
        self.assertEqual(self.api.from_hexa_to_data(data_hexa), data)

    def test_cleanResults(self):
        mylist = ["hey", 5, [], 2, []]
        self.api.clean_results(mylist)
        expected_list = ["hey", 5, 2]
        self.assertEqual(mylist, expected_list)

    def test_registerEquipment(self):
        type_stream = "test"
        brand = "Ikea"
        serial_number = "3648"
        purchase_date = "20-04-2013"
        business_unit = "Business Apps"
        team = "Salesforce"
        owner = ""
        id_equip = self.api.register_equipment(type_stream, brand, serial_number, purchase_date, business_unit, team, owner)

        data = self.api.from_parameters_to_data_register(brand, serial_number, purchase_date, business_unit, team, owner)
        data_hexa = self.api.from_data_to_hexa(data)
        results = self.api.get_transactions_by_type_by_id(type_stream, id_equip)
        found = False
        for result in results:
            if data_hexa in result['data']:
                found = True
        self.assertTrue(found)

    def test_moveEquipment(self):
        id_equip = "test450"
        type_stream = "test"
        date = "20-04-2013"
        new_business_unit = "Business Apps"
        new_team = "Salesforce"
        new_owner = "person"
        self.api.move_equipment(id_equip, type_stream, new_owner, new_business_unit, new_team, date)

        data = self.api.from_parameters_to_data_move(new_owner, new_business_unit, new_team, date)
        data_hexa = self.api.from_data_to_hexa(data)
        results = self.api.get_transactions_by_type_by_id(type_stream, id_equip)
        found = False
        for result in results:
            if data_hexa in result['data']:
                found = True
        self.assertTrue(found)

    def test_getByType(self):
        pass

    def test_getByBrand(self):
        pass

    def test_getByTypeByOwner(self):
        pass

    def test_getByOwner(self):
        pass

    def test_getByTypeByID(self):
        type_stream = "test"
        id_equip = "test38967"
        results = self.api.get_transactions_by_type_by_id(type_stream, id_equip)
        self.assertGreaterEqual(1, len(results))

    def test_getByID(self):
        pass

    def test_register(self):
        print("Register a new equipment :")
        type_stream = input("Type (computer, table, microwave ...) : ")
        brand = input("Brand : ")
        serial_number = input("Serial number : ")
        purchase_date = input("Date of purchase (dd-mm-yyyy format) : ")
        business_unit = input("Business unit : ")
        team = input("Team : ")
        owner = input("Person in charge : ")
        self.api.register_equipment(type_stream, brand, serial_number, purchase_date, business_unit, team, owner)

    def test_lookForEquipment(self):
        print("Look for an equipment by ID :")
        id_equip = input("ID : ")
        objects = self.api.get_transactions_by_id(id_equip)
        self.api.print_results(objects)

    def test_move(self):
        print("Move a registered equipement :")
        id_equip = input("Equipment's ID : ")
        type_stream = input("Type : ")
        new_business_unit = input("New business unit : ")
        new_team = input("New team : ")
        new_owner = input("New person in charge : ")
        date = input("Date of this change : ")
        self.api.move_equipment(id_equip, type_stream, new_owner, new_business_unit, new_team, date)

    def test_lookForType(self):
        print("Look for equipments by type :")
        type_stream = input("Type : ")
        myobjects = self.api.get_transactions_by_type(type_stream)
        self.api.print_results(myobjects)
