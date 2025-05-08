---
title: Trafiklab Timetables
weight: 10
date: 2025-04-01
badge: beta
---

## What does this API provide?

Trafiklab Timetables provides a list of departures or arrivals at a given stop.

### Data format

The data is formatted as JSON.

### Updates

The static data used for this API is updated when changes are made, at most once per day. Real-time data is updated continuously, but lists with departures and
arrivals for a given time are cached for 60 seconds. This means that making new requests for the same location and time within 60 seconds won't return any
updates.

### Breaking changes

This API has the **beta** status. We are actively developing this API based on user feedback. Minor breaking changes
may occur on short notice. New fields may be added without warning.

### Operators covered by this dataset

{{% stip-data-availability scheduled realtime %}}

## Using Trafiklab Timetables

Trafiklab Timetables consists of two different endpoints, one for departures and one for arrivals. Both endpoints take
a stop id and timestamp as parameters, and have the same response structure. They return a list of departures or arrivals from the given stop,
including a bit of information about each vehicle, such as where it is heading or where it comes from.

### Stops

When listing departures or arrivals, the API takes an area id. This id matches `stop_id` from GTFS Sverige 2 stops.txt, `area_id` in GTFS Sweden 3's
areas.txt, and the ids used in the Resrobot APIs.
Each area contains one or more stops, for example when both metro and buses stop at the same area. How areas are divided in stops depends on how the local
agencies structure their data.

{{% note %}}
**Rikshållplatser**

Rikshållplatser, Swedish for "national stops", is the historical name for a grouping of multiple local stops under one name and id. This is done to avoid
duplicate stops when they are considered to be one stop by travelers. An example are certain multimodal stops, where a bus stop and tram stop may be at the same
location. Rikshållplatser typically only group stops which are "identical" for travelers, meaning train stops always have their own rikshållplats as you always
need to walk to another (nearby) stop in case of a bus transfer, as buses do not share platforms with trains.

**Meta-stops**

Meta-stops are groups of multiple nearby stops. This is done to simplify route-planning for travelers. An example meta stop is "Stockholm" which combines
train, metro, tram and bus stops in central stockholm. This way, travelers can easily search a route "from Göteborg to Stockholm" without having to know about
all the local stops. Meta-stops are also used for combining multi-modal stops which are more spread out, such as Sundbyberg Station along with its two bus
stops (on different sides of the station) as well as its metro stop.

{{% /note %}}

An example is Slussen, which contains one area for buses and one area for metro traffic. Both are included when looking up slussen by its area id, and each
departure can be linked to one of these stops. The trafiklab realtime APIs take the id of a rikshållplats or meta-stop, **not** the id of underlying stops!

![2025-04-03-trafiklab-api-stop-hierarchy.png](/media/2025/04/2025-04-03-trafiklab-api-stop-hierarchy.png)

## Making a request

This call will show all departures from Göteborg Central Station (740000002). The id can be obtained
from [Trafiklab Stop Lookup](stop-lookup), [GTFS Sweden 3 (areas.txt)](/api/gtfs-datasets/gtfs-sweden-3/) or [GTFS Sverige 2 (stops.txt, no meta stops)](/api/gtfs-datasets/gtfs-sverige-2/).

### Call

{{% tabs %}} {{% tab "Departures" %}}

```text
https://realtime-api.trafiklab.se/v1/departures/740000002?key=API_KEY
https://realtime-api.trafiklab.se/v1/departures/740000002/2025-04-01T16:00?key=API_KEY
```

{{% /tab %}}

{{% tab "Arrivals" %}}

```text
https://realtime-api.trafiklab.se/v1/arrivals/740000003?key=API_KEY
https://realtime-api.trafiklab.se/v1/arrivals/740000003/2025-04-01T16:00?key=API_KEY
```

{{% /tab %}} {{% /tabs %}}

#### Request parameters

This API makes use of path parameters. They are part of the URL path and must be in the correct order.

```text
https://realtime-api.trafiklab.se/v1/departures/{area id}?key={key}
https://realtime-api.trafiklab.se/v1/departures/{area id}/{time}?key={key}
https://realtime-api.trafiklab.se/v1/arrivals/{area id}?key={key}
https://realtime-api.trafiklab.se/v1/arrivals/{area id}/{time}?key={key}
```

| **Name** | **Type** | **Data type** | **Required** | **Description**                                                                                                 |
|----------|----------|---------------|--------------|-----------------------------------------------------------------------------------------------------------------|
| area id  | Path     | String        | Yes          | The area/rikshallplats id for the stop you want to look up.                                                     |
| time     | Path     | String        | Optional     | The time to look up, in `YYYY-MM-DD\THH:mm` format. For example, 2025-04-01T10:00. Seconds cannot be specified. |
| key      | Query    | String        | Yes          | Your API key                                                                                                    |

