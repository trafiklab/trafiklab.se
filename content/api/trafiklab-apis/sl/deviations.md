---
title: SL Deviations
weight: 20
date: 2024-01-12
badge: new
aliases:
  - /api/sl-storningsinformation-2
  - /api/sl-storningsinformation-2/documentation
  - /api/sl-storningsinformation-2/nivaer
  - /api/sl-storningsinformation-2/console
  - /api/sl-storningsinformation-2/konsol
  - /node/12605
  - /node/12605/documentation
  - /node/12605/nivaer
  - /node/12605/console
  - /node/12605/konsol
  - /api/sl-trafiklaget-2
  - /api/sl-trafiklaget-2/documentation
  - /api/sl-trafiklaget-2/nivaer
  - /api/sl-trafiklaget-2/console
  - /node/12603
  - /node/12603/documentation
  - /node/12603/nivaer
  - /node/12603/console
---

## Description

Using this API, you can get information regarding deviations on SLs transport network. This API replaces the
older [Service Alerts (Störningsinformation)](service-alerts-2.md) and
[Traffic Status (Trafikläget)](sl-traffic-status-2.md) APIs.

## URL

{{% tabs %}} {{% tab "Json" %}}

```text
https://deviations.integration.sl.se/v1/messages?future=<true/false>&site=<siteId1,siteId2>&line=<lineId1,lineId2>&transport_mode=<mode1,mode2>
```

{{% /tab %}} {{% /tabs %}}

## Format

This API returns responses in the JSON format.

## Request

### Key quota levels

This API does not require API keys, and has no quota levels. Fair use rules apply however, and you should only make a
request once a minute.

### Parameters

| Namn                | Type                                                  | Required | Default value                     | Description                                                                                             |
|---------------------|-------------------------------------------------------|----------|-----------------------------------|---------------------------------------------------------------------------------------------------------|
| future              | Boolean                                               | No       | False                             | Include future deviations                                                                               |
| site                | Integer (4-7 digits), can be specified multiple times | No       | Empty (all sites)                 | Only include results with these site ids                                                                |
| line                | Integer, can be specified multiple times              | No       | Empty (all lines)                 | Only include results with these line ids                                                                |
| transport_authority | integer                                               | No       | Empty (all transport authorities) | Only include results with this transport authority                                                      |
| transport_mode      | String, can be specified multiple times               | No       | Empty (all modes)                 | Only include results with this transport mode. Valid values: BUS, METRO, TRAM, TRAIN, SHIP, FERRY, TAXI |

### Headers

These specific headers may be used to alter the response sent by the server.

| Header          | Description                                                                                                                                                                                                                            |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Accept-Encoding | Controls the compression used by the server. Typically managed by the HTTP client used. Valid values are 'gzip', 'identity' and 'deflate'. When using this header, your client has to have support for the given compression standard. |
| age             | Useful for caching responses. The time in seconds since the cached response was generated at first.                                                                                                                                    |

## Response

### Response codes

| Code | Description                                                           |
|------|-----------------------------------------------------------------------|
| 200  | Ok, a valid API response is returned.                                 |
| 400  | Bad request, one of the request parameters contains an invalid value. |
| 404  | Not found, the URL is incorrect                                       |
| 500  | Error on the server side                                              |
| 502  | Error on the server side                                              |
| 503  | Error on the server side                                              |
| 504  | Service temporary unavailable                                         |

### Headers

| Header           | Description                                                                                   |
|------------------|-----------------------------------------------------------------------------------------------|
| Content-Encoding | Content-Encoding of response to enable gzip compressed responses for client that accept it    |
| Cache-Control    | Useful for caching responses. Cache-Control containing max-age, as described in RFC 7234, 5.2 |

### Example response

```json
[
  {
    "version": 1,
    "created": "2022-03-03T19:03:48.713+01:00",
    "modified": "2022-03-03T19:03:48.713+01:00",
    "deviation_case_id": 52432153,
    "publish": {
      "from": "2022-03-03T19:03:48.700+01:00",
      "upto": "2022-03-03T20:03:00.000+01:00"
    },
    "priority": {
      "importance_level": 2,
      "influence_level": 3,
      "urgency_level": 1
    },
    "message_variants": [
      {
        "header": "Entré vid Medborgarplatsen stängd",
        "details": "Vid Medborgarplatsen är entrén från Folkungagatan stängd på grund av underhållsarbete.",
        "scope_alias": "tunnelbanans röda linje 13",
        "weblink": "https://sl.se",
        "language": "sv"
      }
    ],
    "scope": {
      "stop_areas": [
        {
          "id": 1511,
          "transport_authority": 1,
          "name": "Medborgarplatsen",
          "type": "METROSTN",
          "stop_points": [
            {
              "id": 222,
              "name": "Norrö"
            }
          ]
        }
      ],
      "lines": [
        {
          "id": 17,
          "transport_authority": 1,
          "designation": "17",
          "transport_mode": "METRO",
          "name": "Gröna linjen",
          "group_of_lines": "Tunnelbanans gröna linje"
        }
      ]
    }
  }
]
```

### Response structure

The response consists of an array of deviations. Every deviation contains the following fields:

