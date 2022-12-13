---
title: Static data
weight: 10
date: 2019-06-10
---

The static GTFS Regional dataset contains files describing all planned public transport data. It can be combined 
with optional realtime data available in the GTFS Realtime data API. 
The data in this dataset is updated on a daily basis, typically between 03:00 and 07:00.

In order to retrieve the static data you need an API key. Technical details for fetching the data can be found in the
API's OpenAPI specification. Trafiklabs GTFS documentation can help you to get started with GTFS files. 

{{% note %}}
**Where to download**

The dataset can be accessed through the following URL:
[https://opendata.samtrafiken.se/gtfs/{operator}/{operator}.zip?key={apikey}](https://opendata.samtrafiken.se/gtfs/{operator}/{operator}.zip?key={apikey}).

Replace `{operator}` with the abbreviation of the operator you want to download. These abbreviations can be found in the 
OpenAPI specification, but are also listed on [the overview page for this API](_index.md). Replace `{apikey}` with your own API key. 
If you don´t have a key yet, read [here](/docs/using-trafiklab/getting-api-keys) on how to get it.
{{% /note %}}

#### API key levels

| Level  | Calls per minute | Calls per month |
|:-------|:----------------:|:---------------:|
| Bronze |        10        |       50        |
| Silver |        10        |       250       |
| Gold   |        20        |      2500       |


{{% page-ref "/api/trafiklab-apis/gtfs-regional/static-specification"
"/docs/using-trafiklab-data/using-gtfs-files"  %}}

## GTFS Extensions

GTFS Regional uses some of 
[the GTFS Extensions](https://developers.google.com/transit/gtfs/reference/gtfs-extensions).
These extensions are not part of the specification, but are additions to offer additional details. 

### Extended route types

[Extended route types](https://developers.google.com/transit/gtfs/reference/extended-route-types) allow for more
specific transport modes to be used. GTFS Regional does not use the standard one digit GTFS route types, but uses only
extended route types.

The following list shows the most used transport modes. This is a non-extensive list, only meant to give an idea of the
types you should support. You should still be able to handle the other types in a graceful way, as new traffic may make
use of them without prior warning.

| Code | Name                    | Example                                       |
|:-----|:------------------------|:----------------------------------------------|
| 100  | Railway Service         |                                               |
| 401  | Metro Service           |                                               |
| 700  | Bus Service             |                                               |
| 717  | Share Taxi Service      | Advance order traffic (Förbeställningstrafik) |
| 900  | Tram Service            |                                               |
| 1000 | Water Transport Service | Ferry, pendelbåt                              |

### Trip-to-trip transfers

[Trip to trip transfers ](https://developers.google.com/transit/gtfs/reference/gtfs-extensions#TripToTripTransfers) make
use of the `from_trip_id`  and `to_trip_id` columns in the transfers.txt file.

From Googles documentation:

> The `from_trip_id` and `to_trip_id` fields can contain a `trip_id`, as specified by `trips.txt`. If `from_trip_id` is
> specified, the transfer will only apply to the arriving trip with the given trip id, at the given `from_stop_id`. 
> If `to_trip_id` is specified, the transfer will only apply to the departing trip with the given trip id, at the 
> given `to_stop_id`.


## Notes and known issues

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