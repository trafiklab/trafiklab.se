---
title: SL Route-planner v4
weight: 101
date: 2025-04-07
aliases:
  - /api/sl-reseplanerare
---
## Description

{{% info %}}
This API replaces [SL Route planner 3.1](route-planner-31), which will be shut down June 30th, 2025.
{{% /info %}}

## URL

This API consists of 4 endpoints, each with their own URL. No API key is required to use this API.

{{% tabs %}} {{% tab "System info" %}}

```text
https://journeyplanner.integration.sl.se/v2/system-info
```

{{% /tab %}}
{{% tab "Stop lookup" %}}

```text
https://journeyplanner.integration.sl.se/v2/stop-finder?name_sf=odenplan&any_obj_filter_sf=2&type_sf=any
```

{{% /tabs %}}
{{% tab "Journey planner" %}}

```text
https://journeyplanner.integration.sl.se/v2/trips?type_origin=any&type_destination=any&name_origin=9091001000009182&name_destination=9091001000009192&max_length_bicycle=4000&min_length_bicycle=0
```

{{% /tab %}}

{{% tab "Lines" %}}

```text
https://journeyplanner.integration.sl.se/v2/line-list?line_list_subnetwork=tfs&merge_dir=true
```

{{% /tab %}}
{{% /tabs %}}

## Format

This API returns data in the JSON format

## Request

### API Key Levels

This API does not require the use of an API key. You should however not make excessive requests, to ensure the availability
and performance of the API for everyone. If you need large amounts of data, for example all departures from all
stops, [GTFS Regional](../../gtfs-datasets/gtfs-regional/_index.md) might be better suited for your application.

### Parameters


## Response