The interval for which to show departures cannot be specified, and is always 60 minutes. Any filtering should be done on the client side.

### Response

The responses consist of 4 parts:

- The timestamp at which the response was created
- Information about the query (which stop was looked up, which time was requested)
- Information about the stops included in the response
- The actual departures/arrivals in the next 60 minutes

Precise technical documentation is available in the form of an OpenAPI specification on the bottom of this page.

{{% note %}} Note that the actual responses contain more entries and stops - we removed some from this example
response since it's only meant to show the structure of the response. {{% /note %}}

{{% tabs %}} {{% tab "Departures" %}}

```json
{
  "timestamp": "2025-04-01T14:22:43",
  "query": {
    "queryTime": "2025-04-01T14:22:00",
    "query": "740000002"
  },
  "stops": [
    {
      "id": "71314",
      "name": "Göteborg C",
      "lat": 57.708918,
      "lon": 11.973946,
      "transport_modes": [
        "TRAIN"
      ],
      "alerts": []
    },
    {
      "id": "71472",
      "name": "Göteborg C",
      "lat": 57.708918,
      "lon": 11.973946,
      "transport_modes": [
        "TRAIN"
      ],
      "alerts": []
    },
    {
      "id": "2",
      "name": "Göteborg Centralstation",
      "lat": 57.709299,
      "lon": 11.973659,
      "transport_modes": [
        "TRAIN",
        "BUS"
      ],
      "alerts": []
    }
  ],
  "departures": [
    {
      "scheduled": "2025-04-01T14:30:00",
      "realtime": "2025-04-01T14:30:00",
      "delay": 0,
      "canceled": false,
      "route": {
        "name": "Västtågen",
        "designation": "3258",
        "transport_mode_code": 100,
        "transport_mode": "TRAIN",
        "direction": "Vänersborg",
        "origin": {
          "id": "2",
          "name": "Göteborg Centralstation"
        },
        "destination": {
          "id": "241",
          "name": "Vänersborg central"
        }
      },
      "trip": {
        "trip_id": "141010001327690347",
        "start_date": "2025-04-01",
        "technical_number": 130
      },
      "agency": {
        "id": "505000000000000014",
        "name": "Västtrafik",
        "operator": "SJ Götalandståg"
      },
      "stop": {
        "id": "2",
        "name": "Göteborg Centralstation",
        "lat": 57.709299,
        "lon": 11.973659
      },
      "scheduled_platform": {
        "id": "9022050000002017",
        "designation": "9"
      },
      "realtime_platform": {
        "id": "9022050000002017",
        "designation": "9"
      },
      "alerts": [],
      "is_realtime": false
    },
    {
      "scheduled": "2025-04-01T14:40:00",
      "realtime": "2025-04-01T14:40:00",
      "delay": 0,
      "canceled": false,
      "route": {
        "name": "Öresundståg",
        "designation": "1111",
        "transport_mode_code": 100,
        "transport_mode": "TRAIN",
        "direction": "Malmö",
        "origin": {
          "id": "2",
          "name": "Göteborg Centralstation"
        },
        "destination": {
          "id": "110",
          "name": "Varberg bussterminal"
        }
      },
      "trip": {
        "trip_id": "141010001328007643",
        "start_date": "2025-04-01",
        "technical_number": 21
      },
      "agency": {
        "id": "505000000000000636",
        "name": "Öresundståg",
        "operator": "Transdev Sverige AB"
      },
      "stop": {
        "id": "2",
        "name": "Göteborg Centralstation",
        "lat": 57.709299,
        "lon": 11.973659
      },
      "scheduled_platform": {
        "id": "9022050000002017",
        "designation": "9"
      },
      "realtime_platform": {
        "id": "9022050000002017",
        "designation": "9"
      },
      "alerts": [],
      "is_realtime": false
    },
    {
      "scheduled": "2025-04-01T14:59:00",
      "realtime": "2025-04-01T14:59:00",
      "delay": 0,
      "canceled": false,
      "route": {
        "name": "MTRX",
        "designation": null,
        "transport_mode_code": 100,
        "transport_mode": "TRAIN",
        "direction": "Stockholm C",
        "origin": {
          "id": "71314",
          "name": "Göteborg C"
        },
        "destination": {
          "id": "1",
          "name": "Stockholm Centralstation"
        }
      },
      "trip": {
        "trip_id": "680000000000000109",
        "start_date": "2025-04-01",
        "technical_number": 27580
      },
      "agency": {
        "id": "505000000000000159",
        "name": "MTR Express AB",
        "operator": "MTR Express AB"
      },
      "stop": {
        "id": "71314",
        "name": "Göteborg C",
        "lat": 57.708918,
        "lon": 11.973946
      },
      "scheduled_platform": null,
      "realtime_platform": null,
      "alerts": [],
      "is_realtime": false
    }
  ]
}
```

