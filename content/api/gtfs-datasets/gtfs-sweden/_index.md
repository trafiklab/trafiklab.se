---
title: GTFS Sweden 3
layout: "single"
weight: 35
---

GTFS Sweden 3 is a high quality GTFS feed containing most of the public transport data of Sweden. This dataset contains 
high quality detailed data, both static and real-time, in the GTFS format. This dataset is an aggregated dataset of all 
the different datasets in the [GTFS Regional API](/api/gtfs-datasets/gtfs-regional/). There is a single GTFS feed for 
static data. The realtime feeds are, for performance reasons, split up by specific regions or operators. 

## What does this dataset contain?
At the moment this dataset does not contain all of the public transport data of Sweden.
If that is what you are looking for we recommend [GTFS Sverige 2](/api/gtfs-datasets/gtfs-sverige-2/), which is less 
detailed but does contain all of the public transport data of Sweden.

### Data format
The data is in the GTFS format, and makes use of the GTFS Extensions. Realtime data follows the 
GTFS-Realtime(GTFS-RT) standard, and is stored in the protobuf format. This data is also available in the NeTEx format. 
For the NeTEx format, see the [NeTEx Sweden API](/api/netex-datasets/netex-sweden/).

### Updates
The static data in this dataset is updated on a daily basis. The real-time data receives multiple updates 
per minute, see [realtime data](#realtime-data) for more information.

### Operators covered by this dataset
{{% include "/headless/stip-data-availability.md" %}}

### Breaking changes
These datasets have the **stable** status. This means that we will communicate when fields are 
added, or changed. When breaking changes are made, you will get three months or more to update your implementations.

## Static data
The static GTFS Sweden 3 dataset contains files describing all planned public transport data. It can be combined
with optional realtime data available in the GTFS Sweden Realtime data API.
The data in this dataset is updated on a daily basis, typically between 05:00 and 06:00.

In order to retrieve the static data you need an API key. Technical details for fetching the data can be found in the
API's OpenAPI specification. Trafiklabs GTFS documentation can help you to get started with GTFS files.

{{% note %}}
**Where to download**

The dataset can be accessed through the following URL:
[https://opendata.samtrafiken.se/gtfs-sweden/sweden.zip?key={apikey}](https://opendata.samtrafiken.se/gtfs-sweden/sweden.zip.zip?key={apikey}).

Replace `{apikey}` with your own API key. If you don´t have a key yet, read [here](/docs/using-trafiklab/getting-api-keys) on how to get one.
{{% /note %}}

<div style="max-width: 270px">

#### API key levels

| Level  | Maximum calls per minute | Maximum calls per month |
|:-------|:------------------------:|:-----------------------:|
| Bronze |            10            |           50            |
| Silver |            10            |           250           |

</div>

{{% page-ref "/api/gtfs-datasets/gtfs-sweden/static-specification"
"/docs/using-trafiklab-data/the-protobuf-file-format"  %}}

### GTFS Extensions

The extensions are the same as in [the GTFS Regional API](/api/gtfs-datasets/#gtfs-extensions).

### Notes and known issues

See the documentation for [the GTFS Regional API](/api/gtfs-datasets/gtfs-regional/#notes-and-known-issues).

## Realtime data 
The realtime GTFS Sweden data consists of data feeds describing disturbances, deviations, delays, and even realtime
GPS vehicle positions, separated per region or operator just like the GTFS Regional API (for performance reasons).
It should be combined with static data available in the GTFS Sweden 3 API.

In order to retrieve the data you need an API key. Technical details for fetching the data can be found in the
API's OpenAPI specification. Trafiklabs GTFS documentation can help you to get started with GTFS files.

{{% info %}}
**Availability of regional data** differs per operator. See the [top of this page](#operators-covered-by-this-dataset) to see which data is provided
by the operator(s) you are interested in.
{{% /info %}}

{{% note %}}
**Where to download**

The dataset can be accessed through the following URLs:
- [https://opendata.samtrafiken.se/gtfs-rt-sweden/{operator}/ServiceAlertsSweden.pb?key={apikey}](https://opendata.samtrafiken.se/gtfs-rt-sweden/{operator}/ServiceAlertsSweden.pb?key={apikey})
- [https://opendata.samtrafiken.se/gtfs-rt-sweden/{operator}/TripUpdatesSweden.pb?key={apikey}](https://opendata.samtrafiken.se/gtfs-rt-sweden/{operator}/TripUpdatesSweden.pb?key={apikey})
- [https://opendata.samtrafiken.se/gtfs-rt-sweden/{operator}/VehiclePositionsSweden.pb?key={apikey}](https://opendata.samtrafiken.se/gtfs-rt-sweden/{operator}/VehiclePositionsSweden.pb?key={apikey})

Replace `{operator}` with the abbreviation of the operator you want to download. These abbreviations can be found in the
OpenAPI specification, but are also listed on [top of this page](#operators-covered-by-this-dataset). Replace `{apikey}` with your own API key.
If you don´t have a key yet, read [here](/docs/using-trafiklab/getting-api-keys) on how to get one.
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
<br>

### Using real-time data

You can read more about how to use real-time data in our GTFS format documentation:

{{% page-ref page="/docs/using-trafiklab-data/the-protobuf-file-format/" %}}
<br>

## Extra files
Extra files are files which provide additional information about the information in the GTFS files. They are not part of
the GTFS standard, but contain the information which is needed to link the GTFS files to internal operator systems, or
other data which is delivered by the operator.

The extra file can be fetched by taking the URL to the normal GTFS zip file, and adding \__extra_ in the filename. For
example, the file "sweden.zip" becomes "_sweden\_extra.zip_". These files use the same API key as the static data, and
count against the same quota.

In order to retrieve the static data you need an API key. Technical details for fetching the data can be found in the
API's OpenAPI specification. Trafiklabs GTFS documentation can help you to get started with GTFS files.

{{% note %}}
**Where to download**

The dataset can be accessed through the following URL:
[https://opendata.samtrafiken.se/gtfs-sweden/sweden.zip_extra.zip?key={apikey}](https://opendata.samtrafiken.se/gtfs-sweden/sweden.zip_extra.zip?key={apikey}).

Replace `{apikey}` with your own API key.
{{% /note %}}

### trips\_dated\_vehicle\_journey.txt

This file links every GTFS trip\_id to their source GID in the Noptis data. This file is meant for those who want to
combine or integrate their systems with internal systems of transport agencies. Note that this data is only correct for
operators who deliver data to Samtrafiken in the Noptis DOI or Noptis DII format.

The TransportAuthority-number part of the Gid might not always be correct as a consequence of the aggregation process.
We will update this documentation with further instructions in the future.

## Licence
Data from the GTFS Sweden 3 API is available under the CC0 1.0 Universal (CC0 1.0) Public Domain Dedication license.

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