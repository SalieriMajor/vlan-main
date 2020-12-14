import unittest
from services.vlan_parsing import VlanInfo


class TestParseVlanString(unittest.TestCase):
    def test_something(self):
        vlan_info = VlanInfo(None)
        vlan_info.show_vlan_brief_output = """        
VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------------------
1    default                          active
100  mgmt                             active    Po11, Eth1/1, Eth1/2
101  prod                             active    Po11, Eth1/1, Eth1/2

"""
        after_parsing = vlan_info.parse_vlan_string_output()
        expected_after_parsing = [
            {'vlan_id': 1, 'vlan_name': 'default', 'vlan_state': 'active'},
            {'vlan_id': 100, 'vlan_name': 'mgmt', 'vlan_state': 'active'},
            {'vlan_id': 101, 'vlan_name': 'prod', 'vlan_state': 'active'}
        ]
        self.assertEqual(after_parsing, expected_after_parsing)

if __name__ == '__main__':
    unittest.main()
