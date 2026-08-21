---
description: "Directed email"
hidden: true 
layout: "single"
---

# New data available in the GTFS Sweden 3 feed

Over the past few months, we have been expanding the data available in the GTFS Sweden 3 feed. Here is a quick recap to
make sure you haven't missed anything.

Since May 2026, GTFS Sweden 3 has included data for all passenger trains in Sweden, based on data from Trafikverket. For
now, only scheduled data is available, but we plan to add real-time data in the coming year. The current shapes are
basic, and we also expect to make them more detailed over the coming year. However, don't expect them to follow every track
perfectly (yet), as this information is not readily available in the underlying systems.

The addition of all train traffic means the GTFS Sweden 3 feed now is on par with the old GTFS Sverige 2 feed when it
comes to traffic coverage.

Since March 2026, the `trip_short_name` and `samtrafiken_internal_trip_number` fields have been included directly in
GTFS Regional and GTFS Sweden 3. These fields contain the same data as the supplementary files, so you no longer need to
download those files separately. The supplementary files will remain available for backward compatibility.

In case you missed it, GTFS Sweden 3 has also been expanded with two new files — `areas.txt` and `stop_areas.txt` —
containing information about national stop groups (*rikshållplatser*). A national stop group combines multiple stop
areas under a shared name and ID. These IDs match those used in GTFS Sweden 2 and Resrobot, making it easier to combine
data from different sources.

If you have any questions about this change, please contact us through the
[Trafiklab support forum](https://support.trafiklab.se).
