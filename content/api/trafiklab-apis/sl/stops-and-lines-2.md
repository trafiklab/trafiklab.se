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

Listning av hållplatser och linjer i Stockholms län.

För att kunna beskriva trafikinformation på ett konsekvent sätt, är det nödvändigt att ingående begrepp och definitioner är klara och tydliga. De viktigaste
begreppen för denna tjänst presenteras nedan.

{{% error %}}
Denna API kommer stängas ned vid slutet av mars 2024. Den ersätts av [SLs nya network API](sl-network.md).
{{% /error %}}

## Begrepp

| Begrepp                   | Beskrivning                                                                                                                          |
|---------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| Site                      | Site är en gruppering av StopAreas som används för att förenkla sökningen i reseplaneraren.                                          |
| StopArea                  | StopArea är en gruppering av StopPoints med samma trafikslag och namn inom ett avgränsat geografiskt område, exempelvis en terminal. |
| StopPoint                 | En StopPoint är ett stoppställe och ingår i en StopArea                                                                              |
| Line                      | Linje annonserad mot resenär                                                                                                         |
| JourneyPattern            | En unik körväg för en linje                                                                                                          |
| JourneyPatternPointOnLine | Innehåller samtliga stoppställen som trafikeras av en viss linje                                                                     |
| Transportmode             | Trafikslag                                                                                                                           |

## API

### Åtkomst

URL:er för anrop finns specificerade nedan:

- Produktion: `https://api.sl.se/api2/LineData.xml?model=[model]&key=[key]`
- Produktion (JSON): `https://api.sl.se/api2/LineData.json?model=[model]&key=[key]`

Observera att det är extension i anropet som avgör formateringen av svaret.

### API-nycklar, behörighet

API-nycklar kan införskaffas via Trafiklabs utvecklarportal.

En API-nyckel ska användas i URL:en för ett API anrop.

- Exempel: `https://api.sl.se/api2/LineData.xml?model=[model]&key=[key]`

#### Nyckelnivåer

| Nivå  | Max anrop/minut | Max anrop/månad |
|-------|-----------------|-----------------|
| Brons | 5               | 500             |

### Format

API:et har support för XML och JSON dataformatering.

Önskad formatering anges i URL:en för ett API anrop.

- Exempel: `api.sl.se/api2/LineData.xml?model=[model]&key=[key]`

## Datatyper

Alla datatyper representeras alltid i strängform för respektive format.

Typen angiven vid beskrivningar av modeller anger endast en lämplig datatyp att konvertera värdet till i ett givet programmeringsspråk.

| Typ | Exempel | Beskrivning                                                                                                                          |
|-----|---------|--------------------------------------------------------------------------------------------------------------------------------------|
| Int | 123     | Alla datatyper representeras alltid i strängform. Kan dock konverteras till datatypen Int om programmeringsspråket har stöd till det |

## Filtrering av data

För modellerna line och jour är det önskvärt att kunna särskilja vilken trafiktyp datat avser. Detta kan åstadkommas genom att skicka med den valfria parametern
DefaultTransportModeCode som kan innehålla någon av de Transportmode-värdena som returneras vid anrop till modellen transportmode, ex ”BUS” eller ”METRO”

Exempel:

`https://api.sl.se/api2/linedata.xml?key=[nyckel]&model=line&DefaultTransportModeCode=METRO`
`https://api.sl.se/api2/linedata.xml?key=[nyckel]&model=jour&DefaultTransportModeCode=BUS`

## Teckenkodning

UTF-8 används för både XML och Json.

## Prestanda

Eftersom anrop returnerar relativ stor datamängd är det starkt rekommenderat att anropet innehåller följande HEADER parameter för att möjliggöra GZIP
komprimering i svaret.

| Nyckel          | Värde         |
|-----------------|---------------|
| Accept-Encoding | gzip, deflate |

## Uppdateringsfrekvens

