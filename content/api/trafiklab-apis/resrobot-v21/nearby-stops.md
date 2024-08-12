---
title: ResRobot Nearby stops 
weight: 31 
date: 2022-02-07
aliases:
  - /api/trafiklab-apis/resrobot-v2/nearby-stops/
---

## What does this API provide?

ResRobot nearby stops provides information about stops, including their ids and position, by searching for a certain
pair of coordinates.

{{% info %}} Instead of using the station lookup endpoint, you can also use the stops.txt file from GTFS Sverige 2. This
way you can provide autocomplete and other search functions without internet access. It will make your application more
responsive and more reliable as you don't have to wait for API responses.
See [Combining data and APIs](/docs/using-trafiklab-data/combining-data/) for more information. {{% /info %}}

{{% warning %}} Be aware that the current position of for example a smartphone user is personal data. We do not save
this data, but it might be stored for a short time in for example log files. You should probably inform your users and
ask for permission before sending their position to 3rd parties.
{{% /warning %}}

### Data format

The data is formatted as JSON or XML, depending on the `format` query parameter.

### Updates

The static data used for this API is updated when changes are made, at most once per day.

### Operators covered by this dataset

All operators which operate in Sweden are covered by the ResRobot APIs.

### Breaking changes

This API has the **stable** status. When breaking changes are made, we strive to have a 6 months transition period for
users to update their implementations. Examples of breaking changes are the changes to existing fields or query
parameters, or in case new query parameters are required to keep the results the same. The addition of new fields isn't
considered a breaking change, and can happen without warning.

## Using ResRobot Nearby stops

ResRobot Nearby stops takes the search string and the wanted number of results as parameters, and returns a list of
matching stations with their location, name and id. Users can choose between exact matching and approximate matching by
adding a question mark to the end of the search string.

{{% info %}} Only the most important parameters and response variables are described on this page. Looking for more
technical details? These can be found in [the OpenAPI specification](api-spec.md). {{% /info %}}

## Example calls

### Call

{{% tabs %}} {{% tab "Json" %}}

```text
https://api.resrobot.se/v2.1/location.nearbystops?originCoordLat=57.708895&originCoordLong=11.973479&format=json&accessId=API_KEY
```

{{% /tab %}}

{{% tab "Xml" %}}

```text
https://api.resrobot.se/v2.1/location.nearbystops?originCoordLat=57.708895&originCoordLong=11.973479&format=xml&accessId=API_KEY
```

{{% /tab %}} {{% /tabs %}}

#### Request parameters

{{% note %}}
**Changes compared to ResRobot v2.0:**

- The `key` parameter has been renamed to `accessId`.

{{% /note %}}

| **Name**        | **Type** | **Required** | **Description**                                                                                              |
|-----------------|----------|--------------|--------------------------------------------------------------------------------------------------------------|
| accessId        | String   | Yes          | Your API key                                                                                                 |
| originCoordLat  | String   | Yes          | Latitude (WGS84, decimal degree), eg 59.293611                                                               |
| originCoordLong | String   | Yes          | Longitude (WGS84, decimal degree), eg 18.083056                                                              |
| maxNo           | Integer  | No           | The maximum number of results to return, default 10, maximum 1000                                            |
| r               | Integer  | No           | Maximum distance between given coordinates and the stop. Default 1000, max 10000                             |
| lang            | String   | No           | Language (sv/en/de), default sv. Affects both data (names for different transport types) and error messages. |
| format          | String   | No           | Json or Xml                                                                                                  |


### Response

{{% tabs %}} {{% tab "Json" %}}

```json
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


#### Data fields

{{% note %}}
**Changes compared to ResRobot v2.0:**

- The root object now contains an array of `stopLocationOrCoordLocation` instead of an array of `stopLocation`.
- `stopLocation` can now be found in the items present in the `stopLocationOrCoordLocation` array.
- The `products` field has been replaced with an array of Products. Instead of accessing the sum of all products through `products`, you can now obtain all the individual products through `ProductAtStop[].cls`
- `timezoneOffset` has been added to each `StopLocation`.

{{% /note %}}


| **Name**     | **Data type**               | **Description**                                                                                                                                                                                                                                                         |
| ------------ | --------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| stopLocationOrCoordLocation | stopLocationOrCoordLocation[] | List with results                                                                                                                                                                                                          |
| stopLocationOrCoordLocation.StopLocation | StopLocation | Actual data is contained in the `StopLocation` property                                                                                                                                                                                                          |
| StopLocation | Object                      | Object containing a single stop                                                                                                                                                                                                                                                                        |
| StopLocation.name         | String                      | Stop name                                                                                                                                                                                                                                                     |
| StopLocation.extId        | String                      | Stop id for use in other ResRobot APIs.                                                                                                                                                                                                                                    |
| StopLocation.id           | String                      | Internal id. Do not use.                                                              |
| StopLocation.dist         | Integer                     | Distance from the queried coordinates, in meters.                                                                                                                                                                                                                      |
| StopLocation.lat          | String                      | Latitude (WGS84, decimal degree) for this stop, eg 59.293611                                                                                                                                                                                                                           |
| StopLocation.lon          | String                      | Longitude (WGS84, decimal degree) for this stop, eg 18.083056                                                                                                                                                                                                                          |
| StopLocation.productAtStop     | Product[]              | See [common data types](common.md). Only the `cls` field of each product will contain actual data.  |
| StopLocation.weight       | Integer                     | Shows how much traffic is handled at this stop, a stop with more traffic gets a higher weight. Between 0 and 32767.              |
