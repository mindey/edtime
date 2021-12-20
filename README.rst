Decimal Time as Epoch Day (ED)
==============================

Imagine decimal representation of days of `UNIX seconds <https://en.wikipedia.org/wiki/Unix_time>`__, call it "Epoch Days".

Then, imagine grouping the digits of such days representation as follows:

    ``dYear`` **°** ``dMonth`` **″** ``dWeek`` **′** ``day`` **T** ``dHour`` **:** ``dMinute`` **:** ``dSecond``, such that:

- 1 **dYear** = ``1000 days``, 1 **dMonth** = ``100 days``, 1 **dWeek** = ``10 days``,
- 1 **dHour** = ``0.1 days``, 1 **dMinute** = ``0.001 days``, 1 **dSecond** = ``0.00001 days``.

Yes, you just divide ``your UNIX seconds / 86400`` and group digits!

Exmaple
-------

For example, ``2021-09-30T11:25:45Z`` would be represented as ``1633001147`` UNIX seconds, therefore:
``1633001147/86400 = 18900.476238425927 = 18°9″0′0T4:76:23.8425927``, meaning it is ``18th`` **dYear**, ``9th`` **dMonth**, ``0th`` **dWeek**, ``0th`` **day**, ``4th`` **dHour**, ``76th`` **dMinute**, ``23.8425927th`` **dSecond**.

Usage
-----

``pip install edtime``

.. code:: python

    >>> from edtime import edtime
    >>> from datetime import datetime
    >>> t0 = edtime(datetime.utcnow()) # OR edtime.utcnow()
    >>> t1 = edtime.datetime(2021, 12, 20, 4, 52, 47, 954297)
    >>> str(t1)
    '18°9″8′1T2:03:33.2804365'
    >>> float(t1)
    18981.203332804365
    >>> t2 = edtime(18981.203332804365); t2
    edtime.edtime(dyear=18, dmonth=9, dweek=8, dday=1, dhour=2, dminute=3, dsecond=33.2804365)
    >>> t1 == t2
    True
    >>> t3 = edtime(16, 4, 5, 3, 4, 65, 40.5092593); t3 # 2015-01-18T11:10:11
    edtime.edtime(dyear=16, dmonth=4, dweek=5, dday=3, dhour=4, dminute=65, dsecond=40.5092593)
    >>> str(t1 + t2 + t3)
    '54°4″1′5T8:72:07.070133'
    >>> (t1 + t2 + t3).to_datetime().isoformat()
    '2118-12-26T20:55:46.908595'

**For astronomers:**

ED = ``JD - 2440587.5``

.. code:: python

    >>> from edtime import edtime
    >>> d = edtime.datetime(2000, 1, 1, 12)
    >>> d.to_jd()
    >>> 2451545.0
    >>> float(edtime.from_jd(2451545))
    10957.5

Notice
------

#. => 1 ``dSecond`` is:
    * 0.864 standard SI seconds long.
#. => 1 ``dMinute`` is:
    * 86.4 standard SI seconds long.
#. => 1 ``dHour`` is:
    * 8640 standard SI seconds long.
#. => 1 ``dWeek`` is:
    * 10 days long.
#. => 1 ``dMonth`` is:
    * 100 days long.
#. => 1 ``dYear`` is:
    * 1000 days long.
