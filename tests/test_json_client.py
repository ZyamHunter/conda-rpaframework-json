from RPA.JSON import JSON
from resources.json_operations import JsonOperations
import unittest
import copy


class TestJson(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ID = 'guid-003'
        cls.clients = JsonOperations.load_json_from_file("assets/clients.json")

    def setUp(self):
        # Certifique-se de usar uma cópia do JSON original antes de cada teste
        self.current_clients = copy.deepcopy(self.clients)

    def test_get_email_for_specific_order_id(self):
        json_doc = self.current_clients
        email = JSON().get_value_from_json(json_doc, f'$.clients[?(@.orders[*].id=="{self.ID}")].email')
        self.assertEqual(email, 'jane@example.com')

    def test_calculate_total_spending(self):
        json_data = self.current_clients
        total_spending = JsonOperations.calculate_total_spending(json_data, "Jane Example")
        self.assertEqual(total_spending, 2504.13)
    
    def test_update_json_data_nonexistent_key(self):
        key_to_update = "nonexistent_key"
        new_value = "test_value"
        JsonOperations.update_json_data(key_to_update, new_value)
        updated_value = JsonOperations.get_key_in_json_data(key_to_update)
        self.assertIsNone(updated_value)

    def test_get_nonexistent_key_in_json_data(self):
        key = "nonexistent_key"
        value = JsonOperations.get_key_in_json_data(key)
        self.assertIsNone(value)

    def test_load_invalid_json_file(self):
        with self.assertRaises(FileNotFoundError):
            JsonOperations.load_invalid_json_file()

    def test_add_new_client(self):
        new_client = {
            "name": "New Client",
            "email": "newclient@example.com",
            "orders": [
                {"address": "New Street 123", "state": "CA", "price": 50.0, "id": "guid-006"}
            ]
        }
        self.current_clients['clients'].append(new_client)
        self.assertEqual(len(self.current_clients['clients']), 3)

    def test_remove_client(self):
        client_to_remove = "Johnny Example"
        self.current_clients['clients'] = [client for client in self.current_clients['clients'] if client['name'] != client_to_remove]
        self.assertEqual(len(self.current_clients['clients']), 1)

    def test_invalid_order_id(self):
        # Tenta obter o email para um ID de pedido inexistente
        invalid_order_id = "nonexistent-order-id"
        email = JSON().get_value_from_json(
            self.current_clients,
            f'$.clients[?(@.orders[*].id=="{invalid_order_id}")].email'
        )
        self.assertIsNone(email)

    def test_get_orders_with_price_above_threshold(self):
        # Obtém pedidos com preço acima de um limite
        threshold = 100.0
        orders_above_threshold = [
            order for client in self.current_clients['clients']
            for order in client['orders']
            if order['price'] > threshold
        ]
        self.assertGreater(len(orders_above_threshold), 0)

if __name__ == '__main__':
    unittest.main()
