EXTENDED DECIMAL TIME AND DATE
==============================
Extended `decimal time <https://en.wikipedia.org/wiki/Decimal_time>`__ (EDT).

About
-----

I've used 1000-day long periods instead of years since childhood, so why not to extend the decimal time to have them? Look at the axioms below.

This time, is simply days since POSIX zero. I realized the utility of it after creating `0oo.li/calendar <https://0oo.li/calendar/>`__, based on `detime <https://github.com/mindey/detime>`__, which squeezes months and weeks into Earth year. However, if we don't limit our selves to Earth year, we can actually get a beautiful decimal time that works: decimal representation completely coincides with the decimal representation of number of days since origin time (POSIX zero), and it makes perfect sense: it's okay to have months made of 10 weeks.

Axioms
======

#. Relationships follow:
    * 1 dyear = 10 dmonths
    * 1 dmonth = 10 dweeks
    * 1 dweek = 10 days
    * 1 dday = 10 dhours
    * 1 dhour = 100 dminutes
    * 1 dminute = 100 dseconds

#. Starting point follows:
    * Years start at 1970 Jan 1, midnight, like POSIX time.

Corollaries
===========

#. => 1 second is:
    * 0.864 standard SI seconds.
#. => 1 month is:
    * 100 days long.
#. => 1 year is:
    * 1000 days long


Usage
-----

``pip install edtime``

.. code:: bash

    >>> from edtime import edtime
    >>> edtime([unix day | datetime.datetime | dtimetuple])

    >>> edtime.utcnow()
    edtime.edtime(dyear=18, dmonth=9, dweek=5, dday=8, dhour=7, dminute=11, dsecond=11.0)

    >>> edtime.datetime(2021, 9, 30)
    edtime.edtime(dyear=18, dmonth=9, dweek=0, dday=0, dhour=0, dminute=0, dsecond=0.0)

