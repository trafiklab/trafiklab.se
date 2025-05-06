---
title: Trafiklab Stop Lookup
weight: 20
date: 2025-05-02
badge: beta
---

## What does this API provide?

Trafiklab Stop Lookup provides information about stops for the [Trafiklab realtime APIs](_index.md).

### Data format

The data is formatted as JSON.

### Updates

The static data used for this API is updated when changes are made, at most once per day. 

### Breaking changes

This API has the **beta** status. We are actively developing this API based on user feedback. Minor breaking changes
may occur on short notice. New fields may be added without warning.

## Using Trafiklab Stop Lookup

Trafiklab Stop Lookup consists of two different endpoints, one to list all stops and one to search for stops by name. 
Both endpoints have the same response structure. They return a list of stops, including information about each stop, 
such as name, average departures and child-stops.

{{% note %}}
**Rikshållplatser**

Rikshållplatser, Swedish for "national stops", is the historical name for a grouping of multiple local stops under one name and id. This is done to avoid
duplicate stops when they are considered to be one stop by travelers. An example are certain multimodal stops, where a bus stop and tram stop may be at the same
location.

**Meta-stops**

Meta-stops are groups of multiple nearby stops. This is done to simplify route-planning for travelers. An example meta stop is "Stockholm" which combines
train, metro, tram and bus stops in central stockholm. This way, travelers can easily search a route "from Göteborg to Stockholm" without having to know about
all the local stops. Meta-stops are also used for combining multi-modal stops which are more spread out, such as Sundbyberg Station along with its two bus
stops (on different sides of the station) as well as its metro stop.

{{% /note %}}

An example is Slussen, which contains one area for buses and one area for metro traffic. Both are included when looking up slussen by its area id, and each
departure can be linked to one of these stops. The trafiklab realtime APIs take the id of a rikshållplats or meta-stop, **not** the id of underlying stops!
In this example, the area (as named in gtfs), represent the National Stop Group you will recieve in the response.

![2025-04-03-trafiklab-api-stop-hierarchy.png](/media/2025/04/2025-04-03-trafiklab-api-stop-hierarchy.png)

## Making a request

The first call will show all stop groups that has a name matching the searched value, in this case "sto". 
The stop groups are sorted by the most frequent daily departures. In this case the meta stop "Stockholm" will show up first, with all associated information.

In order to list all stop groups, use the second call. This will return all stop groups, sorted by the most frequent daily departures.

### Call

{{% tabs %}} {{% tab "List stops by name" %}}

```text
https://realtime-api.trafiklab.se/v1/stops/name/sto/?key=API_KEY
```

{{% /tab %}}


{{% tab "List all stop groups" %}}

```text
https://realtime-api.trafiklab.se/v1/stops/list?key=API_KEY
```

{{% /tab %}} {{% /tabs %}}

#### Request parameters

This API makes use of path parameters. They are part of the URL path and must be in the correct order.

```text
https://realtime-api.trafiklab.se/v1/stops/name/{searchValue}?key={key}
https://realtime-api.trafiklab.se/v1/stops/list/?key={key}
```

| **Name** | **Type** | **Data type** | **Required** | **Description**                                                                                              |
|----------|----------|---------------|--------------|--------------------------------------------------------------------------------------------------------------|
| name     | Path     | String        | Yes          | The search value to match the name of the stop group you want to look up. Must be minimum 3 characters long. |
| key      | Query    | String        | Yes          | Your API key                                                                                                 |



### Response

The responses consist of 3 parts:

- The timestamp at which the response was created
- Information about the query (search value, which time was requested)
- Information about the stop groups included in the response

Precise technical documentation is available in the form of an OpenAPI specification on the bottom of this page.

{{% note %}} Note that the actual responses contain more entries - we removed some from this example
response since it's only meant to show the structure of the response. {{% /note %}}

{{% tabs %}} {{% tab "List stop groups by name" %}}

```json
{
  "timestamp": "2025-05-02T15:10:56",
  "query": {
    "queryTime": "2025-05-02T15:10:56",
    "query": "sto"
  },
  "stop_groups": [
    {
      "id": "740098000",
      "name": "Stockholm",
      "area_type": "META_STOP",
      "average_daily_stop_times": 3198.92,
      "transport_modes": [
        "BUS",
        "TRAIN",
        "TRAM",
        "METRO"
      ],
      "stops": [
        {
          "id": "1",
          "name": "Stockholm Centralstation",
          "lat": 59.331537,
          "lon": 18.054943
        },
        {
          "id": "1617",
          "name": "Stockholm City",
          "lat": 59.331139,
          "lon": 18.059447
        },
        {
          "id": "12275",
          "name": "T-Centralen",
          "lat": 59.33212,
          "lon": 18.062138
        },
        {
          "id": "12736",
          "name": "T-Centralen",
          "lat": 59.332098,
          "lon": 18.061943
        },
        {
          "id": "12816",
          "name": "Centralen",
          "lat": 59.33114,
          "lon": 18.058496
        },
        {
          "id": "9825",
          "name": "T-Centralen",
          "lat": 59.33166,
          "lon": 18.061694
        },
        {
          "id": "12112",
          "name": "Cityterminalen",
          "lat": 59.331616,
          "lon": 18.055317
        },
        {
          "id": "11008",
          "name": "Cityterminalen",
          "lat": 59.332644,
          "lon": 18.053989
        },
        {
          "id": "68747",
          "name": "Kulturhuset",
          "lat": 59.332463,
          "lon": 18.06344
        },
        {
          "id": "10004",
          "name": "Centralen",
          "lat": 59.331047,
          "lon": 18.056514
        },
        {
          "id": "622",
          "name": "Cityterminalen",
          "lat": 59.332161,
          "lon": 18.054308
        }
      ]
    },
    {
      "id": "740022197",
      "name": "Karlstad Residenstorget",
      "area_type": "RIKSHALLPLATS",
      "average_daily_stop_times": 1411.87,
      "transport_modes": [
        "BUS"
      ],
      "stops": [
        {
          "id": "41045",
          "name": "Karlstad, Residenstorget",
          "lat": 59.380671,
          "lon": 13.499573
        }
      ]
    }
```

