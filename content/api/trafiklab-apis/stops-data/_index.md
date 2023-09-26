---
title: Stops data
layout: "single"
weight: 37
date: 2022-06-01
---

The stops data API contains detailed data of Sweden's national stops and their mappings to stops from the [GTFS Regional](/api/trafiklab-apis/gtfs-regional/)
and [Netex Regional](/api/trafiklab-apis/netex-regional/) APIs.

All of Sweden's stops are included in this dataset.

{{% note %}}
**Where to download**

The dataset can be accessed through the following URL:
[https://opendata.samtrafiken.se/stopsregister-netex-sweden/sweden.zip?key={apikey}](https://opendata.samtrafiken.se/stopsregister-netex-sweden/sweden.zip?key={apikey}).

Replace `{apikey}` with your own `stops data` API key. If you don´t have a key yet, read [here](/docs/using-trafiklab/getting-api-keys) on how to get one.
{{% /note %}}

#### API key levels

| Level  | Maximum calls per minute | Maximum calls per month |
|:-------|:------------------------:|:-----------------------:|
| Bronze |            10            |           50            |
| Silver |            10            |           250           |

### What does this dataset contain?

This dataset contains all of Sweden's stops in the NeTEx format. There are multiple different KeyValue-elements for each StopPlace and Quay which
contain information that does not fit into any standard Netex elements. Many of these extra KeyValue-elements are mostly useful for operators consuming the
data.

This data is based on the data available in the regional data feeds ([GTFS Regional](/api/trafiklab-apis/gtfs-regional/), [Netex Regional](/api/trafiklab-apis/netex-regional/)) and enriched by Samtrafiken. If you are interested in the
original data for a specific PTA, please see the regional datasets.

### Data format

The data is in the NeTEx (**Ne**twork and **T**imetable **Ex**change) format. This is a format in which all European
operators have to publish their data. The data is aimed at both operator-to-traveller communication and internal
communication between different organizations. Samtrafiken
follows [the Nordic NeTEx Profile, which is documented by Entur](https://enturas.atlassian.net/wiki/spaces/PUBLIC/pages/728891481/Nordic+NeTEx+Profile).

### KeyValues explained

Most of the KeyValues refer to DataSource IDs. These IDs can currently be transformed to actual datasources/authorities through
the [NeTEx Sweden API](/api/trafiklab-apis/netex-sweden/)
, by mapping the DataSource IDs to Authority.PrivateCode in the `_shared_data.xml` file. In the future we are going to provide a better way of matching
DataSource IDs to datasources/authorities.

The Keys that are used for mappings all start with the name `local-` and are pipe symbol separated and then colon symbol separated values.
For example a StopPlace with the Key `local-number` with the Value `7:64204|12:7051|74:40|8:64204|100:4` should be interpreted as list of five different values,
where each part is further interpreted by separating by the colon symbol, `7:64204` meaning datasource 7 has local number 64204 for this stop. The table below
explains the meaning of each Key-Value.

"Gid" matches part of the `StopPlace.Id` (or `Quay.Id`) in Netex Regional, as well as the `stop_id` from `stops.txt` in GTFS Regional.

| Key                           | Explanation                                                                                                                                                                           |
|:------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| owner                         | This value indicates which datasource should be considered the owner of this StopPlace and its Quays.<br/>Often this is the county's public authority in which the StopPlace resides. |
| data-from                     | Which datasource actually provides the data for this StopPlace and its Quays.                                                                                                         |
| rikshallplats                 | Samtrafikens Rikshållplatsnummer for this StopPlace, which is used in the GTFS Sverige 2 API (and other places).                                                                      |
| trafikverket-name             | This StopPlace's name as assigned by Trafikverket.                                                                                                                                    |
| trafikverket-signatures       | This StopPlace's signature as assigned by Trafikverket. There can be multiple signatures using pipe character "&#124;" between each signature.                                        |
| preliminary                   | Indicates that this StopPlace has not been validated and might be subjected to change.                                                                                                |
| stip.*                        | Any Keys starting with "stip." refers directly to values found in the "data-from" datasource's corresponding data.                                                                    |
| local-name                    | Format is DataSource:Gid:Name.                                                                                                                                                        |
| local-gid                     | Format is DataSource:Gid.                                                                                                                                                             |
| local-number                  | Format is DataSource:Number.                                                                                                                                                          |
| local-journeypatternpoint-gid | Format is DataSource:Gid.                                                                                                                                                             |
| local-stoppoint-gid           | Format is DataSource:Gid.                                                                                                                                                             |
| local-designation             | Format is DataSource:Designation.                                                                                                                                                     |
| sellable                      | This value will be true if the StopPlace is sellable through samtrafiken systems, and false if not.                                                                                   |

### How often is this dataset updated?

The data in this dataset is updated on a daily basis, typically between 07:50 and 9:00.

### How often does the data format changes? Do breaking changes happen?

This dataset has the **stable** status. This means that we will communicate when fields are added, or changed. When
breaking changes are made, you will get three months or more to update your implementations.
