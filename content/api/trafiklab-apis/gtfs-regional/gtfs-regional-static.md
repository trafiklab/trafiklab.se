---
title: Static data
alias: "api/gtfs-regional-static"
---

{{% info %}} For technical details about HTTP headers, URLs, and response structures, please use the OpenAPI
Specification available on our developer portal. {{% /info %}}

## Retrieving static data

In order to retrieve the static data you need an API key. Follow the link below to read more about API keys.

{{% page-ref page="/docs/using-trafiklab/getting-api-keys" %}}

## GTFS Extensions

GTFS Regional uses some of [the GTFS Extensions](https://developers.google.com/transit/gtfs/reference/gtfs-extensions).

### Extended route types

[Extended route types](https://developers.google.com/transit/gtfs/reference/extended-route-types) allow for more
specific transport modes to be used. GTFS Regional does not use the standard one digit GTFS route types, but uses only
extended route types.

The following list shows the most used transport modes. This is a non-extensive list, only meant to give an idea of the
types you should support. You should still be able to handle the other types in a graceful way, as new traffic may make
use of them without prior warning.

| Code | Name | Example |
| :--- | :--- | :--- |
| 100 | Railway Service |  |
| 401 | Metro Service |  |
| 700 | Bus Service |  |
| 717 | Share Taxi Service | Advance order traffic (Förbeställningstrafik) |
| 900 | Tram Service |  |
| 1000 | Water Transport Service | Ferry, pendelbåt |

### Trip-to-trip transfers

[Trip to trip transfers ](https://developers.google.com/transit/gtfs/reference/gtfs-extensions#TripToTripTransfers)make
use of the `from_trip_id`  and `to_trip_id` columns in the transfers.txt file.

From Googles documentation:

> The `from_trip_id` and `to_trip_id` fields can contain a `trip_id`, as specified by `trips.txt`. If `from_trip_id` is specified, the transfer will only apply to the arriving trip with the given trip id, at the given `from_stop_id`. If `to_trip_id` is specified, the transfer will only apply to the departing trip with the given trip id, at the given `to_stop_id`.
