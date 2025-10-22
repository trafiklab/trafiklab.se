---
title: NeTEx Regional
layout: "single"
weight: 30
aliases: 
  - /api/netex-regional-static-data
  - /node/27769/documentation
  - /api/trafiklab-apis/netex-regional/
  - /api/trafiklab-apis/netex-regional/static/
  - /api/trafiklab-apis/netex-regional/siri/
  - /api/trafiklab-apis/netex-regional/licence/
date: 2019-11-22
---
{{% warning %}} **NeTEx files on Trafiklab will be upgraded to version 1.0.15.** <br>
NeTEx version 1.0.11 will be upgraded to version 1.0.15 on October 28th, 2025.

Version 1.0.15 includes breaking changes, these breaking changes only require minor adjustments. For example spelling fixes in the enums, such as `WHEECHAIR_ASSISTANCE` now corrected to `WHEELCHAIR_ASSISTANCE`

More information will be sent by email to all users with an active NeTEx API key.
{{% /warning %}}

NeTEx regional is a set of NeTEx feeds of high quality. These feeds contain all data present in GTFS Regional, as 
well as additional data which can't be represented in GTFS.

## What does this dataset contain?
This dataset contains high quality detailed data, both static and real-time, in the NeTEx format. Each dataset contains
data for a specific region or operator.

