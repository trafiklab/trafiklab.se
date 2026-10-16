---
title: "News in SL Hållplatser och linjer 2"
date: 2018-10-16
draft: true

---

For a few weeks now, it has been possible to filter by mode of transport in SL Hållplatser och linjer 2. This makes it possible to distinguish between cases where the same line number is used for several different modes of transport.

For example, there have sometimes been line number clashes between Waxholmsbolaget's lines and SL's lines. See the problem described [here](https://kundo.se/org/trafiklabse/d/apier-for-tunnelbanors-stoppnamn/)

**3.5 Filtering data**

For the models line and jour, it is desirable to be able to distinguish which type of traffic the data refers to. This can be achieved by passing the optional parameter DefaultTransportModeCode, which can contain any of the Transportmode values returned when calling the transportmode model, e.g. ”BUS” or ”METRO”

E.g.:

[https://api.sl.se/api2/linedata.xml?key=[key]&model=line&DefaultTransportModeCode=METRO](http://api.sl.se/api2/linedata.xml?key=%5bnyckel%5d&model=line&DefaultTransportModeCode=METRO)

[https://api.sl.se/api2/linedata.xml?key=[key]&model=jour&DefaultTransportModeCode=BUS](http://api.sl.se/api2/linedata.xml?key=%5bnyckel%5d&model=jour&DefaultTransportModeCode=BUS)
