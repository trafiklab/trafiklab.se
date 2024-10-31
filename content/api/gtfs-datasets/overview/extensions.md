---
title: Static data extensions
weight: 2
layout: "single"
sidebar: true
---

## GTFS Extensions

Both GTFS Sverige 2 and GTFS Regional uses some
of [the GTFS Extensions](https://developers.google.com/transit/gtfs/reference/gtfs-extensions).
These extensions are not part of the specification, but are additions to offer additional details.

### Extended Route Types

[Extended route types](https://developers.google.com/transit/gtfs/reference/extended-route-types) allow for more
specific transport modes to be used. GTFS Sverige and GTFS Regional does not use the standard one digit GTFS route
types, but only uses
extended route types.

The following list shows the most used transport modes for GTFS Sverige 2 and GTFS Regional/GTFS Sweden 3. This is a 
non-extensive list, only meant to give an idea of the types you should support. You should still be able to handle the 
other types in a graceful way, as new traffic may make use of them without prior warning.

#### GTFS Sverige 2

| Code | Name                       | Example                                                                          |
|:-----|:---------------------------|:---------------------------------------------------------------------------------|
| 100  | Railway Service            |                                                                                  |
| 101  | High Speed Rail Service    | X2000                                                                            |
| 102  | Long Distance Rail Service | Mälartåg                                                                         |
| 105  | Sleeper Rail Service       | Night train (Nattåg)                                                             |
| 106  | Regional Rail Service      | Commuter trains (Pendeltåg)                                                      |
| 401  | Metro Service              | Tunnelbanan Stockholm                                                            |
| 700  | Bus Service                |                                                                                  |
| 900  | Tram Service               | Trams in Göteborg                                                                |
| 1000 | Water Transport Service    | SL Pendelbåt, Stockholm-Helsinki                                                 |
| 1501 | Communal Taxi Service      | On-demand public transport with advance order conditions (Förbeställningstrafik) |

#### GTFS Regional, GTFS Sweden 3

{{% info %}}
Starting november 12th, codes `101`,`102`,`103`,`105`,`106` and `714` will be taken into use in SJs GTFS Regional feed and the GTFS Sweden 3 feed.
{{% /info %}}

| Code | Name                         | Example                                                                                |
|:-----|:-----------------------------|:---------------------------------------------------------------------------------------|
| 100  | Railway Service              | Train traffic which couldn't be automatically assigned to a more specific category _*_ |
| 101  | High Speed Rail Service      | SJ Snabbtåg, X2000                                                                     |
| 102  | Long Distance Rail Service   | International (Utrikes)                                                                |
| 103  | Inter Regional Rail Service  | SJ InterCity                                                                           |
| 105  | Sleeper Rail Service         | Night train (Nattåg), EuroNight                                                        |
| 106  | Regional Rail Service        | County traffic (Länstrafik)                                                            |
| 401  | Metro Service                | Metro (Tunnelbana)                                                                     |
| 700  | Bus Service                  |                                                                                        |
| 714  | Rail Replacement Bus Service | Replacement bus for train traffic                                                      |
| 900  | Tram Service                 | Trams in Göteborg                                                                      |
| 1000 | Water Transport Service      | SL Pendelbåt, Stockholm-Helsinki                                                       |
| 1501 | Communal Taxi Service        | On-demand public transport with advance order conditions (Förbeställningstrafik)       |

_\*_ Not all operators and data-formats offer the same level of detail in the data delivered to Trafiklab, which means some rail traffic is classified as `Railway
Service` even if it would fit better in another category. As this is improved, the transport code for certain lines may become more specific.

A complete list of all GTFS route types can be found
at [https://developers.google.com/transit/gtfs/reference/extended-route-types](https://developers.google.com/transit/gtfs/reference/extended-route-types). Note
that this list can change over time.

### Trip-to-trip transfers

GTFS Sverige 2 and GTFS Regional includes trip-to-trip transfers, which are detailed transfer rules that provide
additional details on
which transfers are possible, and how long they take.

{{% info %}}
**Trip-to-trip transfers used to be an extension** to the GTFS standard, but [this extension has been
formally adopted](https://github.com/google/transit/pull/284) into the GTFS standard in October 2021.
{{% /info %}}

[Trip to trip transfers ](https://developers.google.com/transit/gtfs/reference/gtfs-extensions#TripToTripTransfers)make
use of the `from_trip_id`  and `to_trip_id` columns in the transfers.txt file.

From Googles documentation:
The `from_trip_id` and `to_trip_id` fields can contain a `trip_id`, as specified by `trips.txt`. If `from_trip_id` is
specified, the transfer will only apply to the arriving trip with the given trip id, at the given `from_stop_id`. If
`to_trip_id` is specified, the transfer will only apply to the departing trip with the given trip id, at the given
`to_stop_id`.