API portalen uppdaterar data en gång per dygn mellan klockan 0.00-2.00 varje dag.

## API modell

Anrop till [https://api.sl.se/api2/LineData](https://api.sl.se/api2/LineData) returnerar alltid en API modell (basmodell) tillbaka, oavsett vilken specifik
datamodell man har begärt i anropet.

| Nyckel        | Typ    | Exempel                 | Beskrivning                                                                                                        |
|---------------|--------|-------------------------|--------------------------------------------------------------------------------------------------------------------|
| StatusCode    | Int    | 0                       | 0 om anropet har gått bra, annars en felkod som inte kan åtgärdas via tex ett modifierat anrop                     |
| ExecutionTime | Int    | 267                     | Antal millisekunder som det har tagit att generera ett svar på servern                                             |
| ResponseData  | Objekt |                         | Container-objekt som innehåller attribut och data                                                                  |
| Version       | String | 2014-06-27 14:03:39.103 | Senast ändrad. Uppdateras normalt sett bara en gång per dygn                                                       |
| Type          | String | DataModelType           | Anger typen av datamodellen som svaret innehåller: Site, StopPoint, Line, JourneyPatternPointOfLine, TransportMode |

### API modell
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

# Specifikation för datamodeller

API:et tillhandahåller följande datamodeller:

| Nyckel | Värde    | Beskrivning                                          |
|--------|----------|------------------------------------------------------|
| model  | **site** | Returnerar svar med Site objekt                      |
| model  | **stop** | Returnerar svar med StopPoint objekt                 |
| model  | **line** | Returnerar svar med Line objekt                      |
| model  | **jour** | Returnerar svar med JourneyPatternPointOnLine objekt |
| model  | **tran** | Returnerar svar med TransportMode objekt             |

Önskad datamodell anges i URL:en för ett API-anrop.

`api.sl.se/api2/LineData.xml?model=[model]&key=[key]`

## Exempel

`https://api.sl.se/api2/LineData.xml?model=site`

## Site

### Beskrivning

Site är en gruppering av StopAreas som används för att förenkla sökningen i reseplaneraren.

### Egenskaper

| Egenskap                | Kan konverteras till | Exempel                 | Beskrivning                               |
|-------------------------|----------------------|-------------------------|-------------------------------------------|
| SiteId                  | Int                  | 1002                    | Unikt identifikationsnummer för en Site   |
| SiteName                | String               | Centralen               | Benämning på området                      |
| StopAreaNumber          | Int                  | 1051                    | Unikt identifikationsnummer för hållplats |
| LastModifiedUtcDateTime | DateTime             | 2014-06-27 14:03:39.103 | Senast ändrad                             |
| ExistsFromDate          | DateTime             | 2014-06-28 00:00:00.000 | Gäller fr.o.m. datum                      |

### Objektstruktur

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

### Beskrivning

StopPoints (Stoppställen) ingår i en StopArea.

### Egenskaper

| Egenskap                   | Kan konverteras till | Exempel                 | Beskrivning                                                                              |
|----------------------------|----------------------|-------------------------|------------------------------------------------------------------------------------------|
| StopPointNumber            | Int                  | 1051                    | Unikt identifikationsnummer för stoppställe                                              |
| StopPointName              | String               | T-Centralen             | Namn på stoppställe                                                                      |
| StopAreaNumber             | Int                  | 1051                    | Number för StopArea. Ett stoppställe ingår endast i en StopArea                          |
| LocationNorthingCoordinate | Double               | 59.3313179695028        | Koordinat i WGS84-format                                                                 |
| LocationEastingCoordinate  | Double               | 18.0616773959365        | Koordinat i WGS84-format                                                                 |
| ZoneShortName              | String               | A                       | Taxezon. A, B eller C. Om SLs taxa inte gäller är taxezon null                           |
| StopAreaTypeCode           | String               | METROSTN                | Användning av hållplatsen. BUSSTERM, TRAMSTN, METROSTN, RAILWSTN, SHIPBER eller FERRYBER |
| LastModifiedUtcDateTime    | DateTime             | 2014-06-03 00:00:00.000 | Senast ändrad                                                                            |
| ExistsFromDate             | DateTime             | 2014-06-03 00:00:00.000 | Gäller fr.o.m. datum                                                                     |

### Objektstruktur

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

### Beskrivning

Returnerar beskrivning av en linje. Innehåller referenser till trafikslag.

### Egenskaper

| Egenskap                 | Kan konverteras till | Exempel                 | Beskrivning                           |
|--------------------------|----------------------|-------------------------|---------------------------------------|
| LineNumber               | Int                  | 3                       | Unikt identifikationsnummer för linje |
| LineDesignation          | String               | 3                       | Linjebeteckning                       |
| DefaultTransportMode     | String               | blåbuss                 | Gruppering av linjer för presentation |
| DefaultTransportModeCode | String               | BUS                     | Trafikslag                            |
| LastModifiedUtcDateTime  | DateTime             | 2007-08-24 00:00:00.000 | Senast ändrad                         |
| ExistsFromDate           | DateTime             | 2007-08-24 00:00:00.000 | Gäller fr.o.m. datum                  |

### Objektstruktur

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

### Beskrivning

Returnerar kopplingen mellan stoppställe och linje. Innehåller samtliga stoppställen som trafikeras av en viss linje.

### Egenskaper

| Egenskap                  | Kan konverteras till | Exempel                 | Beskrivning                                 |
|---------------------------|----------------------|-------------------------|---------------------------------------------|
| LineNumber                | Int                  | 1                       | Unikt identifikationsnummer för linje       |
| DirectionCode             | Int                  | 1                       | Linjeriktning                               |
| JourneyPatternPointNumber | Int                  | 10008                   | Unikt identifikationsnummer för stoppställe |
| LastModifiedUtcDateTime   | DateTime             | 2012-06-23 00:00:00.000 | Senast ändrad                               |
| ExistsFromDate            | DateTime             | 2012-06-23 00:00:00.000 | Gäller fr.o.m. datum                        |

### Objektstruktur

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

### Beskrivning

Returnerar tillgängliga trafikslag. Linjedatan refererar till trafikslaget via egenskapen DefaultTransportModeCode.

### Samband mellan TransportModeCode och StopAreaCode

| DefaultTransportModeCode | StopAreaTypeCode |
|--------------------------|------------------|
| BUS                      | BUSTERM          |
| METRO                    | METROSTN         |
| TRAM                     | TRAMSTN          |
| TRAIN                    | RAILWSTN         |
| SHIP                     | SHIPBER          |
| FERRY                    | FERRYBER         |

### Objektegenskaper

| Egenskap                 | Kan konverteras till | Exempel                 | Beskrivning             |
|--------------------------|----------------------|-------------------------|-------------------------|
| DefaultTransportModeCode | String               | BUS                     | Unik kod för trafikslag |
| DefaultTransportMode     | String               | buss                    | Benämning på trafikslag |
| StopAreaTypeCode         | String               | BUSTERM                 | Typkod för hållplatsen  |
| LastModifiedUtcDateTime  | DateTime             | 2007-08-24 00:00:00.000 | Senast ändrad           |
| ExistsFromDate           | DateTime             | 2007-08-24 00:00:00.000 | Gäller fr.o.m. datum    |

### Objektstruktur

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

## Fullständiga trafikslag exempel

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

Räcker inte dokumentationen så [sök gärna bland alla de hundratals inlägg som finns på vårt supportforum](http://kundo.se/org/trafiklabse/posts/). Det är
troligt att någon redan har hittat och löst samma problem som du har.

Hittar du fortfarande inte svar på din fråga så [skriv ett eget inlägg på forumet](http://kundo.se/org/trafiklabse/) så hjälper vi dig.
