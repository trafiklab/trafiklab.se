---
title: ResRobot Stop lookup
aliases: /apis/trafiklab-apis/resrobot-reseplanerare/platsuppslag
weight: 30
date: 2015-06-24
---

## What does this API provide?

ResRobot stop lookup provides information about stops, including their ids and position, by searching based on their
name.

### Data format

The data is formatted as JSON or XML, depending on the `format` query parameter.

### How often is this data updated?

The static data used for this API is updated when changes are made, at most once per day.

### Which operators are covered by this dataset?

All operators which operate in Sweden are covered by the ResRobot APIs.

### How often does the data format changes? Do breaking changes happen?

This API has the **stable** status. When breaking changes are made, you will get six months or more to update your
implementations. Examples of breaking changes are the changes to existing fields or query parameters, or in case new
query parameters are required to keep the results the same. The addition of new fields isn't considered a breaking
change, and can happen without warning.

## Using ResRobot Stop lookup

ResRobot Stop lookup takes the search string and the wanted number of results as parameters, and returns a list of
matching stations with their location, name and id. Users can choose between exact matching and approximate matching by
adding a question mark to the end of the search string.

{{% info %}}
Only the most important parameters and response variables are described on this page. Looking for more technical
details? These can be found in [the OpenAPI specification](api-spec.md).
{{% /info %}}

{{% info %}} Instead of using the station lookup endpoint, you can also use the stops.txt file from GTFS
Sverige 2. This way you can provide autocomplete and other search functions without internet access. It will make your
application more responsive and more reliable as you don't have to wait for API responses.
See [Combining data and APIs](docs/using-trafiklab-data/combining-data/) for more information. {{% /info %}}

## Example

### Call

{{% tabs %}} {{% tab "Json" %}}

```text
https://api.resrobot.se/v2/location.name?input=Göteborg&format=json&key=API_KEY
```

{{% /tab %}}

{{% tab "Xml" %}}

```text
https://api.resrobot.se/v2/location.name?input=Göteborg&format=xml&key=API_KEY
```

{{% /tab %}} {{% /tabs %}}

#### Request parameters

| **Name**        | **Type** | **Required** | **Description**                                                                                                                                    |
| --------------- | ----------- | ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| key             | String      | Yes               | Your API key                                                                                                                                    |
| input           | String      | Yes               | The search string. Append a question mark for fuzzy search.                                                                                                      |
| maxNo           | Integer     | No              | The maximum number of results to return, default 10, maximum 1000                                                                         |
| lang            | String      | No              | Language (sv/en/de), default sv. Affects both data (names for different transport types) and error messages.
| format          | String      | No              | Json or Xml |

{{% info %}}

**Fuzzy search**

By adding a question mark to the query string, fuzzy matching is used instead of exact matching. This will return
stations which name is an exact or near match to the input string.
{{% /info %}}

### Response

{{% tabs %}} {{% tab "Json" %}}

```javascript
{
  "StopLocation": [
    {
      "id": "740098001",
      "extId": "740098001",
      "name": "GÖTEBORG",
      "lon": 11.973479,
      "lat": 57.708895,
      "weight": 22332,
      "products": 254
    }
  ]
}
```

{{% /tab %}}

{{% tab "Xml" %}}

```xml
<?xml version="1.0" encoding="UTF-8"?>
<LocationList xmlns="hafas_rest_v1">
    <StopLocation id="740098001" extId="740098001" name="GÖTEBORG" lon="11.973479" lat="57.708895" weight="22332" products="254"/>
</LocationList>
```

{{% /tab %}} {{% /tabs %}}

{{% info %}} All-caps stations, like GÖTEBORG in the example above, are virtual stations. These are a group
of stations, for example to group stops which are close to eachother or to group several stops serving the same area.
This is especially useful for people who are not familiar with the environment. Instead of having to choose between
several stops which they don't know, they can simply search for trips to "Göteborg". {{% /info %}}



### Response Data fields

| **Name**     | **Data type**               | **Description**                                                                                                                                                                                                                                                         |
| ------------ | --------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| LocationList | StopLocation[]              | List with results                                                                                                                                                                                                          |
| StopLocation | Object                      |                                                                                                                                                                                                                                                                         |
| name         | String                      | Stop name                                                                                                                                                                                                                                                     |
| extId        | String                      | Stop id for use in other ResRobot APIs.                                                                                                                                                                                                                                    |
| id           | String                      | Internal id. Do not use.                                                              |
| dist         | Integer                     | Distance from the queried coordinates, in meters.                                                                                                                                                                                                                      |
| lat          | String                      | Latitude (WGS84, decimal degree) for this stop, eg 59.293611                                                                                                                                                                                                                           |
| lon          | String                      | Longitude (WGS84, decimal degree) for this stop, eg 18.083056                                                                                                                                                                                                                          |
| products     | Integer                     | Transport modes available at thist stop, as a sum of the following values:<br>1 – Flyg<br>2 - Snabbtåg<br>4 - Tåg<br>8 - Expressbuss<br>16 - Lokaltåg<br>32 - Tunnelbana<br>64 – Spårvagn<br>128 – Buss<br>256 – Båt<br>512 – Taxi<br>(160 – Tunnelbana och Buss) |
| weight       | Integer                     | Shows how much traffic is handled at this stop, a stop with more traffic gets a higher weight. Between 0 and 32767.              |
