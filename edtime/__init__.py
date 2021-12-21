#!/usr/bin/python3

import time
import numbers
import datetime

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-s', '--show', help='Persist showing counting time.')


class Date:

    """
    EXTENDED DECIMAL TIME (EDT)
    ===========================

    Time starts at 1970 Jan 1, at UNIX time start date.

    1 dyear = 1000 days
    1 dmonth = 100 days
    1 dweek = 10 days

    1 day = 86400 SI seconds
    1 dday = 1 day

    1 dhour = 0.1 days
    1 dminute = 0.001 days
    1 dsecond = 0.00001 days

    """

    def __init__(self, *args, **kwargs):
        if args:

            if len(args) == 1:

                if isinstance(args[0], datetime.datetime):
                    self.day = (time.mktime(args[0].timetuple()) + args[0].microsecond/1e6) / 86400.

                elif isinstance(args[0], numbers.Number):
                    if isinstance(args[0], int):
                        self.interpret_date(*args)
                    else:
                        self.day = args[0]
            else:
                self.interpret_date(*args)
        elif kwargs:
            self.interpret_date(**kwargs)
        else:
            self.day = 0.

        self.compute_date()

    def interpret_date(self, dyear=0, dmonth=0, dweek=0, dday=0, dhour=0, dminute=0, dsecond=0.):
        """
            Takes:
            Date properties.

            Sets:
            (self.day - the POSIX day)
        """
        if dyear >= 0:
            self.day = dyear * 1000 + dmonth * 100 + dweek * 10 + dday * 1 + dhour * 0.1 + dminute * 0.001 + dsecond * 0.00001
        else:
            self.day = dyear * 1000 - (dmonth * 100 + dweek * 10 + dday * 1 + dhour * 0.1 + dminute * 0.001 + dsecond * 0.00001)

    def compute_date(self):
        """
            Takes:
            (self.day - the POSIX day)

            Sets:
            Date properties.
        """

        day = str(self.day)
        # if '.' in (day := str(self.day)):
        if '.' in day:
            left, right = day.split('.', 1)
        else:
            left, right = day, ''

        self.dyear, self.dmonth, self.dweek, self.dday = int(left[:-3] or 0.), int(left[-3:-2] or 0.), int(left[-2:-1] or 0.), int(left[-1:] or 0.)

        self.dhour, self.dminute, self.dsecond = int(right[:1] or 0.), int(right[1:3] or 0.), float((right[3:5] or '0') +'.'+(right[5:] or '0'))

    def isoformat(self):
        ds = str(self.dsecond)
        if '.' in ds:
            dsecs, dmils = ds.split('.')
        else:
            dsecs, dmils = ds, '0'

        dsecs = int(dsecs)
        return f'{self.dyear}°{self.dmonth}″{self.dweek}′{self.dday}T{self.dhour}:{self.dminute:02d}:{dsecs:02d}.{dmils}'

    def __add__(self, other):
        return Date(self.day.__add__(other.day))

    def __sub__(self, other):
        return Date(self.day.__sub__(other.day))

    def __mul__(self, other):
        return Date(self.day.__mul__(other.day))

    def __truediv__(self, other):
        return Date(self.day.__truediv__(other.day))

    def __div__(self, other):
        return Date(self.day.__div__(other.day))

    def __floordiv__(self,other):
        return Date(self.day.__floordiv__(other.day))

    def __mod__(self, other):
        return Date(self.day.__mod__(other.day))

    def __eq__(self, other):
        return self.day == other.day

    def __ne__(self, other):
        return self.day != other.day

    def __str__(self):
        return self.isoformat()

    def __float__(self):
        return self.day

    @classmethod
    def utcnow(cls):
        return Date(time.time()/86400.)

    @classmethod
    def datetime(cls, *args, **kwargs):
        return Date(datetime.datetime(*args, **kwargs))

    def to_datetime(self):
        return datetime.datetime.fromtimestamp(self.day*86400.)

    @classmethod
    def from_jd(cls, jd):
        'From Julian days (JD)'
        return Date(jd-2440587.5)

    def to_jd(self):
        'To Julian days (JD)'
        return self.day+2440587.5

    def __repr__(self):
        return f'edtime.edtime(dyear={self.dyear}, dmonth={self.dmonth}, dweek={self.dweek}, dday={self.dday}, dhour={self.dhour}, dminute={self.dminute}, dsecond={self.dsecond})'


edtime = Date


if __name__ == '__main__':
    counter()