For details regarding the response structure, please see the OpenApi specification below. A few example responses can be seen below.

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
  "systemMessages": [
    {
      "type": "error",
      "module": "BROKER",
      "code": -8011,
      "text": ""
    }
  ],
  "locations": [
    {
      "id": "9091001000001079",
      "isGlobalId": true,
      "name": "Stockholm, Stockholm Odenplan",
      "disassembledName": "Stockholm Odenplan",
      "coord": [
        59.343116,
        18.04569
      ],
      "type": "stop",
      "matchQuality": 948,
      "isBest": false,
      "productClasses": [
        0,
        2,
        5
      ],
      "parent": {
        "id": "placeID:33001080:1",
        "name": "Stockholm",
        "type": "locality"
      },
      "properties": {
        "stopId": "18001079",
        "mainLocality": "Stockholm"
      }
    },
    {
      "id": "9091001000009117",
      "isGlobalId": true,
      "name": "Stockholm, Odenplan",
      "disassembledName": "Odenplan",
      "coord": [
        59.342906,
        18.049103
      ],
      "type": "stop",
      "matchQuality": 1000,
      "isBest": true,
      "productClasses": [
        0,
        2,
        5
      ],
      "parent": {
        "id": "placeID:33001080:1",
        "name": "Stockholm",
        "type": "locality"
      },
      "properties": {
        "stopId": "18009117",
        "mainLocality": "Stockholm"
      }
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
      "tripId": "9015001001812227|9025001000001861|2025-04-04T10:32:42Z|9025001000001011|2025-04-04T10:49:30Z",
      "tripParams": "maxLengthBicycle=4000&minLengthBicycle=0&mustExcl=1&mustExclOP=sam%3A%3A&name_destination=9091001000009192&name_origin=9091001000009182&selOP=1&type_destination=any&type_origin=any",
      "tripDuration": 1008,
      "tripRtDuration": 942,
      "rating": 0,
      "isAdditional": false,
      "interchanges": 0,
      "legs": [
        {
          "infos": [

          ],
          "duration": 942,
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
            "departureTimeBaseTimetable": "2025-04-04T10:32:42Z",
            "departureTimePlanned": "2025-04-04T10:32:42Z",
            "departureTimeEstimated": "2025-04-04T10:33:06Z",
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
            "arrivalTimeBaseTimetable": "2025-04-04T10:49:30Z",
            "arrivalTimePlanned": "2025-04-04T10:49:30Z",
            "arrivalTimeEstimated": "2025-04-04T10:48:48Z",
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
              "id": "18001331",
              "name": "Hässelby strand",
              "type": "stop"
            },
            "properties": {
              "tripCode": 429,
              "timetablePeriod": "Current",
              "lineDisplay": "LINE",
              "globalId": "9011001001800000",
              "RealtimeTripId": "9015001001812227",
              "shortTrain": false,
              "AVMSTripID": "9015001001812227"
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
              "departureTimePlanned": "2025-04-04T10:32:42Z",
              "departureTimeEstimated": "2025-04-04T10:33:06Z"
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
              "departureTimePlanned": "2025-04-04T10:34:12Z",
              "departureTimeEstimated": "2025-04-04T10:34:36Z",
              "arrivalTimePlanned": "2025-04-04T10:34:12Z",
              "arrivalTimeEstimated": "2025-04-04T10:33:42Z"
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
              "departureTimePlanned": "2025-04-04T10:35:42Z",
              "departureTimeEstimated": "2025-04-04T10:36:12Z",
              "arrivalTimePlanned": "2025-04-04T10:35:42Z",
              "arrivalTimeEstimated": "2025-04-04T10:35:24Z"
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
              "departureTimePlanned": "2025-04-04T10:37:12Z",
              "departureTimeEstimated": "2025-04-04T10:38:00Z",
              "arrivalTimePlanned": "2025-04-04T10:37:12Z",
              "arrivalTimeEstimated": "2025-04-04T10:37:00Z"
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
              "departureTimePlanned": "2025-04-04T10:38:42Z",
              "departureTimeEstimated": "2025-04-04T10:39:30Z",
              "arrivalTimePlanned": "2025-04-04T10:38:42Z",
              "arrivalTimeEstimated": "2025-04-04T10:38:36Z"
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
              "departureTimePlanned": "2025-04-04T10:40:12Z",
              "departureTimeEstimated": "2025-04-04T10:40:42Z",
              "arrivalTimePlanned": "2025-04-04T10:40:12Z",
              "arrivalTimeEstimated": "2025-04-04T10:39:54Z"
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
              "departureTimePlanned": "2025-04-04T10:42:00Z",
              "departureTimeEstimated": "2025-04-04T10:42:00Z",
              "arrivalTimePlanned": "2025-04-04T10:42:00Z",
              "arrivalTimeEstimated": "2025-04-04T10:41:24Z"
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
              "departureTimePlanned": "2025-04-04T10:44:30Z",
              "departureTimeEstimated": "2025-04-04T10:44:30Z",
              "arrivalTimePlanned": "2025-04-04T10:44:30Z",
              "arrivalTimeEstimated": "2025-04-04T10:42:42Z"
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
              "departureTimePlanned": "2025-04-04T10:46:30Z",
              "departureTimeEstimated": "2025-04-04T10:46:36Z",
              "arrivalTimePlanned": "2025-04-04T10:46:30Z",
              "arrivalTimeEstimated": "2025-04-04T10:46:00Z"
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
              "departureTimePlanned": "2025-04-04T10:48:00Z",
              "departureTimeEstimated": "2025-04-04T10:48:00Z",
              "arrivalTimePlanned": "2025-04-04T10:48:00Z",
              "arrivalTimeEstimated": "2025-04-04T10:47:30Z"
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
              "arrivalTimePlanned": "2025-04-04T10:49:30Z",
              "arrivalTimeEstimated": "2025-04-04T10:48:48Z"
            }
          ],
          "properties": {
            "tripId": "9015001001812227"
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
      "fare": {
        "tickets": [
          {
            "id": "VUX",
            "name": "SL enkelbiljett",
            "comment": "minutes (xsd:duration)",
            "currency": "SEK",
            "priceBrutto": 40.57,
            "priceNetto": 43,
            "taxPercent": 6,
            "fromLeg": 0,
            "toLeg": 0,
            "net": "SL-tarif",
            "person": "ADULT",
            "travellerClass": "SECOND",
            "timeValidity": "SINGLE",
            "validMinutes": 75,
            "isShortHaul": "NO",
            "returnsAllowed": "NO",
            "validForOneJourneyOnly": "UNKNOWN",
            "validForOneOperatorOnly": "UNKNOWN",
            "numberOfChanges": 0,
            "validFrom": "2025-04-04T10:32:00Z",
            "validTo": "2025-04-04T11:47:00Z",
            "validityExtent": "BOARDING",
            "properties": {
              "priceTotalFare": "0.00",
              "riderCategoryName": "Adult",
              "tariffProductDefault": [

              ],
              "tariffProductOption": [

              ],
              "validityPeriodType": "DURATION"
            }
          },
          {
            "id": "RAB",
            "name": "SL enkelbiljett",
            "comment": "minutes (xsd:duration)",
            "currency": "SEK",
            "priceBrutto": 24.53,
            "priceNetto": 26,
            "taxPercent": 6,
            "fromLeg": 0,
            "toLeg": 0,
            "net": "SL-tarif",
            "person": "REDUCED",
            "travellerClass": "SECOND",
            "timeValidity": "SINGLE",
            "validMinutes": 75,
            "isShortHaul": "NO",
            "returnsAllowed": "NO",
            "validForOneJourneyOnly": "UNKNOWN",
            "validForOneOperatorOnly": "UNKNOWN",
            "numberOfChanges": 0,
            "validFrom": "2025-04-04T10:32:00Z",
            "validTo": "2025-04-04T11:47:00Z",
            "validityExtent": "BOARDING",
            "properties": {
              "priceTotalFare": "0.00",
              "riderCategoryName": "Adult",
              "tariffProductDefault": [

              ],
              "tariffProductOption": [

              ],
              "validityPeriodType": "DURATION"
            }
          }
        ],
        "priceCompilations": [
          {
            "ticketId": "VUX",
            "name": "SL enkelbiljett",
            "NumberOfTickets": 1,
            "priceBrutto": 40.57,
            "priceNetto": 43,
            "unitPriceBrutto": 40.57,
            "unitPriceNetto": 43,
            "taxPercent": 6
          },
          {
            "ticketId": "RAB",
            "name": "SL enkelbiljett",
            "NumberOfTickets": 1,
            "priceBrutto": 24.53,
            "priceNetto": 26,
            "unitPriceBrutto": 24.53,
            "unitPriceNetto": 26,
            "taxPercent": 6
          }
        ],
        "priceInformations": [
          {
            "ID": "Default_1",
            "Name": "1",
            "Content": "Biljettpriset är beräknat på resan i förslaget. För vissa resor går det inte att visa ett pris.",
            "URL": "https://sl.se/prisinformation",
            "UrlDescription": "Läs mer på sl.se om hur reseplaneraren och uträkningen av biljettpriset funkar.",
            "Description": "Friskrivning, gäller både tider och priser "
          },
          {
            "ID": "VUX",
            "Name": "SL enkelbiljett"
          }
        ]
      },
      "daysOfService": {
        "rvb": "000000000000000000000000000000080000000000000000"
      }
    },
    {
      "tripId": "9015001001812228|9025001000001861|2025-04-04T10:42:42Z|9025001000001011|2025-04-04T10:59:30Z",
      "tripParams": "maxLengthBicycle=4000&minLengthBicycle=0&mustExcl=1&mustExclOP=sam%3A%3A&name_destination=9091001000009192&name_origin=9091001000009182&selOP=1&type_destination=any&type_origin=any",
      "tripDuration": 1008,
      "tripRtDuration": 942,
      "rating": 0,
      "isAdditional": false,
      "interchanges": 0,
      "legs": [
        {
          "infos": [

          ],
          "duration": 942,
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
            "departureTimeBaseTimetable": "2025-04-04T10:42:42Z",
            "departureTimePlanned": "2025-04-04T10:42:42Z",
            "departureTimeEstimated": "2025-04-04T10:42:42Z",
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
            "arrivalTimeBaseTimetable": "2025-04-04T10:59:30Z",
            "arrivalTimePlanned": "2025-04-04T10:59:30Z",
            "arrivalTimeEstimated": "2025-04-04T10:58:24Z",
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
              "id": "18001331",
              "name": "Hässelby strand",
              "type": "stop"
            },
            "properties": {
              "tripCode": 430,
              "timetablePeriod": "Current",
              "lineDisplay": "LINE",
              "globalId": "9011001001800000",
              "RealtimeTripId": "9015001001812228",
              "shortTrain": false,
              "AVMSTripID": "9015001001812228"
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
              "departureTimePlanned": "2025-04-04T10:42:42Z",
              "departureTimeEstimated": "2025-04-04T10:42:42Z"
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
              "departureTimePlanned": "2025-04-04T10:44:12Z",
              "departureTimeEstimated": "2025-04-04T10:44:12Z",
              "arrivalTimePlanned": "2025-04-04T10:44:12Z",
              "arrivalTimeEstimated": "2025-04-04T10:43:06Z"
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
              "departureTimePlanned": "2025-04-04T10:45:42Z",
              "departureTimeEstimated": "2025-04-04T10:45:42Z",
              "arrivalTimePlanned": "2025-04-04T10:45:42Z",
              "arrivalTimeEstimated": "2025-04-04T10:44:54Z"
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
              "departureTimePlanned": "2025-04-04T10:47:12Z",
              "departureTimeEstimated": "2025-04-04T10:47:12Z",
              "arrivalTimePlanned": "2025-04-04T10:47:12Z",
              "arrivalTimeEstimated": "2025-04-04T10:46:30Z"
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
              "departureTimePlanned": "2025-04-04T10:48:42Z",
              "departureTimeEstimated": "2025-04-04T10:48:48Z",
              "arrivalTimePlanned": "2025-04-04T10:48:42Z",
              "arrivalTimeEstimated": "2025-04-04T10:47:54Z"
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
              "departureTimePlanned": "2025-04-04T10:50:12Z",
              "departureTimeEstimated": "2025-04-04T10:50:12Z",
              "arrivalTimePlanned": "2025-04-04T10:50:12Z",
              "arrivalTimeEstimated": "2025-04-04T10:49:18Z"
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
              "departureTimePlanned": "2025-04-04T10:52:00Z",
              "departureTimeEstimated": "2025-04-04T10:52:00Z",
              "arrivalTimePlanned": "2025-04-04T10:52:00Z",
              "arrivalTimeEstimated": "2025-04-04T10:50:48Z"
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
              "departureTimePlanned": "2025-04-04T10:54:30Z",
              "departureTimeEstimated": "2025-04-04T10:54:30Z",
              "arrivalTimePlanned": "2025-04-04T10:54:30Z",
              "arrivalTimeEstimated": "2025-04-04T10:52:42Z"
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
              "departureTimePlanned": "2025-04-04T10:56:30Z",
              "departureTimeEstimated": "2025-04-04T10:56:36Z",
              "arrivalTimePlanned": "2025-04-04T10:56:30Z",
              "arrivalTimeEstimated": "2025-04-04T10:55:42Z"
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
              "departureTimePlanned": "2025-04-04T10:58:00Z",
              "departureTimeEstimated": "2025-04-04T10:58:00Z",
              "arrivalTimePlanned": "2025-04-04T10:58:00Z",
              "arrivalTimeEstimated": "2025-04-04T10:57:12Z"
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
              "arrivalTimePlanned": "2025-04-04T10:59:30Z",
              "arrivalTimeEstimated": "2025-04-04T10:58:24Z"
            }
          ],
          "properties": {
            "tripId": "9015001001812228"
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
      "fare": {
        "tickets": [
          {
            "id": "VUX",
            "name": "SL enkelbiljett",
            "comment": "minutes (xsd:duration)",
            "currency": "SEK",
            "priceBrutto": 40.57,
            "priceNetto": 43,
            "taxPercent": 6,
            "fromLeg": 0,
            "toLeg": 0,
            "net": "SL-tarif",
            "person": "ADULT",
            "travellerClass": "SECOND",
            "timeValidity": "SINGLE",
            "validMinutes": 75,
            "isShortHaul": "NO",
            "returnsAllowed": "NO",
            "validForOneJourneyOnly": "UNKNOWN",
            "validForOneOperatorOnly": "UNKNOWN",
            "numberOfChanges": 0,
            "validFrom": "2025-04-04T10:42:00Z",
            "validTo": "2025-04-04T11:57:00Z",
            "validityExtent": "BOARDING",
            "properties": {
              "priceTotalFare": "0.00",
              "riderCategoryName": "Adult",
              "tariffProductDefault": [

              ],
              "tariffProductOption": [

              ],
              "validityPeriodType": "DURATION"
            }
          },
          {
            "id": "RAB",
            "name": "SL enkelbiljett",
            "comment": "minutes (xsd:duration)",
            "currency": "SEK",
            "priceBrutto": 24.53,
            "priceNetto": 26,
            "taxPercent": 6,
            "fromLeg": 0,
            "toLeg": 0,
            "net": "SL-tarif",
            "person": "REDUCED",
            "travellerClass": "SECOND",
            "timeValidity": "SINGLE",
            "validMinutes": 75,
            "isShortHaul": "NO",
            "returnsAllowed": "NO",
            "validForOneJourneyOnly": "UNKNOWN",
            "validForOneOperatorOnly": "UNKNOWN",
            "numberOfChanges": 0,
            "validFrom": "2025-04-04T10:42:00Z",
            "validTo": "2025-04-04T11:57:00Z",
            "validityExtent": "BOARDING",
            "properties": {
              "priceTotalFare": "0.00",
              "riderCategoryName": "Adult",
              "tariffProductDefault": [

              ],
              "tariffProductOption": [

              ],
              "validityPeriodType": "DURATION"
            }
          }
        ],
        "priceCompilations": [
          {
            "ticketId": "VUX",
            "name": "SL enkelbiljett",
            "NumberOfTickets": 1,
            "priceBrutto": 40.57,
            "priceNetto": 43,
            "unitPriceBrutto": 40.57,
            "unitPriceNetto": 43,
            "taxPercent": 6
          },
          {
            "ticketId": "RAB",
            "name": "SL enkelbiljett",
            "NumberOfTickets": 1,
            "priceBrutto": 24.53,
            "priceNetto": 26,
            "unitPriceBrutto": 24.53,
            "unitPriceNetto": 26,
            "taxPercent": 6
          }
        ],
        "priceInformations": [
          {
            "ID": "Default_1",
            "Name": "1",
            "Content": "Biljettpriset är beräknat på resan i förslaget. För vissa resor går det inte att visa ett pris.",
            "URL": "https://sl.se/prisinformation",
            "UrlDescription": "Läs mer på sl.se om hur reseplaneraren och uträkningen av biljettpriset funkar.",
            "Description": "Friskrivning, gäller både tider och priser "
          },
          {
            "ID": "VUX",
            "Name": "SL enkelbiljett"
          }
        ]
      },
      "daysOfService": {
        "rvb": "000000000000000000000000000000080000000000000000"
      }
    }
  ]
}
```

{{% /tab %}}

{{% tab "Lines" %}}

```json
{
  "transportations": [
    {
      "id": "tfs:01050: :H:y01",
      "name": "Buss Buss 50",
      "disassembledName": "50",
      "number": "Buss 50",
      "product": {
        "id": 3,
        "class": 5,
        "name": "Buss",
        "iconId": 3
      },
      "operator": {
        "id": "1",
        "name": "Storstockholms Lokaltrafik"
      },
      "destination": {
        "name": "Lektorsstigen, Stockholm",
        "type": "stop"
      },
      "properties": {
        "tripCode": 0,
        "timetablePeriod": "Current",
        "validity": {
          "from": "2024-06-01",
          "to": "2025-06-21"
        },
        "lineDisplay": "LINE",
        "globalId": "9011001005000000"
      }
    },
    {
      "id": "tfs:01053: :H:y01",
      "name": "Buss Buss 53",
      "disassembledName": "53",
      "number": "Buss 53",
      "product": {
        "id": 3,
        "class": 5,
        "name": "Buss",
        "iconId": 3
      },
      "operator": {
        "id": "1",
        "name": "Storstockholms Lokaltrafik"
      },
      "destination": {
        "name": "Henriksdalsberget, Nacka",
        "type": "stop"
      },
      "properties": {
        "tripCode": 0,
        "timetablePeriod": "Current",
        "validity": {
          "from": "2024-06-01",
          "to": "2025-06-21"
        },
        "lineDisplay": "LINE",
        "globalId": "9011001005300000"
      }
    },
    {
      "id": "tfs:01054: :H:y01",
      "name": "Buss Buss 54",
      "disassembledName": "54",
      "number": "Buss 54",
      "product": {
        "id": 3,
        "class": 5,
        "name": "Buss",
        "iconId": 3
      },
      "operator": {
        "id": "1",
        "name": "Storstockholms Lokaltrafik"
      },
      "destination": {
        "name": "Moa Martinsons torg, Stockholm",
        "type": "stop"
      },
      "properties": {
        "tripCode": 0,
        "timetablePeriod": "Current",
        "validity": {
          "from": "2024-06-01",
          "to": "2025-06-21"
        },
        "lineDisplay": "LINE",
        "globalId": "9011001005400000"
      }
    }
  ]
}
```

{{% /tab %}}
{{% tab "Transport Authorities" %}}

```json
[
  {
    "id": 1,
    "gid": 9010001000000000,
    "name": "Storstockholms Lokaltrafik",
    "formal_name": "AB Storstockholms Lokaltrafik",
    "code": "string",
    "street": "Lindhagensgatan 100",
    "postal_code": 10573,
    "city": "Stockholm",
    "country": "Sweden",
    "valid": {
      "from": "2024-01-01T01:00:00",
      "to": "2024-01-01T01:00:00"
    }
  }
]
```

{{% /tab %}}
{{% /tabs %}}

## OpenAPI specification

{{% oai-spec url="/openapi/sl-journey-planner.json" %}}