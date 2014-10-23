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
        positionCalculator.updatePosition(SensorReading.fromString("( accelerometerReading = ( x = 13.31, y = -1.07, z = -6.06),  compassReading = 73.34, currentTime = 23080 )"))
        positionCalculator.updatePosition(SensorReading.fromString("( accelerometerReading = ( x = 14.49, y = -0.32, z = -6.00),  compassReading = 72.60, currentTime = 23099 )"))
        positionCalculator.updatePosition(SensorReading.fromString("( accelerometerReading = ( x = 15.62, y = -0.10, z = -6.40),  compassReading = 71.79, currentTime = 23117 )"))
        positionCalculator.updatePosition(SensorReading.fromString("( accelerometerReading = ( x = 14.47, y = -2.43, z = -6.01),  compassReading = 73.57, currentTime = 23137 )"))
        positionCalculator.updatePosition(SensorReading.fromString("( accelerometerReading = ( x = 6.13, y = -6.35, z = -3.68),  compassReading = 69.48, currentTime = 23169 )"))
        positionCalculator.updatePosition(SensorReading.fromString("( accelerometerReading = ( x = 5.38, y = -4.39, z = 3.31),  compassReading = 65.00, currentTime = 23188 )"))
        positionCalculator.updatePosition(SensorReading.fromString("( accelerometerReading = ( x = 5.09, y = -2.84, z = -1.13),  compassReading = 68.82, currentTime = 23206 )"))
        positionCalculator.updatePosition(SensorReading.fromString("( accelerometerReading = ( x = 6.38, y = -0.10, z = -1.42),  compassReading = 70.47, currentTime = 23225 )"))
        positionCalculator.updatePosition(SensorReading.fromString("( accelerometerReading = ( x = 6.64, y = -0.54, z = -1.97),  compassReading = 117.41, currentTime = 23614 )"))
        positionCalculator.updatePosition(SensorReading.fromString("( accelerometerReading = ( x = 6.42, y = -0.80, z = -1.23),  compassReading = 115.78, currentTime = 23632 )"))
        positionCalculator.updatePosition(SensorReading.fromString("( accelerometerReading = ( x = 6.49, y = -1.81, z = -1.99),  compassReading = 114.33, currentTime = 23652 )"))
        positionCalculator.updatePosition(SensorReading.fromString("( accelerometerReading = ( x = 13.70, y = -3.07, z = -5.72),  compassReading = 116.17, currentTime = 23698 )"))
        positionCalculator.updatePosition(SensorReading.fromString("( accelerometerReading = ( x = 15.61, y = -6.01, z = -10.48),  compassReading = 115.37, currentTime = 23716 )"))
        self.assertEqual(positionCalculator.stepCounter.getSteps(), 1)
        self.assertAlmostEqual(positionCalculator.getX(), 0, None, None, 0.1)
        self.assertAlmostEqual(positionCalculator.getY(), 4, None, None, 0.1)
