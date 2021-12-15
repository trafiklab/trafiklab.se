---
title: Realtime data
aliases:
  - "api/gtfs-regional-realtime"
weight: 20
date: 2019-06-10
---

The realtime GTFS Regional data consists of data feeds describing disturbances, deviations, delays, and even realtime 
GPS vehicle positions, separated per region or operator. It should be combined with static data available in the GTFS 
Regional API.

In order to retrieve the data you need an API key. Technical details for fetching the data can be found in the
API's OpenAPI specification. Trafiklabs GTFS documentation can help you to get started with GTFS files.

{{% info %}}
**Availability of regional data** differs per operator. See the [overview page](_index.md) to see which data is provided
by the operator(s) you are interested in.
{{% /info %}}

{{% note %}}
**Where to download**

The dataset can be accessed through the following URLs:
- [https://opendata.samtrafiken.se/gtfs-rt/{operator}/ServiceAlerts.pb?key={apikey}](https://opendata.samtrafiken.se/gtfs-rt/{operator}/ServiceAlerts.pb?key={apikey})
- [https://opendata.samtrafiken.se/gtfs-rt/{operator}/TripUpdates.pb?key={apikey}](https://opendata.samtrafiken.se/gtfs-rt/{operator}/TripUpdates.pb?key={apikey})
- [https://opendata.samtrafiken.se/gtfs-rt/{operator}/VehiclePositions.pb?key={apikey}](https://opendata.samtrafiken.se/gtfs-rt/{operator}/VehiclePositions.pb?key={apikey})

Replace `{operator}` with the abbreviation of the operator you want to download. These abbreviations can be found in the
OpenAPI specification, but are also listed on the [static data documentation page](static.md). Replace `{apikey}` with your own API key.
{{% /note %}}

{{% page-ref page="/docs/using-trafiklab/getting-api-keys" %}}

## Available real-time data

### ServiceAlerts

Service alerts allow you to get information about disruptions on the transit network. This can anything from planned
roadworks (a certain stop might not get served for a few days) to electricity outages on a rail network. ServiceAlerts
are broad and general information. Delays and cancellations of individual trips are usually communicated
using [Trip updates](#tripupdates).
See [the table on the GTFS Regional overview page](./_index.md#which-operators-are-covered-by-this-dataset) to find out which
operators are supported (Realtime data column).

{{% info %}} ServiceAlerts can remain unchanged for relatively long periods (for example a couple of
hours). You can prevent unnecessary downloads by making use
of [Conditional HTTP requests](/docs/using-trafiklab-data/best-practices/conditional-get-requests.md). {{% 
/info %}}

### TripUpdates

Trip updates contain real-time departure and arrival times for individual trips. This means you can get the current,
estimated delay for each vehicle on each stop.
See [the table on the GTFS Regional overview page](./_index.md#which-operators-are-covered-by-this-dataset) to find out which
operators are supported (Real-time data column).

{{% warning %}} In some cases it isn't possible to link certain delays to a specific trip. In this case, they
may be linked to a route instead. {{% /warning %}}

### VehiclePositions

The vehiclepositions.pb feed contains the GPS positions for all operators. Depending on the operator, these positions
are updated every 1 to 3 seconds. The availability of this data is indicated in a separate column
in [the GTFS Regional availability table](./_index.md#which-operators-are-covered-by-this-dataset).

## Using real-time data

You can read more about how to use real-time data in our GTFS format documentation:

{{% page-ref page="/docs/using-trafiklab-data/using-gtfs-files/" %}}