| Name                                      | Type       | Description                                                                                                                                                                                                                                                                                                                                        | Example value                                                                          |
|-------------------------------------------|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| version                                   | *Integer*  | The message version (sequential)                                                                                                                                                                                                                                                                                                                   | 1                                                                                      |
| created                                   | *DateTime* | When the message was created                                                                                                                                                                                                                                                                                                                       | 2022-03-03T19:03:48.713+01:00                                                          |
| modified                                  | DateTime   | When the message was last updated, if it has been updated                                                                                                                                                                                                                                                                                          | 2022-03-03T19:03:48.713+01:00                                                          |
| deviation_case_id                         | Integer    | The id for the deviation                                                                                                                                                                                                                                                                                                                           | 52432153                                                                               |
| publish.from                              | *DateTime* | Start of the period when this deviation message version is valid                                                                                                                                                                                                                                                                                   | 2022-03-03T19:03:48.700+01:00                                                          |
| publish.upto                              | DateTime   | End of the period when this deviation message version is valid                                                                                                                                                                                                                                                                                     | 2022-03-03T19:03:48.700+01:00                                                          |
| priority.<wbr>importance_level            | *Integer*  | The importance level of the deviation message, **only used to sort messages**. The importance gives a presentation system a hint of what message to present first. This value should have the highest data quality of all three priority fields. When in doubt, use this value to sort messages based on priority and ignore the other two fields. | 2                                                                                      |
| priority.<wbr>influence_level             | *Integer*  | The influence level of the deviation message, **only used to sort messages**. This influence level is a hint about how many persons that is influenced by a deviation.                                                                                                                                                                             | 3                                                                                      |
| priority.<wbr>urgency_level               | *Integer*  | The urgency level of the deviation message, **only used to sort messages**. This is a hint of how fast information about a deviation shall reach the receivers.                                                                                                                                                                                    | 1                                                                                      |
| message_variants                          | *Array*    | Variants of a message in different languages                                                                                                                                                                                                                                                                                                       |                                                                                        |
| message_variants.<wbr>header              | *String*   | The header of the message                                                                                                                                                                                                                                                                                                                          | Entré vid Medborgarplatsen stängd                                                      |
| message_variants.<wbr>details             | *String*   | The full contents of the message                                                                                                                                                                                                                                                                                                                   | Vid Medborgarplatsen är entrén från Folkungagatan stängd på grund av underhållsarbete. |
| message_variants.<wbr>scope_alias         | *String*   | A readable representation of the scope                                                                                                                                                                                                                                                                                                             | Tunnelbanans röda linje 13                                                             |
| message_variants.<wbr>weblink             | *String*   | The header of the message                                                                                                                                                                                                                                                                                                                          | https://sl.se                                                                          |
| message_variants.<wbr>language            | *String*   | The language of the message                                                                                                                                                                                                                                                                                                                        | sv                                                                                     |
| scope                                     | Object     | The stop(s) and/or line(s) affected by the deviation                                                                                                                                                                                                                                                                                               |                                                                                        |
| scope.<wbr>stop_areas                     | Array      | The affected stop area(s)                                                                                                                                                                                                                                                                                                                          |                                                                                        |
| scope.<wbr>stop_areas.<wbr>transport_authority | *Integer*  | Stop Area transport authority id                                                                                                                                                                                                                                                                                                                   | 1                                                                                      |
| scope.<wbr>stop_areas.id                  | *Integer*  | Stop Area id                                                                                                                                                                                                                                                                                                                                       | 1511                                                                                   |
| scope.<wbr>stop_areas.name                | *String*   | Stop Area name                                                                                                                                                                                                                                                                                                                                     | Medborgarplatsen                                                                       |
| scope.<wbr>stop_areas.type                | *String*   | Stop Area type                                                                                                                                                                                                                                                                                                                                     | METROSTN                                                                               |
| scope.<wbr>stop_points                    | *Array*    | The affected stop point(s)                                                                                                                                                                                                                                                                                                                         |                                                                                        |
| scope.<wbr>stop_points.id                 | *Integer*  | Stop point id                                                                                                                                                                                                                                                                                                                                      | 222                                                                                    |
| scope.<wbr>stop_points.name               | *String*   | Stop point name                                                                                                                                                                                                                                                                                                                                    | Norrö                                                                                  |
| scope.<wbr>lines                          | Array      | The affected line(s)                                                                                                                                                                                                                                                                                                                               |                                                                                        |
| scope.<wbr>lines.id                       | *Integer*  | Line id                                                                                                                                                                                                                                                                                                                                            | 17                                                                                     |
| scope.<wbr>lines.<wbr>transport_authority      | *Integer*  | Line transport authority                                                                                                                                                                                                                                                                                                                           | 1                                                                                      |
| scope.<wbr>lines.<wbr>designation              | String     | Line designation                                                                                                                                                                                                                                                                                                                                   | 17                                                                                     |
| scope.<wbr>lines.<wbr>transport_mode           | *String*   | Line transport mode. Valid values: BUS, METRO, TRAM, TRAIN, SHIP, FERRY, TAXI                                                                                                                                                                                                                                                                      | METRO                                                                                  |
| scope.<wbr>lines.<wbr>name                     | *String*   | Line name                                                                                                                                                                                                                                                                                                                                          | Gröna linjen                                                                           |
| scope.<wbr>lines.<wbr>group_of_lines           | *String*   | Name used to group lines                                                                                                                                                                                                                                                                                                                           | Gröna linjen                                                                           |

## OpenAPI specification

{{% oai-spec url="/openapi/sl-deviations.json" %}}