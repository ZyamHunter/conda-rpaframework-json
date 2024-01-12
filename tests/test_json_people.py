from RPA.JSON import JSON
from resources.json_operations import JsonOperations
import unittest
import copy


class TestPeople(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.peoples = JsonOperations.load_json_from_file("assets/peoples.json")

    def setUp(self):
        # Certifique-se de usar uma cópia do JSON original antes de cada teste
        self.current_peoples = copy.deepcopy(self.peoples)

    def test_get_age_of_person(self):
        age = self.current_peoples['people'][0]['age']
        self.assertEqual(age, 30)

    def test_get_street_address(self):
        street_address = self.current_peoples['people'][1]['address']['street']
        self.assertEqual(street_address, '456 Oak St')

    def test_get_email_contacts(self):
        emails = [contact['value'] for contact in self.current_peoples['people'][0]['contacts'] if contact['type'] == 'email']
        self.assertListEqual(emails, ['john@example.com'])

    def test_update_city_name(self):
        self.current_peoples['people'][1]['address']['city'] = 'NewCity'
        updated_city = self.current_peoples['people'][1]['address']['city']
        self.assertEqual(updated_city, 'NewCity')

    def test_add_new_person(self):
        new_person = {
            "id": 3,
            "name": "Bob Johnson",
            "age": 35,
            "address": {
                "street": "789 Pine St",
                "city": "AnotherCity",
                "state": "TX",
                "zip": "54321"
            },
            "contacts": [
                {
                    "type": "email",
                    "value": "bob@example.com"
                },
                {
                    "type": "phone",
                    "value": "+1 555-9876"
                }
            ]
        }
        self.current_peoples['people'].append(new_person)
        self.assertEqual(len(self.current_peoples['people']), 3)

    def test_remove_contact(self):
        contacts_before = len(self.current_peoples['people'][1]['contacts'])
        self.current_peoples['people'][1]['contacts'] = [contact for contact in self.current_peoples['people'][1]['contacts'] if contact['type'] != 'email']
        contacts_after = len(self.current_peoples['people'][1]['contacts'])
        self.assertEqual(contacts_after, contacts_before - 1)

    def test_invalid_key_access(self):
        with self.assertRaises(KeyError):
            invalid_value = self.current_peoples['people'][0]['invalid_key']

    def test_update_zip_code(self):
        self.current_peoples['people'][0]['address']['zip'] = '54321'
        updated_zip = self.current_peoples['people'][0]['address']['zip']
        self.assertEqual(updated_zip, '54321')

    def test_add_contact_to_person(self):
        new_contact = {"type": "fax", "value": "+1 555-9999"}
        self.current_peoples['people'][0]['contacts'].append(new_contact)
        self.assertEqual(len(self.current_peoples['people'][0]['contacts']), 3)

    def test_remove_person(self):
        del self.current_peoples['people'][1]
        self.assertEqual(len(self.current_peoples['people']), 1)

    def test_invalid_array_access(self):
        with self.assertRaises(IndexError):
            invalid_value = self.current_peoples['people'][4]

    def test_negative_age_value(self):
        self.current_peoples['people'][0]['age'] = -5
        updated_age = self.current_peoples['people'][0]['age']
        self.assertEqual(updated_age, -5)

    def test_check_json_structure(self):
        self.assertTrue('people' in self.current_peoples)
        self.assertTrue('address' in self.current_peoples['people'][0])
        self.assertTrue('contacts' in self.current_peoples['people'][1])

if __name__ == '__main__':
    unittest.main()