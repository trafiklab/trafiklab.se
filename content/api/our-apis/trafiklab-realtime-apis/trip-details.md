---
title: Trafiklab Trips
weight: 20
date: 2025-12-08
badge: beta
---

## What does this API provide?

Trafiklab Trips provides a list of all departures and arrivals for a given trip. This way you can show the complete
journey of a specific vehicle.

{{% note %}}
**These APIs are licensed as CC-BY**

This allows you to do whatever you want as long as you include a little "data from Trafiklab.se" attribution on
screens and website widgets. Read more about this in the license text at the bottom of this page.
{{% /note %}}

### Data format

The data is formatted as JSON.

### Updates

The scheduled data used for this API is updated when changes are made, at most once per day. Real-time data is updated
continuously, but lists with departures and
arrivals for a given time are cached for 60 seconds. This means that making new requests for the same trip within 60
seconds won't return any
updates.

### Breaking changes

This API has the **beta** status. We are actively developing this API based on user feedback. Minor breaking changes
may occur on short notice. New fields may be added without warning.

### Operators covered by this dataset

{{% stip-data-availability scheduled realtime %}}

## Using Trafiklab Trips

Trafiklab Trips consists of one endpoint, to which you supply the `trip_id` and the `start_date` for the journey.
The start date is the planning date to which the trip belongs, and may differ from the date at which the vehicle
actually stops at its first stop.

## Making a request

The `trip_id` and `start_date` can be obtained from [Trafiklab Stop Lookup](timetables.md),
[GTFS Sweden 3 static data (trips.txt, calendar_dates.txt)](/api/gtfs-datasets/gtfs-sweden-3/)
or [GTFS Sweden 3 Realtime](/api/gtfs-datasets/gtfs-sweden-3/).

### Making an API call

#### Request parameters

This API makes use of path parameters. They are part of the URL path and must be in the correct order.

```text
https://realtime-api.trafiklab.se/v1/trips/{trip_id}/{start_date}?key={key}
```

| **Name**   | **Type** | **Data type** | **Required** | **Description**                                                                                                                                |
|------------|----------|---------------|--------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| trip_id    | Path     | String        | Yes          | The trip_id for the trip you want to look up.                                                                                                  |
| start_date | Path     | String        | Yes          | The scheduled date for this trip, to differ between different days on which this trip is ran. In `YYYY-MM-DD` format. For example, 2025-12-31. |
| key        | Query    | String        | Yes          | Your API key                                                                                                                                   |

#### Example API call

This call will show all departures and arrivals for Skånetrafikens bus 3 (trip_id 121120000386193630) scheduled on
November 11th, 2025.

```text
https://realtime-api.trafiklab.se/v1/trips/121120000386193630/2025-11-11?key=API_KEY
```

### Response

The responses consist of four parts:

- The timestamp at which the response was created
- Information about the query (which trip was looked up, which start_date was requested)
- Information about the route on which the trip is run
- The actual departures/arrivals for this trip

Precise technical documentation is available in the form of an OpenAPI specification on the bottom of this page.

