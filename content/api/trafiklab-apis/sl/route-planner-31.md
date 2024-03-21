---
title: SL Route-planner v3.1
weight: 100
date: 2019-01-14
aliases:
  - /api/sl-reseplanerare
  - /api/sl-reseplanerare-31
  - /api/sl-reseplanerare-31/documentation
  - /api/sl-reseplanerare-31/console
  - /api/sl-reseplanerare-31/nivaer
  - /node/25593
  - /node/25593/documentation
  - /node/25593/console
  - /node/25593/nivaer
---

## Description

With this API, you can get travel proposals from point A to point B within Stockholm County using SL's traffic. Waxholmsbolaget's traffic is also included in
SL's journey planner. The API can be used to calculate travel proposals between any combination of positions and/or stops. The API returns travel proposals
based on the "best match" for the input.

In the journey planner, there are four different functions that can be called:

- **Trip:** Calculates a journey from a starting point to a destination. These can be station IDs or coordinates based on addresses or "points of interest."
- **JourneyDetail:** Returns detailed information about part of a journey with a vehicle. It returns a list of all stops/stations, including all arrival and
  departure times with real-time data (if available).
- **Reconstruction:** Used to recreate a copy of a Trip using a reconstruction context. The result will be a complete copy given that the underlying data has
  not changed.
- **GisRoute:** Provides detailed information about the route.
- **XSD:** Returns an XSD containing definitions for all the input parts of the response structures for the services in SL Reseplanerare 3.

The journey planner is invoked with a GET request per service with UTF-8 URL-encoded GET parameters.

## Changes Since the Previous Version

A change has been made that may affect implemented applications. For version 3.1 of the journey planner, the response format regarding the "crd" elements in the
polyline describing the detailed route has changed. The points in this version are represented by double values compared to version 3.0, which represented them
as integers.

Previous version (3.0): `<crd>17973032</crd><crd>59360501</crd><crd>9</crd> <crd>18</crd>`

Travelplanner 3.1: `<crd>17.973032</crd><crd>59.360501</crd><crd>9.0E-6</crd><crd>1.8E-5</crd>`

## URL

- **Trip:** `https://journeyplanner.integration.sl.se/v1/TravelplannerV3_1/trip.<FORMAT>?key=<YOUR API KEY>&<parameters>`
- **JourneyDetail:** `https://journeyplanner.integration.sl.se/v1/TravelplannerV3_1/journeydetail.<FORMAT>?key=<YOUR API KEY>&<parameters>`
- **Reconstruction:** `https://journeyplanner.integration.sl.se/v1/TravelplannerV3_1/Reconstruction.<FORMAT>?key=<YOUR API KEY>&<parameters>`
- **Gisroute**: https://journeyplanner.integration.sl.se/v1/TravelplannerV3_1/gisroute.<FORMAT>?key=<YOUR API KEY>&<parameters>
- **TTI**: https://journeyplanner.integration.sl.se/v1/TravelplannerV3_1/tti?key=<YOUR API KEY>
- **XSD:** `https://journeyplanner.integration.sl.se/v1/TravelplannerV3_1/xsd.xml?key=<YOUR API KEY>`

{{% warning %}}
The old domain and base URL `https://api.sl.se/api2/TravelplannerV3_1/` has changed on January 15th, and will stop working on March 15th.
Query parameters, response bodies and API keys remain unchanged.
{{% /warning %}}

### API Key Levels

| Level  | Max Requests/Minute | Max Requests/Month |
|--------|---------------------|--------------------|
| Bronze | 30                  | 10,000             |
| Silver | 60                  | 500,000            |
| Gold   |                     | As needed          |

## Format

JSON or XML according to the extension of the service call.

## Trip

### Parameters

{{% warning %}}
**Change in Site-ids used as search parameter**

After an unexpected breaking change in february 2024 the SiteId value expected by the SL Routeplanner 3.1 API has changed.
These values changed in february but do still match (given that both APIs are accessed through the integration.sl.se domain).

If you are using site-ids you stored previously, you should convert 4-7 digits site-ids in the form
of `ABCDEFG` (padding with zeroes on the left side) into `3BA1CDEFG`.
{{% /warning %}}

| Name              | Description                                                                     | Comment                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|-------------------|---------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Lang              | Language (en/sv/de)                                                             | Language in the response, default is de.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| originExtId       | Starting point, ID (9 digits)                                                   | Can be obtained through SL Stop Lookup or SL Nearby stops.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| originCoordLat    | Latitude for the starting point. WGS84 in decimal notation, for example 64.00.  | Must be provided together with originCoordLong.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| originCoordLong   | Longitude for the starting point. WGS84 in decimal notation, for example 17.50. | Must be provided together with originCoordLat.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| destExtId         | Destination, ID  (9 digits)                                                     | Can be obtained through SL Stop Lookup or SL Nearby stops.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| destCoordLat      | Latitude for the destination. WGS84 in decimal notation, for example 64.00.     | Must be provided together with destCoordLong.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| destCoordLong     | Longitude for the destination. WGS84 in decimal notation, for example 17.50.    | Must be provided together with destCoordLat                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Via               | List of specifications for stations to pass.                                    | Optional Separated by ; in the following format: `viaId\|waitTime\|status\|products` <ul><li>viaId, external ID of the stop/station to pass</li><li>waitTime, minutes to stop at the passed stop/station (optional)</li><li>status, one of EXR (boarding and alighting required), NER (boarding not required), NXR (alighting not required), NEXR (boarding and alighting not required). Optional, EXT is default.</li><li>products, transport modes for via, see Product</li></ul> Ex1. via two stops, 300109001;300109117 Ex2, via two stops with 15 and 10 minutes waiting time, 300109001\|15;300109117\|10 |
| viaId             | ID for station to pass.                                                         | Optional Single ID for a stop/station to pass, e.g., 300109001.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| viaWaitTime       | Waiting time for the passed station                                             | Optional Number of minutes to spend at the via-station specified with viaId.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Avoid             | List of stations to avoid passing.                                              | Optional Separated by ; in the following format: `avoidId\|avoidStatus` <ul><li>avoidId, internal or external ID for stop/station to avoid</li><li>avoidStatus, one of NPAVO (do not pass), NCAVO (do not change at)</li></ul> Optional.                                                                                                                                                                                                                                                                                                                                                                        |
| avoidID           | ID for station to avoid.                                                        | Optional Internal or external ID for stop/station to avoid for changes.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| changeTimePercent | Extended change time, percentage (100-500)                                      | Optional Percentage extension of the originally calculated time to manage a change. For example, 200 doubles the time that the system will use for the traveler to make a change. Default 100.                                                                                                                                                                                                                                                                                                                                                                                                                  |
| minChangeTime     | Minimum change time (min)                                                       | Optional Minimum number of minutes to be used when changing.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| maxChangeTime     | Maximum change time                                                             | Optional Maximum number of minutes to be used when changing.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| addChangeTime     | Extended change time                                                            | Optional Number of minutes added to the calculated change time.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| maxChange         | Maximum number of changes (0-11)                                                | Optional Maximum number of changes on suggested journeys.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Date              | Date YYYY-MM-DD                                                                 | Optional. Date for the journey. Default is today's date (server time)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Time              | Time HH:MM                                                                      | Optional Time for the journey. Default is the current time (server time)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| searchForArrival  | 0 or 1                                                                          | Optional. If 1, use the specified date and time for arrival instead of departure.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| numF              | 0-6                                                                             | Optional Minimum number of journeys after the specified start time, default is 4. numF and numB together cannot exceed 6.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| numB              | 0-6                                                                             | Optional. Minimum number of journeys before the specified start time, default is 1. numF and numB together cannot exceed 6.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Products          | Transport modes, integer                                                        | Optional Combination value of desired transport modes if not all should be used in the search for journeys. Bitmask as follows: Commuter train (1) Metro (2) Local train/tram (4) Bus (8) Not in use (16) Not in use (32) Boat type (64) Local traffic (128) The value is given as the integer value of the combined bitmask, e.g., Bus and boat, 8+64 = 72                                                                                                                                                                                                                                                     |
| Lines             | Included line filtering.                                                        | Line or lines, separated by commas, to be used to filter results, exclamation mark is used for exclusion of lines. E.g.: lines=55,122 (only lines 55 and 122) lines=!19 (Not line 19)                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Context           | Earlier or later journeys                                                       | Optional. Parameter that specifies the starting point for searching for later or earlier journeys. The value is obtained from the result value srcF or srcB in a call to the trip service. See 2.4.2                                                                                                                                                                                                                                                                                                                                                                                                            |
| Poly              | 0 or 1                                                                          | Optional. Specifies whether detailed routes should be calculated for the results. For a description of the polyline, see 2.4.5. Default is 0.                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Passlist          | 0 or 1                                                                          | Optional. Specifies whether stops/stations passed during the journey should be retrieved. Default is 0.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| originWalk        | 0 or 1 + detailing                                                              | Optional, Default 1 Specifies whether a journey can start with a walking distance. For detailing distance, min and max number of meters can be specified as `1,[min distance],[max distance],[speed],[as the crow flies]` Speed is specified as follows: &lt; 100: faster = 100: normal (default) &gt; 100: slower As the crow flies: 1= on 0= off Example: `1,0,1000,0,1` Allows fast walking but a maximum of 1000 meters as the crow flies.                                                                                                                                                                  |
| destWalk          | 0 or 1 + detailing                                                              | Optional. Similar to originWalk but for destination.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| originBike        |                                                                                 | Optional. Similar to originWalk Comment: To get accurate results, you need to disable walking search, i.e., set the parameter originWalk=0                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| destBike          |                                                                                 | Optional. Similar to originWalk Comment: To get accurate results, you need to disable walking search, i.e., set the parameter destWalk=0                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| originCar         |                                                                                 | Not used at the moment                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| destCar           |                                                                                 | Not used at the moment                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| originTaxi        |                                                                                 | Not used at the moment                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| destTaxi          |                                                                                 | Not used at the moment                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| originPark        |                                                                                 | Not used at the moment Enables "Park and Ride" at the beginning of a journey. To fine-tune the distance to the next station, see originWalk                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| destPark          |                                                                                 | Not used at the moment Enables "Park and Ride" at the end of a journey. To fine-tune the distance to the next station, see originWalk                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |

