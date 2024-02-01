---
title: SL Traffic status v2.0 (Trafikläget 2)
weight: 600
date: 2014-03-14
aliases:
  - /api/sl-trafiklaget-2
  - /api/sl-trafiklaget-2/documentation
  - /api/sl-trafiklaget-2/nivaer
  - /api/sl-trafiklaget-2/console
  - /node/12603
  - /node/12603/documentation
  - /node/12603/nivaer
  - /node/12603/console
---

{{% error %}}
Due to technical reasons, this API is being replaced by [SLs Deviations API](deviations.md) and [GTFS Service alerts](../gtfs-regional/realtime.md). It will
stop working in the near future.
{{% /error %}}

## Description

This API provides information about the current status of SL's traffic situation. It offers an overview
of the current status for each type of traffic. The information used by this API can be found on the
front page of sl.se under the heading "Trafikläget kl. xx:xx" ("Traffic situation at xx:xx"). The API has only one method that returns a summary
of the current traffic situation, considering disruptions that may affect passengers. The response is a list of different traffic types, each with a summary
status and a number of events (0 or more). There are three possible statuses for events:

- "No major disruptions"
- "Major impact"
- "Closed"

An event affects its traffic type, so that the traffic type's summary status is equal to the worst status among currently active events belonging to that
traffic type. In addition to the status, an event may also be planned.

*SL will replace this API with a new, similar API in the near future. The documentation for the current API
has therefore not been translated for the new Trafiklab website.*

## URL

`https://api.sl.se/api2/trafficsituation.<FORMAT>?key=<YOUR API KEY>`

### API Key Levels

| Level  | Max requests/minute | Max requests/month |
|--------|---------------------|--------------------|
| Bronze | 30                  | 10,000             |
| Silver | 60                  | 100,000            |
| Gold   |                     | As needed          |

## Format

JSON or XML according to the format specified in the service call.

## Parameters

| Parameters | Data Type | Mandatory | Description      |
|------------|-----------|-----------|------------------|
| Key        | String    | Yes       | A valid API key. |

## Result

### Response Structure

| Name          | Data Type     | Description                                                                             |
|---------------|---------------|-----------------------------------------------------------------------------------------|
| StatusCode    | Integer       | Contains the status code for the potential message.                                     |
| Message       | String        | Contains any call-related messages, such as error messages. See "Error Messages" below. |
| ExecutionTime | Long          | Indicates the time it took for the server to generate the response (in ms).             |
| ResponseData  | TrafficStatus | Contains the actual response data from the service. See "Response Data" below.          |

### Response Data

| Name         | Data Type | Description                                    |
|--------------|-----------|------------------------------------------------|
| TrafficTypes | List      | A TrafficType object for each type of traffic. |

### TrafficType

| Name            | Data Type | Description                                                                                                                                                                                            |
|-----------------|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Name            | String    | Name of the traffic type: "Tunnelbana", "Pendeltåg", etc.                                                                                                                                              |
| Type            | String    | "metro", "train", "local", "tram", "bus" or "fer". fer = Boat, local = Local train, tram = Tram                                                                                                        |
| StatusIcon      | String    | Assistive information indicating which icon to display on the web. Possible values: EventMajor: "Closed", EventMinor: "Major impact", EventGood: "No major disruptions", EventPlanned: "Planned event" |
| Expanded        | Boolean   | Assistive information indicating whether the information has high priority or not.                                                                                                                     |
| HasPlannedEvent | Boolean   | Assistive information indicating whether there are planned events.                                                                                                                                     |
| Events          | List      | A TrafficEvent object for each event.                                                                                                                                                                  |

### TrafficEvent

| Name                            | Data Type | Description                                                                                                                                |
|---------------------------------|-----------|--------------------------------------------------------------------------------------------------------------------------------------------|
| EventId                         | Integer   | Event number.                                                                                                                              |
| Message                         | String    | Message regarding the disruption/event.                                                                                                    |
| Expanded                        | Boolean   | Assistive information indicating whether the information has high priority or not.                                                         |
| Planned                         | Boolean   | Assistive information indicating whether the event is planned or not.                                                                      |
| SortIndex                       | Integer   | Sorting order of the event.                                                                                                                |
| StatusIcon                      | String    | Assistive information indicating which icon to display on the web.                                                                         |
| LineNumbers                     | String    | Line numbers affected by the event, a comma-separated string e.g., "177, 69K, 508".                                                        |
| LineNumbers/InputDataIsOptional | Boolean   | Always set to True, indicating that line numbers are optional.                                                                             |
| TrafficLine                     | String    | Name of the line affected by the event. May be absent if the event affects the entire traffic type or if lines do not exist (e.g., buses). |
| EventInfoUrl                    | String    | Link to storningsinformation.sl.se, or to a specific page with information about the event.                                                |

### Error Messages

No error messages are available at this time.

## Support

If the documentation is not sufficient, please [search among the hundreds of posts on our support forum](https://kundo.se/org/trafiklabse/posts/). It is likely
that someone has already encountered and solved the same problem you have. If you still cannot find an answer to your
question, [post your own thread on the forum](https://kundo.se/org/trafiklabse/) and we will assist you.
