---
title: Departure boards
description: We'll discuss which data-sources you need for departure boards
---

A departure board contains simple yet extremely useful public transport data. Departure and arrival board APIs return
departures and arrivals for a stations based on its id. This means that showing a departure board consists of two parts:
finding the station id, and fetching the data.

### For apps, small websites, ...

If you simply want to show the next departures on a digital signage board in shopping mall, on a smartphone, smartwatch,
smartmirror, ... you can make use
of [the ResRobot Stolptidstabeller 2 API](/api/trafiklab-apis/resrobot-v2/timetables.md)
. This API provides an easy way to fetch the departures or arrivals at any stop, either now or in the future.

#### Finding the id of a stop

In order to specify which station you want data from, you will need to obtain the id for that station. Follow the link
below to read about the different methods to obtain the id of a stop for the ResRobot APIs.

{{% page-ref page="obtaining-stop-ids" %}}

#### Getting the departures or arrivals

The departures or arrivals for the chosen id can be obtained by a single request to
our [ResRobot Stolptidstabeller 2 API](/api/trafiklab-apis/resrobot-v2/timetables.md).
Read the API documentation for more information about the parameters and response format.

### For large websites and analytics

Larger websites or apps that need to handle a lot of traffic, it might be easier to create your own, local API. This can
be done either through a self-hosted [OpenTripPlanner](https://github.com/opentripplanner) instance, fed
with [GTFS Sverige 2](/api/trafiklab-apis/gtfs-sverige-2/)
or [GTFS Regional](/api/trafiklab-apis/gtfs-regional/) data, or by creating your own
wrapper around our GTFS data.