### Search for Earlier or Later Journeys

In the result from the trip, two output parameters, scrB and scrF, can be used to search for earlier (scrB) or later (scrF) departures. This is done by sending
the same search to the trip with the _context_ parameter set to the value of the one to be used.

### Notes

In the search results, there are different types of notes.

Fixed notes are entered as "notes". Fixed notes are notes linked to the departure in the timetable, such as pre-booking by phone.

Disruption messages are entered as "Messages".

### Prices

Prices for a journey come in "TariffResult," and the prices are specified as integers in öre. For example:

```xml

<TariffResult>
    <fareSetItem name="ONEWAY" desc="SL">
        <fareItem name="Reskassa" desc="Helt pris" cur="SEK" price="3100"/>
        <fareItem name="övriga försäljningsställen" desc="Helt pris" cur="SEK" price="4400"/>
        <fareItem name="Konduktör på Spårväg City" desc="Helt pris" cur="SEK" price="6200"/>
        <fareItem name="Reskassa" desc="Reducerat pris" cur="SEK" price="2100"/>
        <fareItem name="övriga försäljningsställen" desc="Reducerat pris" cur="SEK" price="3000"/>
        <fareItem name="Konduktör på Spårväg City" desc="Reducerat pris" cur="SEK" price="4100"/>
    </fareSetItem>
</TariffResult>
```

### Detailed Routes

Trip and journeyDetail can provide a detailed route for the result in "Polyline", for example:

```xml

<Polyline type="WGS84" delta="true" dim="2" crdEncS="NNNNNN">
    <crd>18.06199</crd>
    <crd>59.332455</crd>
    <crd>2.7E-5</crd>
    <crd>-9.0E-6</crd>
    <crd>-1.8E-5</crd>
    <crd>9.0E-6</crd>
</Polyline>
```

The coordinate list consists of a starting longitude and latitude, and the following differences from the previous point. In the example above, a line
consisting of points (longitude, latitude):
(18.061711,59.331331),( 18.062017, 59.332446),( 18.061999, 59.332455)

### Real-time

Real-time is currently available for buses, commuter trains, tram and Roslagsbanan.

Real-time is a forecast, i.e., it is approximate.

If there is real-time, this is indicated in separate fields. For real-time in the travel proposal, "rtTime" and "rtDate" are added to the response. The old
fields "time" and
"date" are still there so that you know what has changed from/to.

In this version of the API, real-time is not parameter-driven but is always delivered if data is available.

### Response Format

The API can return both XML and JSON.
The JSON content is automatically converted from XML according to the following rules:

- Element names become object properties
- Text (PCDATA) becomes an object property with the name `$`: <a>foo</a> becomes `{ "a": { "$" : "foo" } }`
- Nested elements become nested properties: `<a><b>foo</b><c>foo</c></a>` becomes `{ "a": { "b" : { "$": "foo" }, "c": { "$": "foo"} } }`
- If there are multiple elements with the same name, it is translated into a JSON array, e.g.: `<a><b>foo1</b><b>foo2</b></a>`
  becomes `{ "a": { "b" : [{"$": foo1" }, {"$": "foo2" }] } }`
- Attribute names become object properties: `<a atb="foo1">foo2</a>` becomes `{ "a": { "atb" : "foo1", "$" : "foo2" } }`

### Response Structure

In the table below, the XML structure is described. Some obvious attributes are not included as it becomes very much otherwise, such as Lat and Lon, to give an
easier overview of what is less obvious.
For more information about various attributes and elements so there is also xsd'n hafasRestTrip.xsd.

Example explanation of the structure in the table below:
element1/element2 => element2 is a sub-element to element1.
element1.attribut1 => attribut1 is an attribute of element1.

| Element                                       | Notes                                                                                                                                                                                                                                                                        |
|-----------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Element                                       | Notes                                                                                                                                                                                                                                                                        |
| Element *Error*                               | Element som innehåller felbeskrivning                                                                                                                                                                                                                                        |
| Complex type *Polyline*                       | Detaljerad färdväg, om poly=1 angivits.                                                                                                                                                                                                                                      |
| Element Product<br>Complex type *ProductType* | Produktkontext, möjliggör åtkomst till intern data.<br>Ex. <br>`<Product name=" " admin="100017" operatorCode="SL"`<br>`operator="Storstockholms Lokaltrafik" num="11297"`<br>`line="17" catOutS="MET" catOutL="TUNNELBANA "`<br>`catOut="METRO " catIn="MET" catCode="1"/>` |
| Element *JourneyDetailRef*                    | Referens till journey detail för ett detta leg-elementet.                                                                                                                                                                                                                    |
| Simple type *PrognosisType*                   | Innehåller typ av prognos. Om den rapporterades in av extern part, räknades ut, eller rättades av systemet.                                                                                                                                                                  |
| Element *Stops*                               | En lista av journey stops/stations, om passlist=1 angivits.                                                                                                                                                                                                                  |
| Complex type *StopType*                       | Elementet stop innehåller namnet, route index, latitude, longitude, departure time/date, arrival time/date, track, realtidsdata för ankomst och avgång sampt track.                                                                                                          |
| Element *Messages*                            | Innehåller en lista av meddelanden för denna trip.                                                                                                                                                                                                                           |
| Element *Names*                               | Lists av journey names                                                                                                                                                                                                                                                       |
| Element *JourneyStatus*                       | Innehåller status för Journey.                                                                                                                                                                                                                                               |
| Element *TripList*                            | Rotelement, innehåller en lista på alla Trips vid anrop till trip. Om ett större fel har inträffat under anrop så innehåller attributen errorCode och errortext felbeskrivning.                                                                                              |
| Element *Trip*                                | Trip-objektet innehåller en lista med Leg-objekt med den uträknade resan.                                                                                                                                                                                                    |
| Element *LegList*                             | Innehåller alla Leg-element för en Trip.                                                                                                                                                                                                                                     |
| Element *Leg*                                 | Leg-objektet är en del av en resa. Det kan vara antingen en gångväg, cykel eller bilväg eller oftast en resa med bus, tåg, eller annat typ av transportmedel.                                                                                                                |
| Element *Origin*                              | Innehåller namn, typ, rout index, realtidsdata för startpunkten för denna resa.                                                                                                                                                                                              |
| Element *Destination*                         | Innehåller namn, typ, rout index, realtidsdata för destinationen för denna resa.                                                                                                                                                                                             |
| Element *GisRef*                              | Referens till en specifik route i ett Leg-element.                                                                                                                                                                                                                           |

