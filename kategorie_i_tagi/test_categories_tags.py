
import unittest
from categories_tags import CategoryTagManager
import json

class TestCategoryTagManagerWithJSON(unittest.TestCase):
    def setUp(self):
        self.manager = CategoryTagManager()
        self.manager.add_category("Home")
        self.manager.add_category("Work")
        self.manager.add_category("Personal")
        self.manager.add_tag("Urgent")
        self.manager.add_tag("Important")
        self.manager.add_tag("Chores")
        self.manager.remove_category("Home")
        # Load JSON data
        with open("test_data.json", "r") as file:
            self.data = json.load(file)

    def test_filter_by_category(self):
        tasks = self.manager.filter_tasks_by_category(self.data["tasks"], "Work")
        self.assertEqual(len(tasks), 3)

    def test_filter_by_tag(self):
        tasks = self.manager.filter_tasks_by_tag(self.data["tasks"], "Urgent")
        self.assertEqual(len(tasks), 4)

if __name__ == "__main__":
    unittest.main()
