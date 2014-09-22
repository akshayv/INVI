__author__ = 'akshay'

import difflib

class VoiceParser:

    @staticmethod
    def getMatchingLocation(input, locations):
        maxRatio = 0
        closestLocation = None
        for location in locations:
            ratio = difflib.SequenceMatcher(None, input, location).ratio()
            if ratio > maxRatio:
                maxRatio = ratio
                closestLocation = location
        return closestLocation


if __name__ == "__main__":
    locations = ["Seminar Room 4", "To LT15", "Student Area", "P14", "Tutorial Room 8", "P21"]
    print VoiceParser.getMatchingLocation("P12", locations)