### Genererad exempeldata

```xml
<?xml version="1.0" encoding="utf-8"?>
<Trip alternative="false" valid="true" idx="1" tripId="tripId1" ctxRecon="ctxRecon1" duration="P396DT1H1M1S"
      return="false" ecoUrl="ecoUrl1" checksum="checksum1" xmlns="hafas_rest">
    <Messages>
        <Message id="id1" externalId="externalId1" act="true" pub="pub1" head="head1" lead="lead1" text="text1"
                 tckr="tckr1" company="company1" category="category1" priority="1" products="1" icon="icon1"
                 routeIdxFrom="1" routeIdxTo="1" sTime="sTime1" sDate="sDate1" eTime="eTime1" eDate="eDate1"
                 altStart="altStart1" altEnd="altEnd1">
            <affectedProduct name="name1" num="num1" line="line1" catOut="catOut1" catIn="catIn1" catCode="catCode1"
                             catOutS="catOutS1" catOutL="catOutL1" operatorCode="operatorCode1" operator="operator1"
                             admin="admin1"/>
            <affectedProduct name="name2" num="num2" line="line2" catOut="catOut2" catIn="catIn2" catCode="catCode2"
                             catOutS="catOutS2" catOutL="catOutL2" operatorCode="operatorCode2" operator="operator2"
                             admin="admin2"/>
            <affectedProduct name="name3" num="num3" line="line3" catOut="catOut3" catIn="catIn3" catCode="catCode3"
                             catOutS="catOutS3" catOutL="catOutL3" operatorCode="operatorCode3" operator="operator3"
                             admin="admin3"/>
        </Message>
        <Message id="id2" externalId="externalId2" act="false" pub="pub2" head="head2" lead="lead2" text="text2"
                 tckr="tckr2" company="company2" category="category2" priority="-2147483647" products="-2147483647"
                 icon="icon2" routeIdxFrom="-2147483647" routeIdxTo="-2147483647" sTime="sTime2" sDate="sDate2"
                 eTime="eTime2" eDate="eDate2" altStart="altStart2" altEnd="altEnd2">
            <affectedProduct name="name4" num="num4" line="line4" catOut="catOut4" catIn="catIn4" catCode="catCode4"
                             catOutS="catOutS4" catOutL="catOutL4" operatorCode="operatorCode4" operator="operator4"
                             admin="admin4"/>
            <affectedProduct name="name5" num="num5" line="line5" catOut="catOut5" catIn="catIn5" catCode="catCode5"
                             catOutS="catOutS5" catOutL="catOutL5" operatorCode="operatorCode5" operator="operator5"
                             admin="admin5"/>
            <affectedProduct name="name6" num="num6" line="line6" catOut="catOut6" catIn="catIn6" catCode="catCode6"
                             catOutS="catOutS6" catOutL="catOutL6" operatorCode="operatorCode6" operator="operator6"
                             admin="admin6"/>
        </Message>
        <Message id="id3" externalId="externalId3" act="true" pub="pub3" head="head3" lead="lead3" text="text3"
                 tckr="tckr3" company="company3" category="category3" priority="2147483647" products="2147483647"
                 icon="icon3" routeIdxFrom="2147483647" routeIdxTo="2147483647" sTime="sTime3" sDate="sDate3"
                 eTime="eTime3" eDate="eDate3" altStart="altStart3" altEnd="altEnd3">
            <affectedProduct name="name7" num="num7" line="line7" catOut="catOut7" catIn="catIn7" catCode="catCode7"
                             catOutS="catOutS7" catOutL="catOutL7" operatorCode="operatorCode7" operator="operator7"
                             admin="admin7"/>
            <affectedProduct name="name8" num="num8" line="line8" catOut="catOut8" catIn="catIn8" catCode="catCode8"
                             catOutS="catOutS8" catOutL="catOutL8" operatorCode="operatorCode8" operator="operator8"
                             admin="admin8"/>
            <affectedProduct name="name9" num="num9" line="line9" catOut="catOut9" catIn="catIn9" catCode="catCode9"
                             catOutS="catOutS9" catOutL="catOutL9" operatorCode="operatorCode9" operator="operator9"
                             admin="admin9"/>
        </Message>
    </Messages>
    <Eco co2="0.0" part="0.0" partV="0.0" nmhc="0.0" nox="0.0" prime="0.0" so2="0.0"/>
    <ServiceDays planningPeriodBegin="planningPeriodBegin1" planningPeriodEnd="planningPeriodEnd1" sDaysR="sDaysR1"
                 sDaysI="sDaysI1" sDaysB="sDaysB1" routeIdxFrom="1" routeIdxTo="1"/>
    <ServiceDays planningPeriodBegin="planningPeriodBegin2" planningPeriodEnd="planningPeriodEnd2" sDaysR="sDaysR2"
                 sDaysI="sDaysI2" sDaysB="sDaysB2" routeIdxFrom="-2147483647" routeIdxTo="-2147483647"/>
    <ServiceDays planningPeriodBegin="planningPeriodBegin3" planningPeriodEnd="planningPeriodEnd3" sDaysR="sDaysR3"
                 sDaysI="sDaysI3" sDaysB="sDaysB3" routeIdxFrom="2147483647" routeIdxTo="2147483647"/>
    <LegList>
        <Leg idx="anySimpleType" name="name1" number="number1" category="category1" type="type1" cancelled="false"
             partCancelled="false" reachable="true" direction="direction1" duration="P396DT1H1M1S" dist="1">
            <Origin name="name1" type="ST" id="id1" extId="extId1" lon="1" lat="1" routeIdx="1"
                    prognosisType="PROGNOSED" time="time1" date="date1" tz="0" track="track1" rtTime="rtTime1"
                    rtDate="rtDate1" rtTz="0" rtTrack="rtTrack1" hasMainMast="true" mainMastId="mainMastId1"
                    mainMastExtId="mainMastExtId1">
                <Notes>
                    <Note key="key1" type="U" priority="1" routeIdxFrom="1" routeIdxTo="1">Note1</Note>
                    <Note key="key2" type="A" priority="-2147483647" routeIdxFrom="-2147483647"
                          routeIdxTo="-2147483647">Note2
                    </Note>
                    <Note key="key3" type="I" priority="2147483647" routeIdxFrom="2147483647" routeIdxTo="2147483647">
                        Note3
                    </Note>
                </Notes>
            </Origin>
            <Destination name="name1" type="ST" id="id1" extId="extId1" lon="1" lat="1" routeIdx="1"
                         prognosisType="PROGNOSED" time="time1" date="date1" tz="0" track="track1" rtTime="rtTime1"
                         rtDate="rtDate1" rtTz="0" rtTrack="rtTrack1" hasMainMast="true" mainMastId="mainMastId1"
                         mainMastExtId="mainMastExtId1"/>
            <JourneyDetailRef ref="ref1"/>
            <GeometryRef ref="anySimpleType"/>
            <GisRef ref="ref1"/>
            <GisRoute dist="1" durS="P396DT1H1M1S" durR="P396DT1H1M1S" durST="P396DT1H1M1S" durW2C="P396DT1H1M1S"
                      durW2D="P396DT1H1M1S" dirTxt="dirTxt1" dirGeo="1">
                <seg name="name1" rType="U" rNum="rNum1" man="NO" manTx="manTx1" dirTx="dirTx1" ori="U" polyS="1"
                     polyE="1" dist="1"/>
                <seg name="name2" rType="M" rNum="rNum2" man="FR" manTx="manTx2" dirTx="dirTx2" ori="N"
                     polyS="-2147483647" polyE="-2147483647" dist="-2147483647"/>
                <seg name="name3" rType="H" rNum="rNum3" man="TO" manTx="manTx3" dirTx="dirTx3" ori="S"
                     polyS="2147483647" polyE="2147483647" dist="2147483647"/>
                <polyline name="name1" delta="true" dim="2" type="WGS84" crdEncYX="crdEncYX1" crdEncZ="crdEncZ1"
                          crdEncS="crdEncS1">
                    <crd>1</crd>
                    <crd>-2147483647</crd>
                    <crd>2147483647</crd>
                </polyline>
                <altPolyline name="name1" delta="true" dim="2" type="WGS84" crdEncYX="crdEncYX1" crdEncZ="crdEncZ1"
                             crdEncS="crdEncS1">
                    <crd>1</crd>
                    <crd>-2147483647</crd>
                    <crd>2147483647</crd>
                </altPolyline>
                <altPolyline name="name2" delta="false" dim="1" type="WGS84" crdEncYX="crdEncYX2" crdEncZ="crdEncZ2"
                             crdEncS="crdEncS2">
                    <crd>0</crd>
                    <crd>2</crd>
                    <crd>-2147483646</crd>
                </altPolyline>
                <altPolyline name="name3" delta="true" dim="-2147483647" type="PLANAR" crdEncYX="crdEncYX3"
                             crdEncZ="crdEncZ3" crdEncS="crdEncS3">
                    <crd>2147483646</crd>
                    <crd>-1</crd>
                    <crd>3</crd>
                </altPolyline>
            </GisRoute>
            <JourneyStatus>P</JourneyStatus>
            <Product name="name1" num="num1" line="line1" catOut="catOut1" catIn="catIn1" catCode="catCode1"
                     catOutS="catOutS1" catOutL="catOutL1" operatorCode="operatorCode1" operator="operator1"
                     admin="admin1"/>
            <Polyline name="name1" delta="true" dim="2" type="WGS84" crdEncYX="crdEncYX1" crdEncZ="crdEncZ1"
                      crdEncS="crdEncS1">
                <crd>1</crd>
                <crd>-2147483647</crd>
                <crd>2147483647</crd>
            </Polyline>
            <Stops>
                <Stop name="name1" id="id1" extId="extId1" routeIdx="1" lon="1" lat="1" arrPrognosisType="PROGNOSED"
                      depPrognosisType="PROGNOSED" depTime="depTime1" depDate="depDate1" depTz="0" arrTime="arrTime1"
                      arrDate="arrDate1" arrTz="0" passingTime="passingTime1" passingDate="passingDate1" passingTz="0"
                      arrTrack="arrTrack1" depTrack="depTrack1" rtDepTime="rtDepTime1" rtDepDate="rtDepDate1"
                      rtDepTz="0" rtArrTime="rtArrTime1" rtArrDate="rtArrDate1" rtArrTz="0" rtArrTrack="rtArrTrack1"
                      rtDepTrack="rtDepTrack1" rtPassingTime="rtPassingTime1" rtPassingDate="rtPassingDate1"
                      rtPassingTz="0" cancelled="false" hasMainMast="true" mainMastId="mainMastId1"
                      mainMastExtId="mainMastExtId1"/>
                <Stop name="name2" id="id2" extId="extId2" routeIdx="-2147483647" lon="-79228162514264337593543950335"
                      lat="-79228162514264337593543950335" arrPrognosisType="MANUAL" depPrognosisType="MANUAL"
                      depTime="depTime2" depDate="depDate2" depTz="1" arrTime="arrTime2" arrDate="arrDate2" arrTz="1"
                      passingTime="passingTime2" passingDate="passingDate2" passingTz="1" arrTrack="arrTrack2"
                      depTrack="depTrack2" rtDepTime="rtDepTime2" rtDepDate="rtDepDate2" rtDepTz="1"
                      rtArrTime="rtArrTime2" rtArrDate="rtArrDate2" rtArrTz="1" rtArrTrack="rtArrTrack2"
                      rtDepTrack="rtDepTrack2" rtPassingTime="rtPassingTime2" rtPassingDate="rtPassingDate2"
                      rtPassingTz="1" cancelled="true" hasMainMast="false" mainMastId="mainMastId2"
                      mainMastExtId="mainMastExtId2"/>
                <Stop name="name3" id="id3" extId="extId3" routeIdx="2147483647" lon="79228162514264337593543950335"
                      lat="79228162514264337593543950335" arrPrognosisType="REPORTED" depPrognosisType="REPORTED"
                      depTime="depTime3" depDate="depDate3" depTz="-2147483647" arrTime="arrTime3" arrDate="arrDate3"
                      arrTz="-2147483647" passingTime="passingTime3" passingDate="passingDate3" passingTz="-2147483647"
                      arrTrack="arrTrack3" depTrack="depTrack3" rtDepTime="rtDepTime3" rtDepDate="rtDepDate3"
                      rtDepTz="-2147483647" rtArrTime="rtArrTime3" rtArrDate="rtArrDate3" rtArrTz="-2147483647"
                      rtArrTrack="rtArrTrack3" rtDepTrack="rtDepTrack3" rtPassingTime="rtPassingTime3"
                      rtPassingDate="rtPassingDate3" rtPassingTz="-2147483647" cancelled="false" hasMainMast="true"
                      mainMastId="mainMastId3" mainMastExtId="mainMastExtId3"/>
            </Stops>
        </Leg>
        <Leg idx="anySimpleType" name="name2" number="number2" category="category2" type="type2" cancelled="true"
             partCancelled="true" reachable="true" direction="direction2" duration="-P10675199DT2H48M5.477S"
             dist="-2147483647">
            <Origin name="name2" type="ADR" id="id2" extId="extId2" lon="-79228162514264337593543950335"
                    lat="-79228162514264337593543950335" routeIdx="-2147483647" prognosisType="MANUAL" time="time2"
                    date="date2" tz="1" track="track2" rtTime="rtTime2" rtDate="rtDate2" rtTz="1" rtTrack="rtTrack2"
                    hasMainMast="false" mainMastId="mainMastId2" mainMastExtId="mainMastExtId2">
                <Notes>
                    <Note key="key4" type="R" priority="0" routeIdxFrom="0" routeIdxTo="0">Note4</Note>
                    <Note key="key5" type="H" priority="2" routeIdxFrom="2" routeIdxTo="2">Note5</Note>
                    <Note key="key6" type="U" priority="-2147483646" routeIdxFrom="-2147483646"
                          routeIdxTo="-2147483646">Note6
                    </Note>
                </Notes>
            </Origin>
            <Destination name="name2" type="ADR" id="id2" extId="extId2" lon="-79228162514264337593543950335"
                         lat="-79228162514264337593543950335" routeIdx="-2147483647" prognosisType="MANUAL" time="time2"
                         date="date2" tz="1" track="track2" rtTime="rtTime2" rtDate="rtDate2" rtTz="1"
                         rtTrack="rtTrack2" hasMainMast="false" mainMastId="mainMastId2"
                         mainMastExtId="mainMastExtId2"/>
            <JourneyDetailRef ref="ref2"/>
            <GeometryRef ref="anySimpleType"/>
            <GisRef ref="ref2"/>
            <GisRoute dist="-2147483647" durS="-P10675199DT2H48M5.477S" durR="-P10675199DT2H48M5.477S"
                      durST="-P10675199DT2H48M5.477S" durW2C="-P10675199DT2H48M5.477S" durW2D="-P10675199DT2H48M5.477S"
                      dirTxt="dirTxt2" dirGeo="-2147483647">
                <seg name="name4" rType="T" rNum="rNum4" man="ON" manTx="manTx4" dirTx="dirTx4" ori="E" polyS="0"
                     polyE="0" dist="0"/>
                <seg name="name5" rType="T4L" rNum="rNum5" man="LE" manTx="manTx5" dirTx="dirTx5" ori="W" polyS="2"
                     polyE="2" dist="2"/>
                <seg name="name6" rType="T2L" rNum="rNum6" man="RI" manTx="manTx6" dirTx="dirTx6" ori="NE"
                     polyS="-2147483646" polyE="-2147483646" dist="-2147483646"/>
                <polyline name="name2" delta="false" dim="1" type="WGS84" crdEncYX="crdEncYX2" crdEncZ="crdEncZ2"
                          crdEncS="crdEncS2">
                    <crd>0</crd>
                    <crd>2</crd>
                    <crd>-2147483646</crd>
                </polyline>
                <altPolyline name="name4" delta="false" dim="2147483647" type="HAFASGEO" crdEncYX="crdEncYX4"
                             crdEncZ="crdEncZ4" crdEncS="crdEncS4">
                    <crd>-2147483645</crd>
                    <crd>2147483645</crd>
                    <crd>-2</crd>
                </altPolyline>
                <altPolyline name="name5" delta="true" dim="0" type="WGS84" crdEncYX="crdEncYX5" crdEncZ="crdEncZ5"
                             crdEncS="crdEncS5">
                    <crd>4</crd>
                    <crd>-2147483644</crd>
                    <crd>2147483644</crd>
                </altPolyline>
                <altPolyline name="name6" delta="false" dim="2" type="PLANAR" crdEncYX="crdEncYX6" crdEncZ="crdEncZ6"
                             crdEncS="crdEncS6">
                    <crd>-3</crd>
                    <crd>5</crd>
                    <crd>-2147483643</crd>
                </altPolyline>
            </GisRoute>
            <JourneyStatus>R</JourneyStatus>
            <Product name="name2" num="num2" line="line2" catOut="catOut2" catIn="catIn2" catCode="catCode2"
                     catOutS="catOutS2" catOutL="catOutL2" operatorCode="operatorCode2" operator="operator2"
                     admin="admin2"/>
            <Polyline name="name2" delta="false" dim="1" type="WGS84" crdEncYX="crdEncYX2" crdEncZ="crdEncZ2"
                      crdEncS="crdEncS2">
                <crd>0</crd>
                <crd>2</crd>
                <crd>-2147483646</crd>
            </Polyline>
            <Stops>
                <Stop name="name4" id="id4" extId="extId4" routeIdx="0" lon="0.9" lat="0.9" arrPrognosisType="CORRECTED"
                      depPrognosisType="CORRECTED" depTime="depTime4" depDate="depDate4" depTz="2147483647"
                      arrTime="arrTime4" arrDate="arrDate4" arrTz="2147483647" passingTime="passingTime4"
                      passingDate="passingDate4" passingTz="2147483647" arrTrack="arrTrack4" depTrack="depTrack4"
                      rtDepTime="rtDepTime4" rtDepDate="rtDepDate4" rtDepTz="2147483647" rtArrTime="rtArrTime4"
                      rtArrDate="rtArrDate4" rtArrTz="2147483647" rtArrTrack="rtArrTrack4" rtDepTrack="rtDepTrack4"
                      rtPassingTime="rtPassingTime4" rtPassingDate="rtPassingDate4" rtPassingTz="2147483647"
                      cancelled="true" hasMainMast="false" mainMastId="mainMastId4" mainMastExtId="mainMastExtId4"/>
                <Stop name="name5" id="id5" extId="extId5" routeIdx="2" lon="1.1" lat="1.1"
                      arrPrognosisType="CALCULATED" depPrognosisType="CALCULATED" depTime="depTime5" depDate="depDate5"
                      depTz="0" arrTime="arrTime5" arrDate="arrDate5" arrTz="0" passingTime="passingTime5"
                      passingDate="passingDate5" passingTz="0" arrTrack="arrTrack5" depTrack="depTrack5"
                      rtDepTime="rtDepTime5" rtDepDate="rtDepDate5" rtDepTz="0" rtArrTime="rtArrTime5"
                      rtArrDate="rtArrDate5" rtArrTz="0" rtArrTrack="rtArrTrack5" rtDepTrack="rtDepTrack5"
                      rtPassingTime="rtPassingTime5" rtPassingDate="rtPassingDate5" rtPassingTz="0" cancelled="false"
                      hasMainMast="true" mainMastId="mainMastId5" mainMastExtId="mainMastExtId5"/>
                <Stop name="name6" id="id6" extId="extId6" routeIdx="-2147483646" lon="-79228162514264337593543950335"
                      lat="-79228162514264337593543950335" arrPrognosisType="PROGNOSED" depPrognosisType="PROGNOSED"
                      depTime="depTime6" depDate="depDate6" depTz="2" arrTime="arrTime6" arrDate="arrDate6" arrTz="2"
                      passingTime="passingTime6" passingDate="passingDate6" passingTz="2" arrTrack="arrTrack6"
                      depTrack="depTrack6" rtDepTime="rtDepTime6" rtDepDate="rtDepDate6" rtDepTz="2"
                      rtArrTime="rtArrTime6" rtArrDate="rtArrDate6" rtArrTz="2" rtArrTrack="rtArrTrack6"
                      rtDepTrack="rtDepTrack6" rtPassingTime="rtPassingTime6" rtPassingDate="rtPassingDate6"
                      rtPassingTz="2" cancelled="true" hasMainMast="false" mainMastId="mainMastId6"
                      mainMastExtId="mainMastExtId6"/>
            </Stops>
        </Leg>
        <Leg idx="anySimpleType" name="name3" number="number3" category="category3" type="type3" cancelled="false"
             partCancelled="false" reachable="false" direction="direction3" duration="P10675199DT2H48M5.477S"
             dist="2147483647">
            <Origin name="name3" type="POI" id="id3" extId="extId3" lon="79228162514264337593543950335"
                    lat="79228162514264337593543950335" routeIdx="2147483647" prognosisType="REPORTED" time="time3"
                    date="date3" tz="-2147483647" track="track3" rtTime="rtTime3" rtDate="rtDate3" rtTz="-2147483647"
                    rtTrack="rtTrack3" hasMainMast="true" mainMastId="mainMastId3" mainMastExtId="mainMastExtId3">
                <Notes>
                    <Note key="key7" type="A" priority="2147483646" routeIdxFrom="2147483646" routeIdxTo="2147483646">
                        Note7
                    </Note>
                    <Note key="key8" type="I" priority="-1" routeIdxFrom="-1" routeIdxTo="-1">Note8</Note>
                    <Note key="key9" type="R" priority="3" routeIdxFrom="3" routeIdxTo="3">Note9</Note>
                </Notes>
            </Origin>
            <Destination name="name3" type="POI" id="id3" extId="extId3" lon="79228162514264337593543950335"
                         lat="79228162514264337593543950335" routeIdx="2147483647" prognosisType="REPORTED" time="time3"
                         date="date3" tz="-2147483647" track="track3" rtTime="rtTime3" rtDate="rtDate3"
                         rtTz="-2147483647" rtTrack="rtTrack3" hasMainMast="true" mainMastId="mainMastId3"
                         mainMastExtId="mainMastExtId3"/>
            <JourneyDetailRef ref="ref3"/>
            <GeometryRef ref="anySimpleType"/>
            <GisRef ref="ref3"/>
            <GisRoute dist="2147483647" durS="P10675199DT2H48M5.477S" durR="P10675199DT2H48M5.477S"
                      durST="P10675199DT2H48M5.477S" durW2C="P10675199DT2H48M5.477S" durW2D="P10675199DT2H48M5.477S"
                      dirTxt="dirTxt3" dirGeo="2147483647">
                <seg name="name7" rType="TR" rNum="rNum7" man="KL" manTx="manTx7" dirTx="dirTx7" ori="SE"
                     polyS="2147483646" polyE="2147483646" dist="2147483646"/>
                <seg name="name8" rType="NT" rNum="rNum8" man="KR" manTx="manTx8" dirTx="dirTx8" ori="NW" polyS="-1"
                     polyE="-1" dist="-1"/>
                <seg name="name9" rType="CT" rNum="rNum9" man="HL" manTx="manTx9" dirTx="dirTx9" ori="SW" polyS="3"
                     polyE="3" dist="3"/>
                <polyline name="name3" delta="true" dim="-2147483647" type="PLANAR" crdEncYX="crdEncYX3"
                          crdEncZ="crdEncZ3" crdEncS="crdEncS3">
                    <crd>2147483646</crd>
                    <crd>-1</crd>
                    <crd>3</crd>
                </polyline>
                <altPolyline name="name7" delta="true" dim="-2147483646" type="HAFASGEO" crdEncYX="crdEncYX7"
                             crdEncZ="crdEncZ7" crdEncS="crdEncS7">
                    <crd>2147483643</crd>
                    <crd>-4</crd>
                    <crd>6</crd>
                </altPolyline>
                <altPolyline name="name8" delta="false" dim="2147483646" type="WGS84" crdEncYX="crdEncYX8"
                             crdEncZ="crdEncZ8" crdEncS="crdEncS8">
                    <crd>-2147483642</crd>
                    <crd>2147483642</crd>
                    <crd>-5</crd>
                </altPolyline>
                <altPolyline name="name9" delta="true" dim="-1" type="PLANAR" crdEncYX="crdEncYX9" crdEncZ="crdEncZ9"
                             crdEncS="crdEncS9">
                    <crd>7</crd>
                    <crd>-2147483641</crd>
                    <crd>2147483641</crd>
                </altPolyline>
            </GisRoute>
            <JourneyStatus>A</JourneyStatus>
            <Product name="name3" num="num3" line="line3" catOut="catOut3" catIn="catIn3" catCode="catCode3"
                     catOutS="catOutS3" catOutL="catOutL3" operatorCode="operatorCode3" operator="operator3"
                     admin="admin3"/>
            <Polyline name="name3" delta="true" dim="-2147483647" type="PLANAR" crdEncYX="crdEncYX3" crdEncZ="crdEncZ3"
                      crdEncS="crdEncS3">
                <crd>2147483646</crd>
                <crd>-1</crd>
                <crd>3</crd>
            </Polyline>
            <Stops>
                <Stop name="name7" id="id7" extId="extId7" routeIdx="2147483646" lon="79228162514264337593543950335"
                      lat="79228162514264337593543950335" arrPrognosisType="MANUAL" depPrognosisType="MANUAL"
                      depTime="depTime7" depDate="depDate7" depTz="-2147483646" arrTime="arrTime7" arrDate="arrDate7"
                      arrTz="-2147483646" passingTime="passingTime7" passingDate="passingDate7" passingTz="-2147483646"
                      arrTrack="arrTrack7" depTrack="depTrack7" rtDepTime="rtDepTime7" rtDepDate="rtDepDate7"
                      rtDepTz="-2147483646" rtArrTime="rtArrTime7" rtArrDate="rtArrDate7" rtArrTz="-2147483646"
                      rtArrTrack="rtArrTrack7" rtDepTrack="rtDepTrack7" rtPassingTime="rtPassingTime7"
                      rtPassingDate="rtPassingDate7" rtPassingTz="-2147483646" cancelled="false" hasMainMast="true"
                      mainMastId="mainMastId7" mainMastExtId="mainMastExtId7"/>
                <Stop name="name8" id="id8" extId="extId8" routeIdx="-1" lon="0.8" lat="0.8" arrPrognosisType="REPORTED"
                      depPrognosisType="REPORTED" depTime="depTime8" depDate="depDate8" depTz="2147483646"
                      arrTime="arrTime8" arrDate="arrDate8" arrTz="2147483646" passingTime="passingTime8"
                      passingDate="passingDate8" passingTz="2147483646" arrTrack="arrTrack8" depTrack="depTrack8"
                      rtDepTime="rtDepTime8" rtDepDate="rtDepDate8" rtDepTz="2147483646" rtArrTime="rtArrTime8"
                      rtArrDate="rtArrDate8" rtArrTz="2147483646" rtArrTrack="rtArrTrack8" rtDepTrack="rtDepTrack8"
                      rtPassingTime="rtPassingTime8" rtPassingDate="rtPassingDate8" rtPassingTz="2147483646"
                      cancelled="true" hasMainMast="false" mainMastId="mainMastId8" mainMastExtId="mainMastExtId8"/>
                <Stop name="name9" id="id9" extId="extId9" routeIdx="3" lon="1.2" lat="1.2" arrPrognosisType="CORRECTED"
                      depPrognosisType="CORRECTED" depTime="depTime9" depDate="depDate9" depTz="-1" arrTime="arrTime9"
                      arrDate="arrDate9" arrTz="-1" passingTime="passingTime9" passingDate="passingDate9" passingTz="-1"
                      arrTrack="arrTrack9" depTrack="depTrack9" rtDepTime="rtDepTime9" rtDepDate="rtDepDate9"
                      rtDepTz="-1" rtArrTime="rtArrTime9" rtArrDate="rtArrDate9" rtArrTz="-1" rtArrTrack="rtArrTrack9"
                      rtDepTrack="rtDepTrack9" rtPassingTime="rtPassingTime9" rtPassingDate="rtPassingDate9"
                      rtPassingTz="-1" cancelled="false" hasMainMast="true" mainMastId="mainMastId9"
                      mainMastExtId="mainMastExtId9"/>
            </Stops>
        </Leg>
    </LegList>
    <TariffResult>
        <fareSetItem name="name1" desc="desc1">
            <ticketParam name="name1" value="value1"/>
            <ticketParam name="name2" value="value2"/>
            <ticketParam name="name3" value="value3"/>
            <fareItem name="name1" desc="desc1" price="0" cur="cur1" shpCtx="shpCtx1">
                <ticket name="name1" desc="desc1" price="0" cur="cur1" shpCtx="shpCtx1">
                    <ticketParam name="name1" value="value1"/>
                    <ticketParam name="name2" value="value2"/>
                    <ticketParam name="name3" value="value3"/>
                </ticket>
                <ticket name="name2" desc="desc2" price="1" cur="cur2" shpCtx="shpCtx2">
                    <ticketParam name="name4" value="value4"/>
                    <ticketParam name="name5" value="value5"/>
                    <ticketParam name="name6" value="value6"/>
                </ticket>
                <ticket name="name3" desc="desc3" price="-2147483647" cur="cur3" shpCtx="shpCtx3">
                    <ticketParam name="name7" value="value7"/>
                    <ticketParam name="name8" value="value8"/>
                    <ticketParam name="name9" value="value9"/>
                </ticket>
            </fareItem>
            <fareItem name="name2" desc="desc2" price="1" cur="cur2" shpCtx="shpCtx2">
                <ticket name="name4" desc="desc4" price="2147483647" cur="cur4" shpCtx="shpCtx4">
                    <ticketParam name="name10" value="value10"/>
                    <ticketParam name="name11" value="value11"/>
                    <ticketParam name="name12" value="value12"/>
                </ticket>
                <ticket name="name5" desc="desc5" price="0" cur="cur5" shpCtx="shpCtx5">
                    <ticketParam name="name13" value="value13"/>
                    <ticketParam name="name14" value="value14"/>
                    <ticketParam name="name15" value="value15"/>
                </ticket>
                <ticket name="name6" desc="desc6" price="2" cur="cur6" shpCtx="shpCtx6">
                    <ticketParam name="name16" value="value16"/>
                    <ticketParam name="name17" value="value17"/>
                    <ticketParam name="name18" value="value18"/>
                </ticket>
            </fareItem>
            <fareItem name="name3" desc="desc3" price="-2147483647" cur="cur3" shpCtx="shpCtx3">
                <ticket name="name7" desc="desc7" price="-2147483646" cur="cur7" shpCtx="shpCtx7">
                    <ticketParam name="name19" value="value19"/>
                    <ticketParam name="name20" value="value20"/>
                    <ticketParam name="name21" value="value21"/>
                </ticket>
                <ticket name="name8" desc="desc8" price="2147483646" cur="cur8" shpCtx="shpCtx8">
                    <ticketParam name="name22" value="value22"/>
                    <ticketParam name="name23" value="value23"/>
                    <ticketParam name="name24" value="value24"/>
                </ticket>
                <ticket name="name9" desc="desc9" price="-1" cur="cur9" shpCtx="shpCtx9">
                    <ticketParam name="name25" value="value25"/>
                    <ticketParam name="name26" value="value26"/>
                    <ticketParam name="name27" value="value27"/>
                </ticket>
            </fareItem>
        </fareSetItem>
        <fareSetItem name="name2" desc="desc2">
            <ticketParam name="name4" value="value4"/>
            <ticketParam name="name5" value="value5"/>
            <ticketParam name="name6" value="value6"/>
            <fareItem name="name4" desc="desc4" price="2147483647" cur="cur4" shpCtx="shpCtx4">
                <ticket name="name10" desc="desc10" price="3" cur="cur10" shpCtx="shpCtx10">
                    <ticketParam name="name28" value="value28"/>
                    <ticketParam name="name29" value="value29"/>
                    <ticketParam name="name30" value="value30"/>
                </ticket>
                <ticket name="name11" desc="desc11" price="-2147483645" cur="cur11" shpCtx="shpCtx11">
                    <ticketParam name="name31" value="value31"/>
                    <ticketParam name="name32" value="value32"/>
                    <ticketParam name="name33" value="value33"/>
                </ticket>
                <ticket name="name12" desc="desc12" price="2147483645" cur="cur12" shpCtx="shpCtx12">
                    <ticketParam name="name34" value="value34"/>
                    <ticketParam name="name35" value="value35"/>
                    <ticketParam name="name36" value="value36"/>
                </ticket>
            </fareItem>
            <fareItem name="name5" desc="desc5" price="0" cur="cur5" shpCtx="shpCtx5">
                <ticket name="name13" desc="desc13" price="-2" cur="cur13" shpCtx="shpCtx13">
                    <ticketParam name="name37" value="value37"/>
                    <ticketParam name="name38" value="value38"/>
                    <ticketParam name="name39" value="value39"/>
                </ticket>
                <ticket name="name14" desc="desc14" price="4" cur="cur14" shpCtx="shpCtx14">
                    <ticketParam name="name40" value="value40"/>
                    <ticketParam name="name41" value="value41"/>
                    <ticketParam name="name42" value="value42"/>
                </ticket>
                <ticket name="name15" desc="desc15" price="-2147483644" cur="cur15" shpCtx="shpCtx15">
                    <ticketParam name="name43" value="value43"/>
                    <ticketParam name="name44" value="value44"/>
                    <ticketParam name="name45" value="value45"/>
                </ticket>
            </fareItem>
            <fareItem name="name6" desc="desc6" price="2" cur="cur6" shpCtx="shpCtx6">
                <ticket name="name16" desc="desc16" price="2147483644" cur="cur16" shpCtx="shpCtx16">
                    <ticketParam name="name46" value="value46"/>
                    <ticketParam name="name47" value="value47"/>
                    <ticketParam name="name48" value="value48"/>
                </ticket>
                <ticket name="name17" desc="desc17" price="-3" cur="cur17" shpCtx="shpCtx17">
                    <ticketParam name="name49" value="value49"/>
                    <ticketParam name="name50" value="value50"/>
                    <ticketParam name="name51" value="value51"/>
                </ticket>
                <ticket name="name18" desc="desc18" price="5" cur="cur18" shpCtx="shpCtx18">
                    <ticketParam name="name52" value="value52"/>
                    <ticketParam name="name53" value="value53"/>
                    <ticketParam name="name54" value="value54"/>
                </ticket>
            </fareItem>
        </fareSetItem>
        <fareSetItem name="name3" desc="desc3">
            <ticketParam name="name7" value="value7"/>
            <ticketParam name="name8" value="value8"/>
            <ticketParam name="name9" value="value9"/>
            <fareItem name="name7" desc="desc7" price="-2147483646" cur="cur7" shpCtx="shpCtx7">
                <ticket name="name19" desc="desc19" price="-2147483643" cur="cur19" shpCtx="shpCtx19">
                    <ticketParam name="name55" value="value55"/>
                    <ticketParam name="name56" value="value56"/>
                    <ticketParam name="name57" value="value57"/>
                </ticket>
                <ticket name="name20" desc="desc20" price="2147483643" cur="cur20" shpCtx="shpCtx20">
                    <ticketParam name="name58" value="value58"/>
                    <ticketParam name="name59" value="value59"/>
                    <ticketParam name="name60" value="value60"/>
                </ticket>
                <ticket name="name21" desc="desc21" price="-4" cur="cur21" shpCtx="shpCtx21">
                    <ticketParam name="name61" value="value61"/>
                    <ticketParam name="name62" value="value62"/>
                    <ticketParam name="name63" value="value63"/>
                </ticket>
            </fareItem>
            <fareItem name="name8" desc="desc8" price="2147483646" cur="cur8" shpCtx="shpCtx8">
                <ticket name="name22" desc="desc22" price="6" cur="cur22" shpCtx="shpCtx22">
                    <ticketParam name="name64" value="value64"/>
                    <ticketParam name="name65" value="value65"/>
                    <ticketParam name="name66" value="value66"/>
                </ticket>
                <ticket name="name23" desc="desc23" price="-2147483642" cur="cur23" shpCtx="shpCtx23">
                    <ticketParam name="name67" value="value67"/>
                    <ticketParam name="name68" value="value68"/>
                    <ticketParam name="name69" value="value69"/>
                </ticket>
                <ticket name="name24" desc="desc24" price="2147483642" cur="cur24" shpCtx="shpCtx24">
                    <ticketParam name="name70" value="value70"/>
                    <ticketParam name="name71" value="value71"/>
                    <ticketParam name="name72" value="value72"/>
                </ticket>
            </fareItem>
            <fareItem name="name9" desc="desc9" price="-1" cur="cur9" shpCtx="shpCtx9">
                <ticket name="name25" desc="desc25" price="-5" cur="cur25" shpCtx="shpCtx25">
                    <ticketParam name="name73" value="value73"/>
                    <ticketParam name="name74" value="value74"/>
                    <ticketParam name="name75" value="value75"/>
                </ticket>
                <ticket name="name26" desc="desc26" price="7" cur="cur26" shpCtx="shpCtx26">
                    <ticketParam name="name76" value="value76"/>
                    <ticketParam name="name77" value="value77"/>
                    <ticketParam name="name78" value="value78"/>
                </ticket>
                <ticket name="name27" desc="desc27" price="-2147483641" cur="cur27" shpCtx="shpCtx27">
                    <ticketParam name="name79" value="value79"/>
                    <ticketParam name="name80" value="value80"/>
                    <ticketParam name="name81" value="value81"/>
                </ticket>
            </fareItem>
        </fareSetItem>
    </TariffResult>
</Trip>
```

