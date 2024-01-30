---
title: SL Departures v4.0 (Realtidsinformation 4)
weight: 200
date: 2016-11-30
aliases:
  - /api/sl-realtidsinformation-4/sl-realtidsinformation-4
  - /api/sl-realtidsinformation-4
  - /api/sl-realtidsinformation-4/dokumentation
  - /api/sl-realtidsinformation-4/nivaer
  - /api/sl-realtidsinformation-4/konsol
  - /node/15754
  - /node/15754/dokumentation
  - /node/15754/nivaer
  - /node/15754/konsol
---

## Description

Real-time information regarding buses, subways, commuter trains, and local trains.

## URL

`https://api.sl.se/api2/realtimedeparturesV4.<FORMAT>?key=<YOUR API KEY>&siteid=<SITEID>&timewindow=<TIMEWINDOW>`

### API Key Levels

| Level    | Max calls/minute | Max calls/month |
|----------|------------------|-----------------|
| Bronze   | 30               | 10,000          |
| Silver   | 60               | 500,000         |
| Silver + | 60               | 1,500,000       |
| Gold     |                  | 10,000,000      |
| Gold +   |                  | 30,000,000      |
| Platinum |                  | On demand       |

## Format

JSON or XML according to the extension in the service call.

## Parameters

| Parameters       | Data Type | Mandatory | Description                                                                                                                                                         |
|------------------|-----------|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Format           | String    | Yes       | Format of the response data. Valid values are “json” or “xml”.                                                                                                      |
| SiteId           | Integer   | Yes       | Unique identification number for the location for which current departures should be fetched, e.g., 9192 for Slussen. Obtained from the SL Location Lookup service. |
| TimeWindow       | Integer   | Yes       | Fetch departures within the desired time window. The time window is the number of minutes from now. Max 60.                                                         |
| Key              | String    | Yes       | A valid API key.                                                                                                                                                    |
| Bus              | Boolean   | No        | Default = true. If false, excludes bus data from the response.                                                                                                      |
| Metro            | Boolean   | No        | Default = true. If false, excludes metro data from the response.                                                                                                    |
| Train            | Boolean   | No        | Default = true. If false, excludes train data from the response.                                                                                                    |
| Tram             | Boolean   | No        | Default = true. If false, excludes tram data from the response.                                                                                                     |
| Ship             | Boolean   | No        | Default = false. If true, includes information about uncertain prognosis.                                                                                           |
| EnablePrediction | Boolean   | No        | Default = true. If false, excludes prediction data from the response.                                                                                               |

## Result

Results from real-time search. For XML format, the root element name is "ResponseOfDepartures."

### Response Structure

| Name          | Data Type | Description                                                                            |
|---------------|-----------|----------------------------------------------------------------------------------------|
| StatusCode    | Integer   | Contains the status code for the possible message.                                     |
| Message       | String    | Contains any call-related messages such as error messages. See “Error Messages” below. |
| ExecutionTime | Long      | Indicates how long (in ms) it took for the server to generate the response.            |
| ResponseData  | Departure | Contains the actual response data from the service. See “Response Data” below.         |

### Response Data/ResponseData

| Name                | Data Type | Description                                                                                                      |
|---------------------|-----------|------------------------------------------------------------------------------------------------------------------|
| LatestUpdate        | DateTime  | Indicates when the real-time information (DPS) was last updated.                                                 |
| DataAge             | Integer   | Number of seconds since the LatestUpdate timestamp.                                                              |
| Buses               | List      | List of all bus departures for the given siteId, see response structure.                                         |
| Metros              | List      | List of all subway departures for the given siteId, see response structure.                                      |
| Trains              | List      | List of all commuter train departures for the given siteId, see response structure.                              |
| Trams               | List      | List of all local train departures for the given siteId, see response structure.                                 |
| Ships               | List      | List of all boat departures for the given siteId, see response structure.                                        |
| StopPointDeviations | List      | List of stop area-specific deviations/disruptions. In other words, disruptions not tied to a specific departure. |

#### Departure

| Name                     | Data Type | Description                                                                                                                                                                                                                                                                                                               |
|--------------------------|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TransportMode            | String    | Mode of transport: "BUS", "METRO", "TRAIN", "TRAM", or "SHIP".                                                                                                                                                                                                                                                            |
| LineNumber               | String    | Line designation/number.                                                                                                                                                                                                                                                                                                  |
| Destination              | String    | Name of the line's end station.                                                                                                                                                                                                                                                                                           |
| JourneyDirection         | Integer   | Journey direction ID. 0 for unknown direction, otherwise 1 or 2.                                                                                                                                                                                                                                                          |
| GroupOfLine              | String    | For bus: Specifies if it is a blue bus. If it is a blue bus, it says "bluebus", otherwise the element is missing (XML) or null (JSON). For local train: Line group, e.g., "Tvärbanan" or "Roslagsbanan". For subway: Line grouping. Red/green/blue line. For boat: Specifies if it is a commuter boat or Waxholmsbolaget. |
| StopAreaName             | String    | Stop area name.                                                                                                                                                                                                                                                                                                           |
| StopAreaNumber           | Integer   | ID for the current stop area. Subway before transfer: 0.                                                                                                                                                                                                                                                                  |
| StopPointNumber          | Integer   | ID for the current stopping point. Subway before transfer: 0.                                                                                                                                                                                                                                                             |
| StopPointDesignation     | String    | Additional identifier for stopping point, e.g., letter for bus shelter or track for commuter train.                                                                                                                                                                                                                       |
| TimeTabledDateTime       | DateTime  | Departure time according to the timetable.                                                                                                                                                                                                                                                                                |
| ExpectedDateTime         | DateTime  | Expected departure time. If there is an associated disruption with sufficiently high priority, this may be null/empty. This is the case until a few minutes before departure.                                                                                                                                             |
| DisplayTime              | String    | Departure time for presentation. Can take formats like x min, HH:mm, or Now. If there is an associated disruption with sufficiently high priority, this may be set to "-". This is the case until a few minutes before departure.                                                                                         |
| JourneyNumber            | Integer   | Journey number for the departure.                                                                                                                                                                                                                                                                                         |
| Deviations               | List      | Contains the type "Deviation" below. This can be empty or contain 1 to several deviations.                                                                                                                                                                                                                                |
| SecondaryDestinationName | String    | Only for: Commuter train. Name of the intermediate destination.                                                                                                                                                                                                                                                           |
| PredictionState          | String    | Can have three different values: NORMAL, UNRELIABLE, UNKNOWN. UNRELIABLE indicates an uncertain prognosis. Name of the intermediate destination.                                                                                                                                                                          |

#### Deviation

| Name            | Data Type | Description                                                               |
|-----------------|-----------|---------------------------------------------------------------------------|
| Consequence     | String    | Description of the consequence for the current deviation.                 |
| ImportanceLevel | Integer   | Significance level for the current deviation. 0-9 where 9 is most severe. |
