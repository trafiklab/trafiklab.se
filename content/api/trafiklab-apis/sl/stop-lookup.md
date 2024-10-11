---
title: SL Stop lookup
weight: 200
date: 2014-03-14
aliases:
  - /api/sl-platsuppslag
  - /api/sl-platsuppslag/dokumentation
  - /api/sl-platsuppslag/nivaer
  - /api/sl-platsuppslag/konsol
  - /node/12617
  - /node/12617/dokumentation
  - /node/12617/nivaer
  - /node/12617/konsol

---

## Description

Using this API, you can retrieve information regarding SLs stops by providing a part of the name of a stop. You can opt to only search for stops, or to search
for both stops, addresses and places.

## Format

Json or xml, as specified in the API request.

## Request

### URL

`https://journeyplanner.integration.sl.se/v1/typeahead.<FORMAT>?key=TRAFIKLAB-SLAPI-INTEGRATION-2024&searchstring=<QUERY>`

{{% warning %}}
The old URL `https://api.sl.se/api2/typeahead.<FORMAT>?key=TRAFIKLAB-SLAPI-INTEGRATION-2024&searchstring=<QUERY>` has changed on November 16th, and will stop working on March 15th.
Query parameters, response bodies and API keys remain unchanged.
{{% /warning %}}

### Parameters

The following parameters can be provided in the query string:

| **Name**     | **Type** | **Required** | **Description**                                                                                                                                                                                                                          |
|--------------|----------|--------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Key          | String   | Yes          | The API key, `TRAFIKLAB-SLAPI-INTEGRATION-2024` for new users or projects since oktober 1st 2024.                                                                                                                                        |
| SearchString | String   | Yes          | The search query, limited to 20 characters.                                                                                                                                                                                              |
| StationsOnly | Boolean  | No           | Whether to search for stations only, or to even include addresses and places. `true` in order to only search stops. `true` by default.                                                                                                   |
| MaxResults   | Integer  | No           | The maximum number of result to return. Between 1 and 50, default 10.                                                                                                                                                                    |
| type         | String   | No           | Type filter for stops: <ul><li>S: Stations only <li>P: Points of interests (POI) only <li>A: Addresses only <li>SP: Stations and POIs <li>SA: Stations and addresses <li>AP: Addresses and POI <li>ALL: Stations, Addresses and POI</ul> |

### Example call

{{% tabs %}} {{% tab "Json" %}}

```text
https://journeyplanner.integration.sl.se/v1/typeahead.json?searchstring=Oden&stationsonly=true&maxresults=5&key=TRAFIKLAB-SLAPI-INTEGRATION-2024
```

{{% /tab %}} {{% tab "Xml" %}}

```text
https://journeyplanner.integration.sl.se/v1/typeahead.xml?searchstring=Oden&stationsonly=true&maxresults=5&key=TRAFIKLAB-SLAPI-INTEGRATION-2024
```

{{% /tab %}} {{% /tabs %}}

## Results

### Response structure

| **Name**      | **Type** | **Description**                                                                  |
|---------------|----------|----------------------------------------------------------------------------------|
| StatusCode    | Integer  | Contains a status code corresponding to the possible message                     |
| Message       | String   | Contain error messages in case something went wrong. See "Error messages" below. |
| ExecutionTime | Long     | How long time the server needed to generate the response, in milliseconds.       |
| ResponseData  | Sites    | The actual response                                                              |

#### Sites

| **Name** | **Type** | **Description**            |
|----------|----------|----------------------------|
| Sites    | List     | A list of all found sites. |

### Site

| **Name** | **Type** | **Description**                                                    |
|----------|----------|--------------------------------------------------------------------|
| Name     | String   | The name of the stop                                               |
| SiteId   | Integer  | The id of the stop area.                                           |
| Type     | String   | The place type: ”Station”, ”Address” or ”Poi” (Point of interest). |
| X        | String   | X-coordinate in SWEREF format.                                     |
| Y        | String   | Y-coordinate in SWEREF format.                                     |

{{% note %}}
**SL Stop Lookup in combination with other APIs**

The SiteId value returned by the SL Stop lookup API matches the SiteId value expected by the SL Routeplanner 3.1 API. These values changed in february but do
still match each other (given that both APIs are accessed through the integration.sl.se domain).

In order to use values returned by the SL Stop Lookup API in combination with the SL Transport API, you should convert the values returned by the SL Stop Lookup
API, in the form of `3BA1CDEFG`, into a number `ABCDEFG`. It is however recommended to use the site ids returned by the Transport Api `/sites` endpoint if
possible instead of combining APIs.
{{% /note %}}

### Example response

{{% tabs %}} {{% tab "Json" %}}

```json
{
  "StatusCode": 0,
  "Message": null,
  "ExecutionTime": 0,
  "ResponseData": [
    {
      "Name": "Odenplan (Stockholm)",
      "SiteId": "300109117",
      "Type": "Station",
      "X": "18049099",
      "Y": "59342901",
      "Products": null
    },
    {
      "Name": "Odengatan/Valhallavägen (Stockholm)",
      "SiteId": "300101082",
      "Type": "Station",
      "X": "18065891",
      "Y": "59346622",
      "Products": null
    },
    {
      "Name": "Stockholm Odenplan (Stockholm)",
      "SiteId": "300101079",
      "Type": "Station",
      "X": "18045683",
      "Y": "59343116",
      "Products": null
    },
    {
      "Name": "Odengatan/Sveavägen (Stockholm)",
      "SiteId": "300101030",
      "Type": "Station",
      "X": "18055311",
      "Y": "59344294",
      "Products": null
    },
    {
      "Name": "Odenvägen (Lidingö)",
      "SiteId": "300102059",
      "Type": "Station",
      "X": "18133795",
      "Y": "59367396",
      "Products": null
    }
  ]
}
```

{{% /tab %}} {{% tab "Xml" %}}

```xml
<?xml version="1.0" encoding="utf-8"?>
<ResponseOfListOfSite xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
    <StatusCode>0</StatusCode>
    <ExecutionTime>0</ExecutionTime>
    <ResponseData>
        <Site>
            <Name>Odenplan (Stockholm)</Name>
            <SiteId>300109117</SiteId>
            <Type>Station</Type>
            <X>18049099</X>
            <Y>59342901</Y>
        </Site>
        <Site>
            <Name>Odengatan/Valhallavägen (Stockholm)</Name>
            <SiteId>300101082</SiteId>
            <Type>Station</Type>
            <X>18065891</X>
            <Y>59346622</Y>
        </Site>
        <Site>
            <Name>Stockholm Odenplan (Stockholm)</Name>
            <SiteId>300101079</SiteId>
            <Type>Station</Type>
            <X>18045683</X>
            <Y>59343116</Y>
        </Site>
        <Site>
            <Name>Odengatan/Sveavägen (Stockholm)</Name>
            <SiteId>300101030</SiteId>
            <Type>Station</Type>
            <X>18055311</X>
            <Y>59344294</Y>
        </Site>
        <Site>
            <Name>Odenvägen (Lidingö)</Name>
            <SiteId>300102059</SiteId>
            <Type>Station</Type>
            <X>18133795</X>
            <Y>59367396</Y>
        </Site>
    </ResponseData>
</ResponseOfListOfSite>
```

{{% /tab %}} {{% /tabs %}}

## Support

If you need more help you can search through [existing questions on our support forum](http://kundo.se/org/trafiklabse/posts/). If you don't find the answer to
your question their, you can create your own post and we'll try to help you as soon as possible.