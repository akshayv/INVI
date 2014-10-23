from unittest import TestCase
from business.deadreckoning.PositionCalculator import PositionCalculator
from domain.deadreckoning.SensorReading import SensorReading
from domain.graph.Point import Point

__author__ = 'akshay'


class TestPositionCalculator(TestCase):
    def test_updatePosition(self):
        positionCalculator = PositionCalculator(0, 0, 90)
        locations = [Point.fromString("( nodeId = 26, x = 5220.0, y = 1600.0, name = Seminar Room 11 )"),
                     Point.fromString("( nodeId = 23, x = 5220.0, y = 1380.0, name = P24 )"),
                     Point.fromString("( nodeId = 27, x = 5220.0, y = 620.0, name = P28 )"),
                     Point.fromString("( nodeId = 25, x = 5220.0, y = 360.0, name = P26 )"),
                     Point.fromString("( nodeId = 21, x = 4800.0, y = 360.0, name = P22 )")]
        positionCalculator.directionSpecifier.setLocationQueue(locations)
        positionCalculator.updatePosition(SensorReading.fromString(
            "( accelerometerReading = ( x = 13.31, y = -1.07, z = -6.06),  compassReading = 73.34, currentTime = 23080 )"))
        positionCalculator.updatePosition(SensorReading.fromString(
            "( accelerometerReading = ( x = 14.49, y = -0.32, z = -6.00),  compassReading = 72.60, currentTime = 23099 )"))
        positionCalculator.updatePosition(SensorReading.fromString(
            "( accelerometerReading = ( x = 15.62, y = -0.10, z = -6.40),  compassReading = 71.79, currentTime = 23117 )"))
        positionCalculator.updatePosition(SensorReading.fromString(
            "( accelerometerReading = ( x = 14.47, y = -2.43, z = -6.01),  compassReading = 73.57, currentTime = 23137 )"))
        positionCalculator.updatePosition(SensorReading.fromString(
            "( accelerometerReading = ( x = 6.13, y = -6.35, z = -3.68),  compassReading = 69.48, currentTime = 23169 )"))
        positionCalculator.updatePosition(SensorReading.fromString(
            "( accelerometerReading = ( x = 5.38, y = -4.39, z = 3.31),  compassReading = 65.00, currentTime = 23188 )"))
        positionCalculator.updatePosition(SensorReading.fromString(
            "( accelerometerReading = ( x = 5.09, y = -2.84, z = -1.13),  compassReading = 68.82, currentTime = 23206 )"))
        positionCalculator.updatePosition(SensorReading.fromString(
            "( accelerometerReading = ( x = 6.38, y = -0.10, z = -1.42),  compassReading = 70.47, currentTime = 23225 )"))
        positionCalculator.updatePosition(SensorReading.fromString(
            "( accelerometerReading = ( x = 6.64, y = -0.54, z = -1.97),  compassReading = 117.41, currentTime = 23614 )"))
        positionCalculator.updatePosition(SensorReading.fromString(
            "( accelerometerReading = ( x = 6.42, y = -0.80, z = -1.23),  compassReading = 115.78, currentTime = 23632 )"))
        positionCalculator.updatePosition(SensorReading.fromString(
            "( accelerometerReading = ( x = 6.49, y = -1.81, z = -1.99),  compassReading = 114.33, currentTime = 23652 )"))
        positionCalculator.updatePosition(SensorReading.fromString(
            "( accelerometerReading = ( x = 13.70, y = -3.07, z = -5.72),  compassReading = 116.17, currentTime = 23698 )"))
        positionCalculator.updatePosition(SensorReading.fromString(
            "( accelerometerReading = ( x = 15.61, y = -6.01, z = -10.48),  compassReading = 115.37, currentTime = 23716 )"))
        self.assertEqual(positionCalculator.stepCounter.getSteps(), 1)
        self.assertAlmostEqual(positionCalculator.getX(), 0, None, None, 0.1)
        self.assertAlmostEqual(positionCalculator.getY(), 4, None, None, 0.1)

    def test_updatePosition_readData(self):
        positionCalculator = PositionCalculator(0, 0, 90)

        locations = [Point.fromString("( nodeId = 26, x = 5220.0, y = 1600.0, name = Seminar Room 11 )"),
                     Point.fromString("( nodeId = 23, x = 5220.0, y = 1380.0, name = P24 )"),
                     Point.fromString("( nodeId = 27, x = 5220.0, y = 620.0, name = P28 )"),
                     Point.fromString("( nodeId = 25, x = 5220.0, y = 360.0, name = P26 )"),
                     Point.fromString("( nodeId = 21, x = 4800.0, y = 360.0, name = P22 )")]
        positionCalculator.directionSpecifier.setLocationQueue(locations)
        positionCalculator.updatePosition(SensorReading.fromString((
            "( accelerometerReading = ( x = -1.07, y = -9.34, z = -2.92),  compassReading = 106.28, currentTime = 705263  )")))
        positionCalculator.updatePosition(SensorReading.fromString((
            "( accelerometerReading = ( x = -0.47, y = -8.90, z = -2.32),  compassReading = 106.29, currentTime = 705283  )")))
        positionCalculator.updatePosition(SensorReading.fromString((
            "( accelerometerReading = ( x = 0.07, y = -8.84, z = -1.23),  compassReading = 105.68, currentTime = 705301  )")))
        positionCalculator.updatePosition(SensorReading.fromString((
            "( accelerometerReading = ( x = -1.40, y = -10.05, z = 1.08),  compassReading = 105.61, currentTime = 705320  )")))
        positionCalculator.updatePosition(SensorReading.fromString((
            "( accelerometerReading = ( x = 0.43, y = -11.78, z = 1.18),  compassReading = 105.60, currentTime = 705339  )")))
        positionCalculator.updatePosition(SensorReading.fromString((
            "( accelerometerReading = ( x = 0.06, y = -11.95, z = 1.78),  compassReading = 105.65, currentTime = 705358  )")))
        positionCalculator.updatePosition(SensorReading.fromString((
            "( accelerometerReading = ( x = -0.23, y = -12.33, z = 1.64),  compassReading = 102.09, currentTime = 705395  )")))
        positionCalculator.updatePosition(SensorReading.fromString((
            "( accelerometerReading = ( x = -3.53, y = -14.18, z = 1.99),  compassReading = 102.27, currentTime = 705414  )")))
        positionCalculator.updatePosition(SensorReading.fromString((
            "( accelerometerReading = ( x = -4.13, y = -18.33, z = -0.10),  compassReading = 104.68, currentTime = 705433  )")))
        positionCalculator.updatePosition(SensorReading.fromString((
            "( accelerometerReading = ( x = -6.70, y = -19.60, z = -2.69),  compassReading = 103.76, currentTime = 705452  )")))
        positionCalculator.updatePosition(SensorReading.fromString((
            "( accelerometerReading = ( x = -5.70, y = -19.60, z = -6.47),  compassReading = 102.67, currentTime = 705471  )")))
        positionCalculator.updatePosition(SensorReading.fromString((
            "( accelerometerReading = ( x = -6.26, y = -19.60, z = -7.61),  compassReading = 101.91, currentTime = 705490  )")))
        positionCalculator.updatePosition(SensorReading.fromString((
            "( accelerometerReading = ( x = -4.03, y = -15.04, z = -6.11),  compassReading = 116.14, currentTime = 705520  )")))
        positionCalculator.updatePosition(SensorReading.fromString((
            "( accelerometerReading = ( x = -4.26, y = -9.64, z = -3.34),  compassReading = 114.86, currentTime = 705540  )")))
        positionCalculator.updatePosition(SensorReading.fromString((
            "( accelerometerReading = ( x = -3.56, y = -7.80, z = 0.02),  compassReading = 114.13, currentTime = 705558  )")))
        positionCalculator.updatePosition(SensorReading.fromString((
            "( accelerometerReading = ( x = -2.81, y = -4.91, z = 3.81),  compassReading = 122.69, currentTime = 705577  )")))
        positionCalculator.updatePosition(SensorReading.fromString((
            "( accelerometerReading = ( x = 0.61, y = 1.90, z = 3.36),  compassReading = 123.58, currentTime = 705596  )")))
        positionCalculator.updatePosition(SensorReading.fromString((
            "( accelerometerReading = ( x = -0.10, y = 6.73, z = 4.49),  compassReading = 124.66, currentTime = 705614  )")))
        positionCalculator.updatePosition(SensorReading.fromString((
            "( accelerometerReading = ( x = 0.83, y = 11.65, z = -0.42),  compassReading = 242.09, currentTime = 705662  )")))
        positionCalculator.updatePosition(SensorReading.fromString((
            "( accelerometerReading = ( x = -0.46, y = 11.68, z = -2.76),  compassReading = 243.33, currentTime = 705681  )")))
        positionCalculator.updatePosition(SensorReading.fromString((
            "( accelerometerReading = ( x = -0.53, y = 10.22, z = -6.43),  compassReading = 245.28, currentTime = 705699  )")))
        positionCalculator.updatePosition(SensorReading.fromString((
            "( accelerometerReading = ( x = -2.79, y = 7.26, z = -9.11),  compassReading = 223.20, currentTime = 705719  )")))
        positionCalculator.updatePosition(SensorReading.fromString((
            "( accelerometerReading = ( x = -3.88, y = 3.61, z = -11.32),  compassReading = 225.10, currentTime = 705737  )")))
        positionCalculator.updatePosition(SensorReading.fromString((
            "( accelerometerReading = ( x = -2.80, y = 0.96, z = -13.61),  compassReading = 224.70, currentTime = 705757  )")))
        positionCalculator.updatePosition(SensorReading.fromString((
            "( accelerometerReading = ( x = -1.37, y = 2.59, z = -14.08),  compassReading = 208.75, currentTime = 705786  )")))
        positionCalculator.updatePosition(SensorReading.fromString((
            "( accelerometerReading = ( x = -5.32, y = 5.08, z = -8.80),  compassReading = 208.06, currentTime = 705806  )")))
        positionCalculator.updatePosition(SensorReading.fromString((
            "( accelerometerReading = ( x = -9.77, y = 4.54, z = 0.10),  compassReading = 208.05, currentTime = 705824  )")))
        positionCalculator.updatePosition(SensorReading.fromString((
            "( accelerometerReading = ( x = -18.45, y = -5.01, z = 11.63),  compassReading = 257.06, currentTime = 705843  )")))
        positionCalculator.updatePosition(SensorReading.fromString((
            "( accelerometerReading = ( x = -17.94, y = -19.60, z = 14.01), compassReading = 254.95, currentTime = 705862  )")))
        positionCalculator.updatePosition(SensorReading.fromString((
            "( accelerometerReading = ( x = -17.94, y = -19.60, z = 14.01), compassReading = 254.95, currentTime = 705962  )")))
        # self.assertEqual(positionCalculator.stepCounter.getSteps(), 1)
        # self.assertAlmostEqual(positionCalculator.getX(), 0, None, None, 0.1)
        # self.assertAlmostEqual(positionCalculator.getY(), 4, None, None, 0.1)