{{% /tab %}}

{{% tab "List all stop groups" %}}

```json
{
  "timestamp": "2025-05-02T16:12:50",
  "query": {
    "queryTime": "2025-05-02T16:12:50",
    "query": null
  },
  "stop_groups": [
    {
      "id": "740050707",
      "name": "Krigtjärnsvägen",
      "area_type": "RIKSHALLPLATS",
      "average_daily_stop_times": 5.17,
      "transport_modes": [
        "BUS"
      ],
      "stops": [
        {
          "id": "70787",
          "name": "Krigtjärnsvägen",
          "lat": 59.950485,
          "lon": 14.938174
        }
      ]
    },
    {
      "id": "740049719",
      "name": "Tynninge",
      "area_type": "RIKSHALLPLATS",
      "average_daily_stop_times": 13.43,
      "transport_modes": [
        "BUS"
      ],
      "stops": [
        {
          "id": "70164",
          "name": "Tynninge",
          "lat": 59.084528,
          "lon": 15.260689
        }
      ]
    },
    {
      "id": "740050708",
      "name": "Dalkarlstorp",
      "area_type": "RIKSHALLPLATS",
      "average_daily_stop_times": 5.17,
      "transport_modes": [
        "BUS"
      ],
      "stops": [
        {
          "id": "70788",
          "name": "Dalkarlstorp",
          "lat": 59.95859,
          "lon": 14.932681
        }
      ]
    },
    {
      "id": "740025749",
      "name": "Molkom, Vårdcentralen",
      "area_type": "RIKSHALLPLATS",
      "average_daily_stop_times": 26.72,
      "transport_modes": [
        "BUS"
      ],
      "stops": [
        {
          "id": "39825",
          "name": "Molkom, Vårdcentralen",
          "lat": 59.600446,
          "lon": 13.722023
        }
      ]
    }
```

{{% /tab %}} {{% /tabs %}}

### Response data fields

#### NationalStopGroupResponse

| **Name**                            | **Data type** | **Description**                                                                                                                                                                                    |
|-------------------------------------|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| timestamp                           | String        | The timestamp.                                                                                                                                                                                     |
| query.queryTime                     | String        | The time for which the stops are requested.                                                                                                                                                        |
| query.query                         | String        | The queried search value to match the stop name (null if no search value is given).                                                                                                                |
| stop_group                          | StopGroup[]   | The stop groups which are included in the query, one or more.                                                                                                                                      |
| stop_group.id                       | String        | The stop group id.                                                                                                                                                                                 |
| stop_group.name                     | String        | The stop group name.                                                                                                                                                                               |
| stop_group.area_type                | String        | The stop group area type (metastop or rikshallplats).                                                                                                                                              |                                                                                                          
| stop_group.avarage_daily_stop_times | Float         | The average daily departures from the stop area.                                                                                                                                                   |
| stop_group.transport_modes          | String        | Transport modes stopping at this stop. This is based on actual traffic in the current timetable period. If a stop does not have traffic in the current timetable period, this array will be empty. |
| stop_group.stops                    | Stop[]        | Child stops included in the stop group.                                                                                                                                                            |

#### Stops

| **Name**                  | **Data type** | **Description**                                                                                                                                                                       |
|---------------------------|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| stop                      | Stop          | Information about the stop within the national stop group.                                                                                                                            |
| stop.id                   | String        | The stop id.                                                                                                                                                                          |
| stop.name                 | String        | The stop name.                                                                                                                                                                        |
| stop.lat                  | String        | The stop latitude (WGS84, decimal degree).                                                                                                                                            |                                                                                                          
| stop.lon                  | String        | The stop longitude (WGS84, decimal degree).                                                                                                                                           |

## License

The Trafiklab Timetables API is available under the CC-BY 4.0 license. You should mention the data is provided by Trafiklab.se.

You are free to:

- Share — copy and redistribute the material in any medium or format for any purpose, even commercially.
- Adapt — remix, transform, and build upon the material for any purpose, even commercially.
- The licensor cannot revoke these freedoms as long as you follow the license terms.

Under the following terms:

- Attribution — You must give appropriate credit , provide a link to the license, and indicate if changes were made . You may do so in any reasonable manner,
  but not in any way that suggests the licensor endorses you or your use.
- No additional restrictions — You may not apply legal terms or technological measures that legally restrict others from doing anything the license permits.

Notices:

You do not have to comply with the license for elements of the material in the public domain or where your use is permitted by an applicable exception or
limitation .

No warranties are given. The license may not give you all of the permissions necessary for your intended use. For example, other rights such as publicity,
privacy, or moral rights may limit how you use the material.

https://creativecommons.org/licenses/by/4.0/legalcode.txt---