### Data format
The data is in the NeTEx (**Ne**twork and **T**imetable **Ex**change) format. This is a format in which all European
operators have to publish their data. The data is aimed at both operator-to-traveller communication and internal
communication between different organizations. Samtrafiken
follows [the Nordic NeTEx Profile, which is documented by Entur](https://enturas.atlassian.net/wiki/spaces/PUBLIC/pages/728891481/Nordic+NeTEx+Profile).

For more technical information about the NeTEx dataset that is provided on Trafiklab, please
visit [Samtrafiken Open Data - NeTEx](https://samtrafiken.atlassian.net/wiki/spaces/SamtrafikenOpenData/pages/989233182/Samtrafiken+NeTEx+export).

### Updates
The static data in this dataset is updated on a daily basis, typically between 03:00 and 07:00.

### Operators covered by this dataset

{{% stip-data-availability abbreviation scheduled realtime vehiclepositions occupancy %}}

### Breaking changes
This dataset has the **stable** status. This means that the fields can be added without prior warning, but when changes
to existing fields are made, you will get three months to update your implementations.

## Static data
The static NeTEx Regional dataset contains files describing all planned public transport data, with more technical
details compared to the GTFS Regional feeds.

In order to retrieve the static data you need an API key. Technical details for fetching the data can be found in the
API's OpenAPI specification.

{{% note %}}
**Where to download**

The dataset can be accessed through the following URL:
[https://opendata.samtrafiken.se/netex/{operator}/{operator}.zip?key={apikey}](https://opendata.samtrafiken.se/netex/{operator}/{operator}.zip?key={apikey}).

Replace `{operator}` with the abbreviation of the operator you want to download. These abbreviations can be found in the
OpenAPI specification, but are also listed on [the top of this page](#operators-covered-by-this-dataset). Replace `{apikey}` with your own API key.
If you don´t have a key yet, read [here](/docs/using-trafiklab/getting-api-keys) on how to get one.
{{% /note %}}

<div style="max-width: 270px">

#### API key levels

| Level  | Maximum calls per minute | Maximum calls per month |
|:-------|:------------------------:|:-----------------------:|
| Bronze |            10            |           50            |
| Silver |            10            |           250           |
| Gold   |            20            |          2500           |

</div>

{{% page-ref "/api/netex-datasets/netex-regional/netex-regional-specification" %}}

### Example download URLs

Below are some example download URLs. For a complete list all operators with data available,
check [the top of this page](#operators-covered-by-this-dataset).

#### Regional operators

| Operator                                | Static data                                                                                                                                      |
|-----------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| **Skånetrafiken (Skåne län)**           | [https://opendata.samtrafiken.se/netex/skane/skane.zip?key=<api-nyckel>](https://opendata.samtrafiken.se/netex/skane/skane.zip?key=<api-nyckel>) |
| **SL (Stockholm län)**                  | [https://opendata.samtrafiken.se/netex/sl/sl.zip?key=<api-nyckel>](https://opendata.samtrafiken.se/netex/sl/sl.zip?key=<api-nyckel>)             |
| **UL (Uppsala län)**                    | [https://opendata.samtrafiken.se/netex/ul/ul.zip?key=<api-nyckel>](https://opendata.samtrafiken.se/netex/ul/ul.zip?key=<api-nyckel>)             |
| **Östgötatrafiken (Östergötlands län)** | [https://opendata.samtrafiken.se/netex/otraf/otraf.zip?key=<api-nyckel>](https://opendata.samtrafiken.se/netex/otraf/otraf.zip?key=<api-nyckel>) |

#### Commercial operators

| Operator | Static data                                                                                                                          | 
|----------|--------------------------------------------------------------------------------------------------------------------------------------|
| **SJ**   | [https://opendata.samtrafiken.se/netex/sj/sj.zip?key=<api-nyckel>](https://opendata.samtrafiken.se/netex/sj/sj.zip?key=<api-nyckel>) |


## Realtime data (SIRI)

Service Interface for Real-time Information (SIRI) is a data-format for real-time data. This data contains updates and real-time changes to the static NeTEx data. The two data formats should be used together, since the real-time data refers to elements defined in the static data.

This SIRI feed is based on version 1.1 of the Norwegian SIRI profile. The profile is based on SIRI 2.0. The full profile documentation can be found here: https://enturas.atlassian.net/wiki/spaces/PUBLIC/pages/637370420/Norwegian+SIRI+profile

{{% info %}}
**Availability of regional data** differs per operator. See the [top of this page](#operators-covered-by-this-dataset) to see which data is provided
by the operator(s) you are interested in.
{{% /info %}}

{{% note %}}
**Where to download**

The dataset can be accessed through the following URL:

- [https://opendata.samtrafiken.se/siri/{operator}/SituationExchange.xml?key={apikey}](https://opendata.samtrafiken.se/siri/{operator}/SituationExchange.xml?key={apikey})
- [https://opendata.samtrafiken.se/siri/{operator}/EstimatedTimetable.xml?key={apikey}](https://opendata.samtrafiken.se/siri/{operator}/EstimatedTimetable.xml?key={apikey})
- [https://opendata.samtrafiken.se/siri/{operator}/VehicleMonitoring.xml?key={apikey}](https://opendata.samtrafiken.se/siri/{operator}/VehicleMonitoring.xml?key={apikey})

Replace `{operator}` with the abbreviation of the operator you want to download. These abbreviations can be found in the
OpenAPI specification, but are also listed on [the top of this page](#operators-covered-by-this-dataset). Replace `{apikey}` with your own API key.
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

### Available Siri data

#### Estimated Timetables (ET)

SIRI-ET is used to model the status of existing VehicleJourneys and to ensure that deviations from the planned data (for
the same operating day) such as cancellations, additional departures, delays, detours and changes in stops, can be
published on short notice. The data is linked to objects in the planned data by use of ID's, which ensures data quality.
For more information and technical specifications, see [SIRI-ET](https://enturas.atlassian.net/wiki/spaces/PUBLIC/pages/637370392/SIRI-ET).

#### Situation Exchange (SX)

SIRI-SX is used to model textual descriptions of disruptions, or deviations from the planned public transport
information. The messages can be applied directly to stops, lines, vehicles etc. in the already existing public
transport data by the use of ID references. For more information and technical specifications, see [SIRI-SX](https://enturas.atlassian.net/wiki/spaces/PUBLIC/pages/637370605/SIRI-SX).

#### Vehicle Monitoring (VM)

SIRI-VM is used to model vehicle-movements and their progress compared to a planned timetable. The data is linked to
objects in the planned data by use of ID's, which ensures data quality. For more information and technical specifications, see [SIRI-VM](https://enturas.atlassian.net/wiki/spaces/PUBLIC/pages/637370425/SIRI-VM).

## Licence

Data from the NeTEx Regional API is available under the CC0 1.0 Universal (CC0 1.0) Public Domain Dedication license.

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