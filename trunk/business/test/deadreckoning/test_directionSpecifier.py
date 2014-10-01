from unittest import TestCase
from business.deadreckoning.DirectionSpecifier import DirectionSpecifier
from domain.graph.Point import Point

__author__ = 'akshay'


class TestPositionCalculator(TestCase):

    locations = [Point.fromString("( nodeId = 26, x = 5220.0, y = 1600.0, name = Seminar Room 11 )"),
                 Point.fromString("( nodeId = 23, x = 5220.0, y = 1380.0, name = P24 )"),
                 Point.fromString("( nodeId = 27, x = 5220.0, y = 620.0, name = P28 )"),
                 Point.fromString("( nodeId = 25, x = 5220.0, y = 360.0, name = P26 )"),
                 Point.fromString("( nodeId = 21, x = 4800.0, y = 360.0, name = P22 )")]
    directionSpecifier = DirectionSpecifier()
    directionSpecifier.setLocationQueue(locations)

    def test_getNextHeading(self):
        self.assertAlmostEqual(self.directionSpecifier.getNextHeading(260, 4800, 2000, 225), 8.60, None, None, 0.01)
        self.assertAlmostEqual(self.directionSpecifier.getNextHeading(190, 4800, 1600, 225), 35, None, None, 0.01)
        self.assertAlmostEqual(self.directionSpecifier.getNextHeading(105, 5220, 800, 350), 265.0, None, None, 0.01)
        self.assertAlmostEqual(self.directionSpecifier.getNextHeading(20, 6000, 800, 190), 105.72, None, None, 0.01)
        self.assertAlmostEqual(self.directionSpecifier.getNextHeading(0, 6000, 2000, 220), 22.85, None, None, 0.01)
        self.assertAlmostEqual(self.directionSpecifier.getNextHeading(300, 4800, 800, 40), 47.69, None, None, 0.01)
        self.assertAlmostEqual(self.directionSpecifier.getNextHeading(90, 5200, 2000, 60), 27.13, None, None, 0.01)
        self.assertAlmostEqual(self.directionSpecifier.getNextHeading(123, 5000, 1200, 180), 85.81, None, None, 0.01)