{{% /tab %}}

{{% tab "Arrivals" %}}

```json
{
  "timestamp": "2025-04-01T14:42:24",
  "query": {
    "queryTime": "2025-04-01T14:42:00",
    "query": "740000003"
  },
  "stops": [
    {
      "id": "3",
      "name": "Malmö Centralstation",
      "lat": 55.608777,
      "lon": 13.000216,
      "transport_modes": [
        "TRAIN",
        "BUS"
      ],
      "alerts": []
    }
  ],
  "arrivals": [
    {
      "scheduled": "2025-04-01T14:39:00",
      "realtime": "2025-04-01T14:42:23",
      "delay": 203,
      "canceled": false,
      "route": {
        "name": "Ringlinjen",
        "designation": "3",
        "transport_mode_code": 700,
        "transport_mode": "BUS",
        "direction": "Ringlinjen via Fridhemstorget",
        "origin": {
          "id": "26806",
          "name": "Malmö Värnhem"
        },
        "destination": {
          "id": "26806",
          "name": "Malmö Värnhem"
        }
      },
      "trip": {
        "trip_id": "121120000367831560",
        "start_date": "2025-04-01",
        "technical_number": 137
      },
      "agency": {
        "id": "505000000000000012",
        "name": "Skånetrafiken",
        "operator": "Nobina Sverige AB"
      },
      "stop": {
        "id": "3",
        "name": "Malmö Centralstation",
        "lat": 55.608777,
        "lon": 13.000216
      },
      "scheduled_platform": {
        "id": "9022050000003004",
        "designation": "D"
      },
      "realtime_platform": {
        "id": "9022050000003004",
        "designation": "D"
      },
      "alerts": [],
      "is_realtime": true
    },
    {
      "scheduled": "2025-04-01T15:12:00",
      "realtime": "2025-04-01T15:08:22",
      "delay": -218,
      "canceled": false,
      "route": {
        "name": "Ø Göteborg - Halmstad - Helsingborg - Malmö - Købe",
        "designation": "804",
        "transport_mode_code": 100,
        "transport_mode": "TRAIN",
        "direction": "Göteborg C",
        "origin": {
          "id": "25317",
          "name": "København Østerport"
        },
        "destination": {
          "id": "2",
          "name": "Göteborg Centralstation"
        }
      },
      "trip": {
        "trip_id": "121120000357559623",
        "start_date": "2025-04-01",
        "technical_number": 1082
      },
      "agency": {
        "id": "505000000000000636",
        "name": "Öresundståg",
        "operator": "Transdev Sverige AB"
      },
      "stop": {
        "id": "3",
        "name": "Malmö Centralstation",
        "lat": 55.608777,
        "lon": 13.000216
      },
      "scheduled_platform": {
        "id": "9022050000003019",
        "designation": "4a"
      },
      "realtime_platform": {
        "id": "9022050000003019",
        "designation": "4a"
      },
      "alerts": [
        {
          "type": "OTHER_CAUSE",
          "title": "Kort tåg - 2 mot 3",
          "text": "Tåget kör med två tågsätt istället för tre på sträckan København Østerport - Helsingborg C. Orsaken är vagnbrist. "
        }
      ],
      "is_realtime": true
    }
  ]
}
```

{{% /tab %}} {{% /tabs %}}

### Response data fields

{{% info %}} The structure for departure and arrival boards is nearly identical. We list the most commonly used fields
for both endpoints in this table. When we write departure/arrival, apply the one that matches the endpoint you're using.
{{% /info %}}

#### DeparturesResponse / ArrivalsResponse

| **Name**              | **Data type**    | **Description**                                                                                                                                                                                    |
|-----------------------|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| timestamp             | String           | List of departures or arrivals.                                                                                                                                                                    |
| query.queryTime       | String           | The time for which departures/arrivals are requested.                                                                                                                                              |
| query.query           | String           | The queried area/rikshallplats id.                                                                                                                                                                 |
| stops                 | Stop[]           | The stops which are included in the query, one or more.                                                                                                                                            |
| stop.id               | String           | The stop id.                                                                                                                                                                                       |
| stop.name             | Datum            | The stop name.                                                                                                                                                                                     |
| stop.lat              | String           | The stop latitude.                                                                                                                                                                                 |                                                                                                          
| stop.lon              | String           | The top longitude.                                                                                                                                                                                 |
| stop.transport_modes  | String           | Transport modes stopping at this stop. This is based on actual traffic in the current timetable period. If a stop does not have traffic in the current timetable period, this array will be empty. |
| departures / arrivals | CallAtLocation[] | Departures or arrivals from the given stop                                                                                                                                                         |