## JourneyDetail

JourneyDetail is used to obtain detailed information about a journey/leg.
This is based on first calling trip. (See 2.4)
In the response from trip, you get a reference, for example,

```xml

<JourneyDetailRef ref="1|3598|0|74|13062017">...</JourneyDetailRef>
```

This reference is used when calling JourneyDetail for the specific journey. The entire line stretch
for the specified journey is returned. If you only want information about stops in the part of the journey
that a search with trip provides, it is recommended to set passlist=1 in trip. This is an extension from api-version 2.

### Parameters

| Name | Description                    | Comment                                                                                                                                       |
|------|--------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| id   | Reference from Trip, see above | It may be necessary to escape the \| character by its URL encoding %7C.                                                                       |
| date | yyyy-MM-DD                     | Optional<br>Provides the corresponding journey on another day, if possible                                                                    |
| poly | 0 or 1                         | Optional.<br>Indicates whether detailed routes should be calculated for the results. For a description of the polyline, see 2.4.5. Default 0. |

Example:

```text
https://journeyplanner.integration.sl.se/v1/TravelplannerV3_1/journeydetail.&lt;FORMAT&gt;?key=&lt;DIN API NYCKEL&gt;&amp;id=1|3598|0|74|13062017
```

# Real-time

If there is real-time information, it is indicated in separate extra fields. For real-time times in JourneyDetail, "rtArrTime," "rtArrDate," "rtDepTime," and "
rtDepDate" are added to the response. The old fields "arrTime," "arrDate," "depTime," and "depDate" are retained to track changes.

