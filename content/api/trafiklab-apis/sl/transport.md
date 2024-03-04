---
title: SL Transport
weight: 10
date: 2024-01-30
badge: new
---

## Description

This API provides information about the lines, stops, and next departures on the SL network. It replaces the existing SL Departures v4 and SL Stops and lines v2
APIs.

### Concepts

| Concept   | Description                                                                                                                                                             |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Site      | A Site is a grouping of StopAreas used to simplify searching in the journey planner.                                                                                    |
| StopArea  | A StopArea is a grouping of StopPoints with the same traffic type and name within a defined geographic area, such as a terminal.                                        |
| StopPoint | A StopPoint is a stopping point, also known as quay, and is part of a StopArea. A stop area for busses may for example contain one stop point on each side of the road. |

## URL

This API consists of 5 endpoints, each with their own URL.

{{% tabs %}} {{% tab "Lines" %}}

```text
https://transport.integration.sl.se/v1/lines
```

{{% /tab %}}
{{% tab "Sites" %}}

```text
https://transport.integration.sl.se/v1/sites
```

{{% /tabs %}}
{{% tab "Departures from site" %}}

```text
https://transport.integration.sl.se/v1/sites/{SiteId}/departures
```

{{% /tab %}}

{{% tab "Stop Points" %}}

```text
https://transport.integration.sl.se/v1/stop-points
```

{{% /tab %}}
{{% tab "Transport Authorities" %}}

```text
https://transport.integration.sl.se/v1/transport-authorities
```

{{% /tab %}}
{{% /tabs %}}

### API Key Levels

This API does not require the use of an API key. You should however not make excessive requests (more than 12 requests per minute), to ensure the availability
and performance of the API for everyone.

## Format

This API returns data in the JSON format

## Request Parameters

When searching for a specific site, or departures from a specific site, the site ID is required. Other API calls do not have any parameters.

| Parameters | Data Type | Mandatory | Description                                                                                                                                                                                                   |
|------------|-----------|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SiteId     | Integer   | Yes       | Unique identification number for the location for which current departures should be fetched, e.g., 9192 for Slussen. Can be obtained from a search through the list of all sites, or the SL stop lookup api. |

## Response

For details regarding the response structure, please see the OpenApi specification below. A few example responses can be seen below.

{{% tabs %}} {{% tab "Lines" %}}

```json
[
  {
    "metro": [
      {
        "id": 13,
        "gid": 9025001000041484,
        "name": "19",
        "designation": "13X",
        "transport_mode": "BUS",
        "group_of_lines": "tunnelbanans gröna linje",
        "transport_authority": {
          "id": 1,
          "name": "Storstockholms Lokaltrafik"
        },
        "contractor": {
          "id": 1,
          "name": "Arriva"
        },
        "valid": {
          "from": "2024-01-01T01:00:00",
          "to": "2024-01-01T01:00:00"
        }
      }
    ],
    "tram": [
      {
        "id": 13,
        "gid": 9025001000041484,
        "name": "19",
        "designation": "13X",
        "transport_mode": "BUS",
        "group_of_lines": "tunnelbanans gröna linje",
        "transport_authority": {
          "id": 1,
          "name": "Storstockholms Lokaltrafik"
        },
        "contractor": {
          "id": 1,
          "name": "Arriva"
        },
        "valid": {
          "from": "2024-01-01T01:00:00",
          "to": "2024-01-01T01:00:00"
        }
      }
    ],
    "train": [
      {
        "id": 13,
        "gid": 9025001000041484,
        "name": "19",
        "designation": "13X",
        "transport_mode": "BUS",
        "group_of_lines": "tunnelbanans gröna linje",
        "transport_authority": {
          "id": 1,
          "name": "Storstockholms Lokaltrafik"
        },
        "contractor": {
          "id": 1,
          "name": "Arriva"
        },
        "valid": {
          "from": "2024-01-01T01:00:00",
          "to": "2024-01-01T01:00:00"
        }
      }
    ],
    "bus": [
      {
        "id": 13,
        "gid": 9025001000041484,
        "name": "19",
        "designation": "13X",
        "transport_mode": "BUS",
        "group_of_lines": "tunnelbanans gröna linje",
        "transport_authority": {
          "id": 1,
          "name": "Storstockholms Lokaltrafik"
        },
        "contractor": {
          "id": 1,
          "name": "Arriva"
        },
        "valid": {
          "from": "2024-01-01T01:00:00",
          "to": "2024-01-01T01:00:00"
        }
      }
    ],
    "ship": [
      {
        "id": 13,
        "gid": 9025001000041484,
        "name": "19",
        "designation": "13X",
        "transport_mode": "BUS",
        "group_of_lines": "tunnelbanans gröna linje",
        "transport_authority": {
          "id": 1,
          "name": "Storstockholms Lokaltrafik"
        },
        "contractor": {
          "id": 1,
          "name": "Arriva"
        },
        "valid": {
          "from": "2024-01-01T01:00:00",
          "to": "2024-01-01T01:00:00"
        }
      }
    ],
    "ferry": [
      {
        "id": 13,
        "gid": 9025001000041484,
        "name": "19",
        "designation": "13X",
        "transport_mode": "BUS",
        "group_of_lines": "tunnelbanans gröna linje",
        "transport_authority": {
          "id": 1,
          "name": "Storstockholms Lokaltrafik"
        },
        "contractor": {
          "id": 1,
          "name": "Arriva"
        },
        "valid": {
          "from": "2024-01-01T01:00:00",
          "to": "2024-01-01T01:00:00"
        }
      }
    ],
    "taxi": [
      {
        "id": 13,
        "gid": 9025001000041484,
        "name": "19",
        "designation": "13X",
        "transport_mode": "BUS",
        "group_of_lines": "tunnelbanans gröna linje",
        "transport_authority": {
          "id": 1,
          "name": "Storstockholms Lokaltrafik"
        },
        "contractor": {
          "id": 1,
          "name": "Arriva"
        },
        "valid": {
          "from": "2024-01-01T01:00:00",
          "to": "2024-01-01T01:00:00"
        }
      }
    ]
  }
]
```

