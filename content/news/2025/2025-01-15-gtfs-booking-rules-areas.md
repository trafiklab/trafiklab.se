---
title: "Upcoming improvements to our GTFS Regional, GTFS Sweden 3 feeds"
date: "2025-01-15"
image: /media/2025/01/gtfs-static-model.2025.png
---

Starting February 11th, all [GTFS Regional](/api/gtfs-datasets/gtfs-regional/) feeds, as well as the [GTFS Sweden 3](/api/gtfs-datasets/gtfs-sweden/) feed, will
be updated to include additional data.

A first improvement, affecting both [GTFS Regional](/api/gtfs-datasets/gtfs-regional/) and [GTFS Sweden 3](/api/gtfs-datasets/gtfs-sweden/), is the addition of
more detailed booking information for trips which need to be booked
beforehand. This is achieved by the addition of a `booking_rules.txt` file, which contains the phone number, time constraints, and information message for
advance bookings. This file is linked to departures and arrivals through 2 new columns in `stops.txt`: `pickup_booking_rule_id` and `drop_off_booking_rule_id`.
For more information regarding booking rules, please see the GTFS standard: https://gtfs.org/documentation/schedule/reference#booking_rulestxt .

A second improvement, affecting only [GTFS Sweden 3](/api/gtfs-datasets/gtfs-sweden/), is the addition of two new files, `areas.txt` and `stop_areas.txt`. These
files contain information about
so-called "Rikshållplatser", clusters of stop areas used to simplify stop lookups in (among others) ticket booking systems and national route planners such as
Resrobot. An area (rikshållplats) is defined in areas.txt, and is mapped to one or more stop through the `stop_areas.txt` file. An area has a name and id, and
can for example include a train station and two nearby bus stations. Area ids match GTFS Sverige 2 stop ids, as well as Resrobot stop ids. For more information
regarding these files, please see the GTFS specification: https://gtfs.org/documentation/schedule/reference/#areastxt

These improvements should not affect existing applications, as no existing fields are modified. You should however always ensure your application does not crash
on the addition of new columns and files.

For questions, please visit [support.trafiklab.se](https://support.trafiklab.se).