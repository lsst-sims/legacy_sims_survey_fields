import unittest

from lsst.survey_fields import FieldsDatabase

class TestFieldDatabase(unittest.TestCase):

    def setUp(self):
        self.fields = FieldsDatabase()

    def test_basic_information_after_creation(self):
        self.assertEqual(self.fields.fields_db_name, "Fields.db")
        self.assertIsNotNone(self.fields.connect)

if __name__ == '__main__':
    unittest.main()
