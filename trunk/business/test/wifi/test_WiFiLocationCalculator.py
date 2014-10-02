from unittest import TestCase
from business.wifi.WiFiLocationCalculator import WiFiLocationCalculator
from domain.wifi.AccessPoint import AccessPoint

__author__ = 'raghav'

class TestWiFiLocationCalculator(TestCase):
    def test_computeTopThreeRSSI(self):
        wifiLocationCalculator = WiFiLocationCalculator()
        topThree = wifiLocationCalculator.computeTopThreeRSSI([{ 'rssi': -53, 'bssid': "28:50:6c:39:af:88" },
            { 'rssi': -58, 'bssid': "28:50:6c:39:af:88" }, { 'rssi': -35, 'bssid': "28:50:6c:39:af:88" }])
        self.assertEquals(topThree, [{'rssi': -35, 'bssid': '28:50:6c:39:af:88'},
             {'rssi': -53, 'bssid': '28:50:6c:39:af:88'}, {'rssi': -58, 'bssid': '28:50:6c:39:af:88'}])

    def test_computeDistanceFromRSSI(self):
        wifiLocationCalculator = WiFiLocationCalculator()
        distance = wifiLocationCalculator.computeDistanceFromRSSI(-50)
        self.assertAlmostEquals(distance, 7.1968, 3)

    def test_computeLocation(self):
        wifiLocationCalculator = WiFiLocationCalculator()
        coordList = [
            { "x": 0, "y": 2, "distance": 2, "bssid": "28:50:6c:39:af:88", "nodeName": "ap-101" },
            { "x": 2, "y": 0, "distance": 1, "bssid": "8f:23:c5:94:df:95", "nodeName": "ap-102" },
            { "x": -2, "y": 0, "distance": 5, "bssid": "53:60:6c:63:ed:68", "nodeName": "ap-103" }
        ]
        location = wifiLocationCalculator.computeLocation(coordList)
        self.assertEquals(location, "{x: 2.6322, y: 1.8822}")

