import unittest

from .test_lib import TestGeneral


def main():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestGeneral))
    unittest.TextTestRunner(verbosity=2).run(suite)
