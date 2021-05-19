---
title: Realtime data
---

{{% info %}} For technical details about HTTP headers, URLs, and response structures, please use the OpenAPI
Specification available on our developer portal. {{% /info %}}

## Retrieving real-time data

In order to retrieve the static data you need an API key. Follow the link below to read more about API keys.

{{% page-ref page="/data/using-trafiklab/getting-api-keys" %}}

## Available real-time data

### ServiceAlerts

Service alerts allow you to get information about disruptions on the transit network. This can anything from planned
roadworks (a certain stop might not get served for a few days) to electricity outages on a rail network. ServiceAlerts
are broad and general information. Delays and cancellations of individual trips are usually communicated
using [Trip updates](gtfs-regional-realtime.md#tripupdates).
See [the table on the GTFS Regional overview page](./#which-operators-are-covered-by-this-dataset) to find out which
operators are supported (Realtime data column).

{{% info %}} ServiceAlerts can remain unchanged for relatively long periods (for example a couple of
hours). You can prevent unnecessary downloads by making use
of [Conditional HTTP requests](../../../../using-trafiklab-data/best-practices/conditional-get-requests.md). {{% 
/info %}}

### TripUpdates

Trip updates contain real-time departure and arrival times for individual trips. This means you can get the current,
estimated delay for each vehicle on each stop.
See [the table on the GTFS Regional overview page](./#which-operators-are-covered-by-this-dataset) to find out which
operators are supported (Real-time data column).

{{% warning %}} In some cases it isn't possible to link certain delays to a specific trip. In this case, they
may be linked to a route instead. {{% /warning %}}

### VehiclePositions

The vehiclepositions.pb feed contains the GPS positions for all operators. Depending on the operator, these positions
are updated every 1 to 3 seconds. The availability of this data is indicated in a separate column
in [the GTFS Regional availability table](./#which-operators-are-covered-by-this-dataset).

## Using real-time data

You can read more about how to use real-time data in our GTFS format documentation:

{{% page-ref page="/data/using-trafiklab-data/using-gtfs-files/" %}}
