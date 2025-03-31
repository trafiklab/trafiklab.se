---
title: SL Nearby stops 2
weight: 300
date: 2019-01-14

---

## Description

{{% info %}}
A new version of this API is currently being developed by SL. In order to ensure that the new version fits the needs of
all users and use cases, SL wants to hear from you on what must be included in this new version. Please contact us
at [info@Trafiklab.se](mailto:info@trafiklab.se) to contribute.
{{% /info %}}
Using this API, you can find SL stops near a pair of coordinates.

## URL

`https://journeyplanner.integration.sl.se/v1/nearbystopsv2.<FORMAT>?key=TRAFIKLAB-SLAPI-INTEGRATION-2024&originCoordLat=<LAT>&originCoordLong=<LONG>&maxNo=<MAX ANTAL SVAR>&r=<RADIUS I METER>`

{{% warning %}}
The old
URL `https://api.sl.se/api2/nearbystopsv2.<FORMAT>?key=TRAFIKLAB-SLAPI-INTEGRATION-2024&originCoordLat=<LAT>&originCoordLong=<LONG>&maxNo=<MAX ANTAL SVAR>&r=<RADIUS I METER>` has
changed on December 4rd, and will stop working on March 15th.
Query parameters, response bodies and API keys remain unchanged.
{{% /warning %}}

## Format

Json or xml, as specified in the API request.

## Request

### Parameters

| Namn            | Type    | Required | Description                                                                                                                                                                                                                                                                                                                                  |
|-----------------|---------|----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Key             | String  | Yes      | The API key, `TRAFIKLAB-SLAPI-INTEGRATION-2024` for new users since oktober 1st 2024.                                                                                                                                                                                                                                                        |
| originCoordLat  | String  | Yes      | Latitude                                                                                                                                                                                                                                                                                                                                     |
| originCoordLong | String  | Yes      | Longitude                                                                                                                                                                                                                                                                                                                                    |
| maxNo           | Integer | No       | The desired number of results. Default 9, maximum value 1000.                                                                                                                                                                                                                                                                                |
| r               | Integer | No       | Radius defining how far to search from the given coordinate, in meters. 1000 is default, 2000 is the maximum value..                                                                                                                                                                                                                         |
| products        | Integer | No       | Product filter specifying which stations to include. The value is obtained by summing the desired values: <ul><li>Commuter train (1)</li><li><li>Underground (2)</li><li>Tram and light rail (4)</li><li>Bus (8)</li><li>Boat/Ferry typ (64)</li><li>Nearby traffic (Närtafik) (128)</li></ul>For example, bus and boat results in 8+64 = 72 |
| type            | String  | No       | Type filter for stops: <ul><li>S: Stations only <li>P: Points of interests (POI) only <li>SP: Stations and POIs </ul>                                                                                                                                                                                                                        |

### Example call

{{% tabs %}} {{% tab "Json" %}}

```text
https://journeyplanner.integration.sl.se/v1/nearbystopsv2.json?originCoordLat=59.328284&originCoordLong=18.016154&key=TRAFIKLAB-SLAPI-INTEGRATION-2024
```

{{% /tab %}} {{% tab "Xml" %}}

```text
https://journeyplanner.integration.sl.se/v1/nearbystopsv2.xml?originCoordLat=59.328284&originCoordLong=18.016154&key=TRAFIKLAB-SLAPI-INTEGRATION-2024
```

{{% /tab %}} {{% /tabs %}}

## Response

### Structure

| Name                        | Type         | Description                            |
|-----------------------------|--------------|----------------------------------------|
| serverVersion               | String       | Technical version information          |
| dialectVersion              | String       | Technical version information          |
| requestId                   | Long         | A technical id identifying the request |
| stopLocationOrCoordLocation | StopLocation | Contains the actual response data      |

#### stopLocationOrCoordLocation

| Name                        | Type | Description                                                                                            |
|-----------------------------|------|--------------------------------------------------------------------------------------------------------|
| stopLocationOrCoordLocation | List | List of the found places. All items are either a ”StopLocation” or a ”CoordLocation”, described below. |

#### StopLocation

| Name          | Type    | Description                                                           |
|---------------|---------|-----------------------------------------------------------------------|
| Id            | String  | Reconstruction Id, see travel planner API                             |
| Name          | String  | Stop name                                                             |
| extId         | String  | HafasId for this stop. See "HafasId and SiteId" below.                |
| mainMastExtId | Integer | SiteId for use with SL Route-planner. See "HafasId and SiteId" below. |
| Lat           | Double  | Latitude                                                              |
| Lon           | Double  | Longitude                                                             |
| Weight        | Integer | How trafficked a station is. Higher means more traffic.               |
| Dist          | Integer | Distance between the requested coordinate and this stop, in meters.   |
| Products      | Integer | See description for request parameters                                |

