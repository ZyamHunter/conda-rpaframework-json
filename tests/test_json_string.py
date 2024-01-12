from RPA.JSON import JSON
from resources.json_operations import JsonOperations
import unittest
import copy

class TestString(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cars = '''
            {
                "cars": [
                    {
                        "brand": "Toyota",
                        "model": "Camry",
                        "year": 2022,
                        "color": "Blue",
                        "features": ["Automatic Transmission", "Air Conditioning", "Backup Camera"]
                    },
                    {
                        "brand": "Honda",
                        "model": "Civic",
                        "year": 2021,
                        "color": "Silver",
                        "features": ["Manual Transmission", "Sunroof", "Bluetooth Connectivity"]
                    },
                    {
                        "brand": "Ford",
                        "model": "Escape",
                        "year": 2023,
                        "color": "Red",
                        "features": ["Hybrid Engine", "Navigation System", "Leather Seats"]
                    }
                ]
            }
        '''

    def setUp(self):
        # Certifique-se de usar uma cópia do JSON original antes de cada teste
        self.current_cars = copy.deepcopy(self.cars)

    def test_convert_string_to_json(self):
        obj = JSON().convert_string_to_json('{"Key": "Value"}')
        assert obj["Key"] == 'Value'

    @unittest.skip("Exemplo de teste que será pulado")
    def test_example_skipped_test(self):
        print("Esse log não será exibido")

    def test_add_feature_to_cars(self):
        new_feature = "Parking Sensors"
        updated_cars = JSON().add_to_json(self.current_cars, '$.cars[*].features', new_feature)
        features_after_update = JSON().get_values_from_json(updated_cars, '$.cars[*].features')
        self.assertTrue(all(new_feature in features for features in features_after_update))

    def test_remove_feature_from_cars(self):
        feature_to_remove = "Air Conditioning"
        updated_cars = JSON().delete_from_json(self.current_cars, f'$.cars[*].features[?(@=="{feature_to_remove}")]')
        features_after_update = JSON().get_values_from_json(updated_cars, '$.cars[*].features')
        self.assertTrue(all(feature != feature_to_remove for features in features_after_update for feature in features))

    def test_filter_cars_by_year(self):
        year_to_filter = 2022
        filtered_cars = JSON().get_values_from_json(self.current_cars, f'$.cars[?(@.year=={year_to_filter})]')
        self.assertTrue(all(car["year"] == year_to_filter for car in filtered_cars))

if __name__ == '__main__':
    unittest.main()