#### CallAtLocation

| **Name**                  | **Data type** | **Description**                                                                                                                                                                                                                      |
|---------------------------|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| scheduled                 | String        | Departure/Arrival time at this stop, formatted as `YYYY-MM-DDTHH:mm:ss` in the local timezone.                                                                                                                                       |
| realtime                  | String        | Realtime departure/arrival time at this stop, formatted as `YYYY-MM-DDTHH:mm:ss` in the local timezone. When no realtime data is available, the scheduled value is used. See also `is_realtime`.                                     |
| delay                     | Integer       | The delay, in seconds, for this departure/arrival. Can be negative in case the vehicle is early. Set to 0 when no realtime data is available, see also `is_realtime`.                                                                |
| canceled                  | String        | Stop latitude (WGS84, decimal degree), ex 59.293611                                                                                                                                                                                  |
| agency.id                 | String        | A unique id identifying this agency. Matches GTFS Sweden 3.                                                                                                                                                                          |
| agency.name               | String        | The name of the agency responsible for this trip.                                                                                                                                                                                    |
| agency.operator           | String        | The name of the company running the trip, such as Nobina, Keolis, ... . May be null when unknown.                                                                                                                                    |
| route.name                | String        | Stop longitude (WGS84, decimal degree), ex 18.083056                                                                                                                                                                                 |
| route.designation         | String        | Internal id, do not use                                                                                                                                                                                                              |
| route.transport_mode      | String        | The transport mode for this route, one of <ul><li>BUS<li>METRO<li>TRAIN<li>TRAM<li>TAXI<li>BOAT</ul>                                                                                                                                 |
| route.transport_mode_code | Integer       | The specific GTFS transport mode code for this route. See [GTFS extended route types](/api/gtfs-datasets/overview/extensions/).                                                                                                      |
| route.direction           | String        | The direction for this route, which is for example shown on the front of buses. This text may be different for the same route at different stops, for example "A via B" will often change to just "A" after stop B has been passed. |
| route.origin.id           | String        | The id of the first stop on this route.                                                                                                                                                                                              |
| route.origin.name         | String        | The name of the first stop on this route.                                                                                                                                                                                            |
| route.destination.id      | String        | The id of the last stop on this route.                                                                                                                                                                                               |
| route.destination.name    | String        | The name of the last stop on this route.                                                                                                                                                                                             |
| trip.trip_id              | String        | The trip id, which can be used in combination with `start_date` to uniquely identify a trip. Matches GTFS Sweden 3 and GTFS Sweden 3 realtime data.                                                                                  |
| trip.start_date           | String        | The date on which this trip was started.                                                                                                                                                                                             |
| trip.technical_number     | Integer       | The technical trip number of this trip. Uniquely identifies a trip in combination with `start_date` and `agency.id`.                                                                                                                 | |
| stop                      | Stop          | Information about the stop where the departure/arrival takes place. Since a queried area can contain multiple stops, this field can be used to identify at which of the stops this departure/arrival takes place.                    |
| stop.id                   | String        | The stop id.                                                                                                                                                                                                                         |
| stop.name                 | String        | The stop name.                                                                                                                                                                                                                       |
| stop.lat                  | String        | The stop latitude.                                                                                                                                                                                                                   |                                                                                                          
| stop.lon                  | String        | The top longitude.                                                                                                                                                                                                                   |
| scheduled_platform        | Platform      | Information about the scheduled platform. Null if no platform information is available.                                                                                                                                              |
| scheduled_platform.id     | String        | The scheduled platform id.                                                                                                                                                                                                           |
| scheduled_platform.name   | String        | The  scheduled platform name.                                                                                                                                                                                                        |
| realtime_platform         | Platform      | Information about the realtime platform. If no realtime data is available, the scheduled platform data is used, see also `is_realtime`. Null if no platform information is available.                                                |
| realtime_platform.id      | String        | The realtime platform id.                                                                                                                                                                                                            |
| realtime_platform.name    | String        | The realtime platform name.                                                                                                                                                                                                          |
| alerts                    | Alert[]       | Any messages for this stop, for example regarding roadworks, delays, changed routes etc.                                                                                                                                             |
| is_realtime               | Boolean       | Indicates weather realtime data is available for this departure/arrival. When false, realtime fields have been filled with scheduled data for easier client-side implementations.                                                    |

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

https://creativecommons.org/licenses/by/4.0/legalcode.txt