{{% /tab %}}
{{% tab "Sites" %}}

```json
[
  {
    "id": 1002,
    "gid": 9001,
    "name": "Odenplan",
    "alias": "string",
    "abbreviation": "CEN",
    "note": "vid Sandhamn",
    "lat": 59.4474618783708,
    "lon": 17.8376900105886,
    "valid": {
      "from": "2024-01-01T01:00:00",
      "to": "2024-01-01T01:00:00"
    },
    "stop_areas": "string"
  }
]
```

{{% /tabs %}}

{{% tab "Departures from site" %}}

```json
{
  "departures": [
    {
      "direction": "string",
      "direction_code": 2,
      "via": "string",
      "destination": "string",
      "state": "NOTEXPECTED",
      "scheduled": "2024-01-01T01:00:00",
      "expected": "2024-01-01T01:00:00",
      "display": "string",
      "journey": {
        "id": 2020062310015,
        "state": "NOTEXPECTED",
        "prediction_state": "NORMAL",
        "passenger_level": "EMPTY"
      },
      "stop_area": {
        "id": 41483,
        "name": "Abborrkroksvägen",
        "sname": "string",
        "type": "BUSTERM"
      },
      "stop_point": {
        "id": 41483,
        "name": "Universitetet",
        "designation": "D"
      },
      "line": {
        "id": 13,
        "designation": "13X",
        "transport_mode": "BUS",
        "group_of_lines": "tunnelbanans gröna linje"
      },
      "deviations": "string"
    }
  ],
  "stop_deviations": [
    {
      "importance": 5,
      "consequence": "INFORMATION",
      "message": "Resa förbi Arlanda C kräver både UL- och SL- biljett."
    }
  ]
}
```

{{% /tab %}}

{{% tab "Stop Points" %}}

```json
[
  {
    "id": 41483,
    "gid": 9022001041483002,
    "pattern_point_gid": 9025001000041484,
    "name": "Universitetet",
    "sname": "string",
    "designation": "D",
    "local_num": 0,
    "type": "PLATFORM",
    "has_entrance": true,
    "lat": 59.4474618783708,
    "lon": 17.8376900105886,
    "door_orientation": 342.3,
    "transport_authority": {
      "id": 1,
      "name": "Storstockholms Lokaltrafik"
    },
    "stop_area": {
      "id": 41483,
      "name": "Abborrkroksvägen",
      "sname": "string",
      "type": "BUSTERM"
    },
    "valid": {
      "from": "2024-01-01T01:00:00",
      "to": "2024-01-01T01:00:00"
    }
  }
]
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

{{% oai-spec url="/openapi/sl-transport.json" %}}