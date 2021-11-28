import edtime
import datetime

def test_computed_interpreted_match():

    date = datetime.datetime(2021, 9, 23, 10, 20, 7, 533206)

    computed = edtime.edtime(date)

    interpreted = edtime.edtime(computed.dyear, computed.dmonth, computed.dweek, computed.dday, computed.dhour, computed.dminute, computed.dsecond)

    assert computed.day == interpreted.day


def test_negative_interpreted_match():

    date = datetime.datetime(1925, 9, 23, 10, 20, 7, 533206)

    computed = edtime.edtime(date)

    interpreted = edtime.edtime(computed.dyear, computed.dmonth, computed.dweek, computed.dday, computed.dhour, computed.dminute, computed.dsecond)

    assert computed.day == interpreted.day

