from datetime import datetime
import pytz
import unittest
from timeforms.misc import (convert_input_to_utc,
                             convert_initial_to_local,
                             convert_output_to_local)

class MiscTestCase(unittest.TestCase):
    def setUp(self):
        self.timezone = pytz.timezone("US/Eastern")
        self.utc_time = datetime.strptime("December 21, 2012 12:00:00", "%B %d, %Y %H:%M:%S")
        self.eastern_time = datetime.strptime("December 21, 2012 7:00:00", "%B %d, %Y %H:%M:%S")
                                          
    def test_input_to_utc(self):
        utc_time = convert_input_to_utc(self.eastern_time, self.timezone)
        self.assertEqual(self.utc_time, utc_time)

    def test_initial_to_local(self):
        eastern_time = convert_initial_to_local(self.utc_time, self.timezone)
        eastern_time = eastern_time.replace(tzinfo=None)
        self.assertEqual(self.eastern_time, eastern_time)

    def test_output_to_local(self):
        format = "%m/%d/%Y %H:%M"
        eastern_time_string = convert_output_to_local(self.utc_time, self.timezone, format=format)
        test_string = datetime.strftime(self.eastern_time, format)
        self.assertEqual(eastern_time_string, test_string)


if __name__ == '__main__':
    unittest.main()
