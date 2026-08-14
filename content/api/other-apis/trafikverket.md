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
  - /api/trafiklab-apis/trafikverket/
image: '/media/2024/09/banner_inlandsbanan.jpg'
image_position: 'bottom'
---


## What is Trafikverkets open API?

Trafikverkets open API is an API to fetch information regarding road and rail traffic.

## How do I use Trafikverkets open API?

A valid API key is required. New users must obtain a key through [Trafikverkets own data portal](https://data.trafikverket.se/oauth2/Account/register). Trafiklab no longer issues new keys for this API, but existing Trafiklab-issued keys continue to work.

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

You use Trafikverkets open API by sending a POST-request containing an XML request. The request describes which data you'd like to retrieve, along with optional filters. The API key is passed in the `LOGIN` element as the `authenticationkey` attribute. Do not put a real API key in source code or share it publicly.

The same request body can be sent to either endpoint listed above. The `.json` or `.xml` suffix determines whether the response is returned as JSON or XML. For example, save the XML request below as `request.xml` and run:

```bash
curl --request POST \
  --url https://api.trafikinfo.trafikverket.se/v2/data.json \
  --header 'Content-Type: application/xml' \
  --data-binary @request.xml
```

In the `QUERY` element, `objecttype` selects the data type, `schemaversion` selects the version of that data type, and `limit` restricts the number of returned records. The `FILTER` element is optional; the `EQ` filter in the example limits results to records where `SomeDataField` equals `2`. The available fields, schema versions, filter operators, and response structure are documented for each data type in Trafikverkets documentation.

A request can look like this:
```xml
<REQUEST>
  <LOGIN authenticationkey="YourApiKey" />
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

Complete and updated documentation is available in Trafikverkets [Data Exchange Portal](https://data.trafikverket.se/documentation/datacache/intro). The portal is Trafikverkets central site for documentation about data exchange services and contains, for instance,

- more information about constructing requests
- more information about response data structures
- error messages
- example code
- an interactive console for testing

If you already have a Trafiklab-issued key, you can continue using it. New keys must be obtained through Trafikverkets own data portal.

Trafikverkets documentation can be found here: [https://data.trafikverket.se/documentation/datacache/intro](https://data.trafikverket.se/documentation/datacache/intro)
