import unittest

from lsst.survey.fields import FieldsDatabase

class TestFieldDatabase(unittest.TestCase):

    def setUp(self):
        self.fields_db = FieldsDatabase()

    def test_basic_information_after_creation(self):
        self.assertEqual(self.fields_db.db_name, "Fields.db")
        self.assertIsNotNone(self.fields_db.connect)

if __name__ == '__main__':
    unittest.main()
