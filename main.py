from datetime import timedelta, datetime, time
from turtledemo.penrose import start
from typing import Tuple, List

OFFICE_HOURS = (time(9, 0), time(17, 0))


def get_timelapse_from_times(start: time, end: time) -> timedelta:
    """
    This function receives two datetime.time objects and returns the timedelta between them.
    we need to create this auxiliary function because you cannot subtract two datetime.time objects directly and I think
    that is better that transforming the time objects to datetime objects and then subtract them, beacuse you will need
    to add dates and it will be more complicated.
    :param start:
    :param end:
    :return:
    """
    timelapse = timedelta(
        hours=end.hour - start.hour,
        minutes=end.minute - start.minute
    )
    return timelapse


def find_available_slots(
        schedule: List[Tuple[time, time]], meeting_duration: timedelta
) -> List[Tuple[time, time]]:
    """
    This function receives a schedule and a meeting duration and returns the available slots for a meeting
    Time complexity: O(n)
    Space complexity: O(n)
    :param schedule: list of tuples with the start and end time of the meetings on datetime.time format
    :param meeting_duration: timedelta with the duration of the meeting
    :return: List of tuples with the start and end time of the available slots for the meeting
    """

    available_slots = []
    # First step is to organize the schedule from the earliest to the latest, in this way we can iterate through the
    # schedule in a more efficient way
    schedule.sort(key=lambda x: x[0])
    # Now we need to iterate through the schedule to find the available slots
    current_start = OFFICE_HOURS[0]  # The current start, is auxiliar variable to keep track of the current start time
    for meeting in schedule:
        if current_start < meeting[0] and get_timelapse_from_times(current_start, meeting[0]) >= meeting_duration:
            # If the current start is before the meeting start, we can add the available slot to the available_slots
            available_slots.append((current_start, meeting[0]))
        # Now we need to update the current start to the end of the current meeting
        current_start = meeting[1]
    # Finally, we need to check if there is an available slot after the last meeting
    if current_start < OFFICE_HOURS[1] and get_timelapse_from_times(current_start, OFFICE_HOURS[1]) >= meeting_duration:
        available_slots.append((current_start, OFFICE_HOURS[1]))
    return available_slots


if __name__ == "__main__":
    example_schedule = [
        (time(9, 0), time(10, 30)),
        (time(12, 0), time(13, 0)),
        (time(15, 0), time(16, 0))
    ]
    example_meeting_duration = timedelta(hours=1)
    available_spots = find_available_slots(example_schedule, example_meeting_duration)
    print(available_spots)
