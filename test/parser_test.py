from pprint import pprint as pp
from os.path import dirname, realpath
import sys
import unittest

sys.path.insert(0, dirname(dirname(realpath(__file__))))

from parser import HostParser
from ops_registry import OpsRegistry


def testop1(paramA, paramB, paramC='paramC'):
    pass

ops_registry = OpsRegistry()
ops_registry.add_operation('test1', testop1)


class HostParserTest(unittest.TestCase):
    host_parser1 = HostParser('test_config_broken.yaml',
                              host_properties_location=".",
                              ops_registry=ops_registry)
    host_parser2 = HostParser('test_config_working.yaml',
                              host_properties_location=".",
                              ops_registry=ops_registry)

    def test_parse(self):
        self.assertFalse(self.host_parser1.parse())
        self.assertTrue(self.host_parser2.parse())


if __name__ == '__main__':
    unittest.main()