```json
{
  "timestamp": "2026-01-20T15:17:55",
  "query": {
    "queryTime": "2026-01-20T00:00:00",
    "query": "121120000372401393"
  },
  "agency": {
    "id": "505000000000000012",
    "name": "Skånetrafiken",
    "operator": "Bergkvarabuss AB"
  },
  "route": {
    "name": "Malmö  - Skanör",
    "designation": "15",
    "transport_mode_code": 700,
    "transport_mode": "BUS",
    "direction": "SkåneExpressen Malmö C",
    "origin": {
      "id": "27782",
      "name": "Skanör Haga"
    },
    "destination": {
      "id": "3",
      "name": "Malmö Centralstation"
    }
  },
  "trip": {
    "trip_id": "121120000372401393",
    "start_date": "2026-01-20",
    "technical_number": 84
  },
  "calls": [
    {
      "scheduledDeparture": "2026-01-20T14:29:00",
      "realtimeDeparture": "2026-01-20T14:29:09",
      "departureDelay": 9,
      "departureCanceled": false,
      "scheduledArrival": "2026-01-20T14:29:00",
      "realtimeArrival": "2026-01-20T14:27:49",
      "arrivalDelay": -71,
      "arrivalCanceled": false,
      "stop": {
        "id": "27782",
        "area_id": "740012583",
        "name": "Skanör Haga",
        "lat": 55.407469,
        "lon": 12.865432
      },
      "scheduled_platform": {
        "id": "9022050027782002",
        "designation": "B"
      },
      "realtime_platform": {
        "id": "9022050027782002",
        "designation": "B"
      },
      "alerts": [],
      "is_realtime": true
    },
    {
      "scheduledDeparture": "2026-01-20T14:32:57",
      "realtimeDeparture": "2026-01-20T14:33:08",
      "departureDelay": 11,
      "departureCanceled": false,
      "scheduledArrival": "2026-01-20T14:32:57",
      "realtimeArrival": "2026-01-20T14:32:32",
      "arrivalDelay": -25,
      "arrivalCanceled": false,
      "stop": {
        "id": "1231",
        "area_id": "740001231",
        "name": "Ljunghusen Storvägen",
        "lat": 55.405538,
        "lon": 12.920899
      },
      "scheduled_platform": {
        "id": "9022050001231002",
        "designation": "B"
      },
      "realtime_platform": {
        "id": "9022050001231002",
        "designation": "B"
      },
      "alerts": [],
      "is_realtime": true
    },
    {
      "scheduledDeparture": "2026-01-20T14:36:12",
      "realtimeDeparture": "2026-01-20T14:35:33",
      "departureDelay": -39,
      "departureCanceled": false,
      "scheduledArrival": "2026-01-20T14:36:12",
      "realtimeArrival": "2026-01-20T14:35:33",
      "arrivalDelay": -39,
      "arrivalCanceled": false,
      "stop": {
        "id": "27779",
        "area_id": "740012580",
        "name": "Höllviken Höllvikstrand",
        "lat": 55.413625,
        "lon": 12.943024
      },
      "scheduled_platform": {
        "id": "9022050027779002",
        "designation": "B"
      },
      "realtime_platform": {
        "id": "9022050027779002",
        "designation": "B"
      },
      "alerts": [],
      "is_realtime": true
    },
    {
      "scheduledDeparture": "2026-01-20T14:38:00",
      "realtimeDeparture": "2026-01-20T14:38:03",
      "departureDelay": 3,
      "departureCanceled": false,
      "scheduledArrival": "2026-01-20T14:38:00",
      "realtimeArrival": "2026-01-20T14:36:56",
      "arrivalDelay": -64,
      "arrivalCanceled": false,
      "stop": {
        "id": "60011",
        "area_id": "740076441",
        "name": "Höllviken Nyckelhålsparken",
        "lat": 55.419085,
        "lon": 12.950939
      },
      "scheduled_platform": {
        "id": "9022050060011002",
        "designation": "B"
      },
      "realtime_platform": {
        "id": "9022050060011002",
        "designation": "B"
      },
      "alerts": [],
      "is_realtime": true
    },
    {
      "scheduledDeparture": "2026-01-20T14:39:50",
      "realtimeDeparture": "2026-01-20T14:40:13",
      "departureDelay": 23,
      "departureCanceled": false,
      "scheduledArrival": "2026-01-20T14:39:50",
      "realtimeArrival": "2026-01-20T14:39:37",
      "arrivalDelay": -13,
      "arrivalCanceled": false,
      "stop": {
        "id": "27777",
        "area_id": "740012578",
        "name": "Höllviken Östra Halörsvägen",
        "lat": 55.423639,
        "lon": 12.960485
      },
      "scheduled_platform": {
        "id": "9022050027777003",
        "designation": "C"
      },
      "realtime_platform": {
        "id": "9022050027777003",
        "designation": "C"
      },
      "alerts": [],
      "is_realtime": true
    },
    {
      "scheduledDeparture": "2026-01-20T14:48:00",
      "realtimeDeparture": "2026-01-20T14:48:15",
      "departureDelay": 15,
      "departureCanceled": false,
      "scheduledArrival": "2026-01-20T14:48:00",
      "realtimeArrival": "2026-01-20T14:45:58",
      "arrivalDelay": -122,
      "arrivalCanceled": false,
      "stop": {
        "id": "27819",
        "area_id": "740020262",
        "name": "Vellinge ängar",
        "lat": 55.472313,
        "lon": 13.01021
      },
      "scheduled_platform": {
        "id": "9022050027819002",
        "designation": "B"
      },
      "realtime_platform": {
        "id": "9022050027819002",
        "designation": "B"
      },
      "alerts": [
        {
          "type": "CONSTRUCTION",
          "title": "Trafikinformation: Hållplats Vellinge ängar",
          "text": "Trafikinformation: Fr.o.m. 27/10 2025 kl. 7.00 är hållplats Vellinge ängar, läge D, stängd p.g.a. arbete med nybyggnation av flerbostadshus på Vallgatan. Linje 150 mot Klågerup och 181 mot Vellinge angör tillfällig hållplats på Norrevångsgatan."
        }
      ],
      "is_realtime": true
    },
    {
      "scheduledDeparture": "2026-01-20T14:59:18",
      "realtimeDeparture": "2026-01-20T14:58:23",
      "departureDelay": -55,
      "departureCanceled": false,
      "scheduledArrival": "2026-01-20T14:59:18",
      "realtimeArrival": "2026-01-20T14:57:58",
      "arrivalDelay": -80,
      "arrivalCanceled": false,
      "stop": {
        "id": "27006",
        "area_id": "740016287",
        "name": "Malmö Mobilia Öster",
        "lat": 55.581464,
        "lon": 13.005878
      },
      "scheduled_platform": {
        "id": "9022050027006002",
        "designation": "B"
      },
      "realtime_platform": {
        "id": "9022050027006002",
        "designation": "B"
      },
      "alerts": [],
      "is_realtime": true
    },
    {
      "scheduledDeparture": "2026-01-20T15:04:00",
      "realtimeDeparture": "2026-01-20T15:03:52",
      "departureDelay": -8,
      "departureCanceled": false,
      "scheduledArrival": "2026-01-20T15:04:00",
      "realtimeArrival": "2026-01-20T15:01:29",
      "arrivalDelay": -151,
      "arrivalCanceled": false,
      "stop": {
        "id": "26814",
        "area_id": "740016782",
        "name": "Malmö Södervärn",
        "lat": 55.588614,
        "lon": 13.006955
      },
      "scheduled_platform": {
        "id": "9022050026814008",
        "designation": "H"
      },
      "realtime_platform": {
        "id": "9022050026814008",
        "designation": "H"
      },
      "alerts": [],
      "is_realtime": true
    },
    {
      "scheduledDeparture": "2026-01-20T15:10:12",
      "realtimeDeparture": "2026-01-20T15:10:47",
      "departureDelay": 35,
      "departureCanceled": false,
      "scheduledArrival": "2026-01-20T15:10:12",
      "realtimeArrival": "2026-01-20T15:10:47",
      "arrivalDelay": 35,
      "arrivalCanceled": false,
      "stop": {
        "id": "71690",
        "area_id": "740015746",
        "name": "Malmö Kungsgatan",
        "lat": 55.600579,
        "lon": 13.007166
      },
      "scheduled_platform": {
        "id": "9022050071690003",
        "designation": "C"
      },
      "realtime_platform": {
        "id": "9022050071690003",
        "designation": "C"
      },
      "alerts": [],
      "is_realtime": true
    },
    {
      "scheduledDeparture": "2026-01-20T15:11:10",
      "realtimeDeparture": "2026-01-20T15:11:24",
      "departureDelay": 14,
      "departureCanceled": false,
      "scheduledArrival": "2026-01-20T15:11:10",
      "realtimeArrival": "2026-01-20T15:11:24",
      "arrivalDelay": 14,
      "arrivalCanceled": false,
      "stop": {
        "id": "26811",
        "area_id": "740015745",
        "name": "Malmö Studentgatan",
        "lat": 55.602798,
        "lon": 13.005198
      },
      "scheduled_platform": {
        "id": "9022050026811002",
        "designation": "B"
      },
      "realtime_platform": {
        "id": "9022050026811002",
        "designation": "B"
      },
      "alerts": [],
      "is_realtime": true
    },
    {
      "scheduledDeparture": "2026-01-20T15:17:00",
      "realtimeDeparture": "2026-01-20T15:16:25",
      "departureDelay": -35,
      "departureCanceled": false,
      "scheduledArrival": "2026-01-20T15:17:00",
      "realtimeArrival": "2026-01-20T15:16:25",
      "arrivalDelay": -35,
      "arrivalCanceled": false,
      "stop": {
        "id": "3",
        "area_id": "740000003",
        "name": "Malmö Centralstation",
        "lat": 55.608777,
        "lon": 13.000216
      },
      "scheduled_platform": {
        "id": "9022050000003009",
        "designation": "I"
      },
      "realtime_platform": {
        "id": "9022050000003009",
        "designation": "I"
      },
      "alerts": [],
      "is_realtime": true
    }
  ]
}
```

