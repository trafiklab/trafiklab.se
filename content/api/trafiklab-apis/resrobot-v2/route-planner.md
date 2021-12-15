---
title: ResRobot Route planner
weight: 20
date: 2015-06-24
aliases: 
  - /api/trafiklab-apis/resrobot-reseplanerare/dokumentation
  - /api/resrobot-reseplanerare/dokumentation/sokresa
  - /api/resrobot-reseplanerare/dokumentation/
  - /api/resrobot-reseplanerare
---
## What does this API provide?

ResRobot Route planner provides routes between two stops or points. Users can specify the start and end point, date,
time, transport modes, and more.

{{% warning %}}
**New version available**

A new version, version 2.1, of ResRobot is available. Existing apps should migrate to the new version,
and it is no longer possible to build new apps on version 2.0.

**Version 2.0, which you are currently looking at, will be discontinued at April 30th, 2022.**   
{{% /warning %}}

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

## Using ResRobot Route planner

ResRobot route planner consists of two different endpoints, one for departures and one for arrivals. Both endpoints take
exactly the same parameters and have the same response structure. API Calls take the stop id as a parameter, as well as
some other parameters to fine-tune the results. It returns a list of departures or arrivals from the given stop,
including a bit of information about each vehicle, such as where it is heading or where it comes from.

{{% info %}}
Only the most important parameters and response variables are described on this page. Looking for more technical
details? These can be found in [the OpenAPI specification](api-specification.md).
{{% /info %}}

{{% warning %}}
**New version available**

A new version of ResRobot is available. Existing apps should migrate to the new version, and it is no longer possible to
build new apps on version 2.0.
{{% /warning %}}

## Example call

This example call retrieves all routes from Stockholm Central Station (740000001) to Malmö Central Station
(740000003), departing right now (since no specific time or date is specified in the call).

### Call
{{% tabs %}} 
{{% tab "Json" %}}
```text
https://api.resrobot.se/v2/trip?format=json&originId=740000001&destId=740000003&passlist=true&showPassingPoints=true&key=API_KEY
```
{{% /tab %}}
{{% tab "Xml" %}}
```text
https://api.resrobot.se/v2/trip?format=xml&originId=740000001&destId=740000003&passlist=true&showPassingPoints=true&key
=API_KEY
```
{{% /tab %}}
{{% /tabs %}} 

#### Request parameters

