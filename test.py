import unittest
from datetime import time, timedelta

from main import find_available_slots


class TestCaseFindAvailableSlots(unittest.TestCase):
    def test_example_case(self):
        """ Test with the example case provided """
        expected_response = [
            (time(10, 30), time(12, 0)),
            (time(13, 0), time(15, 0)),
            (time(16, 0), time(17, 0))
        ]
        example_schedule = [
            (time(9, 0), time(10, 30)),
            (time(12, 0), time(13, 0)),
            (time(15, 0), time(16, 0))
        ]
        example_meeting_duration = timedelta(hours=1)
        response = find_available_slots(example_schedule, example_meeting_duration)
        self.assertEqual(expected_response, response)

    def test_no_meetings(self):
        """ Test with no meetings """
        expected_response = [
            (time(9, 0), time(17, 0))
        ]
        example_schedule = []
        example_meeting_duration = timedelta(hours=1)
        response = find_available_slots(example_schedule, example_meeting_duration)
        self.assertEqual(expected_response, response)

    def test_no_available_slots(self):
        """ Test with no available slots """
        expected_response = []
        example_schedule = [
            (time(9, 0), time(10, 30)),
            (time(12, 0), time(13, 0)),
            (time(14, 30), time(16, 0))
        ]
        example_meeting_duration = timedelta(hours=2)
        response = find_available_slots(example_schedule, example_meeting_duration)
        self.assertEqual(expected_response, response)

    def test_all_occupied(self):
        """ Test with all slots occupied """
        expected_response = []
        example_schedule = [
            (time(9, 0), time(10, 30)),
            (time(10, 30), time(12, 0)),
            (time(12, 0), time(13, 0)),
            (time(13, 0), time(15, 0)),
            (time(15, 0), time(16, 0)),
            (time(16, 0), time(17, 0))
        ]
        example_meeting_duration = timedelta(hours=1)
        response = find_available_slots(example_schedule, example_meeting_duration)
        self.assertEqual(expected_response, response)

    def test_random_order_schedule(self):
        """ Test with a random order schedule """
        expected_response = [
            (time(10, 30), time(12, 0)),
            (time(13, 0), time(15, 0)),
            (time(16, 0), time(17, 0))
        ]
        example_schedule = [
            (time(15, 0), time(16, 0)),
            (time(9, 0), time(10, 30)),
            (time(12, 0), time(13, 0))
        ]
        example_meeting_duration = timedelta(hours=1)
        response = find_available_slots(example_schedule, example_meeting_duration)
        self.assertEqual(expected_response, response)

    def test_meeting_duration_bigger_than_office_hours(self):
        """ Test with a meeting duration bigger than the office hours """
        expected_response = []
        example_schedule = []
        example_meeting_duration = timedelta(hours=10)
        response = find_available_slots(example_schedule, example_meeting_duration)
        self.assertEqual(expected_response, response)

    def test_with_schedule_starting_out_office_hours(self):
        """ Test with a schedule starting before the office hours """
        expected_response = [
            (time(10, 30), time(12, 0)),
            (time(13, 0), time(15, 0)),
            (time(16, 0), time(17, 0))
        ]
        example_schedule = [
            (time(8, 0), time(10, 30)),
            (time(12, 0), time(13, 0)),
            (time(15, 0), time(16, 0))
        ]
        example_meeting_duration = timedelta(hours=1)
        response = find_available_slots(example_schedule, example_meeting_duration)
        self.assertEqual(expected_response, response)

    def test_scheduled_start_end_time_mixed(self):
        """ Test with a schedule with mixed start and end times """
        expected_response = [
            (time(9, 0), time(10, 30)),
            (time(13, 0), time(15, 0)),
            (time(16, 0), time(17, 0))
        ]
        example_schedule = [
            (time(10, 30), time(12, 0)),
            (time(13, 0), time(12, 0)),
            (time(16, 0),time(15, 0))
        ]
        example_meeting_duration = timedelta(hours=1)
        response = find_available_slots(example_schedule, example_meeting_duration)
        self.assertEqual(expected_response, response)


if __name__ == '__main__':
    unittest.main()
