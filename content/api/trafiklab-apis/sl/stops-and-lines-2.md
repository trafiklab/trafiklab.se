---
title: SL Stops and lines v2.0 (Hållplatser och linjer 2)
weight: "400"
date: 2015-03-02
aliases:
  - "/api/sl-hallplatser-och-linjer-2"
  - "/api/sl-hallplatser-och-linjer-2/documentation"
  - "/api/sl-hallplatser-och-linjer-2/nivaer"
  - "/api/sl-hallplatser-och-linjer-2/console"
  - "/node/13609"
  - "/node/13609/documentation"
  - "/node/13609/nivaer"
  - "/node/13609/console"

---

# List of Stops and Lines in Stockholm County

To describe traffic information consistently, it is necessary that the terms and definitions used are clear and precise. The key concepts for this service are
presented below.

{{% error %}}
This API will be shut down at the end of March 2024. It is replaced by [SL's new network API](sl-network.md).
{{% /error %}}

## Concepts

| Concept                   | Description                                                                                                                      |
|---------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| Site                      | A Site is a grouping of StopAreas used to simplify searching in the journey planner.                                             |
| StopArea                  | A StopArea is a grouping of StopPoints with the same traffic type and name within a defined geographic area, such as a terminal. |
| StopPoint                 | A StopPoint is a stopping point and is part of a StopArea                                                                        |
| Line                      | Line advertised to the traveler                                                                                                  |
| JourneyPattern            | A unique route for a line                                                                                                        |
| JourneyPatternPointOnLine | Contains all stopping points served by a particular line                                                                         |
| Transportmode             | Traffic type                                                                                                                     |

## API

### Access

URLs for calls are specified below:

- Production: `https://api.sl.se/api2/LineData.xml?model=[model]&key=[key]`
- Production (JSON): `https://api.sl.se/api2/LineData.json?model=[model]&key=[key]`

Note that it is the extension in the call that determines the formatting of the response.

### API Keys, Authorization

API keys can be obtained through the Trafficlab developer portal.

An API key should be used in the URL for an API call.

- Example: `https://api.sl.se/api2/LineData.xml?model=[model]&key=[key]`

#### Key Levels

| Level  | Max calls/minute | Max calls/month |
|--------|------------------|-----------------|
| Bronze | 5                | 500             |

### Format

The API supports XML and JSON data formatting.

Desired formatting is specified in the URL for an API call.

- Example: `api.sl.se/api2/LineData.xml?model=[model]&key=[key]`

## Data Types

All data types are always represented in string form for their respective formats.

The type specified in model descriptions only indicates a suitable data type to convert the value to in a given programming language.

| Type | Example | Description                                                                                                                                        |
|------|---------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| Int  | 123     | All data types are always represented in string form. However, they can be converted to the Int data type if the programming language supports it. |

## Data Filtering

For the line and jour models, it is desirable to distinguish the traffic type to which the data refers. This can be accomplished by including the optional
parameter DefaultTransportModeCode, which can contain any of the TransportMode values returned by a call to the transportmode model, such as "BUS" or "METRO".

Examples:

`https://api.sl.se/api2/linedata.xml?key=[key]&model=line&DefaultTransportModeCode=METRO`
`https://api.sl.se/api2/linedata.xml?key=[key]&model=jour&DefaultTransportModeCode=BUS`

## Character Encoding

UTF-8 is used for both XML and JSON.

## Performance

Since calls return a relatively large amount of data, it is strongly recommended that the call includes the following HEADER parameter to enable GZIP
compression in the response.

| Key             | Value         |
|-----------------|---------------|
| Accept-Encoding | gzip, deflate |

## Update Frequency

The API portal updates data once per day between 0:00-2:00 every day.

## API Model

Calls to [https://api.sl.se/api2/LineData](https://api.sl.se/api2/LineData) always return an API model (base model), regardless of the specific data model
requested in the call.

| Key           | Type   | Example                 | Description                                                                                                                  |
|---------------|--------|-------------------------|------------------------------------------------------------------------------------------------------------------------------|
| StatusCode    | Int    | 0                       | 0 if the call was successful, otherwise an error code that cannot be fixed via, for example, a modified call                 |
| ExecutionTime | Int    | 282                     | Number of milliseconds it took to generate a response on the server                                                          |
| ResponseData  | Object |                         | Container object containing attributes and data                                                                              |
| Version       | String | 2014-06-27 14:03:39.103 | Last modified. Normally only updated once per day                                                                            |
| Type          | String | DataModelType           | Indicates the type of data model that the response contains: Site, StopPoint, Line, JourneyPatternPointOfLine, TransportMode |

### API Model

{{% tabs %}} {{% tab "Json" %}}

```json
{
  "StatusCode": 0,
  "ExecutionTime": 282,
  "ResponseData": {
    "Version": "2014-10-09 01:05",
    "Type": "DataModelType",
    "Result": [
      /* DataModel, ..., DataModel */
    ]
  }
}
```

{{% /tab %}} {{% tab "Xml" %}}

```xml
<ResponseOfPwsResult xmlns:xsd="https://www.w3.org/2001/XMLSchema" xmlns:xsi="https://www.w3.org/2001/XMLSchema-instance">
    <StatusCode>0</StatusCode>
    <ExecutionTime>267</ExecutionTime>
    <ResponseData>
        <Version xmlns="https://api.sl.se/api/pws">2014-10-09 01:05</Version>
        <Type xmlns="https://api.sl.se/api/pws">DataModelType</Type>
        <!-- DataModel></DataModel -->
        <!-- ... -->
        <!-- <DataModel></DataModel -->
    </ResponseData>
</ResponseOfPwsResult>
```

{{% /tab %}} {{% /tabs %}}

# Specification for Data Models

The API provides the following data models:

| Key   | Value    | Description                                              |
|-------|----------|----------------------------------------------------------|
| model | **site** | Returns response with a Site object                      |
| model | **stop** | Returns response with a StopPoint object                 |
| model | **line** | Returns response with a Line object                      |
| model | **jour** | Returns response with a JourneyPatternPointOnLine object |
| model | **tran** | Returns response with a TransportMode object             |

The desired data model is specified in the URL for an API call.

`api.sl.se/api2/LineData.xml?model=[model]&key=[key]`

## Example

`https://api.sl.se/api2/LineData.xml?model=site`

## Site

### Description

Site is a grouping of StopAreas used to simplify the search in the trip planner.

### Properties

| Property                | Convertible to | Example                 | Description                                  |
|-------------------------|----------------|-------------------------|----------------------------------------------|
| SiteId                  | Int            | 1002                    | Unique identification number for a Site      |
| SiteName                | String         | Centralen               | Name of the area                             |
| StopAreaNumber          | Int            | 1051                    | Unique identification number for a stop area |
| LastModifiedUtcDateTime | DateTime       | 2014-06-27 14:03:39.103 | Last modified                                |
| ExistsFromDate          | DateTime       | 2014-06-28 00:00:00.000 | Effective from date                          |

### Object Structure

{{% tabs %}} {{% tab "Json" %}}

```json
{
  "SiteId": "1002",
  "SiteName": "Centralen",
  "StopAreaNumber": "1051",
  "LastModifiedUtcDateTime": "2014-06-27 14:03:39.103",
  "ExistsFromDate": "2014-06-28 00:00:00.000"
}
```

{{% /tab %}} {{% tab "Xml" %}}

```xml
<Site xmlns="https://api.sl.se/api/pws">
    <SiteId>1002</SiteId>
    <SiteName>Centralen</SiteName>
    <StopAreaNumber>1051</StopAreaNumber>
    <LastModifiedUtcDateTime>2014-06-27 14:03:39.103</LastModifiedUtcDateTime>
    <ExistsFromDate>2014-06-28 00:00:00.000</ExistsFromDate>
</Site>
```

{{% /tab %}} {{% /tabs %}}

## StopPoint

### Description

StopPoints are part of a StopArea.

### Properties

| Property                   | Convertible to | Example                 | Description                                                                        |
|----------------------------|----------------|-------------------------|------------------------------------------------------------------------------------|
| StopPointNumber            | Int            | 1051                    | Unique identification number for a stop point                                      |
| StopPointName              | String         | T-Centralen             | Name of the stop point                                                             |
| StopAreaNumber             | Int            | 1051                    | Number for StopArea; a stop point belongs to only one StopArea                     |
| LocationNorthingCoordinate | Double         | 59.3313179695028        | Coordinate in WGS84 format                                                         |
| LocationEastingCoordinate  | Double         | 18.0616773959365        | Coordinate in WGS84 format                                                         |
| ZoneShortName              | String         | A                       | Fare zone; A, B, or C. If SL's fare does not apply, the zone is null               |
| StopAreaTypeCode           | String         | METROSTN                | Use of the stop point. BUSSTERM, TRAMSTN, METROSTN, RAILWSTN, SHIPBER, or FERRYBER |
| LastModifiedUtcDateTime    | DateTime       | 2014-06-03 00:00:00.000 | Last modified                                                                      |
| ExistsFromDate             | DateTime       | 2014-06-03 00:00:00.000 | Effective from date                                                                |

### Object Structure

{{% tabs %}} {{% tab "Json" %}}

```json
{
  "StopPointNumber": "1051",
  "StopPointName": "T-Centralen",
  "StopAreaNumber": "1051",
  "LocationNorthingCoordinate": "59.3313179695028",
  "LocationEastingCoordinate": "18.0616773959365",
  "ZoneShortName": "A",
  "StopAreaTypeCode": "METROSTN",
  "LastModifiedUtcDateTime": "2014-06-03 00:00:00.000",
  "ExistsFromDate": "2014-06-03 00:00:00.000"
}

```

{{% /tab %}} {{% tab "Xml" %}}

```xml
<StopPoint xmlns="https://api.sl.se/api/pws">
    <StopPointNumber>1051</StopPointNumber>
    <StopPointName>T-Centralen</StopPointName>
    <StopAreaNumber>1051</StopAreaNumber>
    <LocationNorthingCoordinate>59.3313179695028</LocationNorthingCoordinate>
    <LocationEastingCoordinate>18.0616773959365</LocationEastingCoordinate>
    <ZoneShortName>A</ZoneShortName>
    <StopAreaTypeCode>METROSTN</StopAreaTypeCode>
    <LastModifiedUtcDateTime>2014-06-03 00:00:00.000</LastModifiedUtcDateTime>
    <ExistsFromDate>2014-06-03 00:00:00.000</ExistsFromDate>
</StopPoint>
```

{{% /tab %}} {{% /tabs %}}

## Line

### Description

Returns a description of a line, including references to transport modes.

### Properties

| Property                 | Convertible to | Example                 | Description                             |
|--------------------------|----------------|-------------------------|-----------------------------------------|
| LineNumber               | Int            | 3                       | Unique identification number for a line |
| LineDesignation          | String         | 3                       | Line designation                        |
| DefaultTransportMode     | String         | blåbuss                 | Grouping of lines for presentation      |
| DefaultTransportModeCode | String         | BUS                     | Transport mode                          |
| LastModifiedUtcDateTime  | DateTime       | 2007-08-24 00:00:00.000 | Last modified                           |
| ExistsFromDate           | DateTime       | 2007-08-24 00:00:00.000 | Effective from date                     |

### Object Structure

{{% tabs %}} {{% tab "Json" %}}

```json
{
  "LineNumber": "3",
  "LineDesignation": "3",
  "DefaultTransportMode": "blåbuss",
  "DefaultTransportModeCode": "BUS",
  "LastModifiedUtcDateTime": "2007-08-24 00:00:00.000",
  "ExistsFromDate": "2007-08-24 00:00:00.000"
}
```

{{% /tab %}} {{% tab "Xml" %}}

```xml
<Line xmlns="https://api.sl.se/api/pws">
    <LineNumber>3</LineNumber>
    <LineDesignation>3</LineDesignation>
    <DefaultTransportMode>blåbuss</DefaultTransportMode>
    <DefaultTransportModeCode>BUS</DefaultTransportModeCode>
    <LastModifiedUtcDateTime>2007-08-24 00:00:00.000</LastModifiedUtcDateTime>
    <ExistsFromDate>2007-08-24 00:00:00.000</ExistsFromDate>
</Line>
```

{{% /tab %}} {{% /tabs %}}

## JourneyPatternPointOnLine

### Description

Returns the connection between a stop point and a line, including all stop points served by a specific line.

### Properties

| Property                  | Convertible to | Example                 | Description                                   |
|---------------------------|----------------|-------------------------|-----------------------------------------------|
| LineNumber                | Int            | 1                       | Unique identification number for a line       |
| DirectionCode             | Int            | 1                       | Line direction                                |
| JourneyPatternPointNumber | Int            | 10008                   | Unique identification number for a stop point |
| LastModifiedUtcDateTime   | DateTime       | 2012-06-23 00:00:00.000 | Last modified                                 |
| ExistsFromDate            | DateTime       | 2012-06-23 00:00:00.000 | Effective from date                           |

### Object Structure

{{% tabs %}} {{% tab "Json" %}}

```json
{
  "LineNumber": "1",
  "DirectionCode": "1",
  "JourneyPatternPointNumber": "10008",
  "LastModifiedUtcDateTime": "2012-06-23 00:00:00.000",
  "ExistsFromDate": "2012-06-23 00:00:00.000"
}
```

{{% /tab %}} {{% tab "Xml" %}}

```xml
<JourneyPatternPointOnLine xmlns="https://api.sl.se/api/pws">
    <LineNumber>1</LineNumber>
    <DirectionCode>1</DirectionCode>
    <JourneyPatternPointNumber>10008</JourneyPatternPointNumber>
    <LastModifiedUtcDateTime>2012-06-23 00:00:00.000</LastModifiedUtcDateTime>
    <ExistsFromDate>2012-06-23 00:00:00.000</ExistsFromDate>
</JourneyPatternPointOnLine>
```

{{% /tab %}} {{% /tabs %}}

## TransportMode

### Description

Returns available transport modes. Line data refers to the transport mode through the property DefaultTransportModeCode.

### Relationship between TransportModeCode and StopAreaCode

| DefaultTransportModeCode | StopAreaTypeCode |
|--------------------------|------------------|
| BUS                      | BUSTERM          |
| METRO                    | METROSTN         |
| TRAM                     | TRAMSTN          |
| TRAIN                    | RAILWSTN         |
| SHIP                     | SHIPBER          |
| FERRY                    | FERRYBER         |

### Object Properties

| Property                 | Convertible to | Example                 | Description                    |
|--------------------------|----------------|-------------------------|--------------------------------|
| DefaultTransportModeCode | String         | BUS                     | Unique code for transport mode |
| DefaultTransportMode     | String         | bus                     | Name of the transport mode     |
| StopAreaTypeCode         | String         | BUSTERM                 | Type code for the stop area    |
| LastModifiedUtcDateTime  | DateTime       | 2007-08-24 00:00:00.000 | Last modified                  |
| ExistsFromDate           | DateTime       | 2007-08-24 00:00:00.000 | Effective from date            |

### Object Structure

{{% tabs %}} {{% tab "Json" %}}

```json
{
  "DefaultTransportModeCode": "BUS",
  "DefaultTransportMode": "buss",
  "StopAreaTypeCode": "BUSTERM",
  "LastModifiedUtcDateTime": "2007-08-24 00:00:00.000",
  "ExistsFromDate": "2007-08-24 00:00:00.000"
}
```

{{% /tab %}} {{% tab "Xml" %}}

```xml
<TransportMode xmlns="https://api.sl.se/api/pws">
    <DefaultTransportModeCode>BUS</DefaultTransportModeCode>
    <DefaultTransportMode>buss</DefaultTransportMode>
    <StopAreaTypeCode>BUSTERM</StopAreaTypeCode>
    <LastModifiedUtcDateTime>2007-08-24 00:00:00.000</LastModifiedUtcDateTime>
    <ExistsFromDate>2007-08-24 00:00:00.000</ExistsFromDate>
</TransportMode>
```

{{% /tab %}} {{% /tabs %}}

## Complete Transport Modes Example

{{% tabs %}} {{% tab "Json" %}}

```json
{
  "StatusCode": 0,
  "ExecutionTime": 327,
  "ResponseData": {
    "Version": "2014-10-09 18:05",
    "Type": "TransportMode",
    "Result": [
      {
        "DefaultTransportModeCode": "BUS",
        "DefaultTransportMode": "buss",
        "StopAreaTypeCode": "BUSTERM",
        "LastModifiedUtcDateTime": "2007-08-24 00:00:00.000",
        "ExistsFromDate": "2007-08-24 00:00:00.000"
      }
      // ... other TransportMode examples ...
    ]
  }
}
```

{{% /tab %}} {{% tab "Xml" %}}

```xml

<ResponseOfPwsResult xmlns:xsd="https://www.w3.org/2001/XMLSchema" xmlns:xsi="https://www.w3.org/2001/XMLSchema-instance">
    <StatusCode>0</StatusCode>
    <ExecutionTime>277</ExecutionTime>
    <ResponseData>
        <Version xmlns="https://api.sl.se/api/pws">2014-10-09 18:05</Version>
        <Type xmlns="https://api.sl.se/api/pws">TransportMode</Type>
        <TransportMode xmlns="https://api.sl.se/api/pws">
            <DefaultTransportModeCode>BUS</DefaultTransportModeCode>
            <DefaultTransportMode>buss</DefaultTransportMode>
            <StopAreaTypeCode>BUSTERM</StopAreaTypeCode>
            <LastModifiedUtcDateTime>2007-08-24 00:00:00.000</LastModifiedUtcDateTime>
            <ExistsFromDate>2007-08-24 00:00:00.000</ExistsFromDate>
        </TransportMode>
        <TransportMode xmlns="https://api.sl.se/api/pws">
            <DefaultTransportModeCode>FERRY</DefaultTransportModeCode>
            <DefaultTransportMode>färja</DefaultTransportMode>
            <StopAreaTypeCode>FERRYBER</StopAreaTypeCode>
            <LastModifiedUtcDateTime>2007-08-24 00:00:00.000</LastModifiedUtcDateTime>
            <ExistsFromDate>2007-08-24 00:00:00.000</ExistsFromDate>
        </TransportMode>
        <!-- ... other TransportMode examples ... -->
    </ResponseData>
</ResponseOfPwsResult>
```

{{% /tab %}} {{% /tabs %}}

## Support

If you need more help you can [search through the hundreds of posts on our support forum](http://kundo.se/org/trafiklabse/posts/). It's likely that someone has
already encountered and solved the same problem you have.

If you still can't find the answer to your question, [please write a new post on the forum,](http://kundo.se/org/trafiklabse/) and we will assist you.