| **Name**                        | **Data type**            | **Required**                                                   | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ------------------------------- | ------------------------ | -------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| key                             | String                   | Yes                                                            | Your API key.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| lang                            | String (sv/en/de)        | No, default sv                                                 | Language to use in the response. Affects both data (names for different transport types) and error messages.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| date                            | Date (YYYY-MM-DD)        | No, default today                                              | Search on a specific date, specified in YYYY-MM-DD format, e.g. 2021-12-31.<br>You can only search for dates within the timetable period, defined by planningPeriodBegin and planningPeriodEnd which is present in all route-planning responses.                                                                                                                                                                                                                                                                                                                                                                                                |
| time                            | Time (HH:MM)             | No, default now                                                | Search on a specific time, specified in HH:MM format, e.g. 19:06.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| searchForArrival                | Integer (0/1)            | No, default 0                                                  | Search for a latest arrival date/time instead of seraching for a first departure date/time                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| originId                        | String                   | Either originId or originCoordLat+originCoordLong are required | Stop id to search a route from. Can be obtained from the Stop lookup API, Nearby stops API, or GTFS Sverige 2                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| originCoordLat, originCoordLong | String                   | Either originId or originCoordLat+originCoordLong are required | Coordinates of the origin. ResRobot will calculate walking legs if needed<br>Latitude (WGS84, decimal degree), ex 59.330150<br>Longitude (WGS84, decimal degree), ex 18.056618                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| destId                          | String                   | Either destId or destCoordLat+destCoordLong are required       | Stop id to search a route to. Can be obtained from the Stop lookup API, Nearby stops API, or GTFS Sverige 2                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| destCoordLat, destCoordLong     | String                   | Either destId or destCoordLat+destCoordLong are required       | Coordinates of the destination. ResRobot will calculate walking legs if needed<br>Latitude (WGS84, decimal degree), ex 59.330150<br>Longitude (WGS84, decimal degree), ex 18.056618                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| viaId                           | String                   | No, default no via                                             | Id of an additional stop that should be passed on the way.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| numF                            | Integer                  | No, default 6                                                  | Number of results to fetch, departing after the specified date/time. The sum of numF and numB should not be more than 6. Ignored when searchForArrival is set to 1.                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| numB                            | Integer                  | No, default 0                                                  | Number of results to fetch, departing before the specified date/time. The sum of numF and numB should not be more than 6. Ignored when searchForArrival is set to 1.                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| context                         | String                   | Np, default unspecified                                        | Reference for scrolling further up or down from a previous search result.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| maxChange                       | Integer (1-3)            | No, default unlimited                                          | Limits the maximum number of transfers.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| products                        | Integer                  | No, default all products                                       | Only include certain traffic modes, see [common request products](common.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| operators                       | comma seperated integers | No, default all operators                                      | Only include traffic from specified operators. Operators are specified by their id, which can be obtained from GTFS Sverige 2<br>Example: operators=275,287<br>(275=SL, 287=Arlanda Express)                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| passlist                        | Integer                  | No, default 1                                                  | Set to 1 to include a list of the stops which are passed on the route of a vehicle. 0 to leave the list out of the result.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| originWalk                      | comma separated integers | No                                                             | 4 comma separated values: `allow walks`,`minimum walking distance`,`maximum walking distance`,`walking speed in %`<br>`allow walks`: Set to `1` to allow walks to the first stop. Set to `0` to disable this.<br>`minimum walking distance`,`maximum walking distance`: Minimum and maximum distance in meters, between 0 and 10000.<br>`walking speed in %`: walking speed, relative to the default walking speed of 5km/h + 2 minutes to orient. Between 50 and 150%.<br>Walking between 0 and 1000 meters, at 75% of the normal speed look like this: `originWalk=1,0,1000,75`. To disable walking, `originWalk=0` suffices.                 |
| destWalk                        | comma separated integers | No                                                             | 4 comma separated values: `allow walks`,`minimum walking distance`,`maximum walking distance`,`walking speed in %`<br>`allow walks`: Set to `1` to allow walks from the last stop to the destination. Set to `0` to disable this.<br>`minimum walking distance`,`maximum walking distance`: Minimum and maximum distance in meters, between 0 and 10000.<br>`walking speed in %`: walking speed, relative to the default walking speed of 5km/h + 2 minutes to orient. Between 50 and 150%.<br>Walking between 0 and 1000 meters, at 75% of the normal speed look like this: `destwalk=1,0,1000,75`. To disable walking, `destwalk=0` suffices. |
| format                          | String                   | No, default XML                                                | The response format, json or XML                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |

### Response

{{% info %}} Note that an actual response contains more entries and stops - we removed some from this example
response since it's only meant to show the structure of the response. {{% /info %}}

{{% tabs %}} {{% tab "Json" %}}

```javascript
{
  "Trip": [
    {
      "ServiceDays": [
        {
          "planningPeriodBegin": "2020-05-29",
          "planningPeriodEnd": "2020-08-16",
          "sDaysR": "not every day",
          "sDaysI": "2. until 18. Jun 2020 Mo - Fr",
          "sDaysB": "9F3E7800000000000000"
        }
      ],
      "LegList": {
        "Leg": [
          {
            "Origin": {
              "name": "Stockholm Centralstation",
              "type": "ST",
              "id": "740000001",
              "extId": "740000001",
              "lon": 18.058151,
              "lat": 59.330136,
              "routeIdx": 0,
              "time": "11:41:00",
              "date": "2020-06-02"
            },
            "Destination": {
              "name": "Norrköping Centralstation",
              "type": "ST",
              "id": "740000007",
              "extId": "740000007",
              "lon": 16.183343,
              "lat": 58.596625,
              "routeIdx": 6,
              "time": "13:26:00",
              "date": "2020-06-02"
            },
            "Notes": {
              "Note": [
                {
                  "value": "Endast 2 klass",
                  "key": "AA",
                  "type": "A",
                  "priority": 100,
                  "routeIdxFrom": 0,
                  "routeIdxTo": 6
                },
                {
                  "value": "Ej reservering",
                  "key": "AE",
                  "type": "A",
                  "priority": 100,
                  "routeIdxFrom": 0,
                  "routeIdxTo": 2
                },
                {
                  "value": "no WiFi",
                  "key": "SX",
                  "type": "A",
                  "priority": 100,
                  "routeIdxFrom": 0,
                  "routeIdxTo": 6
                },
                {
                  "value": "no A/C",
                  "key": "SY",
                  "type": "A",
                  "priority": 100,
                  "routeIdxFrom": 0,
                  "routeIdxTo": 6
                }
              ]
            },
            "Product": {
              "name": "Regional Tåg 231",
              "num": "231",
              "catCode": "2",
              "catOutS": "JRE",
              "catOutL": "Regional Tåg",
              "operatorCode": "74",
              "operator": "SJ",
              "operatorUrl": "http://www.sj.se"
            },
            "Stops": {
              "Stop": [
                {
                  "name": "Stockholm Centralstation",
                  "id": "740000001",
                  "extId": "740000001",
                  "routeIdx": 0,
                  "lon": 18.058151,
                  "lat": 59.330136,
                  "depTime": "11:41:00",
                  "depDate": "2020-06-02"
                },
                {
                  "name": "Kolmården station (Norrköping kn)",
                  "id": "740001545",
                  "extId": "740001545",
                  "routeIdx": 5,
                  "lon": 16.362597,
                  "lat": 58.675424,
                  "depTime": "13:09:00",
                  "depDate": "2020-06-02",
                  "arrTime": "13:09:00",
                  "arrDate": "2020-06-02"
                },
                {
                  "name": "Norrköping Centralstation",
                  "id": "740000007",
                  "extId": "740000007",
                  "routeIdx": 6,
                  "lon": 16.183343,
                  "lat": 58.596625,
                  "arrTime": "13:26:00",
                  "arrDate": "2020-06-02"
                }
              ]
            },
            "idx": "0",
            "name": "Regional Tåg 231",
            "transportNumber": "231",
            "transportCategory": "JRE",
            "type": "JNY",
            "reachable": true,
            "direction": "Norrköping Centralstation"
          },
          {
            "Origin": {
              "name": "Norrköping Centralstation",
              "type": "ST",
              "id": "740000007",
              "extId": "740000007",
              "lon": 16.183343,
              "lat": 58.596625,
              "routeIdx": 0,
              "time": "13:48:00",
              "date": "2020-06-02"
            },
            "Destination": {
              "name": "Mjölby station",
              "type": "ST",
              "id": "740000180",
              "extId": "740000180",
              "lon": 15.131992,
              "lat": 58.322984,
              "routeIdx": 6,
              "time": "14:35:00",
              "date": "2020-06-02"
            },
            "Notes": {
              "Note": [
                {
                  "value": "Endast 2 klass",
                  "key": "AA",
                  "type": "A",
                  "priority": 100,
                  "routeIdxFrom": 0,
                  "routeIdxTo": 6
                },
                {
                  "value": "Ej reservering",
                  "key": "AE",
                  "type": "A",
                  "priority": 100,
                  "routeIdxFrom": 0,
                  "routeIdxTo": 6
                }
              ]
            },
            "Product": {
              "name": "Länstrafik - Tåg 8739",
              "num": "8739",
              "catCode": "4",
              "catOutS": "JLT",
              "catOutL": "Länstrafik - Tåg",
              "operatorCode": "253",
              "operator": "ÖstgötaTrafiken",
              "operatorUrl": "http://www.ostgotatrafiken.se/"
            },
            "Stops": {
              "Stop": [
                {
                  "name": "Norrköping Centralstation",
                  "id": "740000007",
                  "extId": "740000007",
                  "routeIdx": 0,
                  "lon": 16.183343,
                  "lat": 58.596625,
                  "depTime": "13:48:00",
                  "depDate": "2020-06-02"
                },
                {
                  "name": "Kimstad station (Norrköping kn)",
                  "id": "740068883",
                  "extId": "740068883",
                  "routeIdx": 1,
                  "lon": 15.971764,
                  "lat": 58.546106,
                  "depTime": "13:59:00",
                  "depDate": "2020-06-02",
                  "arrTime": "13:59:00",
                  "arrDate": "2020-06-02"
                },
                {
                  "name": "Mjölby station",
                  "id": "740000180",
                  "extId": "740000180",
                  "routeIdx": 6,
                  "lon": 15.131992,
                  "lat": 58.322984,
                  "arrTime": "14:35:00",
                  "arrDate": "2020-06-02"
                }
              ]
            },
            "idx": "1",
            "name": "Länstrafik - Tåg 8739",
            "transportNumber": "8739",
            "transportCategory": "JLT",
            "type": "JNY",
            "reachable": true,
            "direction": "Motala station"
          },
  ],
  "scrB": "1|OB|MTµ11µ9501µ9341µ9763µ9851µ0µ0µ66133µ9319µ1µ-2147483616µ0µ1µ2|PDHµ60b11222cb3bfeafacd1e38613ce2846|RDµ2062020|RTµ111941",
  "scrF": "1|OF|MTµ11µ9741µ9741µ10003µ10003µ0µ0µ2613µ9631µ8µ-2147482606µ0µ1µ2|PDHµ60b11222cb3bfeafacd1e38613ce2846|RDµ2062020|RTµ111941"
}
    }
    ]
```

{{% /tab %}}

{{% tab "Xml" %}}

```xml
<?xml version="1.0" encoding="UTF-8"?>
<TripList scrB="1|OB|MTµ11µ9501µ9341µ9763µ9851µ0µ0µ66133µ9322µ1µ-2147483616µ0µ1µ2|PDHµ60b11222cb3bfeafacd1e38613ce2846|RDµ2062020|RTµ112220" scrF="1|OF|MTµ11µ9741µ9741µ10003µ10003µ0µ0µ2613µ9631µ8µ-2147482606µ0µ1µ2|PDHµ60b11222cb3bfeafacd1e38613ce2846|RDµ2062020|RTµ112220" xmlns="hafas_rest_v1">
    <Trip idx="0" ctxRecon="T$A=1@O=Stockholm Centralstation@L=740000001@a=128@$A=1@O=Norrköping Centralstation@L=740000007@a=128@$202006021141$202006021326$JRE  231$$1$§T$A=1@O=Norrköping Centralstation@L=740000007@a=128@$A=1@O=Mjölby station@L=740000180@a=128@$202006021348$202006021435$JLT 8739$$1$§T$A=1@O=Mjölby station@L=740000180@a=128@$A=1@O=Tranås station@L=740000041@a=128@$202006021447$202006021508$JLT18839$$1$§T$A=1@O=Tranås station@L=740000041@a=128@$A=1@O=Nässjö Centralstation@L=740000140@a=128@$202006021614$202006021641$JLT27621$$1$§T$A=1@O=Nässjö Centralstation@L=740000140@a=128@$A=1@O=Alvesta station@L=740000004@a=128@$202006021701$202006021753$JLT17619$$1$§T$A=1@O=Alvesta station@L=740000004@a=128@$A=1@O=Malmö Centralstation@L=740000003@a=128@$202006021833$202006022011$JRE 1101$$1$" tripId="C-0" duration="PT8H30M">
        <ServiceDays sDaysR="not every day" sDaysI="2. until 18. Jun 2020 Mo - Fr" sDaysB="9F3E7800000000000000" planningPeriodBegin="2020-05-29" planningPeriodEnd="2020-08-16"/>
        <LegList>
            <Leg type="JNY" idx="0" name="Regional Tåg 231" transportNumber="231" transportCategory="JRE" reachable="true" direction="Norrköping Centralstation">
                <Origin extId="740000001" id="740000001" name="Stockholm Centralstation" type="ST" routeIdx="0" lon="18.058151" lat="59.330136" date="2020-06-02" time="11:41:00"/>
                <Destination extId="740000007" id="740000007" name="Norrköping Centralstation" type="ST" routeIdx="6" lon="16.183343" lat="58.596625" date="2020-06-02" time="13:26:00"/>
                <Notes>
                    <Note routeIdxFrom="0" routeIdxTo="6" key="AA" priority="100" type="A">Endast 2 klass</Note>
                    <Note routeIdxFrom="0" routeIdxTo="2" key="AE" priority="100" type="A">Ej reservering</Note>
                    <Note routeIdxFrom="0" routeIdxTo="6" key="SX" priority="100" type="A">no WiFi</Note>
                    <Note routeIdxFrom="0" routeIdxTo="6" key="SY" priority="100" type="A">no A/C</Note>
                </Notes>
                <Product catCode="2" catOutL="Regional Tåg" catOutS="JRE" name="Regional Tåg 231" num="231" operator="SJ" operatorCode="74" operatorUrl="http://www.sj.se"/>
                <Stops>
                    <Stop depDate="2020-06-02" depTime="11:41:00" routeIdx="0" name="Stockholm Centralstation" id="740000001" extId="740000001" lon="18.058151" lat="59.330136"/>
                    <Stop depDate="2020-06-02" depTime="11:52:00" arrDate="2020-06-02" arrTime="11:52:00" routeIdx="1" name="Flemingsberg station (Huddinge kn)" id="740000031" extId="740000031" lon="17.945678" lat="59.217959"/>
                    <Stop depDate="2020-06-02" depTime="12:03:00" arrDate="2020-06-02" arrTime="12:03:00" routeIdx="2" name="Södertälje Syd station" id="740000055" extId="740000055" lon="17.645367" lat="59.162415"/>
                    <Stop depDate="2020-06-02" depTime="12:19:00" arrDate="2020-06-02" arrTime="12:19:00" routeIdx="3" name="Vagnhärad station (Trosa kn)" id="740000605" extId="740000605" lon="17.496694" lat="58.945739"/>
                    <Stop depDate="2020-06-02" depTime="12:46:00" arrDate="2020-06-02" arrTime="12:46:00" routeIdx="4" name="Nyköping Centralstation" id="740000050" extId="740000050" lon="16.994781" lat="58.755689"/>
                    <Stop depDate="2020-06-02" depTime="13:09:00" arrDate="2020-06-02" arrTime="13:09:00" routeIdx="5" name="Kolmården station (Norrköping kn)" id="740001545" extId="740001545" lon="16.362597" lat="58.675424"/>
                    <Stop arrDate="2020-06-02" arrTime="13:26:00" routeIdx="6" name="Norrköping Centralstation" id="740000007" extId="740000007" lon="16.183343" lat="58.596625"/>
                </Stops>
            </Leg>
            <Leg type="JNY" idx="1" name="Länstrafik - Tåg 8739" transportNumber="8739" transportCategory="JLT" reachable="true" direction="Motala station">
                <Origin extId="740000007" id="740000007" name="Norrköping Centralstation" type="ST" routeIdx="0" lon="16.183343" lat="58.596625" date="2020-06-02" time="13:48:00"/>
                <Destination extId="740000180" id="740000180" name="Mjölby station" type="ST" routeIdx="6" lon="15.131992" lat="58.322984" date="2020-06-02" time="14:35:00"/>
                <Notes>
                    <Note routeIdxFrom="0" routeIdxTo="6" key="AA" priority="100" type="A">Endast 2 klass</Note>
                    <Note routeIdxFrom="0" routeIdxTo="6" key="AE" priority="100" type="A">Ej reservering</Note>
                </Notes>
                <Product catCode="4" catOutL="Länstrafik - Tåg" catOutS="JLT" name="Länstrafik - Tåg 8739" num="8739" operator="ÖstgötaTrafiken" operatorCode="253" operatorUrl="http://www.ostgotatrafiken.se/"/>
                <Stops>
                    <Stop depDate="2020-06-02" depTime="13:48:00" routeIdx="0" name="Norrköping Centralstation" id="740000007" extId="740000007" lon="16.183343" lat="58.596625"/>
                    <Stop depDate="2020-06-02" depTime="13:59:00" arrDate="2020-06-02" arrTime="13:59:00" routeIdx="1" name="Kimstad station (Norrköping kn)" id="740068883" extId="740068883" lon="15.971764" lat="58.546106"/>
                    <Stop depDate="2020-06-02" depTime="14:08:00" arrDate="2020-06-02" arrTime="14:08:00" routeIdx="2" name="Linghem station (Linköping kn)" id="740000849" extId="740000849" lon="15.787188" lat="58.436689"/>
                    <Stop depDate="2020-06-02" depTime="14:16:00" arrDate="2020-06-02" arrTime="14:15:00" routeIdx="3" name="Linköping Centralstation" id="740000009" extId="740000009" lon="15.62496" lat="58.416634"/>
                    <Stop depDate="2020-06-02" depTime="14:22:00" arrDate="2020-06-02" arrTime="14:22:00" routeIdx="4" name="Vikingstad station (Linköping kn)" id="740000868" extId="740000868" lon="15.431971" lat="58.383167"/>
                    <Stop depDate="2020-06-02" depTime="14:28:00" arrDate="2020-06-02" arrTime="14:28:00" routeIdx="5" name="Mantorp station (Mjölby kn)" id="740000616" extId="740000616" lon="15.290732" lat="58.348622"/>
                    <Stop arrDate="2020-06-02" arrTime="14:35:00" routeIdx="6" name="Mjölby station" id="740000180" extId="740000180" lon="15.131992" lat="58.322984"/>
                </Stops>
            </Leg>
            <Leg type="JNY" idx="2" name="Länstrafik - Tåg 18839" transportNumber="18839" transportCategory="JLT" reachable="true" direction="Tranås station">
                <Origin extId="740000180" id="740000180" name="Mjölby station" type="ST" routeIdx="0" lon="15.131992" lat="58.322984" date="2020-06-02" time="14:47:00"/>
                <Destination extId="740000041" id="740000041" name="Tranås station" type="ST" routeIdx="2" lon="14.975022" lat="58.037963" date="2020-06-02" time="15:08:00"/>
                <Notes>
                    <Note routeIdxFrom="0" routeIdxTo="2" key="AA" priority="100" type="A">Endast 2 klass</Note>
                    <Note routeIdxFrom="0" routeIdxTo="2" key="AE" priority="100" type="A">Ej reservering</Note>
                </Notes>
                <Product catCode="4" catOutL="Länstrafik - Tåg" catOutS="JLT" name="Länstrafik - Tåg 18839" num="18839" operator="ÖstgötaTrafiken" operatorCode="253" operatorUrl="http://www.ostgotatrafiken.se/"/>
                <Stops>
                    <Stop depDate="2020-06-02" depTime="14:47:00" routeIdx="0" name="Mjölby station" id="740000180" extId="740000180" lon="15.131992" lat="58.322984"/>
                    <Stop depDate="2020-06-02" depTime="14:56:00" arrDate="2020-06-02" arrTime="14:56:00" routeIdx="1" name="Boxholm station" id="740000015" extId="740000015" lon="15.054145" lat="58.193657"/>
                    <Stop arrDate="2020-06-02" arrTime="15:08:00" routeIdx="2" name="Tranås station" id="740000041" extId="740000041" lon="14.975022" lat="58.037963"/>
                </Stops>
            </Leg>
            <Leg type="JNY" idx="3" name="Länstrafik - Tåg 27621" transportNumber="27621" transportCategory="JLT" reachable="true" direction="Nässjö Centralstation">
                <Origin extId="740000041" id="740000041" name="Tranås station" type="ST" routeIdx="0" lon="14.975022" lat="58.037963" date="2020-06-02" time="16:14:00"/>
                <Destination extId="740000140" id="740000140" name="Nässjö Centralstation" type="ST" routeIdx="2" lon="14.693983" lat="57.652443" date="2020-06-02" time="16:41:00"/>
                <Notes>
                    <Note routeIdxFrom="0" routeIdxTo="2" key="AA" priority="100" type="A">Endast 2 klass</Note>
                    <Note routeIdxFrom="0" routeIdxTo="2" key="AE" priority="100" type="A">Ej reservering</Note>
                </Notes>
                <Product catCode="4" catOutL="Länstrafik - Tåg" catOutS="JLT" name="Länstrafik - Tåg 27621" num="27621" operator="JLT" operatorCode="254" operatorUrl="http://www.jlt.se"/>
                <Stops>
                    <Stop depDate="2020-06-02" depTime="16:14:00" routeIdx="0" name="Tranås station" id="740000041" extId="740000041" lon="14.975022" lat="58.037963"/>
                    <Stop depDate="2020-06-02" depTime="16:28:00" arrDate="2020-06-02" arrTime="16:28:00" routeIdx="1" name="Aneby station" id="740000379" extId="740000379" lon="14.810816" lat="57.836237"/>
                    <Stop arrDate="2020-06-02" arrTime="16:41:00" routeIdx="2" name="Nässjö Centralstation" id="740000140" extId="740000140" lon="14.693983" lat="57.652443"/>
                </Stops>
            </Leg>
            <Leg type="JNY" idx="4" name="Länstrafik - Tåg 17619" transportNumber="17619" transportCategory="JLT" reachable="true" direction="Växjö station">
                <Origin extId="740000140" id="740000140" name="Nässjö Centralstation" type="ST" routeIdx="4" lon="14.693983" lat="57.652443" date="2020-06-02" time="17:01:00"/>
                <Destination extId="740000004" id="740000004" name="Alvesta station" type="ST" routeIdx="10" lon="14.556322" lat="56.898778" date="2020-06-02" time="17:53:00"/>
                <Notes>
                    <Note routeIdxFrom="4" routeIdxTo="10" key="AA" priority="100" type="A">Endast 2 klass</Note>
                    <Note routeIdxFrom="4" routeIdxTo="10" key="AE" priority="100" type="A">Ej reservering</Note>
                </Notes>
                <Product catCode="4" catOutL="Länstrafik - Tåg" catOutS="JLT" name="Länstrafik - Tåg 17619" num="17619" operator="JLT" operatorCode="254" operatorUrl="http://www.jlt.se"/>
                <Stops>
                    <Stop depDate="2020-06-02" depTime="17:01:00" routeIdx="4" name="Nässjö Centralstation" id="740000140" extId="740000140" lon="14.693983" lat="57.652443"/>
                    <Stop depDate="2020-06-02" depTime="17:11:00" arrDate="2020-06-02" arrTime="17:11:00" routeIdx="5" name="Bodafors station (Nässjö kn)" id="740000963" extId="740000963" lon="14.693291" lat="57.504103"/>
                    <Stop depDate="2020-06-02" depTime="17:18:00" arrDate="2020-06-02" arrTime="17:18:00" routeIdx="6" name="Sävsjö station" id="740000078" extId="740000078" lon="14.665308" lat="57.402849"/>
                    <Stop depDate="2020-06-02" depTime="17:25:00" arrDate="2020-06-02" arrTime="17:25:00" routeIdx="7" name="Stockaryd station (Sävsjö kn)" id="740001318" extId="740001318" lon="14.591758" lat="57.313397"/>
                    <Stop depDate="2020-06-02" depTime="17:34:00" arrDate="2020-06-02" arrTime="17:34:00" routeIdx="8" name="Lammhult station (Växjö kn)" id="740037092" extId="740037092" lon="14.585385" lat="57.171035"/>
                    <Stop depDate="2020-06-02" depTime="17:45:00" arrDate="2020-06-02" arrTime="17:45:00" routeIdx="9" name="Moheda station (Alvesta kn)" id="740000122" extId="740000122" lon="14.576863" lat="57.003278"/>
                    <Stop arrDate="2020-06-02" arrTime="17:53:00" routeIdx="10" name="Alvesta station" id="740000004" extId="740000004" lon="14.556322" lat="56.898778"/>
                </Stops>
            </Leg>
            <Leg type="JNY" idx="5" name="Regional Tåg 1101" transportNumber="1101" transportCategory="JRE" reachable="true" direction="Malmö Centralstation">
                <Origin extId="740000004" id="740000004" name="Alvesta station" type="ST" routeIdx="6" lon="14.556322" lat="56.898778" date="2020-06-02" time="18:33:00"/>
                <Destination extId="740000003" id="740000003" name="Malmö Centralstation" type="ST" routeIdx="13" lon="13.00091" lat="55.609456" date="2020-06-02" time="20:11:00"/>
                <Notes>
                    <Note routeIdxFrom="12" routeIdxTo="13" key="AE" priority="100" type="A">Ej reservering</Note>
                    <Note routeIdxFrom="6" routeIdxTo="13" key="AG" priority="100" type="A">Frivillig platsbokning</Note>
                    <Note routeIdxFrom="6" routeIdxTo="13" key="AN" priority="100" type="A">Rullstolslyft</Note>
                </Notes>
                <Product catCode="2" catOutL="Regional Tåg" catOutS="JRE" name="Regional Tåg 1101" num="1101" operator="Öresundståg" operatorCode="300" operatorUrl="http://www.oresundstag.se/"/>
                <Stops>
                    <Stop depDate="2020-06-02" depTime="18:33:00" routeIdx="6" name="Alvesta station" id="740000004" extId="740000004" lon="14.556322" lat="56.898778"/>
                    <Stop depDate="2020-06-02" depTime="18:52:00" arrDate="2020-06-02" arrTime="18:52:00" routeIdx="7" name="Älmhult station" id="740000045" extId="740000045" lon="14.136985" lat="56.551426"/>
                    <Stop depDate="2020-06-02" depTime="19:02:00" arrDate="2020-06-02" arrTime="19:02:00" routeIdx="8" name="Osby station" id="740000295" extId="740000295" lon="13.994254" lat="56.379948"/>
                    <Stop depDate="2020-06-02" depTime="19:22:00" arrDate="2020-06-02" arrTime="19:18:00" routeIdx="9" name="Hässleholm Centralstation" id="740000006" extId="740000006" lon="13.763141" lat="56.157762"/>
                    <Stop depDate="2020-06-02" depTime="19:36:00" arrDate="2020-06-02" arrTime="19:35:00" routeIdx="10" name="Höör station" id="740000185" extId="740000185" lon="13.541395" lat="55.937023"/>
                    <Stop depDate="2020-06-02" depTime="19:46:00" arrDate="2020-06-02" arrTime="19:45:00" routeIdx="11" name="Eslöv station" id="740000260" extId="740000260" lon="13.305491" lat="55.837719"/>
                    <Stop depDate="2020-06-02" depTime="19:58:00" arrDate="2020-06-02" arrTime="19:56:00" routeIdx="12" name="Lund Centralstation" id="740000120" extId="740000120" lon="13.186897" lat="55.708094"/>
                    <Stop arrDate="2020-06-02" arrTime="20:11:00" routeIdx="13" name="Malmö Centralstation" id="740000003" extId="740000003" lon="13.00091" lat="55.609456"/>
                </Stops>
            </Leg>
        </LegList>
    </Trip>
    <Trip idx="1" ctxRecon="T$A=1@O=Stockholm Centralstation@L=740000001@a=128@$A=1@O=Norrköping Centralstation@L=740000007@a=128@$202006021141$202006021326$JRE  231$$1$§T$A=1@O=Norrköping Centralstation@L=740000007@a=128@$A=1@O=Linköping Centralstation@L=740000009@a=128@$202006021348$202006021415$JLT 8739$$1$§T$A=1@O=Linköping Centralstation@L=740000009@a=128@$A=1@O=Kalmar Centralstation@L=740000020@a=128@$202006021426$202006021738$JBL 8561$$1$§T$A=1@O=Kalmar Centralstation@L=740000020@a=128@$A=1@O=Malmö Centralstation@L=740000003@a=128@$202006021800$202006022111$JRE 1107$$1$" tripId="C-1" duration="PT9H30M">
        <ServiceDays sDaysR="not every day" sDaysI="2. until 18. Jun 2020 Mo - Fr" sDaysB="9F3E7800000000000000" planningPeriodBegin="2020-05-29" planningPeriodEnd="2020-08-16"/>
        <LegList>
            <Leg type="JNY" idx="0" name="Regional Tåg 231" transportNumber="231" transportCategory="JRE" reachable="true" direction="Norrköping Centralstation">
                <Origin extId="740000001" id="740000001" name="Stockholm Centralstation" type="ST" routeIdx="0" lon="18.058151" lat="59.330136" date="2020-06-02" time="11:41:00"/>
                <Destination extId="740000007" id="740000007" name="Norrköping Centralstation" type="ST" routeIdx="6" lon="16.183343" lat="58.596625" date="2020-06-02" time="13:26:00"/>
                <Notes>
                    <Note routeIdxFrom="0" routeIdxTo="6" key="AA" priority="100" type="A">Endast 2 klass</Note>
                    <Note routeIdxFrom="0" routeIdxTo="2" key="AE" priority="100" type="A">Ej reservering</Note>
                    <Note routeIdxFrom="0" routeIdxTo="6" key="SX" priority="100" type="A">no WiFi</Note>
                    <Note routeIdxFrom="0" routeIdxTo="6" key="SY" priority="100" type="A">no A/C</Note>
                </Notes>
                <Product catCode="2" catOutL="Regional Tåg" catOutS="JRE" name="Regional Tåg 231" num="231" operator="SJ" operatorCode="74" operatorUrl="http://www.sj.se"/>
                <Stops>
                    <Stop depDate="2020-06-02" depTime="11:41:00" routeIdx="0" name="Stockholm Centralstation" id="740000001" extId="740000001" lon="18.058151" lat="59.330136"/>
                    <Stop depDate="2020-06-02" depTime="11:52:00" arrDate="2020-06-02" arrTime="11:52:00" routeIdx="1" name="Flemingsberg station (Huddinge kn)" id="740000031" extId="740000031" lon="17.945678" lat="59.217959"/>
                    <Stop depDate="2020-06-02" depTime="12:03:00" arrDate="2020-06-02" arrTime="12:03:00" routeIdx="2" name="Södertälje Syd station" id="740000055" extId="740000055" lon="17.645367" lat="59.162415"/>
                    <Stop depDate="2020-06-02" depTime="12:19:00" arrDate="2020-06-02" arrTime="12:19:00" routeIdx="3" name="Vagnhärad station (Trosa kn)" id="740000605" extId="740000605" lon="17.496694" lat="58.945739"/>
                    <Stop depDate="2020-06-02" depTime="12:46:00" arrDate="2020-06-02" arrTime="12:46:00" routeIdx="4" name="Nyköping Centralstation" id="740000050" extId="740000050" lon="16.994781" lat="58.755689"/>
                    <Stop depDate="2020-06-02" depTime="13:09:00" arrDate="2020-06-02" arrTime="13:09:00" routeIdx="5" name="Kolmården station (Norrköping kn)" id="740001545" extId="740001545" lon="16.362597" lat="58.675424"/>
                    <Stop arrDate="2020-06-02" arrTime="13:26:00" routeIdx="6" name="Norrköping Centralstation" id="740000007" extId="740000007" lon="16.183343" lat="58.596625"/>
                </Stops>
            </Leg>
            <Leg type="JNY" idx="1" name="Länstrafik - Tåg 8739" transportNumber="8739" transportCategory="JLT" reachable="true" direction="Motala station">
                <Origin extId="740000007" id="740000007" name="Norrköping Centralstation" type="ST" routeIdx="0" lon="16.183343" lat="58.596625" date="2020-06-02" time="13:48:00"/>
                <Destination extId="740000009" id="740000009" name="Linköping Centralstation" type="ST" routeIdx="3" lon="15.62496" lat="58.416634" date="2020-06-02" time="14:15:00"/>
                <Notes>
                    <Note routeIdxFrom="0" routeIdxTo="3" key="AA" priority="100" type="A">Endast 2 klass</Note>
                    <Note routeIdxFrom="0" routeIdxTo="3" key="AE" priority="100" type="A">Ej reservering</Note>
                </Notes>
                <Product catCode="4" catOutL="Länstrafik - Tåg" catOutS="JLT" name="Länstrafik - Tåg 8739" num="8739" operator="ÖstgötaTrafiken" operatorCode="253" operatorUrl="http://www.ostgotatrafiken.se/"/>
                <Stops>
                    <Stop depDate="2020-06-02" depTime="13:48:00" routeIdx="0" name="Norrköping Centralstation" id="740000007" extId="740000007" lon="16.183343" lat="58.596625"/>
                    <Stop depDate="2020-06-02" depTime="13:59:00" arrDate="2020-06-02" arrTime="13:59:00" routeIdx="1" name="Kimstad station (Norrköping kn)" id="740068883" extId="740068883" lon="15.971764" lat="58.546106"/>
                    <Stop depDate="2020-06-02" depTime="14:08:00" arrDate="2020-06-02" arrTime="14:08:00" routeIdx="2" name="Linghem station (Linköping kn)" id="740000849" extId="740000849" lon="15.787188" lat="58.436689"/>
                    <Stop arrDate="2020-06-02" arrTime="14:15:00" routeIdx="3" name="Linköping Centralstation" id="740000009" extId="740000009" lon="15.62496" lat="58.416634"/>
                </Stops>
            </Leg>
            <Leg type="JNY" idx="2" name="Tåg 8561" transportNumber="8561" transportCategory="JBL" reachable="true" direction="Kalmar Centralstation">
                <Origin extId="740000009" id="740000009" name="Linköping Centralstation" type="ST" routeIdx="0" lon="15.62496" lat="58.416634" date="2020-06-02" time="14:26:00"/>
                <Destination extId="740000020" id="740000020" name="Kalmar Centralstation" type="ST" routeIdx="10" lon="16.360071" lat="56.661283" date="2020-06-02" time="17:38:00"/>
                <Notes>
                    <Note routeIdxFrom="0" routeIdxTo="10" key="AG" priority="100" type="A">Frivillig platsbokning</Note>
                </Notes>
                <Product catCode="2" catOutL="Tåg" catOutS="JBL" name="Tåg 8561" num="8561" operator="Kustpilen" operatorCode="653" operatorUrl="https://klt.se/"/>
                <Stops>
                    <Stop depDate="2020-06-02" depTime="14:26:00" routeIdx="0" name="Linköping Centralstation" id="740000009" extId="740000009" lon="15.62496" lat="58.416634"/>
                    <Stop depDate="2020-06-02" depTime="14:30:00" routeIdx="1" name="Tannefors station (Linköping kn)" id="740001336" extId="740001336" lon="15.659236" lat="58.400471"/>
                    <Stop depDate="2020-06-02" depTime="15:02:00" arrDate="2020-06-02" arrTime="15:01:00" routeIdx="2" name="Rimforsa station (Kinda kn)" id="740000365" extId="740000365" lon="15.6817" lat="58.13555"/>
                    <Stop depDate="2020-06-02" depTime="15:19:00" arrDate="2020-06-02" arrTime="15:19:00" routeIdx="3" name="Kisa station (Kinda kn)" id="740000344" extId="740000344" lon="15.633805" lat="57.985386"/>
                    <Stop depDate="2020-06-02" depTime="15:46:00" arrDate="2020-06-02" arrTime="15:46:00" routeIdx="4" name="Astrid Lindgrens Värld station (Vimmerby kn)" id="740001013" extId="740001013" lon="15.842535" lat="57.674997"/>
                    <Stop depDate="2020-06-02" depTime="15:48:00" arrDate="2020-06-02" arrTime="15:48:00" routeIdx="5" name="Vimmerby station" id="740000351" extId="740000351" lon="15.858266" lat="57.663158"/>
                    <Stop depDate="2020-06-02" depTime="16:04:00" arrDate="2020-06-02" arrTime="16:04:00" routeIdx="6" name="Hultsfred station" id="740000348" extId="740000348" lon="15.846742" lat="57.486754"/>
                    <Stop depDate="2020-06-02" depTime="16:35:00" arrDate="2020-06-02" arrTime="16:30:00" routeIdx="7" name="Berga station (Högsby kn)" id="740000500" extId="740000500" lon="16.032711" lat="57.21634"/>
                    <Stop depDate="2020-06-02" depTime="16:40:00" arrDate="2020-06-02" arrTime="16:40:00" routeIdx="8" name="Högsby station" id="740000923" extId="740000923" lon="16.027812" lat="57.165749"/>
                    <Stop depDate="2020-06-02" depTime="17:05:00" arrDate="2020-06-02" arrTime="17:02:00" routeIdx="9" name="Blomstermåla station (Mönsterås kn)" id="740001000" extId="740001000" lon="16.332627" lat="56.980598"/>
                    <Stop arrDate="2020-06-02" arrTime="17:38:00" routeIdx="10" name="Kalmar Centralstation" id="740000020" extId="740000020" lon="16.360071" lat="56.661283"/>
                </Stops>
            </Leg>
            <Leg type="JNY" idx="3" name="Regional Tåg 1107" transportNumber="1107" transportCategory="JRE" reachable="true" direction="Malmö Centralstation">
                <Origin extId="740000020" id="740000020" name="Kalmar Centralstation" type="ST" routeIdx="0" lon="16.360071" lat="56.661283" date="2020-06-02" time="18:00:00"/>
                <Destination extId="740000003" id="740000003" name="Malmö Centralstation" type="ST" routeIdx="13" lon="13.00091" lat="55.609456" date="2020-06-02" time="21:11:00"/>
                <Notes>
                    <Note routeIdxFrom="5" routeIdxTo="6" key="AE" priority="100" type="A">Ej reservering</Note>
                    <Note routeIdxFrom="12" routeIdxTo="13" key="AE" priority="100" type="A">Ej reservering</Note>
                    <Note routeIdxFrom="0" routeIdxTo="13" key="AG" priority="100" type="A">Frivillig platsbokning</Note>
                    <Note routeIdxFrom="0" routeIdxTo="13" key="AN" priority="100" type="A">Rullstolslyft</Note>
                </Notes>
                <Product catCode="2" catOutL="Regional Tåg" catOutS="JRE" name="Regional Tåg 1107" num="1107" operator="Öresundståg" operatorCode="300" operatorUrl="http://www.oresundstag.se/"/>
                <Stops>
                    <Stop depDate="2020-06-02" depTime="18:00:00" routeIdx="0" name="Kalmar Centralstation" id="740000020" extId="740000020" lon="16.360071" lat="56.661283"/>
                    <Stop depDate="2020-06-02" depTime="18:15:00" arrDate="2020-06-02" arrTime="18:15:00" routeIdx="1" name="Nybro station" id="740000189" extId="740000189" lon="15.909172" lat="56.742357"/>
                    <Stop depDate="2020-06-02" depTime="18:30:00" arrDate="2020-06-02" arrTime="18:29:00" routeIdx="2" name="Emmaboda station" id="740000096" extId="740000096" lon="15.535895" lat="56.62957"/>
                    <Stop depDate="2020-06-02" depTime="18:43:00" arrDate="2020-06-02" arrTime="18:43:00" routeIdx="3" name="Lessebo station" id="740000235" extId="740000235" lon="15.259045" lat="56.749531"/>
                    <Stop depDate="2020-06-02" depTime="18:49:00" arrDate="2020-06-02" arrTime="18:49:00" routeIdx="4" name="Hovmantorp station (Lessebo kn)" id="740000511" extId="740000511" lon="15.140666" lat="56.785838"/>
                    <Stop depDate="2020-06-02" depTime="19:10:00" arrDate="2020-06-02" arrTime="19:04:00" routeIdx="5" name="Växjö station" id="740000250" extId="740000250" lon="14.803625" lat="56.876845"/>
                    <Stop depDate="2020-06-02" depTime="19:33:00" arrDate="2020-06-02" arrTime="19:20:00" routeIdx="6" name="Alvesta station" id="740000004" extId="740000004" lon="14.556322" lat="56.898778"/>
                    <Stop depDate="2020-06-02" depTime="19:52:00" arrDate="2020-06-02" arrTime="19:52:00" routeIdx="7" name="Älmhult station" id="740000045" extId="740000045" lon="14.136985" lat="56.551426"/>
                    <Stop depDate="2020-06-02" depTime="20:02:00" arrDate="2020-06-02" arrTime="20:02:00" routeIdx="8" name="Osby station" id="740000295" extId="740000295" lon="13.994254" lat="56.379948"/>
                    <Stop depDate="2020-06-02" depTime="20:22:00" arrDate="2020-06-02" arrTime="20:18:00" routeIdx="9" name="Hässleholm Centralstation" id="740000006" extId="740000006" lon="13.763141" lat="56.157762"/>
                    <Stop depDate="2020-06-02" depTime="20:36:00" arrDate="2020-06-02" arrTime="20:35:00" routeIdx="10" name="Höör station" id="740000185" extId="740000185" lon="13.541395" lat="55.937023"/>
                    <Stop depDate="2020-06-02" depTime="20:46:00" arrDate="2020-06-02" arrTime="20:45:00" routeIdx="11" name="Eslöv station" id="740000260" extId="740000260" lon="13.305491" lat="55.837719"/>
                    <Stop depDate="2020-06-02" depTime="20:58:00" arrDate="2020-06-02" arrTime="20:56:00" routeIdx="12" name="Lund Centralstation" id="740000120" extId="740000120" lon="13.186897" lat="55.708094"/>
                    <Stop arrDate="2020-06-02" arrTime="21:11:00" routeIdx="13" name="Malmö Centralstation" id="740000003" extId="740000003" lon="13.00091" lat="55.609456"/>
                </Stops>
            </Leg>
        </LegList>
    </Trip>
</TripList>
```

{{% /tab %}} {{% /tabs %}}

#### Response data fields

| **Name**                         | **Data type**     | **Description**                                                                                                                                                                                                                                                                                      |
| -------------------------------- | ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| TripList                         | Trip\[\]          | Root element, contains the results as well as some meta-data.                                                                                                                                                                                                                                        |
| TripList.scrF                    | String            | Use this value as context in a new query to get later results. Only present if there are more results within the next 24 hours.                                                                                                                                                                      |
| TripList.scrB                    | String            | Use this value as context in a new query to get earlier results. Only present if there are more results within the previous 24 hours.                                                                                                                                                                |
| Trip.duration                    | ISO8601 duration  | Total travel time in ISO8601 format<br>Example: PT9H32M                                                                                                                                                                                                                                              |
| Servicedays                      | Object            | Information about the days on which day this trip is executed                                                                                                                                                                                                                                        |
| Servicedays.planningPeriodBegin  | YYYY-MM-DD        | Start of the actual timetable period, moves forward weekly                                                                                                                                                                                                                                           |
| Servicedays.planningPeriodEnd    | YYYY-MM-DD        | End of the actual timetable period, changes about 4 times every year                                                                                                                                                                                                                                 |
| Servicedays.sDaysB               | String            | Binary code describing if there is traffic on each day in the timetable period. The bits are respresented in a hexadecimal string<br>Example: sDaysB=“FFFFE7FFFFFF”<br>Might end in a long series of zeroes in case there is no information for the given trip near the end of the timetable period. |
| Servicedays.sDaysI               | String            | Automatic attempt to describe days on which this trip isn’t executed, in the chosen language<br>E.g. `utom 19. jun; och 18. jun`. Not included if this trip is executed daily.                                                                                                                       |
| Servicedays.sDaysR               | String            | Automatic attempt to describe days on which this trip is executed, in the chosen language<br>E.g. `Every day`, `Not every day`, `On fridays`                                                                                                                                                         |
| LegList                          | Leg\[\]           | List of Legs                                                                                                                                                                                                                                                                                         |
| Leg                              | Object            | Part of the journey, for example travelling with 1 vehicle, walking to or from a stop, or making a transfer.<br>For transfers or walks, only duration and distance are available.                                                                                                                    |
| Leg.category                     | String            | Category type                                                                                                                                                                                                                                                                                        |
| Leg.number                       | Integer           | See product.num                                                                                                                                                                                                                                                                                      |
| Leg.name                         | String            | See product.name                                                                                                                                                                                                                                                                                     |
| Leg.direction                    | String            | Name of the last stop on the vehicle’s trip                                                                                                                                                                                                                                                          |
| Leg.type                         | String            | `JNY` for public transport. `TRSF` for transfers where the traveller has to walk between stations or where the traveller has to wait for more than 15 minutes. `WALK` for walks to the first stop and from the last stop.                                                                            |
| Leg.dist                         | Integer           | Distance of this leg in meter. Relevant när type=WALK eller type=BIKE.                                                                                                                                                                                                                               |
| Leg.Origin                       | Origin            | Information about the departure stop                                                                                                                                                                                                                                                                 |
| Leg.Destination                  | Origin            | Information about the destination stop                                                                                                                                                                                                                                                               |
| Origin.name                      | String            | Name of the departure stop                                                                                                                                                                                                                                                                           |
| Origin.type                      | String            | `ST` for stop.                                                                                                                                                                                                                                                                                       |
| Origin.date                      | Date (YYYY-MM-DD) | Departure date in in YYYY-MM-DD format, e.g. 2021-12-31.                                                                                                                                                                                                                                             |
| Origin.time                      | Time (HH:MM)      | Departure time in HH:MM format, e.g. 19:06.                                                                                                                                                                                                                                                          |
| Origin.lat, Origin.lon           | String            | Latitude and Longitude (WGS84, decimal degree) of the departure stop, e.g. 59.293611 and 18.083056                                                                                                                                                                                                   |
| Origin.id                        | String            | Internal stop id of the departure stop, do not use                                                                                                                                                                                                                                                   |
| Origin.extId                     | String            | Id of the departure stop                                                                                                                                                                                                                                                                             |
| Destination.name                 | String            | Name of the arrival stop                                                                                                                                                                                                                                                                             |
| Destination.type                 | String            | `ST` for stop.                                                                                                                                                                                                                                                                                       |
| Destination.date                 | Date (YYYY-MM-DD) | Arrival date in in YYYY-MM-DD format, e.g. 2021-12-31.                                                                                                                                                                                                                                               |
| Destination.time                 | Time (HH:MM)      | Arrival time in HH:MM format, e.g. 19:06.                                                                                                                                                                                                                                                            |
| Destination.lat, Destination.lon | String            | Latitude and Longitude (WGS84, decimal degree) of the destination stop, e.g. 59.293611 and 18.083056                                                                                                                                                                                                 |
| Destination.id                   | String            | Internal stop id of the destination stop, do not use                                                                                                                                                                                                                                                 |
| Destination.extId                | String            | Id of the destination stop                                                                                                                                                                                                                                                                           |
| Notes                            | Note\[\]          | A list of notes for a leg                                                                                                                                                                                                                                                                            |
| Note.value                       | String            | Text note containing additional information for (a part of) this leg                                                                                                                                                                                                                                 |
| Note.routeIdxFrom                | Integer           | Index of the stop at the start of the stretch to which this note applies                                                                                                                                                                                                                             |
| Note.routeIdxTo                  | Integer           | Index of the stop at the end of the stretch to which this note applies                                                                                                                                                                                                                               |
| Product                          | Product           | See [common data types](common.md)                                                                                                                                                                                                       |
| Stops                            | Stop\[\]          | The intermediate stops that this vehicle passes on during this leg                                                                                                                                                                                                                                   |
| Stop.name                        | String            | Name of the departure stop                                                                                                                                                                                                                                                                           |
| Stop.type                        | String            | `ST` for stop.                                                                                                                                                                                                                                                                                       |
| Stop.depDate                     | Date (YYYY-MM-DD) | Departure date in in YYYY-MM-DD format, e.g. 2021-12-31.                                                                                                                                                                                                                                             |
| Stop.arrDate                     | Date (YYYY-MM-DD) | Arrival date in in YYYY-MM-DD format, e.g. 2021-12-31.                                                                                                                                                                                                                                               |
| Stop.depTime                     | Time (HH:MM)      | Departure time in HH:MM format, e.g. 19:06.                                                                                                                                                                                                                                                          |
| Stop.arrTime                     | Time (HH:MM)      | Arrival time in HH:MM format, e.g. 19:06.                                                                                                                                                                                                                                                            |
| Stop.lat, Stop.lon               | String            | Latitude and Longitude (WGS84, decimal degree) of the departure stop, e.g. 59.293611 and 18.083056                                                                                                                                                                                                   |
| Stop.id                          | String            | Internal stop id of the stop, do not use                                                                                                                                                                                                                                                             |
| Stop.extId                       | String            | Id of the stop                                                                                                                                                                                                                                                                                       |
| Stop.routeIdx                    | Integer           | Zero-based index of the intermediate stop, for use with for example routeIdxFrom and routeIdsTo                                                                                                                                                                                                      |