from __future__ import division
import math
import unittest

from lsst.survey.fields import Field

class TestField(unittest.TestCase):

    def setUp(self):
        self.field = Field(1, 30.0, -30.0, -45.0, 45.0, 60.0, -60.0, 3.0)

    def test_basic_information_after_creation(self):
        self.assertEqual(self.field.fid, 1)
        self.assertEqual(self.field.ra, 30.0)
        self.assertEqual(self.field.dec, -30.0)
        self.assertEqual(self.field.gl, -45.0)
        self.assertEqual(self.field.gb, 45.0)
        self.assertEqual(self.field.el, 60.0)
        self.assertEqual(self.field.eb, -60.0)
        self.assertEqual(self.field.fov, 3.0)
        self.assertEqual(self.field.ra_rad, math.pi / 6)
        self.assertEqual(self.field.dec_rad, -math.pi / 6)
        self.assertEqual(self.field.gl_rad, -math.pi / 4)
        self.assertEqual(self.field.gb_rad, math.pi / 4)
        self.assertEqual(self.field.el_rad, math.pi / 3)
        self.assertEqual(self.field.eb_rad, -math.pi / 3)
        self.assertAlmostEqual(self.field.fov_rad, math.pi / 60, delta=1e-7)

if __name__ == '__main__':
    unittest.main()
