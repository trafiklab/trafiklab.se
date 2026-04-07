---
title: SL Journey-planner v2
weight: 101
date: 2025-05-12
badge: new
aliases:
  - /api/sl-reseplanerare
---
## Description

With this API, you can get travel proposals from point A to point B within Stockholm County using SL’s traffic. Waxholmsbolaget’s traffic is also included in
SL’s journey planner. The API can be used to calculate travel proposals between any combination of positions and/or stops. The API returns travel proposals
based on the “best match” for the input.

{{% success %}}
This API replaces [SL Route planner 3.1](route-planner-31), which will be shut down June 30th, 2025.
{{% /success %}}

## URL

This API consists of 3 endpoints, each with their own URL.

{{% tabs %}} {{% tab "System info" %}}

```text
https://journeyplanner.integration.sl.se/v3/system-info
```

{{% /tab %}}
{{% tab "Stop lookup" %}}

```text
https://journeyplanner.integration.sl.se/v3/stop-finder?name_sf=odenplan&any_obj_filter_sf=2&type_sf=any
```

{{% /tabs %}}
{{% tab "Journey planner" %}}

```text
https://journeyplanner.integration.sl.se/v3/trips?type_origin=any&type_destination=any&name_origin=9091001000009182&name_destination=9091001000009192&calc_number_of_trips=3
```

{{% /tab %}}

{{% /tabs %}}

## Format

This API returns data in the JSON format.

## Request

### API Keys

This API does not require the use of an API key. You should however not make excessive requests, to ensure the availability
and performance of the API for everyone.

If you need large amounts of data, for example to analyze travel times between all stops, [GTFS Regional](../../gtfs-datasets/gtfs-regional/_index.md) might be better suited for your application.

### Parameters

#### Stop Lookup

| Name              | Description                                                                                                                                                                                                                                                             |
|-------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| name_sf           | The street or stop name to search for. Name of the locality (e.g. stop name, POI, address) or coordinate. Syntax for coordinates: "&lt;x&gt;:&lt;y&gt;:WGS84\[dd.ddddd]" E.g. "18.013809:59.335104:WGS84\[dd.ddddd]". Note: Type must be stated in parameter "type_sf". |
| type_sf           | The search . `coord` for coordinates, or `any` for street and stop names                                                                                                                                                                                                |
| any_obj_filter_sf | What to search for. Bitmask used in combination with `any` in `type_sf`.  <ul><li> 2 = stops<li> 12 = streets and addresses<li> 32 = POI<li> 46 = all above                                                                                                             |

#### Trip search

For a complete list of all parameters, see the OpenAPI specification on the bottom of this page.

