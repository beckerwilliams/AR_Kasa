import unittest
import arkasa
import asyncio
import tracemalloc


class test___init__(unittest.TestCase):

    def setUp(self):
        self.prod_hosts = ["192.168.1.3", "192.168.1.15", "192.168.1.16", "192.168.1.18"]
        self.test_host = "192.168.1.15"

    def tearDown(self):
        del self.prod_hosts
        del self.test_host

    # Test Kasa Discovery
    def test_discover(self):
        for dev in self.prod_hosts:
            self.assertTrue(dev in [device for device in asyncio.run(arkasa.discover())])

    def test_get(self):
        smartplug = asyncio.run(arkasa.get(self.test_host))
        self.assertTrue(smartplug.host == self.test_host)

    def test_turn_off(self):
        return self.assertTrue(asyncio.run(arkasa.turn_off(self.test_host)))

    def test_turn_on(self):
        return self.assertTrue(asyncio.run(arkasa.turn_on(self.test_host)))

    def test_hosts(self):
        hosts = asyncio.run(arkasa.hosts())
        for host in self.prod_hosts:
            self.assertTrue(host in self.prod_hosts)


if __name__ == '__main__':
    unittest.main()