#### Coordlocation

| Name          | Type             | Description                                                      |
|---------------|------------------|------------------------------------------------------------------|
| Id            | String           | Reseplanerar reconstruction Id, se reseplanerarens documentation |
| Name          | String           | Namn för POI.                                                    |
| Lat           | String           | Lat.                                                             |
| Lon           | String           | Long.                                                            |
| Dist          | String           | Distans i meter från försedd koordinat i anropet.                |
| Type          | String           | Visar i nuläget endast ”POI”                                     |
| LocationNotes | Lista av element | Se nedan                                                         |

#### LocationNote

These values are examples and subject to change.

| Key | Value                                                                                                                         |
|-----|-------------------------------------------------------------------------------------------------------------------------------|
| PI  | Unique id                                                                                                                     |
| PC  | POI type:Amenity, Historic, Leisure, Shop or Tourism                                                                          |
| PT  | POI type: Hospital, School, Theatre, University, Castle, Park, Library, Mall, Attraction, Chalet, Museum, Viewpoint eller Zoo |
| CN  | Name of the municipality in which the POI is located                                                                          |

### HafasId och SiteId

Information regarding how ids relate to Hafas ids used in the route planner API.

| Type       | Description                                                                                                                      | Example                                                |
|------------|----------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------|
| SiteId     | 3BA1CDEFG where `ABCDEFG` are the 7 last digits of site.number padded with zeroes. Note the first two digits which change place! | SiteId: 9600 → HafasId: 300109600                      |
| StopId     | 4BA1CDEFG where `ABCDEFG` are the 7 last digits of JourneyPatternPoint.number padded with zeroes.                                | JourneyPatternPoint.Number: 56789 → HafasId: 400156789 |
| StopAreaId | 2BA1CDEFG where `ABCDEFG` are the 7 last digits of StopArea.number padded with zeroes.                                           | StopArea.number: 81025 → HafasId: 200181025            |

### Example response

{{% tabs %}} {{% tab "Json" %}}

```json
{
  "stopLocationOrCoordLocation": [
    {
      "StopLocation": {
        "id": "A=1@O=Marieberg@X=18016154@Y=59328284@u=0@U=74@L=400110905@",
        "extId": "400110905",
        "hasMainMast": true,
        "mainMastId": "A=1@O=Marieberg (Stockholm)@X=18015533@Y=59328410@U=74@L=300101273@",
        "mainMastExtId": "300101273",
        "name": "Marieberg",
        "lon": 18.016154,
        "lat": 59.328284,
        "weight": 388,
        "dist": 0,
        "products": 8
      }
    },
    {
      "StopLocation": {
        "id": "A=1@O=Wennerbergsgatan@X=18014140@Y=59328347@u=0@U=74@L=400110903@",
        "extId": "400110903",
        "hasMainMast": true,
        "mainMastId": "A=1@O=Wennerbergsgatan (Stockholm)@X=18013061@Y=59328518@U=74@L=300101263@",
        "mainMastExtId": "300101263",
        "name": "Wennerbergsgatan",
        "lon": 18.01414,
        "lat": 59.328347,
        "weight": 388,
        "dist": 114,
        "products": 8
      }
    },
    {
      "StopLocation": {
        "id": "A=1@O=Fria Ukrainas plats@X=18017871@Y=59327286@u=0@U=74@L=400110729@",
        "extId": "400110729",
        "hasMainMast": true,
        "mainMastId": "A=1@O=Fria Ukrainas plats (Stockholm)@X=18017592@Y=59327124@U=74@L=300101271@",
        "mainMastExtId": "300101271",
        "name": "Fria Ukrainas plats",
        "lon": 18.017871,
        "lat": 59.327286,
        "weight": 1465,
        "dist": 147,
        "products": 8
      }
    },
    {
      "StopLocation": {
        "id": "A=1@O=Västerbroplan@X=18020109@Y=59328302@u=0@U=74@L=400110727@",
        "extId": "400110727",
        "hasMainMast": true,
        "mainMastId": "A=1@O=Västerbroplan (Stockholm)@X=18021125@Y=59328176@U=74@L=300101270@",
        "mainMastExtId": "300101270",
        "name": "Västerbroplan",
        "lon": 18.020109,
        "lat": 59.328302,
        "weight": 1465,
        "dist": 224,
        "products": 8
      }
    },
    {
      "StopLocation": {
        "id": "A=1@O=Wivalliusgatan@X=18013205@Y=59326558@u=0@U=74@L=400110450@",
        "extId": "400110450",
        "hasMainMast": true,
        "mainMastId": "A=1@O=Wivalliusgatan (Stockholm)@X=18013196@Y=59326540@U=74@L=300101272@",
        "mainMastExtId": "300101272",
        "name": "Wivalliusgatan",
        "lon": 18.013205,
        "lat": 59.326558,
        "weight": 1465,
        "dist": 254,
        "products": 8
      }
    }
  ],
  "serverVersion": "1.4",
  "dialectVersion": "1.23",
  "requestId": "1701701254662"
}
```

