---
title: SL Network API
weight: 10
date: 2024-01-30

---

## Description

This API provides information about the lines, stops, and next departures on the SL network.

## URL

{{% tabs %}} {{% tab "Lines" %}}

```text
https://integration.sl.se/open-api-transport/v1/lines
```

{{% /tab %}}
{{% tab "Sites" %}}

```text
https://integration.sl.se/open-api-transport/v1/sites
```

{{% /tabs %}}
{{% tab "Site by id" %}}

```text
https://integration.sl.se/open-api-transport/v1/sites/{SiteId}
```

{{% /tabs %}}
{{% tab "Departures from site" %}}

```text
https://integration.sl.se/open-api-transport/v1/sites/{SiteId}/departures
```

{{% /tab %}}

{{% tab "Stop Points" %}}

```text
https://integration.sl.se/open-api-transport/v1/stop-points
```

{{% /tab %}}
{{% tab "Transport Authorities" %}}

```text
https://integration.sl.se/open-api-transport/v1/transport-authorities
```

{{% /tab %}}
{{% /tabs %}}

### API Key Levels

This API does not require the use of an API key.

## Format

This API returns data in the JSON format

## Request Parameters

When searching for a specific

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
{{% tab "Site by id" %}}

```json
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