# Response Structure

In the table below, the XML structure is described. Some obvious attributes are not included to keep it concise, such as Lat and Lon for a clearer overview of
less obvious elements.

**Example explanation of the structure in the table:**

- element1/element2 => element2 is a sub-element to element1.
- element1.attribut1 => attribut1 is an attribute of element1.

| Name                     | Data Type | Description                                                                                                                     |
|--------------------------|-----------|---------------------------------------------------------------------------------------------------------------------------------|
| JourneyDetail            | Element   | Root element.                                                                                                                   |
| JourneyDetail/Notes      | Element   | Contains notes to be displayed for the journey.                                                                                 |
| JourneyDetail/Stops      | List      | List of stops for this journey.                                                                                                 |
| Stops/Stop               | Element   | Stop contains the name of the stop, route index, latitude, longitude, departure date and time, arrival date and time.           |
| Stop.id                  | Attribute | Id for the specified location in the list of stops. Can be used for further travel from that point.                             |
| Stop.routeIdx            | Attribute | Used in conjunction with routeIdx in the Trip response in a search, to know which part of the list is relevant for the journey. |
| JourneyDetail/Directions | List      | List of directions.                                                                                                             |
| Directions/Direction     | Element   | Direction information.                                                                                                          |
| JourneyDetail/Types      | List      | List of travel types.                                                                                                           |
| JourneyDetail/Names      | List      | List of elements.                                                                                                               |
| Names/Name               | Element   | Contains the name of the journey.                                                                                               |
| JourneyDetail/Messages   | List      | Contains a list of real-time messages to be displayed.                                                                          |
| Polyline                 | Element   | Detailed route if poly=1 is specified.                                                                                          |

