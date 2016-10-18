import unittest

from lsst.sims.survey.fields import FieldsDatabase

class TestFieldDatabase(unittest.TestCase):

    def setUp(self):
        self.fields_db = FieldsDatabase()
        self.query = "select * from Field limit 2;"

    def test_basic_information_after_creation(self):
        self.assertEqual(self.fields_db.db_name, "Fields.db")
        self.assertIsNotNone(self.fields_db.connect)

    def test_opsim3_userregions(self):
        result = self.fields_db.get_opsim3_userregions(self.query)
        truth_result = """userRegion = 0.00,-90.00,0.03
userRegion = 180.00,-87.57,0.03"""
        self.assertEqual(result, truth_result)

    def test_get_ra_dec_arrays(self):
        ra, dec = self.fields_db.get_ra_dec_arrays(self.query)
        self.assertEqual(ra.size, 2)
        self.assertEqual(dec.size, 2)
        self.assertEqual(ra[1], 180.0)
        self.assertAlmostEqual(dec[1], -87.57, delta=1e-2)

    def test_get_rows(self):
        rows = self.fields_db.get_rows(self.query)
        self.assertIsInstance(rows, list)
        self.assertEqual(len(rows), 2)
        self.assertEqual(len(rows[0]), 8)

if __name__ == '__main__':
    unittest.main()
