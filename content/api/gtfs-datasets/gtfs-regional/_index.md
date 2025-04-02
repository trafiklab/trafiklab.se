---
title: GTFS Regional
layout: "single"
weight: 10
aliases:
  - /api/gtfs-regional-static-data
  - /api/gtfs-regional-realtime
  - /api/trafiklab-apis/gtfs-regional/
  - /api/trafiklab-apis/gtfs-regional/static/
  - /api/trafiklab-apis/gtfs-regional/realtime/
  - /api/trafiklab-apis/gtfs-regional/historical-data/
  - /api/trafiklab-apis/gtfs-regional/extra-files/
  - /api/trafiklab-apis/gtfs-regional/licence/
---

GTFS regional is a set of GTFS feeds of high quality, with realtime data and even realtime GPS positions on 
vehicles for some operators. This dataset contains high quality detailed data, both static and real-time, in the GTFS 
format. Each dataset contains data for a specific region or operator. While the combined GTFS feeds do cover all 
regional public transport operators, and some private companies as well, each feed uses their own ids for each stop. If 
you are looking for an aggregated national feed, please look at GTFS Sverige 2.

## What does this dataset contain?

This dataset contains high quality detailed data, both static and real-time, in the GTFS format. Each dataset contains
data for a specific region or operator.

### Data format