### Response data fields

#### TripDetailResponse

| **Name**                  | **Data type**    | **Description**                                                                                                                                                                                                                     |
|---------------------------|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| timestamp                 | String           | List of departures or arrivals.                                                                                                                                                                                                     |
| query.queryTime           | String           | The `start_date` for which departures/arrivals are requested.                                                                                                                                                                       |
| query.query               | String           | The queried `trip_id`                                                                                                                                                                                                               |
| agency.id                 | String           | A unique id identifying this agency. Matches GTFS Sweden 3.                                                                                                                                                                         |
| agency.name               | String           | The name of the agency responsible for this trip.                                                                                                                                                                                   |
| agency.operator           | String           | The name of the company running the trip, such as Nobina, Keolis, ... . May be null when unknown.                                                                                                                                   |
| route.name                | String           | The route name, if set by the operator. Used for lines which are known by their name instead of their number, such as Silverlinjen, Nockebybanan or Saltsjöbanan.                                                                   |
| route.designation         | String           | The public facing designation for this route. Often this is the line number, but it may even contain characters (for example "42X").                                                                                                |
| route.transport_mode      | String           | The transport mode for this route, one of <ul><li>BUS<li>METRO<li>TRAIN<li>TRAM<li>TAXI<li>BOAT</ul>                                                                                                                                |
| route.transport_mode_code | Integer          | The specific GTFS transport mode code for this route. See [GTFS extended route types](/api/gtfs-datasets/overview/extensions/).                                                                                                     |
| route.direction           | String           | The direction for this route, which is for example shown on the front of buses. This text may be different for the same route at different stops, for example "A via B" will often change to just "A" after stop B has been passed. |
| route.origin.id           | String           | The id of the first stop on this route.                                                                                                                                                                                             |
| route.origin.name         | String           | The name of the first stop on this route.                                                                                                                                                                                           |
| route.destination.id      | String           | The id of the last stop on this route.                                                                                                                                                                                              |
| route.destination.name    | String           | The name of the last stop on this route.                                                                                                                                                                                            |
| trip.trip_id              | String           | The trip id, which can be used in combination with `start_date` to uniquely identify a trip. Matches GTFS Sweden 3 and GTFS Sweden 3 realtime data.                                                                                 |
| trip.start_date           | String           | The date on which this trip was started.                                                                                                                                                                                            |
| trip.technical_number     | Integer          | The technical trip number of this trip. Uniquely identifies a trip in combination with `start_date` and `agency.id`.                                                                                                                |
| calls                     | CallAtLocation[] | Departures and arrivals for the given route                                                                                                                                                                                         |