## GisRoute

This service is used to obtain detailed information about the route. Since Trip does not return a polyline for walking and cycling, this is mainly used to draw
the cycling and walking path on the map. In the response from trip, a leg is obtained:

```xml

<Leg type="WALK" idx="1" dist="464" duration="PT6M" name="">
    <Origin id="A=1@O=Stockholm City@X=18059500@Y=59331143@U=74@L=400105313@" extId="400105313" name="Stockholm City"
            type="ST" lon="18.0595" lat="59.331143" hasMainMast="true"
            mainMastId="A=1@O=Centralen (Stockholm)@X=18057657@Y=59331134@U=74@L=300101002@" mainMastExtId="300101002"
            date="2019-02-12" time="08:45:00"/>
    <Destination id="A=2@O=Stockholm, Drottninggatan 22@l=@X=18065001@Y=59330415@u=0@"
                 name="Stockholm, Drottninggatan 22" type="ADR" lon="18.065001" lat="59.330415" date="2019-02-12"
                 time="08:51:00"/>
    <GisRef ref="G|1|G@F|A=1@O=Stockholm City@X=18059500@Y=59331143@U=74@L=400105313@|A=2@O=Stockholm, Drottninggatan 22@l=@X=18065001@Y=59330415@u=0@|12022019|84500|85100|ft|ft@0@1000@120@-1@100@1@1000@0@@@@@false@0@-1@$f@$f@$f@$f@$f@$§bt@0@2000@120@-1@100@1@1000@0@@@@@false@0@-1@$f@$f@$f@$f@$f@$§tt@0@5000@120@-1@100@1@2500@0@@@@@false@0@-1@$f@$f@$f@$f@$f@$§|"/>
</Leg>

```

