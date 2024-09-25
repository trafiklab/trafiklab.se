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

The following list shows the most used transport modes for GTFS Sverige and GTFS Regional. This is a non-extensive list,
only meant to give an idea of the
types you should support. You should still be able to handle the other types in a graceful way, as new traffic may make
use of them without prior warning.

| Code | Name                       | Example                                                     |
|:-----|:---------------------------|:------------------------------------------------------------|
| 100  | Railway Service            |                                                             |
| 101  | High Speed Rail Service    | X2000                                                       |
| 102  | Long Distance Rail Service | Mälartåg                                                    |
| 105  | Sleeper Rail Service       | Night train (Nattåg)                                        |
| 106  | Regional Rail Service      | Commuter trains (Pendeltåg)                                 |
| 401  | Metro Service              | Tunnelbanan Stockholm                                       |
| 700  | Bus Service                |                                                             |
| 702  | Express Bus Service        |                                                             |
| 717  | Share Taxi Service         | Advance order traffic (Förbeställningstrafik)               |
| 900  | Tram Service               | Trams in Göteborg                                           |
| 1000 | Water Transport Service    | SL Pendelbåt, Stockholm-Helsinki                            |
| 1501 | Communal Taxi Service      | Buses with advance order conditions (Förbeställningstrafik) |

A complete list of all route types can be found
at [https://developers.google.com/transit/gtfs/reference/extended-route-types](https://developers.google.com/transit/gtfs/reference/extended-route-types)
.

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
