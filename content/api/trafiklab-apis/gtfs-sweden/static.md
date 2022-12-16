---
title: GTFS Sweden 3 Static data
weight: 10
date: 2022-06-01
---

The static GTFS Sweden 3 dataset contains files describing all planned public transport data. It can be combined 
with optional realtime data available in the GTFS Sweden Realtime data API. 
The data in this dataset is updated on a daily basis, typically between 10:00 and 13:00.

In order to retrieve the static data you need an API key. Technical details for fetching the data can be found in the
API's OpenAPI specification. Trafiklabs GTFS documentation can help you to get started with GTFS files. 

{{% note %}}
**Where to download**

The dataset can be accessed through the following URL:
[https://opendata.samtrafiken.se/gtfs-sweden/sweden.zip?key={apikey}](https://opendata.samtrafiken.se/gtfs-sweden/sweden.zip.zip?key={apikey}).

Replace `{apikey}` with your own API key. If you don´t have a key yet, read [here](/docs/using-trafiklab/getting-api-keys) on how to get one.
{{% /note %}}

#### API key levels

| Level  | Maximum calls per minute | Maximum calls per month |
|:-------|:------------------------:|:-----------------------:|
| Bronze |            10            |           50            |
| Silver |            10            |           250           |

{{% page-ref "/api/trafiklab-apis/gtfs-sweden/static-specification"
"/docs/using-trafiklab-data/using-gtfs-files"  %}}

## GTFS Extensions

The extensions are the same as in [the GTFS Regional API](/api/trafiklab-apis/gtfs-regional/static/#gtfs-extensions).

## Notes and known issues

See the documentation for [the GTFS Regional API](/api/trafiklab-apis/gtfs-regional/static/#notes-and-known-issues).