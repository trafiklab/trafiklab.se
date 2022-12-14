---
title: Trafikverket Open API 
layout: "single"
weight: 90 
summary: Up-to-date information from Trafikverket, regarding both rail and road traffic.
date: 06-02-2014
aliases:
  - /api/trafikverket-oppet-api
  - /api/trafikverket-oppet-api/documentation
  - /api/trafikverket-oppet-api/licens
  - /node/12475
  - /node/12475/documentation
  - /node/12475/licens
---


### What is Trafikverkets open API?

Trafikverkets open API is an API to fetch information regarding road and rail traffic.

### How do I use Trafikverkets open API?

A valid API key is required. This key can be obtained from the [Trafiklab developer portal](https://developer.trafiklab.se).

This API has multiple versions, all using the same API key. You should use the latest available endpoint, but can keep using earlier ones if you have an existing application.

{{% tabs %}} {{% tab "Json" %}}

```text
https://api.trafikinfo.trafikverket.se/v2/data.json
```

{{% /tab %}}

{{% tab "Xml" %}}

```text
https://api.trafikinfo.trafikverket.se/v2/data.xml
```

{{% /tab %}} {{% /tabs %}}

You can use Trafikverkets open API by sending a POST-request, which describes which data you'd like to request, along with optional filters. The data is returned in JSON or XML format, depending on the suffix provided in the request.

A request can look like this:
```xml
<REQUEST>
  <LOGIN authenticationkey="YourTrafiklabKey" />
  <QUERY objecttype="SomeObjectType" schemaversion="SomeObjectVersion" limit="10">
  <FILTER>
    <EQ name="SomeDataField" value="2" />
  </FILTER>
  </QUERY>
</REQUEST>
```

{{% info %}}
If there is no value for a requested field, the field will not be included in the response
{{% /info %}}

The following data types are available:

| Data type | Description |
|-----------|-------------|
| TrainMessage | Messages related to works on railroads, technical problems, and similar. |
| TrainStation | Stop places, not only for passengers but also for cargo and borders |
| TrainAnnouncement | Timetable information, in other words, information regarding trains at stops or stations. Does not include cargo trains |
| Icon | Icons for use on maps or user interfaces |
| RoadCondition | Road status |
| RoadConditionOverview | Overview of road status |
| Situation | Describes actual situations on the road, such as incidents and disturbances of normal traffic. Examples are important information, roadworks, accidents, traffic jams, events, changed ferry times, _kolonnkörning_ (driving behind e.g. snow plows). |
| WeatherStation | Reports from roadside weather stations |

### Coordinates

This API uses the Swedish national coordinate system SWEREF 99 TM. All geometric data is also published in WGS 84. [Read more about how to convert SWEREF 99](/docs/using-trafiklab-data/combining-data/converting-sweref99-to-wgs84.md).

## Detailed documentation

Complete and updated documentation is available at [Trafikverkets website](https://api.trafikinfo.trafikverket.se/), and contains for instance

- more information about constructing requests
- more information about response data structures
- error messages
- example code
- an interactive console for testing

Note that you, as a Trafiklab member, **don't** have to register on Trafikverkets website, as you can fetch your API key directly through Trafiklab.

Trafikverkets documentation can be found here: [https://api.trafikinfo.trafikverket.se/](https://api.trafikinfo.trafikverket.se/)


