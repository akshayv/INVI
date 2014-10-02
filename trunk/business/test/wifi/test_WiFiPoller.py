from unittest import TestCase
from business.wifi.WiFiPoller import WiFiPoller

__author__ = 'raghav'


class TestWiFiPoller(TestCase):
    def test_checkLocation(self):
        wifiPoller = WiFiPoller()
        location = wifiPoller.checkLocation()
        self.assertAlmostEquals(location, "{x: 2.6322, y: 1.8822}")
