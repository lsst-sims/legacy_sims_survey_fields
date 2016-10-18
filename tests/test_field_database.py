import unittest

from lsst.sims.survey.fields import FieldsDatabase

class TestFieldDatabase(unittest.TestCase):

    def setUp(self):
        self.fields_db = FieldsDatabase()

    def test_basic_information_after_creation(self):
        self.assertEqual(self.fields_db.db_name, "Fields.db")
        self.assertIsNotNone(self.fields_db.connect)

    def test_opsim3_userregions(self):
        query = "select * from Field limit 2;"
        result = self.fields_db.get_opsim3_userregions(query)
        truth_result = """userRegion = 0.00,-90.00,0.03
userRegion = 180.00,-87.57,0.03"""
        self.assertEqual(result, truth_result)

if __name__ == '__main__':
    unittest.main()
