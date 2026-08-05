---
title: "Trip number information in GTFS Regional, GTFS Sweden 3"
date: "2026-03-17"
image: '/media/2024/09/banner_departureboard_samtrafiken.jpg'
---

**Starting today, March 17th 2026, trip number information is now directly available in our GTFS Regional and GTFS
Sweden 3 datasets.**

Both public and technical trip numbers are now included directly in our GTFS Regional and GTFS Sweden 3 datasets.
Technical trip numbers are used internally by operators to distinguish between trips, and are unique for an operator on
a given start date. You may, for example, see them behind buses' windscreens. In some cases this technical trip number
may be
identical to the publicly shown trip number, but in other cases it may differ. One example where they may differ is
regional rail traffic, where trip numbers are not always
shown and line numbers are shown instead.

This information was already available in the form of our "extra files", additional CSV files which could be combined
with our GTFS files. While we continue to offer these "extra files", we recommend to build new solutions using the
trip number information which is directly embedded in our GTFS datasets. The extra files are likely to be phased out in
the future, in which case affected users will be contacted in advance.

Technical trip numbers are present in the `samtrafiken_internal_trip_number` field in trips.txt. Publicly announced trip
numbers are present in the `trip_short_name` field in `trips.txt`. In case `trip_short_name` is empty, the value from
`route_short_name` in `routes.txt` should be used. This prevents duplicate data and follows the GTFS standard, ensuring
compatibility with existing software solutions.

We hope these additional fields will make it easier to build new solutions with higher quality data based on our GTFS
datasets. 

The idea stems from feedback received from users who expressed a need for clear train number information. If
there are other improvements we could make, please let us know [on Kundo](https://support.trafiklab.se).

You can read more about this in our documentation for
the [GTFS Regional](https://www.trafiklab.se/api/gtfs-datasets/gtfs-regional/)
and [GTFS Sweden 3](https://www.trafiklab.se/api/gtfs-datasets/gtfs-sweden/) APIs. If you have any questions, please
reach out to us [through our support forum](https://support.trafiklab.se).  