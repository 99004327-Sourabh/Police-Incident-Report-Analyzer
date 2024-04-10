import unittest
from unittest.mock import patch
from io import BytesIO
from datetime import datetime
from src.assignment2 import calculate_bearing, calculate_side_of_town, get_weather_code, extract_text_from_pdf, parse_incident_lines, augment_data


class TestAssignment2Functions(unittest.TestCase):
    def test_calculate_bearing(self):
        # Test calculate_bearing function with known coordinates
        bearing = calculate_bearing((35.220833, -97.443611), (35.3, -97.5))
        self.assertAlmostEqual(bearing, 329.8339, places=4)  # Updated expected value

    def test_calculate_bearing_different_coordinates(self):
        # Test calculate_bearing function with different coordinates
        bearing = calculate_bearing((0, 0), (45, 90))
        self.assertAlmostEqual(bearing, 45.0, places=1)  # Expected bearing for 45-degree angle


if __name__ == '__main__':
    unittest.main()
