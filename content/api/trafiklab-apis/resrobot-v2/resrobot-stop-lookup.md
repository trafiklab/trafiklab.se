---
title: ResRobot Stop lookup
aliases: /api/trafiklab-apis/resrobot-reseplanerare/platsuppslag
weight: 30
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

This dataset has the **stable** status. This means that we will communicate when fields are added, or changed. When
breaking changes are made, you will get three months or more to update your implementations.

## Using ResRobot Stop lookup

ResRobot Stop lookup takes the search string and the wanted number of results as parameters, and returns a list of
matching stations with their location, name and id. Users can choose between exact matching and approximate matching by
adding a question mark to the end of the search string.

{{% info %}}
Only the most important parameters and response variables are described on this page. Looking for more technical
details? These can be found in [the OpenAPI specification](resrobot-spec.md).
{{% /info %}}

{{% info %}} Instead of using the station lookup endpoint, you can also use the stops.txt file from GTFS
Sverige 2. This way you can provide autocomplete and other search functions without internet access. It will make your
application more responsive and more reliable as you don't have to wait for API responses.
See [Combining data and APIs](../../transport-data-formats/combining-data/) for more information. {{% /info %}}

## Example calls

### Exact search

Exact search returns only stations that match exactly with the search string.

#### Call

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

#### Response

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

### Fuzzy search

By adding a question mark to the query string, fuzzy matching is used instead of exact matching. This will return
stations which name is an exact or near match to the input string.

#### Call

{{% tabs %}} {{% tab "Json" %}}

```text
https://api.resrobot.se/v2/location.name?input=Göteborg?&format=json&key=API_KEY
```

{{% /tab %}}

{{% tab "Xml" %}}

```text
https://api.resrobot.se/v2/location.name?input=Göteborg?&format=xml&key=API_KEY
```

{{% /tab %}} {{% /tabs %}}

#### Response

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
    },
    {
      "id": "740000002",
      "extId": "740000002",
      "name": "Göteborg Centralstation",
      "lon": 11.973479,
      "lat": 57.708895,
      "weight": 17428,
      "products": 182
    },
    {
      "id": "740098526",
      "extId": "740098526",
      "name": "GÖTEBORG GAMLESTADEN",
      "lon": 12.004411,
      "lat": 57.729148,
      "weight": 16810,
      "products": 112
    },
    {
      "id": "740016365",
      "extId": "740016365",
      "name": "Göteborg Sävenäs lokstation",
      "lon": 12.021077,
      "lat": 57.725993,
      "weight": 13,
      "products": 128
    },
    {
      "id": "740025610",
      "extId": "740025610",
      "name": "Göteborg Berzeliigatan",
      "lon": 11.981884,
      "lat": 57.698504,
      "weight": 4917,
      "products": 200
    },
    {
      "id": "740015578",
      "extId": "740015578",
      "name": "Göteborg Korsvägen",
      "lon": 11.986909,
      "lat": 57.696625,
      "weight": 4917,
      "products": 200
    },
    {
      "id": "740016358",
      "extId": "740016358",
      "name": "Göteborg Kungsportsplatsen",
      "lon": 11.969748,
      "lat": 57.704023,
      "weight": 4917,
      "products": 200
    },
    {
      "id": "740072430",
      "extId": "740072430",
      "name": "Göteborg Stenpiren",
      "lon": 11.957424,
      "lat": 57.705803,
      "weight": 4669,
      "products": 448
    },
    {
      "id": "740025609",
      "extId": "740025609",
      "name": "Göteborg Bellevue",
      "lon": 12.023477,
      "lat": 57.732456,
      "weight": 4488,
      "products": 192
    },
    {
      "id": "740020752",
      "extId": "740020752",
      "name": "Göteborg Brunnsparken",
      "lon": 11.967843,
      "lat": 57.706945,
      "weight": 4488,
      "products": 192
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
    <StopLocation id="740000002" extId="740000002" name="Göteborg Centralstation" lon="11.973479" lat="57.708895" weight="17428" products="182"/>
    <StopLocation id="740098526" extId="740098526" name="GÖTEBORG GAMLESTADEN" lon="12.004411" lat="57.729148" weight="16810" products="112"/>
    <StopLocation id="740016365" extId="740016365" name="Göteborg Sävenäs lokstation" lon="12.021077" lat="57.725993" weight="13" products="128"/>
    <StopLocation id="740025610" extId="740025610" name="Göteborg Berzeliigatan" lon="11.981884" lat="57.698504" weight="4917" products="200"/>
    <StopLocation id="740015578" extId="740015578" name="Göteborg Korsvägen" lon="11.986909" lat="57.696625" weight="4917" products="200"/>
    <StopLocation id="740016358" extId="740016358" name="Göteborg Kungsportsplatsen" lon="11.969748" lat="57.704023" weight="4917" products="200"/>
    <StopLocation id="740072430" extId="740072430" name="Göteborg Stenpiren" lon="11.957424" lat="57.705803" weight="4669" products="448"/>
    <StopLocation id="740025609" extId="740025609" name="Göteborg Bellevue" lon="12.023477" lat="57.732456" weight="4488" products="192"/>
    <StopLocation id="740020752" extId="740020752" name="Göteborg Brunnsparken" lon="11.967843" lat="57.706945" weight="4488" products="192"/>
</LocationList>
```

{{% /tab %}} {{% /tabs %}}

###  
