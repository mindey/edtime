import detime
import datetime

def test_computed_interpreted_match():

    date = datetime.datetime(2021, 9, 23, 10, 20, 7, 533206)

    computed = detime.detime(date)
    interpreted = detime.detime(51, 8, 11, 4, 30, computed.second)

    assert computed.date == interpreted.date