| Name                 | Required                     | Description                                                                                                                                                                                                                                                                                                                           |
|----------------------|------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| type_origin          | Yes                          | The type of input which is used for the origin. `coord` for coordinates, or `any` for street and stop names.                                                                                                                                                                                                                          |
| name_origin          | Yes                          | The location id or coordinates to depart from. `type_origin` should match the type of input used. Syntax for coordinates: "&lt;x&gt;:&lt;y&gt;:WGS84\[dd.ddddd]" E.g. "18.013809:59.335104:WGS84\[dd.ddddd]". Note: Type must be stated in parameter "type_sf".                                                                       |
| type_destination     | Yes                          | The type of input which is used for the destination. `coord` for coordinates, or `any` for street and stop names.                                                                                                                                                                                                                     |
| name_destination     | Yes                          | The location id, or coordinates. `type_destination` should match the type of input used. Syntax for coordinates: "&lt;x&gt;:&lt;y&gt;:WGS84\[dd.ddddd]" E.g. "18.013809:59.335104:WGS84\[dd.ddddd]". Note: Type must be stated in parameter "type_sf".                                                                                |
| calc_number_of_trips | Yes, 1-3                     | The number of public transport trips to return. 1-3. Walk and bike routes are not affected. In some cases, the journey planner will calculate additional connections, resulting in a higher number of results than stated in this parameter. In some cases the number of connections will be lower than the stated number of results. |
| type_via             | No, default no via           | The type of input which is used for defining a via stop. `coord` for coordinates, or `any` for street and stop names.                                                                                                                                                                                                                 |
| name_via             | No, default no via           | The location id, or coordinates, to use as an additional stop between the origin and destination. `type_via` should match the type of input used. Syntax for coordinates: "&lt;x&gt;:&lt;y&gt;:WGS84\[dd.ddddd]" E.g. "18.013809:59.335104:WGS84\[dd.ddddd]". Note: Type must be stated in parameter "type_sf".                       |
| dwell_time           | No, default no via           | The time to wait at the via stop, in `hh:mm` format.                                                                                                                                                                                                                                                                                  |
| type_not_via         | No, default no stop to avoid | The type of input which is used for defining a stop to avoid. `coord` for coordinates, or `any` for street and stop names.                                                                                                                                                                                                            |
| name_not_via         | No, default no stop to avoid | The location id, or coordinates, to avoid. `type_not_via` should match the type of input used. Syntax for coordinates: "&lt;x&gt;:&lt;y&gt;:WGS84\[dd.ddddd]" E.g. "18.013809:59.335104:WGS84\[dd.ddddd]". Note: Type must be stated in parameter "type_sf".                                                                          |
| language             | No, default `sv`             | The language to use in the response. `sv` or `en`.                                                                                                                                                                                                                                                                                    |
| max_changes          | No, default 9                | The number of changes allowed in results, 0-9.                                                                                                                                                                                                                                                                                        |
| calc_one_direction   | No, default false            | Prevents the journey planner from calculating one result before the requested departure time                                                                                                                                                                                                                                          |
| incl_mot_0           | No, default true             | Whether or not to include commuter trains in trip calculation                                                                                                                                                                                                                                                                         |
| incl_mot_2           | No, default true             | Whether or not to include metro lines in trip calculation                                                                                                                                                                                                                                                                             |
| incl_mot_4           | No, default true             | Whether or not to include trams and local trains (lokalbanor, e.g. lidingöbanan) in trip calculation                                                                                                                                                                                                                                  |
| incl_mot_5           | No, default true             | Whether or not to include busses in trip calculation                                                                                                                                                                                                                                                                                  |
| incl_mot_9           | No, default true             | Whether or not to include ships and ferries in trip calculation                                                                                                                                                                                                                                                                       |
| incl_mot_10          | No, default true             | Whether or not to include on-demand traffic in trip calculation. `incl_mot_5` and `incl_mot_10` should be enabled.                                                                                                                                                                                                                    |
| incl_mot_14          | No, default true             | Whether or not to include national trains in trip calculation                                                                                                                                                                                                                                                                         |
| incl_mot_19          | No, default true             | Whether or not to include accessible bus (närtrafik) in trip calculation                                                                                                                                                                                                                                                              |
| route_type           | No, default `leasttime`      | Calculate trips with the least interchanges (`leastinterchange`) fastest connections (`leasttime`), least walking (`leastwalking`)                                                                                                                                                                                                    |
| gen_c                | No, default true`            | Whether or not to include coordinates for trip legs                                                                                                                                                                                                                                                                                   |

## Response

For details regarding the response structure, please see the OpenApi specification below. A few example responses can be seen below.

{{% note %}} Some endpoints return "error" messages in the `systemMessages` structure, even though the request was handled successfully. When the response returns data, error messages can be
ignored. {{% /note %}}

{{% tabs %}} {{% tab "System info" %}}

```json
{
  "validity": {
    "from": "2025-01-03",
    "to": "2025-06-21"
  }
}
```

{{% /tab %}}
{{% tab "Stop lookup" %}}

```json
{
  "locations": [
    {
      "coord": [
        59.342906,
        18.049103
      ],
      "disassembledName": "Odenplan",
      "id": "9091001000009117",
      "isBest": true,
      "isGlobalId": true,
      "matchQuality": 1000,
      "name": "Stockholm, Odenplan",
      "parent": {
        "id": "placeID:33001080:1",
        "name": "Stockholm",
        "type": "locality"
      },
      "productClasses": [
        0,
        2,
        5
      ],
      "properties": {
        "mainLocality": "Stockholm",
        "stopId": "18009117"
      },
      "type": "stop"
    },
    {
      "coord": [
        59.343116,
        18.04569
      ],
      "disassembledName": "Stockholm Odenplan",
      "id": "9091001000001079",
      "isBest": false,
      "isGlobalId": true,
      "matchQuality": 948,
      "name": "Stockholm, Stockholm Odenplan",
      "parent": {
        "id": "placeID:33001080:1",
        "name": "Stockholm",
        "type": "locality"
      },
      "productClasses": [
        0,
        2,
        5
      ],
      "properties": {
        "mainLocality": "Stockholm",
        "stopId": "18001079"
      },
      "type": "stop"
    }
  ],
  "systemMessages": [
    {
      "code": -8011,
      "module": "BROKER",
      "text": "",
      "type": "error"
    }
  ]
}
```

{{% /tabs %}}

{{% tab "Journey planner" %}}

```json
{
  "systemMessages": [

  ],
  "journeys": [
    {
      "tripDuration": 930,
      "tripRtDuration": 912,
      "rating": 0,
      "isAdditional": false,
      "interchanges": 0,
      "legs": [
        {
          "infos": [

          ],
          "duration": 912,
          "origin": {
            "isGlobalId": true,
            "id": "9025001000001861",
            "name": "Hökarängen, Stockholm",
            "disassembledName": "1",
            "type": "platform",
            "coord": [
              59.257932,
              18.082494
            ],
            "niveau": 0,
            "parent": {
              "isGlobalId": true,
              "id": "9021001001861000",
              "name": "Hökarängen, Stockholm",
              "disassembledName": "Hökarängen",
              "type": "stop",
              "parent": {
                "id": "placeID:33001080:1",
                "name": "Stockholm",
                "type": "locality"
              },
              "properties": {
                "stopId": "18001861"
              },
              "coord": [
                59.257928,
                18.082503
              ],
              "niveau": 0
            },
            "productClasses": [
              2
            ],
            "departureTimeBaseTimetable": "2026-04-07T12:41:18Z",
            "departureTimePlanned": "2026-04-07T12:41:18Z",
            "departureTimeEstimated": "2026-04-07T12:42:12Z",
            "properties": {
              "AREA_NIVEAU_DIVA": "0",
              "area": "1",
              "occupancy": "MANY_SEATS",
              "platform": "1",
              "stoppingPointPlanned": "1",
              "platformName": "1"
            }
          },
          "destination": {
            "isGlobalId": true,
            "id": "9025001000001011",
            "name": "Slussen, Stockholm",
            "disassembledName": "1",
            "type": "platform",
            "coord": [
              59.319633,
              18.072226
            ],
            "niveau": 0,
            "parent": {
              "isGlobalId": true,
              "id": "9021001001011000",
              "name": "Slussen, Stockholm",
              "disassembledName": "Slussen",
              "type": "stop",
              "parent": {
                "id": "placeID:33001080:1",
                "name": "Stockholm",
                "type": "locality"
              },
              "properties": {
                "stopId": "18001011"
              },
              "coord": [
                59.319533,
                18.071615
              ],
              "niveau": 0
            },
            "productClasses": [
              2
            ],
            "arrivalTimeBaseTimetable": "2026-04-07T12:56:48Z",
            "arrivalTimePlanned": "2026-04-07T12:56:48Z",
            "arrivalTimeEstimated": "2026-04-07T12:57:24Z",
            "properties": {
              "AREA_NIVEAU_DIVA": "0",
              "area": "1",
              "platform": "1",
              "stoppingPointPlanned": "1",
              "platformName": "1"
            }
          },
          "transportation": {
            "id": "tfs:02018: :H:y01",
            "name": "Tunnelbana tunnelbanans gröna linje 18",
            "number": "tunnelbanans gröna linje 18",
            "product": {
              "id": 8,
              "class": 2,
              "name": "Tunnelbana",
              "iconId": 1
            },
            "operator": {
              "id": "1",
              "name": "Storstockholms Lokaltrafik"
            },
            "destination": {
              "id": "18001201",
              "name": "Alvik",
              "type": "stop"
            },
            "properties": {
              "tripCode": 57,
              "timetablePeriod": "Current",
              "lineDisplay": "LINE",
              "globalId": "9011001001800000",
              "RealtimeTripId": "9015001001810709",
              "shortTrain": false,
              "AVMSTripID": "9015001001810709"
            },
            "isSamtrafik": false,
            "disassembledName": "18"
          },
          "stopSequence": [
            {
              "isGlobalId": true,
              "id": "9025001000001861",
              "name": "Hökarängen, Stockholm",
              "disassembledName": "1",
              "type": "platform",
              "coord": [
                59.257932,
                18.082494
              ],
              "niveau": 0,
              "parent": {
                "isGlobalId": true,
                "id": "9021001001861000",
                "name": "Hökarängen, Stockholm",
                "disassembledName": "Hökarängen",
                "type": "stop",
                "parent": {
                  "id": "placeID:33001080:1",
                  "name": "Stockholm",
                  "type": "locality"
                },
                "properties": {
                  "stopId": "18001861"
                },
                "coord": [
                  59.257928,
                  18.082503
                ],
                "niveau": 0
              },
              "productClasses": [
                2
              ],
              "properties": {
                "AREA_NIVEAU_DIVA": "0",
                "area": "1",
                "occupancy": "MANY_SEATS",
                "platform": "1",
                "zone": "tfs:32",
                "stoppingPointPlanned": "1",
                "platformName": "1"
              },
              "departureTimePlanned": "2026-04-07T12:41:18Z",
              "departureTimeEstimated": "2026-04-07T12:42:12Z"
            },
            {
              "isGlobalId": true,
              "id": "9025001000001851",
              "name": "Gubbängen, Stockholm",
              "disassembledName": "1",
              "type": "platform",
              "coord": [
                59.263323,
                18.082134
              ],
              "niveau": 0,
              "parent": {
                "isGlobalId": true,
                "id": "9021001001851000",
                "name": "Gubbängen, Stockholm",
                "disassembledName": "Gubbängen",
                "type": "stop",
                "parent": {
                  "id": "placeID:33001080:1",
                  "name": "Stockholm",
                  "type": "locality"
                },
                "properties": {
                  "stopId": "18001851"
                },
                "coord": [
                  59.263327,
                  18.082134
                ],
                "niveau": 0
              },
              "productClasses": [
                2
              ],
              "properties": {
                "AREA_NIVEAU_DIVA": "0",
                "area": "1",
                "occupancy": "MANY_SEATS",
                "platform": "1",
                "zone": "tfs:32",
                "stoppingPointPlanned": "1",
                "platformName": "1"
              },
              "departureTimePlanned": "2026-04-07T12:42:42Z",
              "departureTimeEstimated": "2026-04-07T12:43:42Z",
              "arrivalTimePlanned": "2026-04-07T12:42:18Z",
              "arrivalTimeEstimated": "2026-04-07T12:42:42Z"
            },
            {
              "isGlobalId": true,
              "id": "9025001000001841",
              "name": "Tallkrogen, Stockholm",
              "disassembledName": "1",
              "type": "platform",
              "coord": [
                59.271265,
                18.085566
              ],
              "niveau": 0,
              "parent": {
                "isGlobalId": true,
                "id": "9021001001841000",
                "name": "Tallkrogen, Stockholm",
                "disassembledName": "Tallkrogen",
                "type": "stop",
                "parent": {
                  "id": "placeID:33001080:1",
                  "name": "Stockholm",
                  "type": "locality"
                },
                "properties": {
                  "stopId": "18001841"
                },
                "coord": [
                  59.271255,
                  18.085548
                ],
                "niveau": 0
              },
              "productClasses": [
                2
              ],
              "properties": {
                "AREA_NIVEAU_DIVA": "0",
                "area": "1",
                "occupancy": "MANY_SEATS",
                "platform": "1",
                "zone": "tfs:32",
                "stoppingPointPlanned": "1",
                "platformName": "1"
              },
              "departureTimePlanned": "2026-04-07T12:44:30Z",
              "departureTimeEstimated": "2026-04-07T12:45:24Z",
              "arrivalTimePlanned": "2026-04-07T12:44:06Z",
              "arrivalTimeEstimated": "2026-04-07T12:44:36Z"
            },
            {
              "isGlobalId": true,
              "id": "9025001000001831",
              "name": "Skogskyrkogården, Stockholm",
              "disassembledName": "1",
              "type": "platform",
              "coord": [
                59.278966,
                18.095519
              ],
              "niveau": 0,
              "parent": {
                "isGlobalId": true,
                "id": "9021001001831000",
                "name": "Skogskyrkogården, Stockholm",
                "disassembledName": "Skogskyrkogården",
                "type": "stop",
                "parent": {
                  "id": "placeID:33001080:1",
                  "name": "Stockholm",
                  "type": "locality"
                },
                "properties": {
                  "stopId": "18001831"
                },
                "coord": [
                  59.278966,
                  18.095519
                ],
                "niveau": 0
              },
              "productClasses": [
                2
              ],
              "properties": {
                "AREA_NIVEAU_DIVA": "0",
                "area": "1",
                "occupancy": "MANY_SEATS",
                "platform": "1",
                "zone": "tfs:32",
                "stoppingPointPlanned": "1",
                "platformName": "1"
              },
              "departureTimePlanned": "2026-04-07T12:46:12Z",
              "departureTimeEstimated": "2026-04-07T12:47:06Z",
              "arrivalTimePlanned": "2026-04-07T12:45:48Z",
              "arrivalTimeEstimated": "2026-04-07T12:46:12Z"
            },
            {
              "isGlobalId": true,
              "id": "9025001000001821",
              "name": "Sandsborg, Stockholm",
              "disassembledName": "1",
              "type": "platform",
              "coord": [
                59.285675,
                18.091935
              ],
              "niveau": 0,
              "parent": {
                "isGlobalId": true,
                "id": "9021001001821000",
                "name": "Sandsborg, Stockholm",
                "disassembledName": "Sandsborg",
                "type": "stop",
                "parent": {
                  "id": "placeID:33001080:1",
                  "name": "Stockholm",
                  "type": "locality"
                },
                "properties": {
                  "stopId": "18001821"
                },
                "coord": [
                  59.285675,
                  18.091935
                ],
                "niveau": 0
              },
              "productClasses": [
                2
              ],
              "properties": {
                "AREA_NIVEAU_DIVA": "0",
                "area": "1",
                "occupancy": "MANY_SEATS",
                "platform": "1",
                "zone": "tfs:32",
                "stoppingPointPlanned": "1",
                "platformName": "1"
              },
              "departureTimePlanned": "2026-04-07T12:47:48Z",
              "departureTimeEstimated": "2026-04-07T12:48:48Z",
              "arrivalTimePlanned": "2026-04-07T12:47:24Z",
              "arrivalTimeEstimated": "2026-04-07T12:47:48Z"
            },
            {
              "isGlobalId": true,
              "id": "9025001000001811",
              "name": "Blåsut, Stockholm",
              "disassembledName": "1",
              "type": "platform",
              "coord": [
                59.291185,
                18.091163
              ],
              "niveau": 0,
              "parent": {
                "isGlobalId": true,
                "id": "9021001001811000",
                "name": "Blåsut, Stockholm",
                "disassembledName": "Blåsut",
                "type": "stop",
                "parent": {
                  "id": "placeID:33001080:1",
                  "name": "Stockholm",
                  "type": "locality"
                },
                "properties": {
                  "stopId": "18001811"
                },
                "coord": [
                  59.291166,
                  18.091154
                ],
                "niveau": 0
              },
              "productClasses": [
                2
              ],
              "properties": {
                "AREA_NIVEAU_DIVA": "0",
                "area": "1",
                "occupancy": "MANY_SEATS",
                "platform": "1",
                "zone": "tfs:32",
                "stoppingPointPlanned": "1",
                "platformName": "1"
              },
              "departureTimePlanned": "2026-04-07T12:49:12Z",
              "departureTimeEstimated": "2026-04-07T12:50:06Z",
              "arrivalTimePlanned": "2026-04-07T12:48:48Z",
              "arrivalTimeEstimated": "2026-04-07T12:49:18Z"
            },
            {
              "isGlobalId": true,
              "id": "9025001000001603",
              "name": "Skärmarbrink, Stockholm",
              "disassembledName": "2",
              "type": "platform",
              "coord": [
                59.295286,
                18.090327
              ],
              "niveau": 0,
              "parent": {
                "isGlobalId": true,
                "id": "9021001001601000",
                "name": "Skärmarbrink, Stockholm",
                "disassembledName": "Skärmarbrink",
                "type": "stop",
                "parent": {
                  "id": "placeID:33001080:1",
                  "name": "Stockholm",
                  "type": "locality"
                },
                "properties": {
                  "stopId": "18001601"
                },
                "coord": [
                  59.295272,
                  18.090354
                ],
                "niveau": 0
              },
              "productClasses": [
                2
              ],
              "properties": {
                "AREA_NIVEAU_DIVA": "0",
                "area": "3",
                "occupancy": "MANY_SEATS",
                "platform": "1",
                "zone": "tfs:32",
                "stoppingPointPlanned": "2",
                "platformName": "2"
              },
              "departureTimePlanned": "2026-04-07T12:50:42Z",
              "departureTimeEstimated": "2026-04-07T12:51:36Z",
              "arrivalTimePlanned": "2026-04-07T12:50:18Z",
              "arrivalTimeEstimated": "2026-04-07T12:50:48Z"
            },
            {
              "isGlobalId": true,
              "id": "9025001000001551",
              "name": "Gullmarsplan, Stockholm",
              "disassembledName": "1",
              "type": "platform",
              "coord": [
                59.299184,
                18.080967
              ],
              "niveau": 0,
              "parent": {
                "isGlobalId": true,
                "id": "9021001001551000",
                "name": "Gullmarsplan, Stockholm",
                "disassembledName": "Gullmarsplan",
                "type": "stop",
                "parent": {
                  "id": "placeID:33001080:1",
                  "name": "Stockholm",
                  "type": "locality"
                },
                "properties": {
                  "stopId": "18001551"
                },
                "coord": [
                  59.299157,
                  18.080985
                ],
                "niveau": 0
              },
              "productClasses": [
                2
              ],
              "properties": {
                "AREA_NIVEAU_DIVA": "0",
                "area": "1",
                "occupancy": "FEW_SEATS",
                "platform": "1",
                "zone": "tfs:32",
                "stoppingPointPlanned": "1",
                "platformName": "1"
              },
              "departureTimePlanned": "2026-04-07T12:52:30Z",
              "departureTimeEstimated": "2026-04-07T12:53:00Z",
              "arrivalTimePlanned": "2026-04-07T12:51:54Z",
              "arrivalTimeEstimated": "2026-04-07T12:52:30Z"
            },
            {
              "isGlobalId": true,
              "id": "9025001000001521",
              "name": "Skanstull, Stockholm",
              "disassembledName": "1",
              "type": "platform",
              "coord": [
                59.308493,
                18.076062
              ],
              "niveau": 0,
              "parent": {
                "isGlobalId": true,
                "id": "9021001001521000",
                "name": "Skanstull, Stockholm",
                "disassembledName": "Skanstull",
                "type": "stop",
                "parent": {
                  "id": "placeID:33001080:1",
                  "name": "Stockholm",
                  "type": "locality"
                },
                "properties": {
                  "stopId": "18001521"
                },
                "coord": [
                  59.308498,
                  18.076107
                ],
                "niveau": 0
              },
              "productClasses": [
                2
              ],
              "properties": {
                "AREA_NIVEAU_DIVA": "0",
                "area": "1",
                "occupancy": "FEW_SEATS",
                "platform": "1",
                "zone": "tfs:33",
                "stoppingPointPlanned": "1",
                "platformName": "1"
              },
              "departureTimePlanned": "2026-04-07T12:54:24Z",
              "departureTimeEstimated": "2026-04-07T12:55:24Z",
              "arrivalTimePlanned": "2026-04-07T12:53:54Z",
              "arrivalTimeEstimated": "2026-04-07T12:54:30Z"
            },
            {
              "isGlobalId": true,
              "id": "9025001000001511",
              "name": "Medborgarplatsen, Stockholm",
              "disassembledName": "1",
              "type": "platform",
              "coord": [
                59.314889,
                18.073412
              ],
              "niveau": 0,
              "parent": {
                "isGlobalId": true,
                "id": "9021001001511000",
                "name": "Medborgarplatsen, Stockholm",
                "disassembledName": "Medborgarplatsen",
                "type": "stop",
                "parent": {
                  "id": "placeID:33001080:1",
                  "name": "Stockholm",
                  "type": "locality"
                },
                "properties": {
                  "stopId": "18001511"
                },
                "coord": [
                  59.31488,
                  18.073439
                ],
                "niveau": 0
              },
              "productClasses": [
                2
              ],
              "properties": {
                "AREA_NIVEAU_DIVA": "0",
                "area": "1",
                "occupancy": "FEW_SEATS",
                "platform": "1",
                "zone": "tfs:33",
                "stoppingPointPlanned": "1",
                "platformName": "1"
              },
              "departureTimePlanned": "2026-04-07T12:56:00Z",
              "departureTimeEstimated": "2026-04-07T12:56:48Z",
              "arrivalTimePlanned": "2026-04-07T12:55:30Z",
              "arrivalTimeEstimated": "2026-04-07T12:56:00Z"
            },
            {
              "isGlobalId": true,
              "id": "9025001000001011",
              "name": "Slussen, Stockholm",
              "disassembledName": "1",
              "type": "platform",
              "coord": [
                59.319633,
                18.072226
              ],
              "niveau": 0,
              "parent": {
                "isGlobalId": true,
                "id": "9021001001011000",
                "name": "Slussen, Stockholm",
                "disassembledName": "Slussen",
                "type": "stop",
                "parent": {
                  "id": "placeID:33001080:1",
                  "name": "Stockholm",
                  "type": "locality"
                },
                "properties": {
                  "stopId": "18001011"
                },
                "coord": [
                  59.319533,
                  18.071615
                ],
                "niveau": 0
              },
              "productClasses": [
                2
              ],
              "properties": {
                "AREA_NIVEAU_DIVA": "0",
                "area": "1",
                "platform": "1",
                "zone": "tfs:33",
                "stoppingPointPlanned": "1",
                "platformName": "1"
              },
              "arrivalTimePlanned": "2026-04-07T12:56:48Z",
              "arrivalTimeEstimated": "2026-04-07T12:57:24Z"
            }
          ],
          "properties": {
            "tripId": "9015001001810709"
          },
          "coords": [
            [
              59.257695,
              18.082629
            ],
            [
              59.257793,
              18.082575
            ],
            [
              59.257866,
              18.082539
            ],
            [
              59.257955,
              18.082501
            ],
            [
              59.25803,
              18.082474
            ],
            [
              59.258143,
              18.08244
            ],
            [
              59.258228,
              18.08242
            ],
            [
              59.258304,
              18.082407
            ],
            [
              59.258381,
              18.082398
            ],
            [
              59.258505,
              18.082391
            ],
            [
              59.258691,
              18.082389
            ],
            [
              59.259736,
              18.082403
            ],
            [
              59.261584,
              18.08242
            ],
            [
              59.261974,
              18.082413
            ],
            [
              59.262168,
              18.082404
            ],
            [
              59.262275,
              18.082396
            ],
            [
              59.262432,
              18.082376
            ],
            [
              59.262688,
              18.082325
            ],
            [
              59.263088,
              18.08223
            ],
            [
              59.263666,
              18.082092
            ],
            [
              59.263991,
              18.082018
            ],
            [
              59.264695,
              18.081875
            ],
            [
              59.265079,
              18.0818
            ],
            [
              59.265282,
              18.081766
            ],
            [
              59.265357,
              18.081757
            ],
            [
              59.265491,
              18.081745
            ],
            [
              59.26575,
              18.081733
            ],
            [
              59.265958,
              18.081732
            ],
            [
              59.266152,
              18.081741
            ],
            [
              59.266283,
              18.081755
            ],
            [
              59.266432,
              18.081778
            ],
            [
              59.266563,
              18.081803
            ],
            [
              59.266753,
              18.081847
            ],
            [
              59.26709,
              18.08194
            ],
            [
              59.267406,
              18.082034
            ],
            [
              59.26751,
              18.082067
            ],
            [
              59.267635,
              18.082113
            ],
            [
              59.26778,
              18.082173
            ],
            [
              59.267956,
              18.082251
            ],
            [
              59.268295,
              18.082408
            ],
            [
              59.2685,
              18.08251
            ],
            [
              59.268652,
              18.082592
            ],
            [
              59.269003,
              18.0828
            ],
            [
              59.269153,
              18.082892
            ],
            [
              59.269283,
              18.082976
            ],
            [
              59.269381,
              18.083047
            ],
            [
              59.26944,
              18.083092
            ],
            [
              59.269537,
              18.083173
            ],
            [
              59.269643,
              18.083268
            ],
            [
              59.269853,
              18.08347
            ],
            [
              59.269937,
              18.083556
            ],
            [
              59.27003,
              18.083655
            ],
            [
              59.270067,
              18.083697
            ],
            [
              59.270142,
              18.083788
            ],
            [
              59.270259,
              18.083943
            ],
            [
              59.270479,
              18.084256
            ],
            [
              59.270572,
              18.084391
            ],
            [
              59.270737,
              18.084642
            ],
            [
              59.270824,
              18.084782
            ],
            [
              59.270889,
              18.084893
            ],
            [
              59.270972,
              18.085042
            ],
            [
              59.271086,
              18.085255
            ],
            [
              59.272035,
              18.087079
            ],
            [
              59.273233,
              18.089368
            ],
            [
              59.273389,
              18.089669
            ],
            [
              59.273481,
              18.089853
            ],
            [
              59.27361,
              18.090124
            ],
            [
              59.273756,
              18.090452
            ],
            [
              59.274626,
              18.092455
            ],
            [
              59.274794,
              18.092839
            ],
            [
              59.274916,
              18.093107
            ],
            [
              59.274986,
              18.093251
            ],
            [
              59.275103,
              18.093482
            ],
            [
              59.2752,
              18.093667
            ],
            [
              59.275306,
              18.093861
            ],
            [
              59.275376,
              18.093983
            ],
            [
              59.275431,
              18.094075
            ],
            [
              59.275497,
              18.094175
            ],
            [
              59.275581,
              18.094292
            ],
            [
              59.275686,
              18.094422
            ],
            [
              59.275795,
              18.094541
            ],
            [
              59.275859,
              18.094603
            ],
            [
              59.275896,
              18.094636
            ],
            [
              59.276007,
              18.094725
            ],
            [
              59.276092,
              18.094785
            ],
            [
              59.276159,
              18.094828
            ],
            [
              59.276284,
              18.094902
            ],
            [
              59.276415,
              18.094967
            ],
            [
              59.276546,
              18.095019
            ],
            [
              59.27664,
              18.09505
            ],
            [
              59.276687,
              18.095063
            ],
            [
              59.27687,
              18.095101
            ],
            [
              59.277049,
              18.095129
            ],
            [
              59.277972,
              18.095263
            ],
            [
              59.278726,
              18.095377
            ],
            [
              59.278951,
              18.095411
            ],
            [
              59.279161,
              18.095439
            ],
            [
              59.279315,
              18.095453
            ],
            [
              59.279382,
              18.095455
            ],
            [
              59.279496,
              18.095452
            ],
            [
              59.279662,
              18.095439
            ],
            [
              59.279776,
              18.095426
            ],
            [
              59.279921,
              18.095404
            ],
            [
              59.280024,
              18.095384
            ],
            [
              59.280106,
              18.095363
            ],
            [
              59.28019,
              18.095336
            ],
            [
              59.280268,
              18.095306
            ],
            [
              59.280327,
              18.095282
            ],
            [
              59.280453,
              18.095224
            ],
            [
              59.280569,
              18.095166
            ],
            [
              59.28068,
              18.095102
            ],
            [
              59.280788,
              18.095036
            ],
            [
              59.281038,
              18.094872
            ],
            [
              59.28254,
              18.093863
            ],
            [
              59.284026,
              18.092848
            ],
            [
              59.28422,
              18.09272
            ],
            [
              59.284361,
              18.092633
            ],
            [
              59.284522,
              18.092544
            ],
            [
              59.28471,
              18.092446
            ],
            [
              59.285441,
              18.092077
            ],
            [
              59.285655,
              18.091969
            ],
            [
              59.285996,
              18.091804
            ],
            [
              59.286621,
              18.091507
            ],
            [
              59.286897,
              18.091382
            ],
            [
              59.287037,
              18.091327
            ],
            [
              59.287187,
              18.091277
            ],
            [
              59.287367,
              18.091228
            ],
            [
              59.287517,
              18.091197
            ],
            [
              59.287744,
              18.091169
            ],
            [
              59.287829,
              18.091162
            ],
            [
              59.289113,
              18.091073
            ],
            [
              59.28926,
              18.091063
            ],
            [
              59.289448,
              18.091056
            ],
            [
              59.289639,
              18.091056
            ],
            [
              59.289736,
              18.091059
            ],
            [
              59.289841,
              18.091067
            ],
            [
              59.289961,
              18.091081
            ],
            [
              59.290157,
              18.091111
            ],
            [
              59.290461,
              18.091163
            ],
            [
              59.290658,
              18.091201
            ],
            [
              59.290932,
              18.091264
            ],
            [
              59.291207,
              18.091335
            ],
            [
              59.29149,
              18.091404
            ],
            [
              59.293162,
              18.091798
            ],
            [
              59.293425,
              18.091857
            ],
            [
              59.293567,
              18.091882
            ],
            [
              59.29373,
              18.091899
            ],
            [
              59.293841,
              18.091904
            ],
            [
              59.293917,
              18.091904
            ],
            [
              59.294029,
              18.091894
            ],
            [
              59.294085,
              18.091884
            ],
            [
              59.294165,
              18.091861
            ],
            [
              59.294235,
              18.091835
            ],
            [
              59.294334,
              18.091787
            ],
            [
              59.294412,
              18.091743
            ],
            [
              59.294489,
              18.091692
            ],
            [
              59.294564,
              18.091632
            ],
            [
              59.294635,
              18.091566
            ],
            [
              59.294696,
              18.091503
            ],
            [
              59.294782,
              18.091404
            ],
            [
              59.294856,
              18.091308
            ],
            [
              59.29492,
              18.091218
            ],
            [
              59.294975,
              18.091133
            ],
            [
              59.295039,
              18.091024
            ],
            [
              59.2951,
              18.09091
            ],
            [
              59.295174,
              18.090764
            ],
            [
              59.295683,
              18.089715
            ],
            [
              59.295839,
              18.089398
            ],
            [
              59.296192,
              18.08869
            ],
            [
              59.296317,
              18.088426
            ],
            [
              59.29637,
              18.088305
            ],
            [
              59.296411,
              18.088204
            ],
            [
              59.296513,
              18.087933
            ],
            [
              59.296626,
              18.087606
            ],
            [
              59.296721,
              18.087307
            ],
            [
              59.296754,
              18.087196
            ],
            [
              59.296781,
              18.087095
            ],
            [
              59.296834,
              18.086877
            ],
            [
              59.296879,
              18.086673
            ],
            [
              59.296959,
              18.086278
            ],
            [
              59.297013,
              18.085993
            ],
            [
              59.297065,
              18.085689
            ],
            [
              59.297214,
              18.084785
            ],
            [
              59.297281,
              18.084395
            ],
            [
              59.297341,
              18.084078
            ],
            [
              59.297465,
              18.083466
            ],
            [
              59.297549,
              18.08308
            ],
            [
              59.297591,
              18.0829
            ],
            [
              59.297629,
              18.082751
            ],
            [
              59.297668,
              18.082607
            ],
            [
              59.297719,
              18.082435
            ],
            [
              59.297754,
              18.082331
            ],
            [
              59.297786,
              18.082247
            ],
            [
              59.297835,
              18.082135
            ],
            [
              59.297868,
              18.082071
            ],
            [
              59.29793,
              18.081961
            ],
            [
              59.297974,
              18.081894
            ],
            [
              59.298019,
              18.081831
            ],
            [
              59.298061,
              18.081779
            ],
            [
              59.298133,
              18.0817
            ],
            [
              59.298189,
              18.081646
            ],
            [
              59.298332,
              18.08152
            ],
            [
              59.298449,
              18.081425
            ],
            [
              59.298569,
              18.081333
            ],
            [
              59.298681,
              18.081252
            ],
            [
              59.29877,
              18.081193
            ],
            [
              59.298856,
              18.08114
            ],
            [
              59.299013,
              18.081053
            ],
            [
              59.29916,
              18.080976
            ],
            [
              59.299885,
              18.080603
            ],
            [
              59.300078,
              18.080507
            ],
            [
              59.300224,
              18.080441
            ],
            [
              59.300336,
              18.080396
            ],
            [
              59.30044,
              18.080358
            ],
            [
              59.300939,
              18.080191
            ],
            [
              59.301126,
              18.080124
            ],
            [
              59.301249,
              18.080075
            ],
            [
              59.301317,
              18.080044
            ],
            [
              59.301555,
              18.079926
            ],
            [
              59.301806,
              18.079793
            ],
            [
              59.30211,
              18.079628
            ],
            [
              59.302428,
              18.079448
            ],
            [
              59.302752,
              18.079259
            ],
            [
              59.306819,
              18.076789
            ],
            [
              59.307135,
              18.076603
            ],
            [
              59.307223,
              18.076555
            ],
            [
              59.307337,
              18.076499
            ],
            [
              59.307466,
              18.076438
            ],
            [
              59.307611,
              18.076376
            ],
            [
              59.307785,
              18.076316
            ],
            [
              59.308035,
              18.076246
            ],
            [
              59.308202,
              18.076192
            ],
            [
              59.308378,
              18.076119
            ],
            [
              59.308514,
              18.076056
            ],
            [
              59.30965,
              18.075492
            ],
            [
              59.311001,
              18.074852
            ],
            [
              59.311622,
              18.074553
            ],
            [
              59.311828,
              18.074461
            ],
            [
              59.312245,
              18.074284
            ],
            [
              59.312459,
              18.07419
            ],
            [
              59.313487,
              18.073718
            ],
            [
              59.313714,
              18.073616
            ],
            [
              59.313815,
              18.073574
            ],
            [
              59.313943,
              18.073527
            ],
            [
              59.314064,
              18.073491
            ],
            [
              59.314191,
              18.073462
            ],
            [
              59.314318,
              18.073439
            ],
            [
              59.314438,
              18.073425
            ],
            [
              59.314521,
              18.073419
            ],
            [
              59.314627,
              18.073415
            ],
            [
              59.314874,
              18.073414
            ],
            [
              59.315064,
              18.073412
            ],
            [
              59.315213,
              18.073408
            ],
            [
              59.315385,
              18.073395
            ],
            [
              59.315514,
              18.073379
            ],
            [
              59.315634,
              18.073361
            ],
            [
              59.315743,
              18.073339
            ],
            [
              59.315835,
              18.073316
            ],
            [
              59.315929,
              18.073288
            ],
            [
              59.316075,
              18.073241
            ],
            [
              59.316471,
              18.073101
            ],
            [
              59.316761,
              18.07299
            ],
            [
              59.317263,
              18.072774
            ],
            [
              59.317417,
              18.072719
            ],
            [
              59.317491,
              18.072698
            ],
            [
              59.317544,
              18.072688
            ],
            [
              59.317618,
              18.072677
            ],
            [
              59.3178,
              18.072658
            ],
            [
              59.317927,
              18.072672
            ],
            [
              59.318056,
              18.072674
            ],
            [
              59.318235,
              18.072711
            ],
            [
              59.318315,
              18.072719
            ],
            [
              59.318384,
              18.072719
            ],
            [
              59.318489,
              18.072712
            ],
            [
              59.318575,
              18.072701
            ],
            [
              59.318684,
              18.072682
            ],
            [
              59.318794,
              18.072658
            ],
            [
              59.318932,
              18.07262
            ],
            [
              59.319019,
              18.072588
            ],
            [
              59.319098,
              18.072555
            ],
            [
              59.319227,
              18.072494
            ],
            [
              59.319331,
              18.072437
            ],
            [
              59.319413,
              18.072386
            ],
            [
              59.319501,
              18.072324
            ],
            [
              59.319621,
              18.072231
            ]
          ],
          "realtimeStatus": [
            "MONITORED"
          ],
          "isRealtimeControlled": true
        }
      ],
      "daysOfService": {
        "rvb": "000000000000000000000000000000400000000000000000"
      }
    },
    {
      "tripDuration": 930,
      "tripRtDuration": 900,
      "rating": 0,
      "isAdditional": false,
      "interchanges": 0,
      "legs": [
        {
          "infos": [

          ],
          "duration": 900,
          "origin": {
            "isGlobalId": true,
            "id": "9025001000001861",
            "name": "Hökarängen, Stockholm",
            "disassembledName": "1",
            "type": "platform",
            "coord": [
              59.257932,
              18.082494
            ],
            "niveau": 0,
            "parent": {
              "isGlobalId": true,
              "id": "9021001001861000",
              "name": "Hökarängen, Stockholm",
              "disassembledName": "Hökarängen",
              "type": "stop",
              "parent": {
                "id": "placeID:33001080:1",
                "name": "Stockholm",
                "type": "locality"
              },
              "properties": {
                "stopId": "18001861"
              },
              "coord": [
                59.257928,
                18.082503
              ],
              "niveau": 0
            },
            "productClasses": [
              2
            ],
            "departureTimeBaseTimetable": "2026-04-07T12:51:18Z",
            "departureTimePlanned": "2026-04-07T12:51:18Z",
            "departureTimeEstimated": "2026-04-07T12:52:18Z",
            "properties": {
              "AREA_NIVEAU_DIVA": "0",
              "area": "1",
              "platform": "1",
              "stoppingPointPlanned": "1",
              "platformName": "1"
            }
          },
          "destination": {
            "isGlobalId": true,
            "id": "9025001000001011",
            "name": "Slussen, Stockholm",
            "disassembledName": "1",
            "type": "platform",
            "coord": [
              59.319633,
              18.072226
            ],
            "niveau": 0,
            "parent": {
              "isGlobalId": true,
              "id": "9021001001011000",
              "name": "Slussen, Stockholm",
              "disassembledName": "Slussen",
              "type": "stop",
              "parent": {
                "id": "placeID:33001080:1",
                "name": "Stockholm",
                "type": "locality"
              },
              "properties": {
                "stopId": "18001011"
              },
              "coord": [
                59.319533,
                18.071615
              ],
              "niveau": 0
            },
            "productClasses": [
              2
            ],
            "arrivalTimeBaseTimetable": "2026-04-07T13:06:48Z",
            "arrivalTimePlanned": "2026-04-07T13:06:48Z",
            "arrivalTimeEstimated": "2026-04-07T13:07:18Z",
            "properties": {
              "AREA_NIVEAU_DIVA": "0",
              "area": "1",
              "platform": "1",
              "stoppingPointPlanned": "1",
              "platformName": "1"
            }
          },
          "transportation": {
            "id": "tfs:02018: :H:y01",
            "name": "Tunnelbana tunnelbanans gröna linje 18",
            "number": "tunnelbanans gröna linje 18",
            "product": {
              "id": 8,
              "class": 2,
              "name": "Tunnelbana",
              "iconId": 1
            },
            "operator": {
              "id": "1",
              "name": "Storstockholms Lokaltrafik"
            },
            "destination": {
              "id": "18001201",
              "name": "Alvik",
              "type": "stop"
            },
            "properties": {
              "tripCode": 59,
              "timetablePeriod": "Current",
              "lineDisplay": "LINE",
              "globalId": "9011001001800000",
              "RealtimeTripId": "9015001001810722",
              "shortTrain": false,
              "AVMSTripID": "9015001001810722"
            },
            "isSamtrafik": false,
            "disassembledName": "18"
          },
          "stopSequence": [
            {
              "isGlobalId": true,
              "id": "9025001000001861",
              "name": "Hökarängen, Stockholm",
              "disassembledName": "1",
              "type": "platform",
              "coord": [
                59.257932,
                18.082494
              ],
              "niveau": 0,
              "parent": {
                "isGlobalId": true,
                "id": "9021001001861000",
                "name": "Hökarängen, Stockholm",
                "disassembledName": "Hökarängen",
                "type": "stop",
                "parent": {
                  "id": "placeID:33001080:1",
                  "name": "Stockholm",
                  "type": "locality"
                },
                "properties": {
                  "stopId": "18001861"
                },
                "coord": [
                  59.257928,
                  18.082503
                ],
                "niveau": 0
              },
              "productClasses": [
                2
              ],
              "properties": {
                "AREA_NIVEAU_DIVA": "0",
                "area": "1",
                "platform": "1",
                "zone": "tfs:32",
                "stoppingPointPlanned": "1",
                "platformName": "1"
              },
              "departureTimePlanned": "2026-04-07T12:51:18Z",
              "departureTimeEstimated": "2026-04-07T12:52:18Z"
            },
            {
              "isGlobalId": true,
              "id": "9025001000001851",
              "name": "Gubbängen, Stockholm",
              "disassembledName": "1",
              "type": "platform",
              "coord": [
                59.263323,
                18.082134
              ],
              "niveau": 0,
              "parent": {
                "isGlobalId": true,
                "id": "9021001001851000",
                "name": "Gubbängen, Stockholm",
                "disassembledName": "Gubbängen",
                "type": "stop",
                "parent": {
                  "id": "placeID:33001080:1",
                  "name": "Stockholm",
                  "type": "locality"
                },
                "properties": {
                  "stopId": "18001851"
                },
                "coord": [
                  59.263327,
                  18.082134
                ],
                "niveau": 0
              },
              "productClasses": [
                2
              ],
              "properties": {
                "AREA_NIVEAU_DIVA": "0",
                "area": "1",
                "platform": "1",
                "zone": "tfs:32",
                "stoppingPointPlanned": "1",
                "platformName": "1"
              },
              "departureTimePlanned": "2026-04-07T12:52:42Z",
              "departureTimeEstimated": "2026-04-07T12:53:24Z",
              "arrivalTimePlanned": "2026-04-07T12:52:18Z",
              "arrivalTimeEstimated": "2026-04-07T12:52:30Z"
            },
            {
              "isGlobalId": true,
              "id": "9025001000001841",
              "name": "Tallkrogen, Stockholm",
              "disassembledName": "1",
              "type": "platform",
              "coord": [
                59.271265,
                18.085566
              ],
              "niveau": 0,
              "parent": {
                "isGlobalId": true,
                "id": "9021001001841000",
                "name": "Tallkrogen, Stockholm",
                "disassembledName": "Tallkrogen",
                "type": "stop",
                "parent": {
                  "id": "placeID:33001080:1",
                  "name": "Stockholm",
                  "type": "locality"
                },
                "properties": {
                  "stopId": "18001841"
                },
                "coord": [
                  59.271255,
                  18.085548
                ],
                "niveau": 0
              },
              "productClasses": [
                2
              ],
              "properties": {
                "AREA_NIVEAU_DIVA": "0",
                "area": "1",
                "platform": "1",
                "zone": "tfs:32",
                "stoppingPointPlanned": "1",
                "platformName": "1"
              },
              "departureTimePlanned": "2026-04-07T12:54:30Z",
              "departureTimeEstimated": "2026-04-07T12:55:06Z",
              "arrivalTimePlanned": "2026-04-07T12:54:06Z",
              "arrivalTimeEstimated": "2026-04-07T12:54:18Z"
            },
            {
              "isGlobalId": true,
              "id": "9025001000001831",
              "name": "Skogskyrkogården, Stockholm",
              "disassembledName": "1",
              "type": "platform",
              "coord": [
                59.278966,
                18.095519
              ],
              "niveau": 0,
              "parent": {
                "isGlobalId": true,
                "id": "9021001001831000",
                "name": "Skogskyrkogården, Stockholm",
                "disassembledName": "Skogskyrkogården",
                "type": "stop",
                "parent": {
                  "id": "placeID:33001080:1",
                  "name": "Stockholm",
                  "type": "locality"
                },
                "properties": {
                  "stopId": "18001831"
                },
                "coord": [
                  59.278966,
                  18.095519
                ],
                "niveau": 0
              },
              "productClasses": [
                2
              ],
              "properties": {
                "AREA_NIVEAU_DIVA": "0",
                "area": "1",
                "platform": "1",
                "zone": "tfs:32",
                "stoppingPointPlanned": "1",
                "platformName": "1"
              },
              "departureTimePlanned": "2026-04-07T12:56:12Z",
              "departureTimeEstimated": "2026-04-07T12:56:48Z",
              "arrivalTimePlanned": "2026-04-07T12:55:48Z",
              "arrivalTimeEstimated": "2026-04-07T12:55:54Z"
            },
            {
              "isGlobalId": true,
              "id": "9025001000001821",
              "name": "Sandsborg, Stockholm",
              "disassembledName": "1",
              "type": "platform",
              "coord": [
                59.285675,
                18.091935
              ],
              "niveau": 0,
              "parent": {
                "isGlobalId": true,
                "id": "9021001001821000",
                "name": "Sandsborg, Stockholm",
                "disassembledName": "Sandsborg",
                "type": "stop",
                "parent": {
                  "id": "placeID:33001080:1",
                  "name": "Stockholm",
                  "type": "locality"
                },
                "properties": {
                  "stopId": "18001821"
                },
                "coord": [
                  59.285675,
                  18.091935
                ],
                "niveau": 0
              },
              "productClasses": [
                2
              ],
              "properties": {
                "AREA_NIVEAU_DIVA": "0",
                "area": "1",
                "platform": "1",
                "zone": "tfs:32",
                "stoppingPointPlanned": "1",
                "platformName": "1"
              },
              "departureTimePlanned": "2026-04-07T12:57:48Z",
              "departureTimeEstimated": "2026-04-07T12:58:18Z",
              "arrivalTimePlanned": "2026-04-07T12:57:24Z",
              "arrivalTimeEstimated": "2026-04-07T12:57:24Z"
            },
            {
              "isGlobalId": true,
              "id": "9025001000001811",
              "name": "Blåsut, Stockholm",
              "disassembledName": "1",
              "type": "platform",
              "coord": [
                59.291185,
                18.091163
              ],
              "niveau": 0,
              "parent": {
                "isGlobalId": true,
                "id": "9021001001811000",
                "name": "Blåsut, Stockholm",
                "disassembledName": "Blåsut",
                "type": "stop",
                "parent": {
                  "id": "placeID:33001080:1",
                  "name": "Stockholm",
                  "type": "locality"
                },
                "properties": {
                  "stopId": "18001811"
                },
                "coord": [
                  59.291166,
                  18.091154
                ],
                "niveau": 0
              },
              "productClasses": [
                2
              ],
              "properties": {
                "AREA_NIVEAU_DIVA": "0",
                "area": "1",
                "platform": "1",
                "zone": "tfs:32",
                "stoppingPointPlanned": "1",
                "platformName": "1"
              },
              "departureTimePlanned": "2026-04-07T12:59:12Z",
              "departureTimeEstimated": "2026-04-07T12:59:42Z",
              "arrivalTimePlanned": "2026-04-07T12:58:48Z",
              "arrivalTimeEstimated": "2026-04-07T12:58:48Z"
            },
            {
              "isGlobalId": true,
              "id": "9025001000001603",
              "name": "Skärmarbrink, Stockholm",
              "disassembledName": "2",
              "type": "platform",
              "coord": [
                59.295286,
                18.090327
              ],
              "niveau": 0,
              "parent": {
                "isGlobalId": true,
                "id": "9021001001601000",
                "name": "Skärmarbrink, Stockholm",
                "disassembledName": "Skärmarbrink",
                "type": "stop",
                "parent": {
                  "id": "placeID:33001080:1",
                  "name": "Stockholm",
                  "type": "locality"
                },
                "properties": {
                  "stopId": "18001601"
                },
                "coord": [
                  59.295272,
                  18.090354
                ],
                "niveau": 0
              },
              "productClasses": [
                2
              ],
              "properties": {
                "AREA_NIVEAU_DIVA": "0",
                "area": "3",
                "platform": "1",
                "zone": "tfs:32",
                "stoppingPointPlanned": "2",
                "platformName": "2"
              },
              "departureTimePlanned": "2026-04-07T13:00:42Z",
              "departureTimeEstimated": "2026-04-07T13:01:18Z",
              "arrivalTimePlanned": "2026-04-07T13:00:18Z",
              "arrivalTimeEstimated": "2026-04-07T13:00:24Z"
            },
            {
              "isGlobalId": true,
              "id": "9025001000001551",
              "name": "Gullmarsplan, Stockholm",
              "disassembledName": "1",
              "type": "platform",
              "coord": [
                59.299184,
                18.080967
              ],
              "niveau": 0,
              "parent": {
                "isGlobalId": true,
                "id": "9021001001551000",
                "name": "Gullmarsplan, Stockholm",
                "disassembledName": "Gullmarsplan",
                "type": "stop",
                "parent": {
                  "id": "placeID:33001080:1",
                  "name": "Stockholm",
                  "type": "locality"
                },
                "properties": {
                  "stopId": "18001551"
                },
                "coord": [
                  59.299157,
                  18.080985
                ],
                "niveau": 0
              },
              "productClasses": [
                2
              ],
              "properties": {
                "AREA_NIVEAU_DIVA": "0",
                "area": "1",
                "platform": "1",
                "zone": "tfs:32",
                "stoppingPointPlanned": "1",
                "platformName": "1"
              },
              "departureTimePlanned": "2026-04-07T13:02:30Z",
              "departureTimeEstimated": "2026-04-07T13:03:18Z",
              "arrivalTimePlanned": "2026-04-07T13:01:54Z",
              "arrivalTimeEstimated": "2026-04-07T13:02:06Z"
            },
            {
              "isGlobalId": true,
              "id": "9025001000001521",
              "name": "Skanstull, Stockholm",
              "disassembledName": "1",
              "type": "platform",
              "coord": [
                59.308493,
                18.076062
              ],
              "niveau": 0,
              "parent": {
                "isGlobalId": true,
                "id": "9021001001521000",
                "name": "Skanstull, Stockholm",
                "disassembledName": "Skanstull",
                "type": "stop",
                "parent": {
                  "id": "placeID:33001080:1",
                  "name": "Stockholm",
                  "type": "locality"
                },
                "properties": {
                  "stopId": "18001521"
                },
                "coord": [
                  59.308498,
                  18.076107
                ],
                "niveau": 0
              },
              "productClasses": [
                2
              ],
              "properties": {
                "AREA_NIVEAU_DIVA": "0",
                "area": "1",
                "platform": "1",
                "zone": "tfs:33",
                "stoppingPointPlanned": "1",
                "platformName": "1"
              },
              "departureTimePlanned": "2026-04-07T13:04:24Z",
              "departureTimeEstimated": "2026-04-07T13:05:24Z",
              "arrivalTimePlanned": "2026-04-07T13:03:54Z",
              "arrivalTimeEstimated": "2026-04-07T13:04:30Z"
            },
            {
              "isGlobalId": true,
              "id": "9025001000001511",
              "name": "Medborgarplatsen, Stockholm",
              "disassembledName": "1",
              "type": "platform",
              "coord": [
                59.314889,
                18.073412
              ],
              "niveau": 0,
              "parent": {
                "isGlobalId": true,
                "id": "9021001001511000",
                "name": "Medborgarplatsen, Stockholm",
                "disassembledName": "Medborgarplatsen",
                "type": "stop",
                "parent": {
                  "id": "placeID:33001080:1",
                  "name": "Stockholm",
                  "type": "locality"
                },
                "properties": {
                  "stopId": "18001511"
                },
                "coord": [
                  59.31488,
                  18.073439
                ],
                "niveau": 0
              },
              "productClasses": [
                2
              ],
              "properties": {
                "AREA_NIVEAU_DIVA": "0",
                "area": "1",
                "platform": "1",
                "zone": "tfs:33",
                "stoppingPointPlanned": "1",
                "platformName": "1"
              },
              "departureTimePlanned": "2026-04-07T13:06:00Z",
              "departureTimeEstimated": "2026-04-07T13:06:54Z",
              "arrivalTimePlanned": "2026-04-07T13:05:30Z",
              "arrivalTimeEstimated": "2026-04-07T13:06:00Z"
            },
            {
              "isGlobalId": true,
              "id": "9025001000001011",
              "name": "Slussen, Stockholm",
              "disassembledName": "1",
              "type": "platform",
              "coord": [
                59.319633,
                18.072226
              ],
              "niveau": 0,
              "parent": {
                "isGlobalId": true,
                "id": "9021001001011000",
                "name": "Slussen, Stockholm",
                "disassembledName": "Slussen",
                "type": "stop",
                "parent": {
                  "id": "placeID:33001080:1",
                  "name": "Stockholm",
                  "type": "locality"
                },
                "properties": {
                  "stopId": "18001011"
                },
                "coord": [
                  59.319533,
                  18.071615
                ],
                "niveau": 0
              },
              "productClasses": [
                2
              ],
              "properties": {
                "AREA_NIVEAU_DIVA": "0",
                "area": "1",
                "platform": "1",
                "zone": "tfs:33",
                "stoppingPointPlanned": "1",
                "platformName": "1"
              },
              "arrivalTimePlanned": "2026-04-07T13:06:48Z",
              "arrivalTimeEstimated": "2026-04-07T13:07:18Z"
            }
          ],
          "properties": {
            "tripId": "9015001001810722"
          },
          "coords": [
            [
              59.257695,
              18.082629
            ],
            [
              59.257793,
              18.082575
            ],
            [
              59.257866,
              18.082539
            ],
            [
              59.257955,
              18.082501
            ],
            [
              59.25803,
              18.082474
            ],
            [
              59.258143,
              18.08244
            ],
            [
              59.258228,
              18.08242
            ],
            [
              59.258304,
              18.082407
            ],
            [
              59.258381,
              18.082398
            ],
            [
              59.258505,
              18.082391
            ],
            [
              59.258691,
              18.082389
            ],
            [
              59.259736,
              18.082403
            ],
            [
              59.261584,
              18.08242
            ],
            [
              59.261974,
              18.082413
            ],
            [
              59.262168,
              18.082404
            ],
            [
              59.262275,
              18.082396
            ],
            [
              59.262432,
              18.082376
            ],
            [
              59.262688,
              18.082325
            ],
            [
              59.263088,
              18.08223
            ],
            [
              59.263666,
              18.082092
            ],
            [
              59.263991,
              18.082018
            ],
            [
              59.264695,
              18.081875
            ],
            [
              59.265079,
              18.0818
            ],
            [
              59.265282,
              18.081766
            ],
            [
              59.265357,
              18.081757
            ],
            [
              59.265491,
              18.081745
            ],
            [
              59.26575,
              18.081733
            ],
            [
              59.265958,
              18.081732
            ],
            [
              59.266152,
              18.081741
            ],
            [
              59.266283,
              18.081755
            ],
            [
              59.266432,
              18.081778
            ],
            [
              59.266563,
              18.081803
            ],
            [
              59.266753,
              18.081847
            ],
            [
              59.26709,
              18.08194
            ],
            [
              59.267406,
              18.082034
            ],
            [
              59.26751,
              18.082067
            ],
            [
              59.267635,
              18.082113
            ],
            [
              59.26778,
              18.082173
            ],
            [
              59.267956,
              18.082251
            ],
            [
              59.268295,
              18.082408
            ],
            [
              59.2685,
              18.08251
            ],
            [
              59.268652,
              18.082592
            ],
            [
              59.269003,
              18.0828
            ],
            [
              59.269153,
              18.082892
            ],
            [
              59.269283,
              18.082976
            ],
            [
              59.269381,
              18.083047
            ],
            [
              59.26944,
              18.083092
            ],
            [
              59.269537,
              18.083173
            ],
            [
              59.269643,
              18.083268
            ],
            [
              59.269853,
              18.08347
            ],
            [
              59.269937,
              18.083556
            ],
            [
              59.27003,
              18.083655
            ],
            [
              59.270067,
              18.083697
            ],
            [
              59.270142,
              18.083788
            ],
            [
              59.270259,
              18.083943
            ],
            [
              59.270479,
              18.084256
            ],
            [
              59.270572,
              18.084391
            ],
            [
              59.270737,
              18.084642
            ],
            [
              59.270824,
              18.084782
            ],
            [
              59.270889,
              18.084893
            ],
            [
              59.270972,
              18.085042
            ],
            [
              59.271086,
              18.085255
            ],
            [
              59.272035,
              18.087079
            ],
            [
              59.273233,
              18.089368
            ],
            [
              59.273389,
              18.089669
            ],
            [
              59.273481,
              18.089853
            ],
            [
              59.27361,
              18.090124
            ],
            [
              59.273756,
              18.090452
            ],
            [
              59.274626,
              18.092455
            ],
            [
              59.274794,
              18.092839
            ],
            [
              59.274916,
              18.093107
            ],
            [
              59.274986,
              18.093251
            ],
            [
              59.275103,
              18.093482
            ],
            [
              59.2752,
              18.093667
            ],
            [
              59.275306,
              18.093861
            ],
            [
              59.275376,
              18.093983
            ],
            [
              59.275431,
              18.094075
            ],
            [
              59.275497,
              18.094175
            ],
            [
              59.275581,
              18.094292
            ],
            [
              59.275686,
              18.094422
            ],
            [
              59.275795,
              18.094541
            ],
            [
              59.275859,
              18.094603
            ],
            [
              59.275896,
              18.094636
            ],
            [
              59.276007,
              18.094725
            ],
            [
              59.276092,
              18.094785
            ],
            [
              59.276159,
              18.094828
            ],
            [
              59.276284,
              18.094902
            ],
            [
              59.276415,
              18.094967
            ],
            [
              59.276546,
              18.095019
            ],
            [
              59.27664,
              18.09505
            ],
            [
              59.276687,
              18.095063
            ],
            [
              59.27687,
              18.095101
            ],
            [
              59.277049,
              18.095129
            ],
            [
              59.277972,
              18.095263
            ],
            [
              59.278726,
              18.095377
            ],
            [
              59.278951,
              18.095411
            ],
            [
              59.279161,
              18.095439
            ],
            [
              59.279315,
              18.095453
            ],
            [
              59.279382,
              18.095455
            ],
            [
              59.279496,
              18.095452
            ],
            [
              59.279662,
              18.095439
            ],
            [
              59.279776,
              18.095426
            ],
            [
              59.279921,
              18.095404
            ],
            [
              59.280024,
              18.095384
            ],
            [
              59.280106,
              18.095363
            ],
            [
              59.28019,
              18.095336
            ],
            [
              59.280268,
              18.095306
            ],
            [
              59.280327,
              18.095282
            ],
            [
              59.280453,
              18.095224
            ],
            [
              59.280569,
              18.095166
            ],
            [
              59.28068,
              18.095102
            ],
            [
              59.280788,
              18.095036
            ],
            [
              59.281038,
              18.094872
            ],
            [
              59.28254,
              18.093863
            ],
            [
              59.284026,
              18.092848
            ],
            [
              59.28422,
              18.09272
            ],
            [
              59.284361,
              18.092633
            ],
            [
              59.284522,
              18.092544
            ],
            [
              59.28471,
              18.092446
            ],
            [
              59.285441,
              18.092077
            ],
            [
              59.285655,
              18.091969
            ],
            [
              59.285996,
              18.091804
            ],
            [
              59.286621,
              18.091507
            ],
            [
              59.286897,
              18.091382
            ],
            [
              59.287037,
              18.091327
            ],
            [
              59.287187,
              18.091277
            ],
            [
              59.287367,
              18.091228
            ],
            [
              59.287517,
              18.091197
            ],
            [
              59.287744,
              18.091169
            ],
            [
              59.287829,
              18.091162
            ],
            [
              59.289113,
              18.091073
            ],
            [
              59.28926,
              18.091063
            ],
            [
              59.289448,
              18.091056
            ],
            [
              59.289639,
              18.091056
            ],
            [
              59.289736,
              18.091059
            ],
            [
              59.289841,
              18.091067
            ],
            [
              59.289961,
              18.091081
            ],
            [
              59.290157,
              18.091111
            ],
            [
              59.290461,
              18.091163
            ],
            [
              59.290658,
              18.091201
            ],
            [
              59.290932,
              18.091264
            ],
            [
              59.291207,
              18.091335
            ],
            [
              59.29149,
              18.091404
            ],
            [
              59.293162,
              18.091798
            ],
            [
              59.293425,
              18.091857
            ],
            [
              59.293567,
              18.091882
            ],
            [
              59.29373,
              18.091899
            ],
            [
              59.293841,
              18.091904
            ],
            [
              59.293917,
              18.091904
            ],
            [
              59.294029,
              18.091894
            ],
            [
              59.294085,
              18.091884
            ],
            [
              59.294165,
              18.091861
            ],
            [
              59.294235,
              18.091835
            ],
            [
              59.294334,
              18.091787
            ],
            [
              59.294412,
              18.091743
            ],
            [
              59.294489,
              18.091692
            ],
            [
              59.294564,
              18.091632
            ],
            [
              59.294635,
              18.091566
            ],
            [
              59.294696,
              18.091503
            ],
            [
              59.294782,
              18.091404
            ],
            [
              59.294856,
              18.091308
            ],
            [
              59.29492,
              18.091218
            ],
            [
              59.294975,
              18.091133
            ],
            [
              59.295039,
              18.091024
            ],
            [
              59.2951,
              18.09091
            ],
            [
              59.295174,
              18.090764
            ],
            [
              59.295683,
              18.089715
            ],
            [
              59.295839,
              18.089398
            ],
            [
              59.296192,
              18.08869
            ],
            [
              59.296317,
              18.088426
            ],
            [
              59.29637,
              18.088305
            ],
            [
              59.296411,
              18.088204
            ],
            [
              59.296513,
              18.087933
            ],
            [
              59.296626,
              18.087606
            ],
            [
              59.296721,
              18.087307
            ],
            [
              59.296754,
              18.087196
            ],
            [
              59.296781,
              18.087095
            ],
            [
              59.296834,
              18.086877
            ],
            [
              59.296879,
              18.086673
            ],
            [
              59.296959,
              18.086278
            ],
            [
              59.297013,
              18.085993
            ],
            [
              59.297065,
              18.085689
            ],
            [
              59.297214,
              18.084785
            ],
            [
              59.297281,
              18.084395
            ],
            [
              59.297341,
              18.084078
            ],
            [
              59.297465,
              18.083466
            ],
            [
              59.297549,
              18.08308
            ],
            [
              59.297591,
              18.0829
            ],
            [
              59.297629,
              18.082751
            ],
            [
              59.297668,
              18.082607
            ],
            [
              59.297719,
              18.082435
            ],
            [
              59.297754,
              18.082331
            ],
            [
              59.297786,
              18.082247
            ],
            [
              59.297835,
              18.082135
            ],
            [
              59.297868,
              18.082071
            ],
            [
              59.29793,
              18.081961
            ],
            [
              59.297974,
              18.081894
            ],
            [
              59.298019,
              18.081831
            ],
            [
              59.298061,
              18.081779
            ],
            [
              59.298133,
              18.0817
            ],
            [
              59.298189,
              18.081646
            ],
            [
              59.298332,
              18.08152
            ],
            [
              59.298449,
              18.081425
            ],
            [
              59.298569,
              18.081333
            ],
            [
              59.298681,
              18.081252
            ],
            [
              59.29877,
              18.081193
            ],
            [
              59.298856,
              18.08114
            ],
            [
              59.299013,
              18.081053
            ],
            [
              59.29916,
              18.080976
            ],
            [
              59.299885,
              18.080603
            ],
            [
              59.300078,
              18.080507
            ],
            [
              59.300224,
              18.080441
            ],
            [
              59.300336,
              18.080396
            ],
            [
              59.30044,
              18.080358
            ],
            [
              59.300939,
              18.080191
            ],
            [
              59.301126,
              18.080124
            ],
            [
              59.301249,
              18.080075
            ],
            [
              59.301317,
              18.080044
            ],
            [
              59.301555,
              18.079926
            ],
            [
              59.301806,
              18.079793
            ],
            [
              59.30211,
              18.079628
            ],
            [
              59.302428,
              18.079448
            ],
            [
              59.302752,
              18.079259
            ],
            [
              59.306819,
              18.076789
            ],
            [
              59.307135,
              18.076603
            ],
            [
              59.307223,
              18.076555
            ],
            [
              59.307337,
              18.076499
            ],
            [
              59.307466,
              18.076438
            ],
            [
              59.307611,
              18.076376
            ],
            [
              59.307785,
              18.076316
            ],
            [
              59.308035,
              18.076246
            ],
            [
              59.308202,
              18.076192
            ],
            [
              59.308378,
              18.076119
            ],
            [
              59.308514,
              18.076056
            ],
            [
              59.30965,
              18.075492
            ],
            [
              59.311001,
              18.074852
            ],
            [
              59.311622,
              18.074553
            ],
            [
              59.311828,
              18.074461
            ],
            [
              59.312245,
              18.074284
            ],
            [
              59.312459,
              18.07419
            ],
            [
              59.313487,
              18.073718
            ],
            [
              59.313714,
              18.073616
            ],
            [
              59.313815,
              18.073574
            ],
            [
              59.313943,
              18.073527
            ],
            [
              59.314064,
              18.073491
            ],
            [
              59.314191,
              18.073462
            ],
            [
              59.314318,
              18.073439
            ],
            [
              59.314438,
              18.073425
            ],
            [
              59.314521,
              18.073419
            ],
            [
              59.314627,
              18.073415
            ],
            [
              59.314874,
              18.073414
            ],
            [
              59.315064,
              18.073412
            ],
            [
              59.315213,
              18.073408
            ],
            [
              59.315385,
              18.073395
            ],
            [
              59.315514,
              18.073379
            ],
            [
              59.315634,
              18.073361
            ],
            [
              59.315743,
              18.073339
            ],
            [
              59.315835,
              18.073316
            ],
            [
              59.315929,
              18.073288
            ],
            [
              59.316075,
              18.073241
            ],
            [
              59.316471,
              18.073101
            ],
            [
              59.316761,
              18.07299
            ],
            [
              59.317263,
              18.072774
            ],
            [
              59.317417,
              18.072719
            ],
            [
              59.317491,
              18.072698
            ],
            [
              59.317544,
              18.072688
            ],
            [
              59.317618,
              18.072677
            ],
            [
              59.3178,
              18.072658
            ],
            [
              59.317927,
              18.072672
            ],
            [
              59.318056,
              18.072674
            ],
            [
              59.318235,
              18.072711
            ],
            [
              59.318315,
              18.072719
            ],
            [
              59.318384,
              18.072719
            ],
            [
              59.318489,
              18.072712
            ],
            [
              59.318575,
              18.072701
            ],
            [
              59.318684,
              18.072682
            ],
            [
              59.318794,
              18.072658
            ],
            [
              59.318932,
              18.07262
            ],
            [
              59.319019,
              18.072588
            ],
            [
              59.319098,
              18.072555
            ],
            [
              59.319227,
              18.072494
            ],
            [
              59.319331,
              18.072437
            ],
            [
              59.319413,
              18.072386
            ],
            [
              59.319501,
              18.072324
            ],
            [
              59.319621,
              18.072231
            ]
          ],
          "realtimeStatus": [
            "MONITORED"
          ],
          "isRealtimeControlled": true
        }
      ],
      "daysOfService": {
        "rvb": "000000000000000000000000000000400000000000000000"
      }
    },
    {
      "tripDuration": 930,
      "tripRtDuration": 912,
      "rating": 0,
      "isAdditional": false,
      "interchanges": 0,
      "legs": [
        {
          "infos": [

          ],
          "duration": 912,
          "origin": {
            "isGlobalId": true,
            "id": "9025001000001861",
            "name": "Hökarängen, Stockholm",
            "disassembledName": "1",
            "type": "platform",
            "coord": [
              59.257932,
              18.082494
            ],
            "niveau": 0,
            "parent": {
              "isGlobalId": true,
              "id": "9021001001861000",
              "name": "Hökarängen, Stockholm",
              "disassembledName": "Hökarängen",
              "type": "stop",
              "parent": {
                "id": "placeID:33001080:1",
                "name": "Stockholm",
                "type": "locality"
              },
              "properties": {
                "stopId": "18001861"
              },
              "coord": [
                59.257928,
                18.082503
              ],
              "niveau": 0
            },
            "productClasses": [
              2
            ],
            "departureTimeBaseTimetable": "2026-04-07T12:58:48Z",
            "departureTimePlanned": "2026-04-07T12:58:48Z",
            "departureTimeEstimated": "2026-04-07T12:58:48Z",
            "properties": {
              "AREA_NIVEAU_DIVA": "0",
              "area": "1",
              "occupancy": "MANY_SEATS",
              "platform": "1",
              "stoppingPointPlanned": "1",
              "platformName": "1"
            }
          },
          "destination": {
            "isGlobalId": true,
            "id": "9025001000001011",
            "name": "Slussen, Stockholm",
            "disassembledName": "1",
            "type": "platform",
            "coord": [
              59.319633,
              18.072226
            ],
            "niveau": 0,
            "parent": {
              "isGlobalId": true,
              "id": "9021001001011000",
              "name": "Slussen, Stockholm",
              "disassembledName": "Slussen",
              "type": "stop",
              "parent": {
                "id": "placeID:33001080:1",
                "name": "Stockholm",
                "type": "locality"
              },
              "properties": {
                "stopId": "18001011"
              },
              "coord": [
                59.319533,
                18.071615
              ],
              "niveau": 0
            },
            "productClasses": [
              2
            ],
            "arrivalTimeBaseTimetable": "2026-04-07T13:14:18Z",
            "arrivalTimePlanned": "2026-04-07T13:14:18Z",
            "arrivalTimeEstimated": "2026-04-07T13:14:00Z",
            "properties": {
              "AREA_NIVEAU_DIVA": "0",
              "area": "1",
              "platform": "1",
              "stoppingPointPlanned": "1",
              "platformName": "1"
            }
          },
          "transportation": {
            "id": "tfs:02018: :H:y01",
            "name": "Tunnelbana tunnelbanans gröna linje 18",
            "number": "tunnelbanans gröna linje 18",
            "product": {
              "id": 8,
              "class": 2,
              "name": "Tunnelbana",
              "iconId": 1
            },
            "operator": {
              "id": "1",
              "name": "Storstockholms Lokaltrafik"
            },
            "destination": {
              "id": "18001201",
              "name": "Alvik",
              "type": "stop"
            },
            "properties": {
              "tripCode": 60,
              "timetablePeriod": "Current",
              "lineDisplay": "LINE",
              "globalId": "9011001001800000",
              "RealtimeTripId": "9015001001810732",
              "shortTrain": false,
              "AVMSTripID": "9015001001810732"
            },
            "isSamtrafik": false,
            "disassembledName": "18"
          },
          "stopSequence": [
            {
              "isGlobalId": true,
              "id": "9025001000001861",
              "name": "Hökarängen, Stockholm",
              "disassembledName": "1",
              "type": "platform",
              "coord": [
                59.257932,
                18.082494
              ],
              "niveau": 0,
              "parent": {
                "isGlobalId": true,
                "id": "9021001001861000",
                "name": "Hökarängen, Stockholm",
                "disassembledName": "Hökarängen",
                "type": "stop",
                "parent": {
                  "id": "placeID:33001080:1",
                  "name": "Stockholm",
                  "type": "locality"
                },
                "properties": {
                  "stopId": "18001861"
                },
                "coord": [
                  59.257928,
                  18.082503
                ],
                "niveau": 0
              },
              "productClasses": [
                2
              ],
              "properties": {
                "AREA_NIVEAU_DIVA": "0",
                "area": "1",
                "occupancy": "MANY_SEATS",
                "platform": "1",
                "zone": "tfs:32",
                "stoppingPointPlanned": "1",
                "platformName": "1"
              },
              "departureTimePlanned": "2026-04-07T12:58:48Z",
              "departureTimeEstimated": "2026-04-07T12:58:48Z"
            },
            {
              "isGlobalId": true,
              "id": "9025001000001851",
              "name": "Gubbängen, Stockholm",
              "disassembledName": "1",
              "type": "platform",
              "coord": [
                59.263323,
                18.082134
              ],
              "niveau": 0,
              "parent": {
                "isGlobalId": true,
                "id": "9021001001851000",
                "name": "Gubbängen, Stockholm",
                "disassembledName": "Gubbängen",
                "type": "stop",
                "parent": {
                  "id": "placeID:33001080:1",
                  "name": "Stockholm",
                  "type": "locality"
                },
                "properties": {
                  "stopId": "18001851"
                },
                "coord": [
                  59.263327,
                  18.082134
                ],
                "niveau": 0
              },
              "productClasses": [
                2
              ],
              "properties": {
                "AREA_NIVEAU_DIVA": "0",
                "area": "1",
                "occupancy": "MANY_SEATS",
                "platform": "1",
                "zone": "tfs:32",
                "stoppingPointPlanned": "1",
                "platformName": "1"
              },
              "departureTimePlanned": "2026-04-07T13:00:12Z",
              "departureTimeEstimated": "2026-04-07T13:00:12Z",
              "arrivalTimePlanned": "2026-04-07T12:59:48Z",
              "arrivalTimeEstimated": "2026-04-07T12:59:06Z"
            },
            {
              "isGlobalId": true,
              "id": "9025001000001841",
              "name": "Tallkrogen, Stockholm",
              "disassembledName": "1",
              "type": "platform",
              "coord": [
                59.271265,
                18.085566
              ],
              "niveau": 0,
              "parent": {
                "isGlobalId": true,
                "id": "9021001001841000",
                "name": "Tallkrogen, Stockholm",
                "disassembledName": "Tallkrogen",
                "type": "stop",
                "parent": {
                  "id": "placeID:33001080:1",
                  "name": "Stockholm",
                  "type": "locality"
                },
                "properties": {
                  "stopId": "18001841"
                },
                "coord": [
                  59.271255,
                  18.085548
                ],
                "niveau": 0
              },
              "productClasses": [
                2
              ],
              "properties": {
                "AREA_NIVEAU_DIVA": "0",
                "area": "1",
                "occupancy": "MANY_SEATS",
                "platform": "1",
                "zone": "tfs:32",
                "stoppingPointPlanned": "1",
                "platformName": "1"
              },
              "departureTimePlanned": "2026-04-07T13:02:00Z",
              "departureTimeEstimated": "2026-04-07T13:02:00Z",
              "arrivalTimePlanned": "2026-04-07T13:01:36Z",
              "arrivalTimeEstimated": "2026-04-07T13:00:42Z"
            },
            {
              "isGlobalId": true,
              "id": "9025001000001831",
              "name": "Skogskyrkogården, Stockholm",
              "disassembledName": "1",
              "type": "platform",
              "coord": [
                59.278966,
                18.095519
              ],
              "niveau": 0,
              "parent": {
                "isGlobalId": true,
                "id": "9021001001831000",
                "name": "Skogskyrkogården, Stockholm",
                "disassembledName": "Skogskyrkogården",
                "type": "stop",
                "parent": {
                  "id": "placeID:33001080:1",
                  "name": "Stockholm",
                  "type": "locality"
                },
                "properties": {
                  "stopId": "18001831"
                },
                "coord": [
                  59.278966,
                  18.095519
                ],
                "niveau": 0
              },
              "productClasses": [
                2
              ],
              "properties": {
                "AREA_NIVEAU_DIVA": "0",
                "area": "1",
                "occupancy": "MANY_SEATS",
                "platform": "1",
                "zone": "tfs:32",
                "stoppingPointPlanned": "1",
                "platformName": "1"
              },
              "departureTimePlanned": "2026-04-07T13:03:42Z",
              "departureTimeEstimated": "2026-04-07T13:03:42Z",
              "arrivalTimePlanned": "2026-04-07T13:03:18Z",
              "arrivalTimeEstimated": "2026-04-07T13:02:30Z"
            },
            {
              "isGlobalId": true,
              "id": "9025001000001821",
              "name": "Sandsborg, Stockholm",
              "disassembledName": "1",
              "type": "platform",
              "coord": [
                59.285675,
                18.091935
              ],
              "niveau": 0,
              "parent": {
                "isGlobalId": true,
                "id": "9021001001821000",
                "name": "Sandsborg, Stockholm",
                "disassembledName": "Sandsborg",
                "type": "stop",
                "parent": {
                  "id": "placeID:33001080:1",
                  "name": "Stockholm",
                  "type": "locality"
                },
                "properties": {
                  "stopId": "18001821"
                },
                "coord": [
                  59.285675,
                  18.091935
                ],
                "niveau": 0
              },
              "productClasses": [
                2
              ],
              "properties": {
                "AREA_NIVEAU_DIVA": "0",
                "area": "1",
                "occupancy": "MANY_SEATS",
                "platform": "1",
                "zone": "tfs:32",
                "stoppingPointPlanned": "1",
                "platformName": "1"
              },
              "departureTimePlanned": "2026-04-07T13:05:18Z",
              "departureTimeEstimated": "2026-04-07T13:05:18Z",
              "arrivalTimePlanned": "2026-04-07T13:04:54Z",
              "arrivalTimeEstimated": "2026-04-07T13:04:06Z"
            },
            {
              "isGlobalId": true,
              "id": "9025001000001811",
              "name": "Blåsut, Stockholm",
              "disassembledName": "1",
              "type": "platform",
              "coord": [
                59.291185,
                18.091163
              ],
              "niveau": 0,
              "parent": {
                "isGlobalId": true,
                "id": "9021001001811000",
                "name": "Blåsut, Stockholm",
                "disassembledName": "Blåsut",
                "type": "stop",
                "parent": {
                  "id": "placeID:33001080:1",
                  "name": "Stockholm",
                  "type": "locality"
                },
                "properties": {
                  "stopId": "18001811"
                },
                "coord": [
                  59.291166,
                  18.091154
                ],
                "niveau": 0
              },
              "productClasses": [
                2
              ],
              "properties": {
                "AREA_NIVEAU_DIVA": "0",
                "area": "1",
                "occupancy": "MANY_SEATS",
                "platform": "1",
                "zone": "tfs:32",
                "stoppingPointPlanned": "1",
                "platformName": "1"
              },
              "departureTimePlanned": "2026-04-07T13:06:42Z",
              "departureTimeEstimated": "2026-04-07T13:06:42Z",
              "arrivalTimePlanned": "2026-04-07T13:06:18Z",
              "arrivalTimeEstimated": "2026-04-07T13:05:36Z"
            },
            {
              "isGlobalId": true,
              "id": "9025001000001603",
              "name": "Skärmarbrink, Stockholm",
              "disassembledName": "2",
              "type": "platform",
              "coord": [
                59.295286,
                18.090327
              ],
              "niveau": 0,
              "parent": {
                "isGlobalId": true,
                "id": "9021001001601000",
                "name": "Skärmarbrink, Stockholm",
                "disassembledName": "Skärmarbrink",
                "type": "stop",
                "parent": {
                  "id": "placeID:33001080:1",
                  "name": "Stockholm",
                  "type": "locality"
                },
                "properties": {
                  "stopId": "18001601"
                },
                "coord": [
                  59.295272,
                  18.090354
                ],
                "niveau": 0
              },
              "productClasses": [
                2
              ],
              "properties": {
                "AREA_NIVEAU_DIVA": "0",
                "area": "3",
                "occupancy": "MANY_SEATS",
                "platform": "1",
                "zone": "tfs:32",
                "stoppingPointPlanned": "2",
                "platformName": "2"
              },
              "departureTimePlanned": "2026-04-07T13:08:12Z",
              "departureTimeEstimated": "2026-04-07T13:08:12Z",
              "arrivalTimePlanned": "2026-04-07T13:07:48Z",
              "arrivalTimeEstimated": "2026-04-07T13:06:54Z"
            },
            {
              "isGlobalId": true,
              "id": "9025001000001551",
              "name": "Gullmarsplan, Stockholm",
              "disassembledName": "1",
              "type": "platform",
              "coord": [
                59.299184,
                18.080967
              ],
              "niveau": 0,
              "parent": {
                "isGlobalId": true,
                "id": "9021001001551000",
                "name": "Gullmarsplan, Stockholm",
                "disassembledName": "Gullmarsplan",
                "type": "stop",
                "parent": {
                  "id": "placeID:33001080:1",
                  "name": "Stockholm",
                  "type": "locality"
                },
                "properties": {
                  "stopId": "18001551"
                },
                "coord": [
                  59.299157,
                  18.080985
                ],
                "niveau": 0
              },
              "productClasses": [
                2
              ],
              "properties": {
                "AREA_NIVEAU_DIVA": "0",
                "area": "1",
                "occupancy": "FEW_SEATS",
                "platform": "1",
                "zone": "tfs:32",
                "stoppingPointPlanned": "1",
                "platformName": "1"
              },
              "departureTimePlanned": "2026-04-07T13:10:00Z",
              "departureTimeEstimated": "2026-04-07T13:10:00Z",
              "arrivalTimePlanned": "2026-04-07T13:09:24Z",
              "arrivalTimeEstimated": "2026-04-07T13:08:36Z"
            },
            {
              "isGlobalId": true,
              "id": "9025001000001521",
              "name": "Skanstull, Stockholm",
              "disassembledName": "1",
              "type": "platform",
              "coord": [
                59.308493,
                18.076062
              ],
              "niveau": 0,
              "parent": {
                "isGlobalId": true,
                "id": "9021001001521000",
                "name": "Skanstull, Stockholm",
                "disassembledName": "Skanstull",
                "type": "stop",
                "parent": {
                  "id": "placeID:33001080:1",
                  "name": "Stockholm",
                  "type": "locality"
                },
                "properties": {
                  "stopId": "18001521"
                },
                "coord": [
                  59.308498,
                  18.076107
                ],
                "niveau": 0
              },
              "productClasses": [
                2
              ],
              "properties": {
                "AREA_NIVEAU_DIVA": "0",
                "area": "1",
                "occupancy": "FEW_SEATS",
                "platform": "1",
                "zone": "tfs:33",
                "stoppingPointPlanned": "1",
                "platformName": "1"
              },
              "departureTimePlanned": "2026-04-07T13:11:54Z",
              "departureTimeEstimated": "2026-04-07T13:12:12Z",
              "arrivalTimePlanned": "2026-04-07T13:11:24Z",
              "arrivalTimeEstimated": "2026-04-07T13:11:18Z"
            },
            {
              "isGlobalId": true,
              "id": "9025001000001511",
              "name": "Medborgarplatsen, Stockholm",
              "disassembledName": "1",
              "type": "platform",
              "coord": [
                59.314889,
                18.073412
              ],
              "niveau": 0,
              "parent": {
                "isGlobalId": true,
                "id": "9021001001511000",
                "name": "Medborgarplatsen, Stockholm",
                "disassembledName": "Medborgarplatsen",
                "type": "stop",
                "parent": {
                  "id": "placeID:33001080:1",
                  "name": "Stockholm",
                  "type": "locality"
                },
                "properties": {
                  "stopId": "18001511"
                },
                "coord": [
                  59.31488,
                  18.073439
                ],
                "niveau": 0
              },
              "productClasses": [
                2
              ],
              "properties": {
                "AREA_NIVEAU_DIVA": "0",
                "area": "1",
                "occupancy": "FEW_SEATS",
                "platform": "1",
                "zone": "tfs:33",
                "stoppingPointPlanned": "1",
                "platformName": "1"
              },
              "departureTimePlanned": "2026-04-07T13:13:30Z",
              "departureTimeEstimated": "2026-04-07T13:13:36Z",
              "arrivalTimePlanned": "2026-04-07T13:13:00Z",
              "arrivalTimeEstimated": "2026-04-07T13:12:48Z"
            },
            {
              "isGlobalId": true,
              "id": "9025001000001011",
              "name": "Slussen, Stockholm",
              "disassembledName": "1",
              "type": "platform",
              "coord": [
                59.319633,
                18.072226
              ],
              "niveau": 0,
              "parent": {
                "isGlobalId": true,
                "id": "9021001001011000",
                "name": "Slussen, Stockholm",
                "disassembledName": "Slussen",
                "type": "stop",
                "parent": {
                  "id": "placeID:33001080:1",
                  "name": "Stockholm",
                  "type": "locality"
                },
                "properties": {
                  "stopId": "18001011"
                },
                "coord": [
                  59.319533,
                  18.071615
                ],
                "niveau": 0
              },
              "productClasses": [
                2
              ],
              "properties": {
                "AREA_NIVEAU_DIVA": "0",
                "area": "1",
                "platform": "1",
                "zone": "tfs:33",
                "stoppingPointPlanned": "1",
                "platformName": "1"
              },
              "arrivalTimePlanned": "2026-04-07T13:14:18Z",
              "arrivalTimeEstimated": "2026-04-07T13:14:00Z"
            }
          ],
          "properties": {
            "tripId": "9015001001810732"
          },
          "coords": [
            [
              59.257695,
              18.082629
            ],
            [
              59.257793,
              18.082575
            ],
            [
              59.257866,
              18.082539
            ],
            [
              59.257955,
              18.082501
            ],
            [
              59.25803,
              18.082474
            ],
            [
              59.258143,
              18.08244
            ],
            [
              59.258228,
              18.08242
            ],
            [
              59.258304,
              18.082407
            ],
            [
              59.258381,
              18.082398
            ],
            [
              59.258505,
              18.082391
            ],
            [
              59.258691,
              18.082389
            ],
            [
              59.259736,
              18.082403
            ],
            [
              59.261584,
              18.08242
            ],
            [
              59.261974,
              18.082413
            ],
            [
              59.262168,
              18.082404
            ],
            [
              59.262275,
              18.082396
            ],
            [
              59.262432,
              18.082376
            ],
            [
              59.262688,
              18.082325
            ],
            [
              59.263088,
              18.08223
            ],
            [
              59.263666,
              18.082092
            ],
            [
              59.263991,
              18.082018
            ],
            [
              59.264695,
              18.081875
            ],
            [
              59.265079,
              18.0818
            ],
            [
              59.265282,
              18.081766
            ],
            [
              59.265357,
              18.081757
            ],
            [
              59.265491,
              18.081745
            ],
            [
              59.26575,
              18.081733
            ],
            [
              59.265958,
              18.081732
            ],
            [
              59.266152,
              18.081741
            ],
            [
              59.266283,
              18.081755
            ],
            [
              59.266432,
              18.081778
            ],
            [
              59.266563,
              18.081803
            ],
            [
              59.266753,
              18.081847
            ],
            [
              59.26709,
              18.08194
            ],
            [
              59.267406,
              18.082034
            ],
            [
              59.26751,
              18.082067
            ],
            [
              59.267635,
              18.082113
            ],
            [
              59.26778,
              18.082173
            ],
            [
              59.267956,
              18.082251
            ],
            [
              59.268295,
              18.082408
            ],
            [
              59.2685,
              18.08251
            ],
            [
              59.268652,
              18.082592
            ],
            [
              59.269003,
              18.0828
            ],
            [
              59.269153,
              18.082892
            ],
            [
              59.269283,
              18.082976
            ],
            [
              59.269381,
              18.083047
            ],
            [
              59.26944,
              18.083092
            ],
            [
              59.269537,
              18.083173
            ],
            [
              59.269643,
              18.083268
            ],
            [
              59.269853,
              18.08347
            ],
            [
              59.269937,
              18.083556
            ],
            [
              59.27003,
              18.083655
            ],
            [
              59.270067,
              18.083697
            ],
            [
              59.270142,
              18.083788
            ],
            [
              59.270259,
              18.083943
            ],
            [
              59.270479,
              18.084256
            ],
            [
              59.270572,
              18.084391
            ],
            [
              59.270737,
              18.084642
            ],
            [
              59.270824,
              18.084782
            ],
            [
              59.270889,
              18.084893
            ],
            [
              59.270972,
              18.085042
            ],
            [
              59.271086,
              18.085255
            ],
            [
              59.272035,
              18.087079
            ],
            [
              59.273233,
              18.089368
            ],
            [
              59.273389,
              18.089669
            ],
            [
              59.273481,
              18.089853
            ],
            [
              59.27361,
              18.090124
            ],
            [
              59.273756,
              18.090452
            ],
            [
              59.274626,
              18.092455
            ],
            [
              59.274794,
              18.092839
            ],
            [
              59.274916,
              18.093107
            ],
            [
              59.274986,
              18.093251
            ],
            [
              59.275103,
              18.093482
            ],
            [
              59.2752,
              18.093667
            ],
            [
              59.275306,
              18.093861
            ],
            [
              59.275376,
              18.093983
            ],
            [
              59.275431,
              18.094075
            ],
            [
              59.275497,
              18.094175
            ],
            [
              59.275581,
              18.094292
            ],
            [
              59.275686,
              18.094422
            ],
            [
              59.275795,
              18.094541
            ],
            [
              59.275859,
              18.094603
            ],
            [
              59.275896,
              18.094636
            ],
            [
              59.276007,
              18.094725
            ],
            [
              59.276092,
              18.094785
            ],
            [
              59.276159,
              18.094828
            ],
            [
              59.276284,
              18.094902
            ],
            [
              59.276415,
              18.094967
            ],
            [
              59.276546,
              18.095019
            ],
            [
              59.27664,
              18.09505
            ],
            [
              59.276687,
              18.095063
            ],
            [
              59.27687,
              18.095101
            ],
            [
              59.277049,
              18.095129
            ],
            [
              59.277972,
              18.095263
            ],
            [
              59.278726,
              18.095377
            ],
            [
              59.278951,
              18.095411
            ],
            [
              59.279161,
              18.095439
            ],
            [
              59.279315,
              18.095453
            ],
            [
              59.279382,
              18.095455
            ],
            [
              59.279496,
              18.095452
            ],
            [
              59.279662,
              18.095439
            ],
            [
              59.279776,
              18.095426
            ],
            [
              59.279921,
              18.095404
            ],
            [
              59.280024,
              18.095384
            ],
            [
              59.280106,
              18.095363
            ],
            [
              59.28019,
              18.095336
            ],
            [
              59.280268,
              18.095306
            ],
            [
              59.280327,
              18.095282
            ],
            [
              59.280453,
              18.095224
            ],
            [
              59.280569,
              18.095166
            ],
            [
              59.28068,
              18.095102
            ],
            [
              59.280788,
              18.095036
            ],
            [
              59.281038,
              18.094872
            ],
            [
              59.28254,
              18.093863
            ],
            [
              59.284026,
              18.092848
            ],
            [
              59.28422,
              18.09272
            ],
            [
              59.284361,
              18.092633
            ],
            [
              59.284522,
              18.092544
            ],
            [
              59.28471,
              18.092446
            ],
            [
              59.285441,
              18.092077
            ],
            [
              59.285655,
              18.091969
            ],
            [
              59.285996,
              18.091804
            ],
            [
              59.286621,
              18.091507
            ],
            [
              59.286897,
              18.091382
            ],
            [
              59.287037,
              18.091327
            ],
            [
              59.287187,
              18.091277
            ],
            [
              59.287367,
              18.091228
            ],
            [
              59.287517,
              18.091197
            ],
            [
              59.287744,
              18.091169
            ],
            [
              59.287829,
              18.091162
            ],
            [
              59.289113,
              18.091073
            ],
            [
              59.28926,
              18.091063
            ],
            [
              59.289448,
              18.091056
            ],
            [
              59.289639,
              18.091056
            ],
            [
              59.289736,
              18.091059
            ],
            [
              59.289841,
              18.091067
            ],
            [
              59.289961,
              18.091081
            ],
            [
              59.290157,
              18.091111
            ],
            [
              59.290461,
              18.091163
            ],
            [
              59.290658,
              18.091201
            ],
            [
              59.290932,
              18.091264
            ],
            [
              59.291207,
              18.091335
            ],
            [
              59.29149,
              18.091404
            ],
            [
              59.293162,
              18.091798
            ],
            [
              59.293425,
              18.091857
            ],
            [
              59.293567,
              18.091882
            ],
            [
              59.29373,
              18.091899
            ],
            [
              59.293841,
              18.091904
            ],
            [
              59.293917,
              18.091904
            ],
            [
              59.294029,
              18.091894
            ],
            [
              59.294085,
              18.091884
            ],
            [
              59.294165,
              18.091861
            ],
            [
              59.294235,
              18.091835
            ],
            [
              59.294334,
              18.091787
            ],
            [
              59.294412,
              18.091743
            ],
            [
              59.294489,
              18.091692
            ],
            [
              59.294564,
              18.091632
            ],
            [
              59.294635,
              18.091566
            ],
            [
              59.294696,
              18.091503
            ],
            [
              59.294782,
              18.091404
            ],
            [
              59.294856,
              18.091308
            ],
            [
              59.29492,
              18.091218
            ],
            [
              59.294975,
              18.091133
            ],
            [
              59.295039,
              18.091024
            ],
            [
              59.2951,
              18.09091
            ],
            [
              59.295174,
              18.090764
            ],
            [
              59.295683,
              18.089715
            ],
            [
              59.295839,
              18.089398
            ],
            [
              59.296192,
              18.08869
            ],
            [
              59.296317,
              18.088426
            ],
            [
              59.29637,
              18.088305
            ],
            [
              59.296411,
              18.088204
            ],
            [
              59.296513,
              18.087933
            ],
            [
              59.296626,
              18.087606
            ],
            [
              59.296721,
              18.087307
            ],
            [
              59.296754,
              18.087196
            ],
            [
              59.296781,
              18.087095
            ],
            [
              59.296834,
              18.086877
            ],
            [
              59.296879,
              18.086673
            ],
            [
              59.296959,
              18.086278
            ],
            [
              59.297013,
              18.085993
            ],
            [
              59.297065,
              18.085689
            ],
            [
              59.297214,
              18.084785
            ],
            [
              59.297281,
              18.084395
            ],
            [
              59.297341,
              18.084078
            ],
            [
              59.297465,
              18.083466
            ],
            [
              59.297549,
              18.08308
            ],
            [
              59.297591,
              18.0829
            ],
            [
              59.297629,
              18.082751
            ],
            [
              59.297668,
              18.082607
            ],
            [
              59.297719,
              18.082435
            ],
            [
              59.297754,
              18.082331
            ],
            [
              59.297786,
              18.082247
            ],
            [
              59.297835,
              18.082135
            ],
            [
              59.297868,
              18.082071
            ],
            [
              59.29793,
              18.081961
            ],
            [
              59.297974,
              18.081894
            ],
            [
              59.298019,
              18.081831
            ],
            [
              59.298061,
              18.081779
            ],
            [
              59.298133,
              18.0817
            ],
            [
              59.298189,
              18.081646
            ],
            [
              59.298332,
              18.08152
            ],
            [
              59.298449,
              18.081425
            ],
            [
              59.298569,
              18.081333
            ],
            [
              59.298681,
              18.081252
            ],
            [
              59.29877,
              18.081193
            ],
            [
              59.298856,
              18.08114
            ],
            [
              59.299013,
              18.081053
            ],
            [
              59.29916,
              18.080976
            ],
            [
              59.299885,
              18.080603
            ],
            [
              59.300078,
              18.080507
            ],
            [
              59.300224,
              18.080441
            ],
            [
              59.300336,
              18.080396
            ],
            [
              59.30044,
              18.080358
            ],
            [
              59.300939,
              18.080191
            ],
            [
              59.301126,
              18.080124
            ],
            [
              59.301249,
              18.080075
            ],
            [
              59.301317,
              18.080044
            ],
            [
              59.301555,
              18.079926
            ],
            [
              59.301806,
              18.079793
            ],
            [
              59.30211,
              18.079628
            ],
            [
              59.302428,
              18.079448
            ],
            [
              59.302752,
              18.079259
            ],
            [
              59.306819,
              18.076789
            ],
            [
              59.307135,
              18.076603
            ],
            [
              59.307223,
              18.076555
            ],
            [
              59.307337,
              18.076499
            ],
            [
              59.307466,
              18.076438
            ],
            [
              59.307611,
              18.076376
            ],
            [
              59.307785,
              18.076316
            ],
            [
              59.308035,
              18.076246
            ],
            [
              59.308202,
              18.076192
            ],
            [
              59.308378,
              18.076119
            ],
            [
              59.308514,
              18.076056
            ],
            [
              59.30965,
              18.075492
            ],
            [
              59.311001,
              18.074852
            ],
            [
              59.311622,
              18.074553
            ],
            [
              59.311828,
              18.074461
            ],
            [
              59.312245,
              18.074284
            ],
            [
              59.312459,
              18.07419
            ],
            [
              59.313487,
              18.073718
            ],
            [
              59.313714,
              18.073616
            ],
            [
              59.313815,
              18.073574
            ],
            [
              59.313943,
              18.073527
            ],
            [
              59.314064,
              18.073491
            ],
            [
              59.314191,
              18.073462
            ],
            [
              59.314318,
              18.073439
            ],
            [
              59.314438,
              18.073425
            ],
            [
              59.314521,
              18.073419
            ],
            [
              59.314627,
              18.073415
            ],
            [
              59.314874,
              18.073414
            ],
            [
              59.315064,
              18.073412
            ],
            [
              59.315213,
              18.073408
            ],
            [
              59.315385,
              18.073395
            ],
            [
              59.315514,
              18.073379
            ],
            [
              59.315634,
              18.073361
            ],
            [
              59.315743,
              18.073339
            ],
            [
              59.315835,
              18.073316
            ],
            [
              59.315929,
              18.073288
            ],
            [
              59.316075,
              18.073241
            ],
            [
              59.316471,
              18.073101
            ],
            [
              59.316761,
              18.07299
            ],
            [
              59.317263,
              18.072774
            ],
            [
              59.317417,
              18.072719
            ],
            [
              59.317491,
              18.072698
            ],
            [
              59.317544,
              18.072688
            ],
            [
              59.317618,
              18.072677
            ],
            [
              59.3178,
              18.072658
            ],
            [
              59.317927,
              18.072672
            ],
            [
              59.318056,
              18.072674
            ],
            [
              59.318235,
              18.072711
            ],
            [
              59.318315,
              18.072719
            ],
            [
              59.318384,
              18.072719
            ],
            [
              59.318489,
              18.072712
            ],
            [
              59.318575,
              18.072701
            ],
            [
              59.318684,
              18.072682
            ],
            [
              59.318794,
              18.072658
            ],
            [
              59.318932,
              18.07262
            ],
            [
              59.319019,
              18.072588
            ],
            [
              59.319098,
              18.072555
            ],
            [
              59.319227,
              18.072494
            ],
            [
              59.319331,
              18.072437
            ],
            [
              59.319413,
              18.072386
            ],
            [
              59.319501,
              18.072324
            ],
            [
              59.319621,
              18.072231
            ]
          ],
          "realtimeStatus": [
            "MONITORED"
          ],
          "isRealtimeControlled": true
        }
      ],
      "daysOfService": {
        "rvb": "000000000000000000000000000000400000000000000000"
      }
    }
  ]
}
```

{{% /tab %}}
{{% /tabs %}}

## OpenAPI specification

{{% oai-spec url="/openapi/sl-journey-planner.json" %}}