#### CallAtLocation

| **Name**                | **Data type** | **Description**                                                                                                                                                                                                                                                                                                                        |
|-------------------------|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| scheduled               | String        | Departure time at this stop, formatted as `YYYY-MM-DDTHH:mm:ss` in the local timezone.                                                                                                                                                                                                                                                 |
| realtime                | String        | Realtime departure time at this stop, formatted as `YYYY-MM-DDTHH:mm:ss` in the local timezone. When no realtime data is available, the scheduled value is used. See also `is_realtime`.                                                                                                                                               |
| delay                   | Integer       | The delay, in seconds, for this departure/arrival. Can be negative in case the vehicle is early. Set to 0 when no realtime data is available, see also `is_realtime`.                                                                                                                                                                  |
| canceled                | String        | True if this departure has been cancelled. This means that either the entire trip, or a part of the trip including this departure/arrival, has been cancelled. Note that a departure can be cancelled while the arrival at the same stop can still be serviced, or the arrival can be cancelled while the departure still is serviced. |
| scheduledArrival        | String        | Arrival time at this stop, formatted as `YYYY-MM-DDTHH:mm:ss` in the local timezone.                                                                                                                                                                                                                                                   |
| realtimeArrival         | String        | Realtime arrival time at this stop, formatted as `YYYY-MM-DDTHH:mm:ss` in the local timezone. When no realtime data is available, the scheduled value is used. See also `is_realtime`.                                                                                                                                                 |
| arrivalDelay            | Integer       | The delay, in seconds, for this arrival/arrival. Can be negative in case the vehicle is early. Set to 0 when no realtime data is available, see also `is_realtime`.                                                                                                                                                                    |
| arrivalCanceled         | String        | True if this arrival has been cancelled. This means that either the entire trip, or a part of the trip including this arrival/arrival, has been cancelled. Note that a arrival can be cancelled while the arrival at the same stop can still be serviced, or the arrival can be cancelled while the arrival still is serviced.         | 
| stop                    | Stop          | Information about the stop where the departure/arrival takes place. Since a queried area can contain multiple stops, this field can be used to identify at which of the stops this departure/arrival takes place.                                                                                                                      |
| stop.id                 | String        | The stop id.                                                                                                                                                                                                                                                                                                                           |
| stop.name               | String        | The stop name.                                                                                                                                                                                                                                                                                                                         |
| stop.lat                | Float         | The stop latitude.                                                                                                                                                                                                                                                                                                                     |                                                                                                          
| stop.lon                | Float         | The top longitude.                                                                                                                                                                                                                                                                                                                     |
| scheduled_platform      | Platform      | Information about the scheduled platform. Null if no platform information is available.                                                                                                                                                                                                                                                |
| scheduled_platform.id   | String        | The scheduled platform id.                                                                                                                                                                                                                                                                                                             |
| scheduled_platform.name | String        | The scheduled platform name.                                                                                                                                                                                                                                                                                                           |
| realtime_platform       | Platform      | Information about the realtime platform. If no realtime data is available, the scheduled platform data is used, see also `is_realtime`. Null if no platform information is available.                                                                                                                                                  |
| realtime_platform.id    | String        | The realtime platform id.                                                                                                                                                                                                                                                                                                              |
| realtime_platform.name  | String        | The realtime platform name.                                                                                                                                                                                                                                                                                                            |
| alerts                  | Alert[]       | Any messages for this stop, for example regarding roadworks, delays, changed routes etc.                                                                                                                                                                                                                                               |
| is_realtime             | Boolean       | Indicates weather realtime data is available for this departure/arrival. When false, realtime fields have been filled with scheduled data for easier client-side implementations.                                                                                                                                                      |

## License

These Trafiklab APIs are available under the CC-BY 4.0 license. You should mention the data is provided by Trafiklab.se,
for example through the use of a little
footnote text on public displays or website widgets. Contact us for exemptions if you're implementing solutions for
public transport operators, such as onboard
displays.

You are free to:

- Share — copy and redistribute the material in any medium or format for any purpose, even commercially.
- Adapt — remix, transform, and build upon the material for any purpose, even commercially.
- The licensor cannot revoke these freedoms as long as you follow the license terms.

Under the following terms:

- Attribution — You must give appropriate credit , provide a link to the license, and indicate if changes were made .
  You may do so in any reasonable manner,
  but not in any way that suggests the licensor endorses you or your use.
- No additional restrictions — You may not apply legal terms or technological measures that legally restrict others from
  doing anything the license permits.

Notices:

You do not have to comply with the license for elements of the material in the public domain or where your use is
permitted by an applicable exception or
limitation .

No warranties are given. The license may not give you all of the permissions necessary for your intended use. For
example, other rights such as publicity,
privacy, or moral rights may limit how you use the material.

https://creativecommons.org/licenses/by/4.0/legalcode.txt