The data is in the GTFS format, and makes use of [GTFS Extensions](/api/gtfs-datasets/overview/extensions/#extended-route-types).
Realtime data follows the GTFS-Realtime(GTFS-RT) standard, and is stored in the protobuf format.

This data is also available in the NeTEx format. For the NeTEx format, see the [NeTEx regional API](/api/netex-datasets/netex-regional/).

### Updates

The static data in this dataset is updated on a daily basis. The real-time data receives multiple updates
per minute, see [realtime data](#realtime-data) for more information.

### Operators covered by this dataset

{{% stip-data-availability abbreviation scheduled realtime vehiclepositions occupancy %}}

### Breaking changes

Both the static and realtime data feeds are stable. While we add new data all the time, we don't
make breaking changes. Should we need to make a breaking change, we'll inform users first, and you'll have around
6 months time to make the necessary adjustments to your code.

## Static data

The static GTFS Regional dataset contains files describing all planned public transport data. It can be combined
with optional realtime data available in the GTFS Realtime data API.
The data in this dataset is updated on a daily basis, typically between 03:00 and 07:00.

In order to retrieve the static data you need an API key. Technical details for fetching the data can be found in the
API's OpenAPI specification. Trafiklabs GTFS documentation can help you to get started with GTFS files.

{{% note %}}
**Where to download**

The dataset can be accessed through the following URL:
[https://opendata.samtrafiken.se/gtfs/{operator}/{operator}.zip?key={apikey}](https://opendata.samtrafiken.se/gtfs/{operator}/{operator}.zip?key={apikey})

Replace `{operator}` with the abbreviation of the operator you want to download. These abbreviations can be found in the
OpenAPI specification, but are also listed here [above](#operators-covered-by-this-dataset).
Replace `{apikey}` with your own API key. If you don´t have a key yet,
read [here](/docs/using-trafiklab/getting-api-keys) on how to get one.
{{% /note %}}

<div style="max-width: 270px">

#### API key levels

| Level  | Maximum calls per minute | Maximum calls per month |
|:-------|:------------------------:|:-----------------------:|
| Bronze |            10            |           50            |
| Silver |            10            |           250           |
| Gold   |            20            |          2500           |

</div>
{{% page-ref "/api/gtfs-datasets/gtfs-regional/static-specification" "/api/gtfs-datasets/overview"  %}}
<br>

### Notes and known issues

- Since GTFS defines vehicle types on a route-level, the vehicle-type for some trips might be incorrect if those
  trips deviate from the route's most common vehicle type. This can for example happen when some trips on a bus
  route are executed with a taxi instead of a bus.
- Calendar.txt is only used to define validity periods, not to define service dates. Actual service dates are
  described in calendar_dates.txt.
- When both `route_short_name` and `route_long_name` have a value, `route_long_name` should be considered the correct
  line name. In this case, `route_short_name` should only be used for systems that cannot show the long name.
- There might be differences between GTFS Sverige 2 and GTFS Regional Static, for example in the validity period for
  routes which might be longer in GTFS Sverige 2. This is due to the higher detail of the GTFS Regional Static dataset.
- GTFS Regional contains transfers between stop points within the same stop, as well as transfers between different
  stop areas and transfers to and from specific trips.
- [Extended route types are used](/api/gtfs-datasets/overview/extensions/#extended-route-types). Not all routes can however be classified in detail
  depending on the data source, which may lead to some operators using more specific route_types, while the GTFS feeds for other similar operators still 
  may use the more generic `route_type` 100.

## Realtime data

The realtime GTFS Regional data consists of data feeds describing disturbances, deviations, delays, and even realtime
GPS vehicle positions, separated per region or operator. It should be combined with static data available in the GTFS
Regional API.

In order to retrieve the data you need an API key. Technical details for fetching the data can be found in the
API's OpenAPI specification. Trafiklabs GTFS documentation can help you to get started with GTFS files.

{{% info %}}
**Availability of regional data** differs per operator. See the [top of this page](#operators-covered-by-this-dataset)
to see which data is provided
by the operator(s) you are interested in.
{{% /info %}}

{{% note %}}
**Where to download**

The dataset can be accessed through the following URLs:
- [https://opendata.samtrafiken.se/gtfs-rt/{operator}/ServiceAlerts.pb?key={apikey}](https://opendata.samtrafiken.se/gtfs-rt/{operator}/ServiceAlerts.pb?key={apikey})
- [https://opendata.samtrafiken.se/gtfs-rt/{operator}/TripUpdates.pb?key={apikey}](https://opendata.samtrafiken.se/gtfs-rt/{operator}/TripUpdates.pb?key={apikey})
- [https://opendata.samtrafiken.se/gtfs-rt/{operator}/VehiclePositions.pb?key={apikey}](https://opendata.samtrafiken.se/gtfs-rt/{operator}/VehiclePositions.pb?key={apikey})

Replace `{operator}` with the abbreviation of the operator you want to download. These abbreviations can be found in
the OpenAPI specification, but are also listed at the [top of this page](#operators-covered-by-this-dataset).
Replace `{apikey}` with your own API key. If you don´t have a key yet, read [here](/docs/using-trafiklab/getting-api-keys) on how to get one.
{{% /note %}}

<div style="max-width: 270px">

#### API key levels

| Level  | Maximum calls per minute | Maximum calls per month |
|:-------|:------------------------:|:-----------------------:|
| Bronze |            50            |         30 000          |
| Silver |           250            |        2 000 000        |
| Gold   |           500            |       22 500 000        |

</div>

### Available real-time data

#### ServiceAlerts

Service alerts allow you to get information about disruptions on the transit network. This can be anything from planned
roadworks (a certain stop might not get served for a few days) to electricity outages on a rail network. ServiceAlerts
are broad and general information. Trafiklab's serviceAlerts are updated every 15 seconds.

Delays and cancellations of individual trips are usually communicated
using [Trip updates](#tripupdates).
See [the GTFS Regional availability table](#operators-covered-by-this-dataset) to find out which
operators are supported (Realtime data column).

{{% info %}} ServiceAlerts can remain unchanged for relatively long periods (for example a couple of
hours). You can prevent unnecessary downloads by making use
of [Conditional HTTP requests](/docs/using-trafiklab-data/best-practices/conditional-get-requests.md).
{{% /info %}}

#### TripUpdates

Trip updates contain real-time departure and arrival times for individual trips. This means you can get the current,
estimated delay for each vehicle on each stop. Trafiklab's tripUpdates are updated every 15 seconds.
See [the GTFS Regional availability table](#operators-covered-by-this-dataset) to find out which
operators are supported (Real-time data column).

{{% warning %}} In some cases it isn't possible to link certain delays to a specific trip. In this case, they
may be linked to a route instead. {{% /warning %}}

#### VehiclePositions

The vehiclepositions.pb feed contains the GPS positions for all operators. Depending on the operator, Trafiklab's
vehiclepositions are updated every 2 seconds. The availability of this data is indicated in a separate column
in [the GTFS Regional availability table](#operators-covered-by-this-dataset).

### Using real-time data

You can read more about how to use real-time data in our GTFS format documentation:

{{% page-ref page="/api/gtfs-datasets/overview" %}}
<br>

## Historical data
Historical GTFS data can be accessed through the KoDa API.

{{% page-ref page="/api/our-apis/koda" %}}
<br>

## Extra files
Extra files are files which provide additional information about the information in the GTFS files. They are not part of
the GTFS standard, but contain the information which is needed to link the GTFS files to internal operator systems, or
other data which is delivered by the operator.

The extra files can be fetched by taking the URL to a normal GTFS zip file, and adding \__extra_ in the filename. For
example, the file "otraf.zip" becomes "_otraf\_extra.zip_". These files use the same API key as the static data, and
count against the same quota.

In order to retrieve the static data you need an API key. Technical details for fetching the data can be found in the
API's OpenAPI specification. Trafiklabs GTFS documentation can help you to get started with GTFS files.

{{% note %}}
**Where to download**

The dataset can be accessed through the following URL:
[https://opendata.samtrafiken.se/gtfs/{operator}/{operator}_extra.zip?key={apikey}](https://opendata.samtrafiken.se/gtfs/{operator}/{operator}_extra.zip?key={apikey}).

Replace `{operator}` with the abbreviation of the operator you want to download. These abbreviations can be found in the

[//]: # (OpenAPI specification, but are also listed on the [static data documentation page]&#40;static.md&#41;. Replace `{apikey}` with your own API key.)
{{% /note %}}

### trips\_dated\_vehicle\_journey.txt

This file links every GTFS trip\_id to their source GID in the Noptis data. This file is meant for those who want to
combine or integrate their systems with internal systems of transport agencies. Note that this data is only correct for
operators who deliver data to Samtrafiken in the Noptis DOI or Noptis DII format.

## Licence
Data from the GTFS Regional API is available under the CC0 1.0 Universal (CC0 1.0) Public Domain Dedication license.

#### Summary

The person who associated a work with this deed has dedicated the work to the public domain by waiving all of his or her
rights to the work worldwide under copyright law, including all related and neighboring rights, to the extent allowed by
law.

#### Other Information

In no way are the patent or trademark rights of any person affected by CC0, nor are the rights that other persons may
have in the work or in how the work is used, such as publicity or privacy rights.

Unless expressly stated otherwise, the person who associated a work with this deed makes no warranties about the work,
and disclaims liability for all uses of the work, to the fullest extent permitted by applicable law.

When using or citing the work, you should not imply endorsement by the author or the affirmer.

{{% info %}}
More information, as well as the complete license text, can be found at
[the creative commons website](https://creativecommons.org/publicdomain/zero/1.0/deed.en).
{{% /info %}} 
