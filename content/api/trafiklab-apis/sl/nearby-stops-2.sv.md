---
title: SL Nearby stops v2.0 (Närliggande hållplatser 2)
weight: 300
date: 2019-01-14
aliases:
  - /api/sl-narliggande-hallplatser-2
  - /api/sl-narliggande-hallplatser-2/dokumentation
  - /api/sl-narliggande-hallplatser-2/nivaer
  - /api/sl-narliggande-hallplatser-2/konsol
  - /node/25595
  - /node/25595/dokumentation
  - /node/25595/nivaer
  - /node/25595/konsol
---

## Beskrivning

Med detta API kan du få information om närliggande hållplatser till en försedd plats baserad på lat och long.

## URL

`https://journeyplanner.integration.sl.se/v1/nearbystopsv2.<FORMAT>?key=<DIN NYCKEL>&originCoordLat=<LAT>&originCoordLong=<LONG>&maxNo=<MAX ANTAL SVAR>&r=<RADIUS I METER>`

{{% warning %}}
Den tidigare
länken `https://api.sl.se/api2/nearbystopsv2.<FORMAT>?key=<DIN NYCKEL>&originCoordLat=<LAT>&originCoordLong=<LONG>&maxNo=<MAX ANTAL SVAR>&r=<RADIUS I METER>`
har ändrats den 4:e december, och kommer sluta fungera den 15e mars 2024.
Parametrar, svarsstrukturer och API nycklar är oförändrade.
{{% /warning %}}

### API-nyckelnivåer

| Nivå   | Max anrop/minut | Max anrop/månad |
|--------|-----------------|-----------------|
| Brons  | 30              | 10 000          |
| Silver | 60              | 500 000         |
| Guld   |                 | Efter behov     |

## Format

Json eller xml enligt ändelse till serviceanropet.

## Parametrar

| Namn            | Datatyp | Tvingande | Beskrivning                                                                                                                                                                                                                                                                                                                                               |
|-----------------|---------|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Key             | String  | Ja        | Din API nyckel.                                                                                                                                                                                                                                                                                                                                           |
| originCoordLat  | String  | Ja        | Lat.                                                                                                                                                                                                                                                                                                                                                      |
| originCoordLong | String  | Ja        | Long.                                                                                                                                                                                                                                                                                                                                                     |
| maxNo           | Integer | Nej       | Maximalt antal resultat som önskas. 9 är default, max är 1000.                                                                                                                                                                                                                                                                                            |
| r               | Integer | Nej       | Radius runt försedd koordinat som närliggande hållplatser skall hämtas ut för. 1000 är default, max är 2000.                                                                                                                                                                                                                                              |
| products        |         | Nej       | Produktfilter, Kombinationsvärde av önskade trafikslag om inte alla ska användas vid utsökning av resor. Bitmask enligt följande: Pendeltåg (1), Tunnelbana (2), Lokalbana/spårvagn (4), Buss (8), Ej i bruk (16), Ej i bruk (32), Båt typ (64), Närtrafik (128). Värdes anges som heltalsvärdet av den kombinerade bitmasken, ex Buss och båt, 8+64 = 72 |
| type            |         | Nej       | Typfilter för platser, S: sök efter endast stationer, P: Sök efter endast POI, SP: Sök efter stationer och POI                                                                                                                                                                                                                                            |

## Resultat

### Svarsstruktur

| Namn                        | Datatyp      | Beskrivning                                                      |
|-----------------------------|--------------|------------------------------------------------------------------|
| serverVersion               | String       | Versionsinformation.                                             |
| dialectVersion              | String       | Versionsinformation.                                             |
| requestId                   | Long         | En id som identifierar anropen.                                  |
| stopLocationOrCoordLocation | StopLocation | Innehåller själva svarsdata från tjänsten. Se ”Svarsdata” nedan. |

### Svarsdata

| Namn                        | Datatyp          | Beskrivning                                                                    |
|-----------------------------|------------------|--------------------------------------------------------------------------------|
| stopLocationOrCoordLocation | Lista av element | Lista med de platser som hittats. Se ”StopLocation” och ”CoordLocation” nedan. |

