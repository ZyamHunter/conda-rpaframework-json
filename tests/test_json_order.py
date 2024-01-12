from RPA.JSON import JSON
from resources.json_operations import JsonOperations
import unittest
import copy

class TestOrder(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.orders = JsonOperations.load_json_from_file("assets/orders.json")

    def setUp(self):
        # Certifique-se de usar uma cópia do JSON original antes de cada teste
        self.current_orders = copy.deepcopy(self.orders)
    
    def test_add_item_to_order(self):
        # Add an item to the specified order
        js = JSON()
        order_id = "order-001"
        item_to_add = {"name": "Item D", "price": 25.0}
        before = self.current_orders
        after = js.add_to_json(before, f'$.orders[?(@.id=="{order_id}")].items', item_to_add)
        self.assertEqual(len(after['orders'][0]['items']), 3)

    def test_verify_null_values(self):
        # Verify that there are no null values in the People list
        js = JSON()
        data = self.current_orders
        names = js.get_values_from_json(data, "$.People[*].Name")
        self.assertFalse(None in names)

    def test_update_order_price(self):
        # Update the price of a specific item in an order
        js = JSON()
        order_id = "order-001"
        item_name = "Item A"
        new_price = 15.0
        before = self.current_orders

        # Busca o índice do item no array
        index = next((index for index, item in enumerate(before['orders'][0]['items']) if item["name"] == item_name), None)

        # Atualiza o preço se o item for encontrado
        if index is not None:
            before['orders'][0]['items'][index]['price'] = new_price

        after = js.get_value_from_json(before, f'$.orders[?(@.id=="{order_id}")].items[?(@.name=="{item_name}")].price')
        self.assertEqual(after, new_price)

    def test_remove_item_from_order(self):
        # Remove a specific item from an order
        js = JSON()
        order_id = "order-001"
        item_to_remove = "Item A"
        before = self.current_orders
        after = js.delete_from_json(before, f'$.orders[?(@.id=="{order_id}")].items[?(@.name=="{item_to_remove}")]')
        self.assertEqual(len(after['orders'][0]['items']), 1)

    def test_nested_value_extraction(self):
        # Extract a nested value from JSON structure
        js = JSON()
        data = self.current_orders
        item_names = js.get_values_from_json(data, "$.orders[*].items[*].name")
        self.assertIn("Item A", item_names)
        self.assertIn("Item B", item_names)
        self.assertIn("Item C", item_names)

if __name__ == '__main__':
    unittest.main()