The value in the "ref" in the GisRef object is used as input for gisroute.

### Parameters

| Name | Description                    | Description                                                                                  |
|------|--------------------------------|----------------------------------------------------------------------------------------------|
| ctx  |                                | The value in ctxRecon obtained in the response from trip.                                    |
| lang | sv = Swedish<br />en = English |                                                                                              |
| poly | 0 or 1                         | Optional. Specifies whether detailed routes should be calculated for the results. Default 0. |

Example:

```text
http://https://journeyplanner.integration.sl.se/v1/TravelplannerV3_1/gisroute.&lt;FORMAT&gt;?key=&lt;YOUR API KEY&gt;&amp;ctx=G|1|G@F|A=1@O=Stockholm%20City@X=18059500@Y=59331143@U=74@L=400105313@|A=2@O=Stockholm,%20Drottninggatan%2022@l=@X=18065001@Y=59330415@u=0@|12022019|84500|85100|ft|ft@0@1000@120@-1@100@1@1000@0@@@@@false@0@-1@$f@$f@$f@$f@$f@$%C2%A7bt@0@2000@120@-1@100@1@1000@0@@@@@false@0@-1@$f@$f@$f@$f@$f@$%C2%A7tt@0@5000@120@-1@100@1@2500@0@@@@@false@0@-1@$f@$f@$f@$f@$f@$%C2%A7%7C&amp;lang=sv&amp;poly=1
```