#### StopLocation

| Namn          | Datatyp | Beskrivning                                                                                             |
|---------------|---------|---------------------------------------------------------------------------------------------------------|
| Id            | String  | Reconstruction Id, se reseplanerarens dokumentation                                                     |
| Name          | String  | Namn för hållplats.                                                                                     |
| extId         | String  | HafasId för hållplatsen. Läs mer om HafasId i sektionen HafasId och SiteId.                             |
| mainMastExtId | Integer | SiteId att användas tillsammans med SL Route-planner. Läs mer om SiteId i sektionen HafasId och SiteId. |                                                                              |
| Lat           | Double  | Lat.                                                                                                    |
| Lon           | Double  | Long.                                                                                                   |
| Weight        | Integer | Anger hur mycket en station används, ju högre värde desto större användning.                            |
| Dist          | Integer | Distans i meter från försedd koordinat i anropet.                                                       |
| Products      | Integer | Se beskrivning för anropsparametrar                                                                     |

#### CoordLocation

| Namn          | Datatyp          | Beskrivning                                                      |
|---------------|------------------|------------------------------------------------------------------|
| Id            | String           | Reseplanerar reconstruction Id, se reseplanerarens dokumentation |
| Name          | String           | Namn för POI.                                                    |
| Lat           | String           | Lat.                                                             |
| Lon           | String           | Long.                                                            |
| Dist          | String           | Distans i meter från försedd koordinat i anropet.                |
| Type          | String           | Visar i nuläget endast ”POI”                                     |
| LocationNotes | Lista av element | Se nedan                                                         |

##### LocationNote

Namn/värde lista.

Dessa värden gäller för närvarande men kan komma att ändras utan att information skickas i förväg.

| Key | Value                                                                                                                        |
|-----|------------------------------------------------------------------------------------------------------------------------------|
| PI  | Unikt id                                                                                                                     |
| PC  | POI kategori: Amenity, Historic, Leisure, Shop eller Tourism                                                                 |
| PT  | POI typ: Hospital, School, Theatre, University, Castle, Park, Library, Mall, Attraction, Chalet, Museum, Viewpoint eller Zoo |
| CN  | Namnet på kommunen som POI:en befinner sig i.                                                                                |

### HafasId och SiteId

Information om hur HafasId byggs på SiteId, StopId och StopAreaId.
HafasId nyttjas bland annat i Reseplanerar api’et.

| Typ        | Beskrivning                                                                        | Exempel                                              |
|------------|------------------------------------------------------------------------------------|------------------------------------------------------|
| SiteId     | 3BA1CDEFG där där ABCDEFG är de 7 sista sifforna i site.number utfyllt med nollor. | SiteId: 9600 HafasId: 300109600                      |
| StopId     | 4BA1CDEFG där ABCDEFG är journeyPatternPoint utfyllt med nollor.                   | JourneyPatternPoint.Number: 56789 HafasId: 400156789 |
| StopAreaId | 2BA1CDEFG där ABCDEFG är stopArea.number utfyllt med nollor                        | StopArea.number: 81025 HafasId: 200181025            |

### XSD

#### Url

Exempel:
https://api.sl.se/api2/nearbystops/xsd.xml?key=<DIN API NYCKEL>&xsdname= hafasRestLocation.xsd

## Felmeddelanden

| Statuskod | Meddelande                                                                               |
|-----------|------------------------------------------------------------------------------------------|
| 1001      | problem with request: Key is undefined                                                   |
|           | Nyckel har ej skickats med.                                                              |
| 1002      | problem with request: Key is invalid                                                     |
|           | Nyckel är ogiltig                                                                        |
| 1003      | Invalid api                                                                              |
|           | Ogiltigt api                                                                             |
| 1004      | problem with request: This api is currently not available for keys with priority above 2 |
| 1005      | Nyckel finns, men ej för detta api                                                       |
|           | problem with request: Invalid api for key                                                |
| 1006      | To many requests per minute                                                              |
|           | För många anrop per minut, för den profil som används                                    |
| 1007      | To many requests per month                                                               |
|           | För många anrop per månad, för den profil som använd                                     