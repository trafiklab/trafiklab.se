---
title: GTFS Sweden Static data 
aliases: 
  - "/api/gtfs-sweden-static"
weight: 10
date: 2019-06-10
---

The static GTFS Sweden dataset contains files describing all planned public transport data. It can be combined 
with optional realtime data available in the GTFS Sweden Realtime data API. 
The data in this dataset is updated on a daily basis, typically between 10:00 and 13:00.

In order to retrieve the static data you need an API key. Technical details for fetching the data can be found in the
API's OpenAPI specification. Trafiklabs GTFS documentation can help you to get started with GTFS files. 

{{% note %}}
**Where to download**

The dataset can be accessed through the following URL:
[https://opendata.samtrafiken.se/gtfs-sweden/sweden.zip?key={apikey}](https://opendata.samtrafiken.se/gtfs-sweden/sweden.zip.zip?key=APIKEY).

Replace `{apikey}` with your own API key. 
{{% /note %}}

{{% page-ref "/docs/using-trafiklab/getting-api-keys" "/api/trafiklab-apis/gtfs-sweden/static-specification" 
"/docs/using-trafiklab-data/using-gtfs-files"  %}}

## GTFS Extensions

The extensions are the same as in [the GTFS Regional API](/api/trafiklab-apis/gtfs-regional/static/#gtfs-extensions).

## Notes and known issues

See the documentation for [the GTFS Regional API](/api/trafiklab-apis/gtfs-regional/static/#notes-and-known-issues).