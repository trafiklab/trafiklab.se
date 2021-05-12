---
title: Combining data and APIs
---
Most of our APIs and datasets are based on different databases and systems, which results in different ids. However, some of the datasets can be combined.

## Datasets that can be combined

### GTFS Regional and GTFS Regional Realtime 

GTFS Regional and GTFS Regional Realtime are backed by the same system. They are meant to be used together.

### GTFS Sverige 2 and the ResRobot APIs

GTFS Sverige 2 uses the same stop-id's as the ResRobot APIs. This means that you can use the stops.txt file from GTFS Sverige 2 to search for nearby stops and autocomplete. The stop-id from GTFS Sverige 2 can then be used to make queries through the ResRobot API.

### SL APIs

SLs APIs are meant to be used together. They share location ids.

## Datasets that cannot be combined

### SLs APIs and ResRobot

The systems behind these APIs are too different to combine them. Both content and ids are different.

### GTFS Sverige 2 and GTFS Regional

GTFS Sverige 2 and GTFS Regional are not backed by the same data. An aggregated feed ("GTFS Sverige 3") based on the GTFS Regional data is on our roadmap, but will take some time before it's finished.