---
title: Static data
---

{% hint style="info" %} For technical details about HTTP headers, URLs, and response structures, please use the OpenAPI
Specification available on our developer portal. {% endhint %}

### Retrieving Static data

In order to retrieve the static data you need an API key. Follow the link below to read more about API keys.

{% page-ref page="../../../../an-introduction-to-trafiklab/using-trafiklab/getting-api-keys.md" %}

### GTFS Extensions

GTFS Sverige 2 uses some of [the GTFS Extensions](https://developers.google.com/transit/gtfs/reference/gtfs-extensions).

#### Extended Route Types

[Extended route types](https://developers.google.com/transit/gtfs/reference/extended-route-types) allow for more
specific transport modes to be used. GTFS Sverige does not use the standard one digit GTFS route types, but uses only
extended route types.

The following list shows the most used transport modes. This is a non-extensive list, only meant to give an idea of the
types you should support. You should still be able to handle the other types in a gracefull way, as new traffic may make
use of them without prior warning.

| Code | Name | Example |
| :--- | :--- | :--- |
| 101  | High Speed Rail Service | X2000 |
| 102  | Long Distance Rail Service | Mälartåg |
| 105 | Sleeper Rail Service | Night train \(Nattåg\) |
| 106 | Regional Rail Service | Commuter trains \(Pendeltåg\) |
| 401 | Metro Service | Tunnelbanan Stockholm |
| 700 | Bus Service |  |
| 702 | Express Bus Service |  |
| 900 | Tram Service | Trams in Göteborg |
| 1000 | Water Transport Service | SL Pendelbåt, Stockholm-Helsinki |
| 1501 | Communal Taxi Service | Buses with advance order conditions \(Förbeställningstrafik\) |

A complete list of all route types can be found
at [https://developers.google.com/transit/gtfs/reference/extended-route-types](https://developers.google.com/transit/gtfs/reference/extended-route-types)
.

#### Trip-to-trip transfers

[Trip to trip transfers ](https://developers.google.com/transit/gtfs/reference/gtfs-extensions#TripToTripTransfers)make
use of the `from_trip_id`  and `to_trip_id` columns in the transfers.txt file.

From Googles documentation:

> The `from_trip_id` and `to_trip_id` fields can contain a `trip_id`, as specified by `trips.txt`. If `from_trip_id` is specified, the transfer will only apply to the arriving trip with the given trip id, at the given `from_stop_id`. If `to_trip_id` is specified, the transfer will only apply to the departing trip with the given trip id, at the given `to_stop_id`.