{{% /tab %}} {{% tab "Xml" %}}

```xml
<?xml version="1.0" encoding="UTF-8"?>
<LocationList serverVersion="1.4" dialectVersion="1.23" requestId="1701701276854" xmlns="hafas_rest">
    <StopLocation id="A=1@O=Marieberg@X=18016154@Y=59328284@u=0@U=74@L=400110905@" extId="400110905" name="Marieberg" hasMainMast="true"
                  mainMastId="A=1@O=Marieberg (Stockholm)@X=18015533@Y=59328410@U=74@L=300101273@" mainMastExtId="300101273" lon="18.016154" lat="59.328284"
                  weight="388" products="8" dist="0"/>
    <StopLocation id="A=1@O=Wennerbergsgatan@X=18014140@Y=59328347@u=0@U=74@L=400110903@" extId="400110903" name="Wennerbergsgatan" hasMainMast="true"
                  mainMastId="A=1@O=Wennerbergsgatan (Stockholm)@X=18013061@Y=59328518@U=74@L=300101263@" mainMastExtId="300101263" lon="18.01414"
                  lat="59.328347" weight="388" products="8" dist="114"/>
    <StopLocation id="A=1@O=Fria Ukrainas plats@X=18017871@Y=59327286@u=0@U=74@L=400110729@" extId="400110729" name="Fria Ukrainas plats" hasMainMast="true"
                  mainMastId="A=1@O=Fria Ukrainas plats (Stockholm)@X=18017592@Y=59327124@U=74@L=300101271@" mainMastExtId="300101271" lon="18.017871"
                  lat="59.327286" weight="1465" products="8" dist="147"/>
    <StopLocation id="A=1@O=Västerbroplan@X=18020109@Y=59328302@u=0@U=74@L=400110727@" extId="400110727" name="Västerbroplan" hasMainMast="true"
                  mainMastId="A=1@O=Västerbroplan (Stockholm)@X=18021125@Y=59328176@U=74@L=300101270@" mainMastExtId="300101270" lon="18.020109" lat="59.328302"
                  weight="1465" products="8" dist="224"/>
    <StopLocation id="A=1@O=Wivalliusgatan@X=18013205@Y=59326558@u=0@U=74@L=400110450@" extId="400110450" name="Wivalliusgatan" hasMainMast="true"
                  mainMastId="A=1@O=Wivalliusgatan (Stockholm)@X=18013196@Y=59326540@U=74@L=300101272@" mainMastExtId="300101272" lon="18.013205"
                  lat="59.326558" weight="1465" products="8" dist="254"/>
</LocationList>
```

{{% /tab %}} {{% /tabs %}}

### XSD

`https://api.sl.se/api2/nearbystops/xsd.xml?key=TRAFIKLAB-SLAPI-INTEGRATION-2024&xsdname=hafasRestLocation.xsd</p>`

## Error messages

The language in the response matches the language in the request.

| Statuskod | Meddelande                                                                               |
|-----------|------------------------------------------------------------------------------------------|
| 1001      | problem with request: Key is undefinedNyckel har ej skickats med.                        |
| 1002      | problem with request: Key is invalidNyckel är ogiltig                                    |
| 1003      | Invalid apiOgiltigt api                                                                  |
| 1004      | problem with request: This api is currently not available for keys with priority above 2 |
| 1005      | Nyckel finns, men ej för detta apiproblem with request: Invalid api for key              |
| 1006      | To many requests per minuteFör många anrop per minut, för den profil som används         |
| 1007      | To many requests per monthFör många anrop per månad, för den profil som används          |
| R0001     | Unknown service method                                                                   |
| R0002     | Invalid or missing request parameters.                                                   |
| R0007     | Internal communication error.                                                            |
