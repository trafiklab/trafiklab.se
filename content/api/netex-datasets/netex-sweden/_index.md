---
title: NeTEx Sweden
layout: "single"
weight: 35
date: 2022-06-01
aliases:
  - /api/trafiklab-apis/netex-sweden/
  - /api/trafiklab-apis/netex-sweden/static/
  - /api/trafiklab-apis/netex-sweden/licence/
---

NeTEx Sweden is a NeTEx feed of high quality. The feed contains all data present in GTFS Sweden, as
well as additional data which can't be represented in GTFS.

At the moment this dataset does not contain all of the public transport data of Sweden.
If that is what you are looking for we recommend GTFS Sverige 2, which is much less detailed but does contain all of the public transport data of Sweden.

## What does this dataset contain?

This dataset contains high quality detailed data in the NeTEx format. Realtime SIRI data is not available for the aggregated NeTEx data. If your use case
requires real-time data, please use the regional NeTEx data or national GTFS data.
This dataset is an aggregated dataset of all the different datasets in the [Netex Regional API](/api/netex-datasets/netex-regional/).

### Data format

The data is in the NeTEx (**Ne**twork and **T**imetable **Ex**change) format. This is a format in which all European
operators have to publish their data. The data is aimed at both operator-to-traveller communication and internal
communication between different organizations.

### Updates

The static data in this dataset is updated on a daily basis, typically between 10:00 and 13:00.

### Operators covered by this dataset

{{% stip-data-availability-static %}}

### Breaking changes

This dataset has the **stable** status. This means that the fields can be added without prior warning, but when changes
to existing fields are made, you will get three months to update your implementations.

## Static data 

The static NeTEx Sweden dataset contains files describing all planned public transport data, with more technical
details compared to the GTFS Sweden feed but with the overall same timetable data.

In order to retrieve the static data you need an API key. Technical details for fetching the data can be found in the
API's OpenAPI specification.

To see which operators are included in this dataset see the [table above](#operators-covered-by-this-dataset).

{{% note %}}
**Where to download**

The dataset can be accessed through the following URL:
[https://opendata.samtrafiken.se/netex-sweden/sweden.zip?key={apikey}](https://opendata.samtrafiken.se/netex-sweden/sweden.zip?key={apikey}).

Replace `{apikey}` with your own API key. If you don´t have a key yet, read [here](/docs/using-trafiklab/getting-api-keys) on how to get one.
{{% /note %}}

<div style="max-width: 270px">

#### API key levels

| Level  | Maximum calls per minute | Maximum calls per month |
|:-------|:------------------------:|:-----------------------:|
| Bronze |            10            |           50            |
| Silver |            10            |           250           |

</div>

{{% page-ref "/api/netex-datasets/netex-sweden/netex-sweden-specification" %}}

## Licence

Data from the NeTEx Sweden API is available under the CC0 1.0 Universal (CC0 1.0) Public Domain Dedication license.

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