### Response Structure

The response from gisroute is the same as for the result from trip, with the difference that there is only one journey in the result. It also includes an object
to describe the route, GisRoute:

```xml

<GisRoute dist="189" durS="PT2M">
    <seg dist="22" man="ST" manTx="Fortsätt på Renstiernas gata" name="Renstiernas gata" ori="N" polyE="10" polyS="7"
         rType="CT"/>
    <seg man="TO" manTx="Ankomst på Renstiernas gata"/>
    <polyline type="WGS84" dim="3" crdEncS="NNNNNHMNNNN" crdEncZ="???????????" delta="true">
        <crd>18.080803</crd>
        <crd>59.315164</crd>
        <crd>0.0</crd>
        <crd>3.45E-4</crd>
        <crd>4.1E-5</crd>
        <crd>0.0</crd>
        <crd>-2.7E-5</crd>
        <crd>6.1E-5</crd>
        <crd>0.0</crd>
        <crd>9.0E-5</crd>
        <crd>1.1E-5</crd>
        <crd>0.0</crd>
        <crd>2.5E-5</crd>
        <crd>2.7E-5</crd>
        <crd>0.0</crd>
        <crd>9.9E-5</crd>
        <crd>4.0E-6</crd>
        <crd>0.0</crd>
        <crd>1.7E-4</crd>
        <crd>1.5E-5</crd>
        <crd>0.0</crd>
        <crd>0.001985</crd>
        <crd>2.48E-4</crd>
        <crd>0.0</crd>
        <crd>8.8E-5</crd>
        <crd>1.1E-5</crd>
        <crd>0.0</crd>
        <crd>4.0E-5</crd>
        <crd>3.5E-5</crd>
        <crd>0.0</crd>
        <crd>-4.9E-5</crd>
        <crd>1.05E-4</crd>
        <crd>0.0</crd>
    </polyline>
</GisRoute>
```

The segments describe parts of the journey, and the polyline describes coordinates in the same way documented in the Trip.

## Reconstruction

To reconstruct a journey retrieved via the trip service, the reconstruction service can be used (for example, for sharing functions or similar).

In the response from trip, you get:

```xml

<Trip idx="0" ctxRecon="T$A=1@O=T-Centralen@L=400101052@a=128@$A=1@O=Slussen@L=400101012@a=128@$201706140859$201706140902$ $" checksum="774B67E9_4" tripId="C-0"
      duration="PT3M">...
</Trip>
```

The value in ctxRecon is used as input for reconstruction

### Parameters

| Name | Description        | Description                                                                       |
|------|--------------------|-----------------------------------------------------------------------------------|
| ctx  |                    | The value in ctxRecon obtained in the response from trip.                         |
| poly | 0 or 1             | Optional. Specifies whether detailed routes should be calculated for the results. |
| date | Date< (YYYY-MM-DD) | Optional. Tries to reconstruct a journey on the specified date, if possible.      |

Example:

```text
https://journeyplanner.integration.sl.se/v1/TravelplannerV3_1/reconstruction.<FORMAT>?key=<DIN API NYCKEL>&amp;ctx=T%24A%3D1%40O%3DT-Centralen%40L%3D400101052%40a%3D128%40%24A%3D1%40O%3DSlussen%40L%3D400101012%40a%3D128%40%24201706140859%24201706140902%24%20%24
```

## Response Structure

The response from reconstruction is the same as the result from trip, with the difference that there is only one journey in the result.

## XSD

Returns an XSD containing definitions for all the components of the response structures for the services in SL Reseplanerare 3.

### Parameters

No specific parameters are used for this service.

Example:

```text
https://journeyplanner.integration.sl.se/v1/TravelplannerV3_1/xsd.xml?key=<DIN API NYCKEL>.xsd
```

## TTI – Time Table Info

The Time Table Info service shows for which time period timetable data is available in the journey planner. The information can, for example, be used to
highlight a searchable time period in a calendar.

### Parameters

No specific parameters are used for this service.

Example:

```text
https://journeyplanner.integration.sl.se/v1/TravelplannerV3_1/tti?key=<DIN API NYCKEL>
```

### Response Structure

The response contains information about the valid search period, in the example below, the date interval is from 2016-12-11 to 2018-12-08.

```xml

<TimetableInfoList serverVersion="1.7.6" dialectVersion="1.23" requestId="1507536412387"
                   begin="2016-12-11" end="2018-12-08">
    <TimetableInfo ident="7mtpu" date="2017-10-05" time="10:50:08"/>
    <TimetableInfo ident="65wha" date="2017-09-26" time="07:30:36"/>
    <TimetableInfo ident="6jpdq" date="2017-09-14" time="07:50:04"/>
    <TimetableInfo ident="2x6uq" date="2017-07-06" time="09:19:28"/>
</TimetableInfoList>
```

## Error Messages

| Status Code | Message                                                                                      |
|-------------|----------------------------------------------------------------------------------------------|
| 1001        | Problem with the request: Key is not present in the requests                                 |
| 1002        | Problem with the request: Key is invalid                                                     |
| 1003        | Invalid API.                                                                                 |
| 1004        | Problem with the request: This API is currently not available for keys with priority above 2 |
| 1005        | Key exists but not for this API<br>Problem with the request: Invalid API for key             |
| 1006        | Too many requests per minute for the used profile.                                           |
| 1007        | Too many requests per month for the used profile.                                            |

## Differences compared to TravelPlannerV3

The XSD has been updated, but apart from the changes listed below, the existing functions are not affected.

**Changes:**

- The format of coordinates in the polyline in the Trip request has been modified. They are now described using double values, and difference values are
  indicated with exponents.
