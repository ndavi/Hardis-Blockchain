from unittest import TestCase
from api.GraphAPI import GraphAPI


class TestGraphAPI(TestCase):

    def setUp(self):
        self.api = GraphAPI()
        self.address = "KGCKNRJDFDHBGKFMMEBFEXLIRUWGEDGZGMIHULJDQUGMJSXLXPECBQRO9ERGKDLDEXCVONWENYPKCCSJDGUTBGOKBA"

    def test_decode_message(self):
        print(self.api.decode_message("VDKGARADYTHPJQEQW9CIIQYYQAW"))
        print(self.api.decode_message("ODJ9EAEAEAEAGAXCSCGADBEAGARCCDADDDIDHDTCFDZAVAWAGAQAJ9EAEAEAEAGAQCFDPCBDSCGADBEAGA9DTCBDCDJDCDGAQAJ9EAEAEAEAGAGDTCFDXCPC9DEABDIDADQCTCFDGADBEAGAYACBYA9BWAXAGAQAJ9EAEAEAEAGASCPCHDTCEACDUCEADDIDFDRCWCPCGDTCGADBEAGAWAZARAUAWARAWAUAVABBGAQAJ9EAEAEAEAGAQCIDGDXCBDTCGDGDEAIDBDXCHDGADBEAGALBKBNBGAQAJ9EAEAEAEAGAHDTCPCADGADBEAGANBXCVCXCHDPC9DGAQAJ9EAEAEAEAGAFDTCGDDDCDBDGDXCQC9DTCEADDTCFDGDCDBDGADBEAGAYBACOBHCGAJ9QD"))

    def test_register_equipment(self):
        print("Register a new equipment :")
        type_equip = input("Type (computer, table, microwave ...) : ")
        brand = input("Brand : ")
        serial_number = input("Serial number : ")
        purchase_date = input("Date of purchase (dd-mm-yyyy format) : ")
        business_unit = input("Business unit : ")
        team = input("Team : ")
        owner = input("Person in charge : ")
        self.api.register_equipment(type_equip, brand, serial_number, purchase_date, business_unit, team, owner)

    def test_get_transactions_by_owner(self):
        results = self.api.get_transactions_by_owner("OREY")
        self.api.print_results(results)

    def test_get_transactions_by_type(self):
        results = self.api.get_transactions_by_type("computer")
        self.api.print_results(results)

    def test_get_transactions_by_brand(self):
        results = self.api.get_transactions_by_brand("Lenovo")
        self.api.print_results(results)

    def test_get_transactions_by_ID(self):
        results = self.api.get_transactions_by_id("computer34223")
        self.api.print_results(results)

    def test_move_equipment(self):
        print("Move an equipment :")
        type_equip = input("Type of the equipment : ")
        id_equip = input("Equipment's ID : ")
        if type_equip not in id_equip:
            print("Type and ID of this object don't match ! Try again.")
            return
        new_business_unit = input("New business unit : ")
        new_team = input("New team : ")
        new_owner = input("New person in charge : ")
        date = input("Date of this change : ")
        self.api.move_equipment(type_equip, id_equip, new_owner, new_business_unit, new_team, date)

    def test_get_id_by_type(self):
        print(self.api.get_id_by_type("computer"))

    def test_get_streams(self):
        print(self.api.get_streams())

    def test_get_all_ids(self):
        print(self.api.get_all_ids())