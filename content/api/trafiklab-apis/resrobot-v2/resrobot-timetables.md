---
title: ResRobot Timetables
aliases: /node/14075/documentation
weight: 10
---

## What does this API provide?

ResRobot Timetables provides a list of departures or arrivals at a given stop. Users can specify the stop, date, time,
transport modes, ... . Realtime data is available for SL, Skånetrafiken, Västtrafik and Trafikverket (All train traffic
including SJ, MTRX, .... except for Arlanda Express).

### Data format

The data is formatted as JSON or XML, depending on the `format` query parameter.

### How often is this data updated?

The static data used for this API is updated when changes are made, at most once per day. Real-time data is updated once
every minute.

### Which operators are covered by this dataset?

All operators which operate in Sweden are covered by the ResRobot APIs.

### How often does the data format changes? Do breaking changes happen?

This dataset has the **stable** status. This means that we will communicate when fields are added, or changed. When
breaking changes are made, you will get three months or more to update your implementations.

## Using ResRobot Timetables

ResRobot Timetables consists of two different endpoints, one for departures and one for arrivals. Both endpoints take
exactly the same parameters and have the same response structure. API Calls take the stop id as a parameter, as well as
some other parameters to fine-tune the results. It returns a list of departures or arrivals from the given stop,
including a bit of information about each vehicle, such as where it is heading or where it comes from.

{{% info %}}
Only the most important parameters and response variables are described on this page. Looking for more technical 
details? These can be found in [the OpenAPI specification](resrobot-spec.md).
{{% /info %}}

## Example call

This call will show all departures from Göteborg Central Station (740000002). The id can be obtained
from [ResRobot Stop lookup](resrobot-station-lookup.md) or [GTFS Sverige 2](../gtfs/gtfs-sverige-2-static/).

### Call

{{% tabs %}} {{% tab "Json" %}}

```text
https://api.resrobot.se/v2/departureBoard?id=740000002&format=json&key=API_KEY
```

{{% /tab %}}

{{% tab "Xml" %}}

```text
https://api.resrobot.se/v2/departureBoard?id=740000002&format=xml&key=API_KEY
```

{{% /tab %}} {{% /tabs %}}

#### Request parameters

| **Name**      | **Data type** | **Required** | **Description**                                                                                                                                                                                           |
| ------------- | ----------- | ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| key           | String      | Ja               | Your API key                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| id            | String      | Ja               | Id för hållplatsen. Detta id kan erhållas från Platsuppslag eller Närliggande Hållplats APIet.<br>Notera att svaret även kan returnera avgångar från närliggande hållplatser om det finns en gånglänk definerad.|
| direction     | String      | Nej              | Filter on vehicles heading towards a certain stop. Id of the stop which included vehicles should be heading to.|
| date          | Date        | Nej              | Search on a specific date, specified in YYYY-MM-DD format, eg 2021-12-31, default today|
| time          | String      | Nej              | Search on a specific time, specified in HH:MM format, eg 19:05, default now.|
| maxJourneys   | Integer     | Nej              | The maximum number of results to return. Default 20|
| operators     | String      | Nej              | Only include traffic from certain operators<br>Example: operators=275,287<br>(275=SL, 287=Arlanda Express)|
| products      | Integer     | Nej              | Only include certain traffic modes<br>Sum of the :<br>2 - Snabbtåg, Expresståg, Arlanda Express<br>4 - Regionaltåg, InterCitytåg<br>8 - Expressbuss, Flygbussar<br>16 - Lokaltåg, Pågatåg, Öresundståg<br>32 - Tunnelbana<br>64 – Spårvagn<br>128 – Buss<br>256 – Färja, Utrikes Färja<br>512 - Taxi<br>(inte en fullständig lista)<br>Exempel: 6 = 2 (Snabbtåg, Expresståg, Arlanda Express) + 4 (Regionaltåg, InterCitytåg) |
| passlist      | Integer     | Nej              | Set to 1 to include a list of the stops which are passed on the route of a vehicle. 0 to leave the list out of the result.|
| lang          | String      | Nej              | Language (sv/en/de), default sv. Affects both data (names for different transport types) and error messages.|
| format        | String      | Nej              | The response format, json or XML                                                                                                                                                                                                                                                                                                                                                                                                       | |

### Response

För en exakt teknisk beskrivning av varje fält i svaret hanvisar vi till vår OpenAPI dokumentation.

{{% note %}} Note that an actual response contains more entries and stops - we removed some from this example
response since it's only meant to show the structure of the response. {{% /note %}}

{{% tabs %}} {{% tab "Json" %}}

```javascript
{
  "Departure": [
    {
      "Product": {
        "name": "Länstrafik - Buss Grön X",
        "num": "Grön X",
        "catCode": "7",
        "catOutS": "BLT",
        "catOutL": "Länstrafik - Buss",
        "operatorCode": "279",
        "operator": "Västtrafik",
        "operatorUrl": "http://www.vasttrafik.se/"
      },
      "Stops": {
        "Stop": [
          {
            "name": "Göteborg Nordstan",
            "id": "740015585",
            "extId": "740015585",
            "routeIdx": 7,
            "lon": 11.970791,
            "lat": 57.709246,
            "depTime": "11:31:00",
            "depDate": "2020-06-02"
          },
          {
            "name": "Göteborg Heden",
            "id": "740015568",
            "extId": "740015568",
            "routeIdx": 8,
            "lon": 11.975169,
            "lat": 57.702567,
            "arrTime": "11:36:00",
            "arrDate": "2020-06-02"
          },
          {
            "name": "Sommarhemsvägen (Härryda kn)",
            "id": "740061214",
            "extId": "740061214",
            "routeIdx": 27,
            "lon": 12.135186,
            "lat": 57.653711,
            "arrTime": "12:09:00",
            "arrDate": "2020-06-02"
          },
          {
            "name": "Mölnlycke Häggvägen (Härryda kn)",
            "id": "740015972",
            "extId": "740015972",
            "routeIdx": 28,
            "lon": 12.138134,
            "lat": 57.657756,
            "arrTime": "12:13:00",
            "arrDate": "2020-06-02"
          }
        ]
      },
      "name": "Länstrafik - Buss Grön X",
      "type": "S",
      "stop": "Göteborg Nordstan",
      "stopid": "740015585",
      "stopExtId": "740015585",
      "time": "11:31:00",
      "date": "2020-06-02",
      "direction": "Mölnlycke Häggvägen (Härryda kn)",
      "transportNumber": "Grön X",
      "transportCategory": "BLT"
    },
    {
      "Product": {
        "name": "Länstrafik - Buss 519",
        "num": "519",
        "catCode": "7",
        "catOutS": "BLT",
        "catOutL": "Länstrafik - Buss",
        "operatorCode": "279",
        "operator": "Västtrafik",
        "operatorUrl": "http://www.vasttrafik.se/"
      },
      "Stops": {
        "Stop": [
          {
            "name": "Göteborg Polhemsplatsen",
            "id": "740059478",
            "extId": "740059478",
            "routeIdx": 1,
            "lon": 11.977317,
            "lat": 57.70832,
            "depTime": "11:31:00",
            "depDate": "2020-06-02"
          },
          {
            "name": "Göteborg Svingeln",
            "id": "740015597",
            "extId": "740015597",
            "routeIdx": 2,
            "lon": 11.991008,
            "lat": 57.712536,
            "arrTime": "11:35:00",
            "arrDate": "2020-06-02"
          }
          {
            "name": "Partille centrum",
            "id": "740015667",
            "extId": "740015667",
            "routeIdx": 14,
            "lon": 12.105252,
            "lat": 57.738623,
            "arrTime": "11:57:00",
            "arrDate": "2020-06-02"
          }
        ]
      },
      "name": "Länstrafik - Buss 519",
      "type": "S",
      "stop": "Göteborg Polhemsplatsen",
      "stopid": "740059478",
      "stopExtId": "740059478",
      "time": "11:31:00",
      "date": "2020-06-02",
      "direction": "Partille centrum",
      "transportNumber": "519",
      "transportCategory": "BLT"
    },
    {
      "Product": {
        "name": "Länstrafik - Buss Blå Ex",
        "num": "Blå Ex",
        "catCode": "7",
        "catOutS": "BLT",
        "catOutL": "Länstrafik - Buss",
        "operatorCode": "279",
        "operator": "Västtrafik",
        "operatorUrl": "http://www.vasttrafik.se/"
      },
      "Stops": {
        "Stop": [
          {
            "name": "Göteborg Polhemsplatsen",
            "id": "740059478",
            "extId": "740059478",
            "routeIdx": 15,
            "lon": 11.977317,
            "lat": 57.70832,
            "depTime": "11:31:00",
            "depDate": "2020-06-02"
          },
          {
            "name": "Heden Nya Allén (Göteborg kn)",
            "id": "740074042",
            "extId": "740074042",
            "routeIdx": 16,
            "lon": 11.972472,
            "lat": 57.702585,
            "arrTime": "11:34:00",
            "arrDate": "2020-06-02"
          },
          {
            "name": "Pilgatan (Göteborg kn)",
            "id": "740062991",
            "extId": "740062991",
            "routeIdx": 17,
            "lon": 11.96031,
            "lat": 57.696751,
            "arrTime": "11:38:00",
            "arrDate": "2020-06-02"
          },
          {
            "name": "Särö centrum (Kungsbacka kn)",
            "id": "740075576",
            "extId": "740075576",
            "routeIdx": 29,
            "lon": 11.96511,
            "lat": 57.52085,
            "arrTime": "12:12:00",
            "arrDate": "2020-06-02"
          }
        ]
      },
      "name": "Länstrafik - Buss Blå Ex",
      "type": "S",
      "stop": "Göteborg Polhemsplatsen",
      "stopid": "740059478",
      "stopExtId": "740059478",
      "time": "11:31:00",
      "date": "2020-06-02",
      "direction": "Särö centrum (Kungsbacka kn)",
      "transportNumber": "Blå Ex",
      "transportCategory": "BLT"
    }
  ]
}
```

{{% /tab %}}

{{% tab "Xml" %}}

```xml
<?xml version="1.0" encoding="UTF-8"?>
<DepartureBoard xmlns="hafas_rest_v1">
    <Departure direction="Göteborg Eketrägatan" name="Länstrafik - Buss 16" transportNumber="16" transportCategory="BLT" type="S" stopid="740015585" stopExtId="740015585" stop="Göteborg Nordstan" date="2020-06-02" time="11:29:00">
        <Product catCode="7" catOutL="Länstrafik - Buss" catOutS="BLT" name="Länstrafik - Buss 16" num="16" operator="Västtrafik" operatorCode="279" operatorUrl="http://www.vasttrafik.se/"/>
        <Stops>
            <Stop depDate="2020-06-02" depTime="11:29:00" routeIdx="12" name="Göteborg Nordstan" id="740015585" extId="740015585" lon="11.970791" lat="57.709246"/>
            <Stop arrDate="2020-06-02" arrTime="11:33:00" routeIdx="13" name="Frihamnsporten (Göteborg kn)" id="740072023" extId="740072023" lon="11.959528" lat="57.718208"/>
            <Stop arrDate="2020-06-02" arrTime="11:35:00" routeIdx="14" name="Pumpgatan (Göteborg kn)" id="740059497" extId="740059497" lon="11.946152" lat="57.712725"/>
            <Stop arrDate="2020-06-02" arrTime="11:36:00" routeIdx="15" name="Regnbågsgatan (Göteborg kn)" id="740059509" extId="740059509" lon="11.942754" lat="57.710774"/>
            <Stop arrDate="2020-06-02" arrTime="11:38:00" routeIdx="16" name="Lindholmen (Göteborg kn)" id="740059410" extId="740059410" lon="11.938052" lat="57.708104"/>
            <Stop arrDate="2020-06-02" arrTime="11:38:00" routeIdx="17" name="Sannegårdshamnen (Göteborg kn)" id="740059537" extId="740059537" lon="11.930816" lat="57.70779"/>
            <Stop arrDate="2020-06-02" arrTime="11:40:00" routeIdx="18" name="Nordviksgatan (Göteborg kn)" id="740059465" extId="740059465" lon="11.922061" lat="57.707017"/>
            <Stop arrDate="2020-06-02" arrTime="11:41:00" routeIdx="19" name="Sörhallstorget (Göteborg kn)" id="740059197" extId="740059197" lon="11.919642" lat="57.703106"/>
            <Stop arrDate="2020-06-02" arrTime="11:43:00" routeIdx="20" name="Eriksbergstorget (Göteborg kn)" id="740059199" extId="740059199" lon="11.913233" lat="57.702342"/>
            <Stop arrDate="2020-06-02" arrTime="11:44:00" routeIdx="21" name="Danaplatsen (Göteborg kn)" id="740059175" extId="740059175" lon="11.912954" lat="57.705039"/>
            <Stop arrDate="2020-06-02" arrTime="11:46:00" routeIdx="22" name="Säterigatan (Göteborg kn)" id="740059623" extId="740059623" lon="11.918375" lat="57.709138"/>
            <Stop arrDate="2020-06-02" arrTime="11:47:00" routeIdx="23" name="Lundby Gamla Kyrka (Göteborg kn)" id="740059420" extId="740059420" lon="11.915939" lat="57.712806"/>
            <Stop arrDate="2020-06-02" arrTime="11:50:00" routeIdx="24" name="Göteborg Eketrägatan" id="740025624" extId="740025624" lon="11.910285" lat="57.716275"/>
        </Stops>
    </Departure>
    <Departure direction="Landvetter Airport (Härryda kn)" name="Flygtransfer - Buss ." transportNumber="." transportCategory="BAX" type="S" stopid="740020483" stopExtId="740020483" stop="Göteborg Nils Ericsonterminal" date="2020-06-02" time="11:30:00">
        <Product catCode="3" catOutL="Flygtransfer - Buss" catOutS="BAX" name="Flygtransfer - Buss ." num="." operator="Flygbussarna" operatorCode="277" operatorUrl="http://www.flygbussarna.se"/>
        <Stops>
            <Stop depDate="2020-06-02" depTime="11:30:00" routeIdx="0" name="Göteborg Nils Ericsonterminal" id="740020483" extId="740020483" lon="11.971852" lat="57.710271"/>
            <Stop arrDate="2020-06-02" arrTime="11:58:00" routeIdx="4" name="Hangarvägen (Härryda kn)" id="740061273" extId="740061273" lon="12.302709" lat="57.673694"/>
            <Stop arrDate="2020-06-02" arrTime="12:00:00" routeIdx="5" name="Landvetter Airport (Härryda kn)" id="740000554" extId="740000554" lon="12.29594" lat="57.667878"/>
        </Stops>
    </Departure>
    <Departure direction="Kärra Klareberg (Göteborg kn)" name="Länstrafik - Buss Rosa X" transportNumber="Rosa X" transportCategory="BLT" type="S" stopid="740015585" stopExtId="740015585" stop="Göteborg Nordstan" date="2020-06-02" time="11:30:00">
        <Product catCode="7" catOutL="Länstrafik - Buss" catOutS="BLT" name="Länstrafik - Buss Rosa X" num="Rosa X" operator="Västtrafik" operatorCode="279" operatorUrl="http://www.vasttrafik.se/"/>
        <Stops>
            <Stop depDate="2020-06-02" depTime="11:30:00" routeIdx="25" name="Göteborg Nordstan" id="740015585" extId="740015585" lon="11.970791" lat="57.709246"/>
            <Stop arrDate="2020-06-02" arrTime="11:35:00" routeIdx="26" name="Göteborg Hjalmar Brantingspl" id="740015569" extId="740015569" lon="11.953676" lat="57.720833"/>
            <Stop arrDate="2020-06-02" arrTime="11:43:00" routeIdx="27" name="Kärraporten (Göteborg kn)" id="740050830" extId="740050830" lon="11.99463" lat="57.787884"/>
            <Stop arrDate="2020-06-02" arrTime="11:45:00" routeIdx="28" name="Lillekärr Södra (Göteborg kn)" id="740059406" extId="740059406" lon="11.990531" lat="57.789241"/>
            <Stop arrDate="2020-06-02" arrTime="11:46:00" routeIdx="29" name="Kärra Kyrka (Göteborg kn)" id="740059383" extId="740059383" lon="11.991268" lat="57.792001"/>
            <Stop arrDate="2020-06-02" arrTime="11:47:00" routeIdx="30" name="Kärra Centrum (Göteborg kn)" id="740059386" extId="740059386" lon="11.990873" lat="57.794284"/>
            <Stop arrDate="2020-06-02" arrTime="11:48:00" routeIdx="31" name="Lillekärr Norra (Göteborg kn)" id="740059405" extId="740059405" lon="11.990729" lat="57.796118"/>
            <Stop arrDate="2020-06-02" arrTime="11:49:00" routeIdx="32" name="Burmans Gata (Göteborg kn)" id="740059154" extId="740059154" lon="11.990316" lat="57.798203"/>
            <Stop arrDate="2020-06-02" arrTime="11:51:00" routeIdx="33" name="Kärra Klareberg (Göteborg kn)" id="740015575" extId="740015575" lon="11.991808" lat="57.800163"/>
        </Stops>
    </Departure>
    <Departure direction="Hinnebäcksgatan (Göteborg kn)" name="Länstrafik - Buss 17" transportNumber="17" transportCategory="BLT" type="S" stopid="740015585" stopExtId="740015585" stop="Göteborg Nordstan" date="2020-06-02" time="11:30:00">
        <Product catCode="7" catOutL="Länstrafik - Buss" catOutS="BLT" name="Länstrafik - Buss 17" num="17" operator="Västtrafik" operatorCode="279" operatorUrl="http://www.vasttrafik.se/"/>
        <Stops>
            <Stop depDate="2020-06-02" depTime="11:30:00" routeIdx="14" name="Göteborg Nordstan" id="740015585" extId="740015585" lon="11.970791" lat="57.709246"/>
            <Stop arrDate="2020-06-02" arrTime="11:35:00" routeIdx="15" name="Göteborg Hjalmar Brantingspl" id="740015569" extId="740015569" lon="11.953676" lat="57.720833"/>
            <Stop arrDate="2020-06-02" arrTime="11:37:00" routeIdx="16" name="Göteborg Vågmästareplatsen" id="740025706" extId="740025706" lon="11.945037" lat="57.720671"/>
            <Stop arrDate="2020-06-02" arrTime="11:38:00" routeIdx="17" name="Swedenborgsplatsen (Göteborg kn)" id="740059614" extId="740059614" lon="11.94519" lat="57.726631"/>
            <Stop arrDate="2020-06-02" arrTime="11:40:00" routeIdx="18" name="Björnsonsgatan (Göteborg kn)" id="740059135" extId="740059135" lon="11.944614" lat="57.729535"/>
            <Stop arrDate="2020-06-02" arrTime="11:41:00" routeIdx="19" name="Hildedalsgatan (Göteborg kn)" id="740059296" extId="740059296" lon="11.942502" lat="57.732321"/>
            <Stop arrDate="2020-06-02" arrTime="11:41:00" routeIdx="20" name="Bäckedalsvägen (Göteborg kn)" id="740059162" extId="740059162" lon="11.942151" lat="57.734649"/>
            <Stop arrDate="2020-06-02" arrTime="11:44:00" routeIdx="21" name="Grimbo (Göteborg kn)" id="740059258" extId="740059258" lon="11.940318" lat="57.741913"/>
            <Stop arrDate="2020-06-02" arrTime="11:46:00" routeIdx="22" name="Gunnesgärde (Göteborg kn)" id="740059269" extId="740059269" lon="11.933297" lat="57.748906"/>
            <Stop arrDate="2020-06-02" arrTime="11:48:00" routeIdx="23" name="Brunnehagen (Göteborg kn)" id="740059148" extId="740059148" lon="11.92847" lat="57.750695"/>
            <Stop arrDate="2020-06-02" arrTime="11:48:00" routeIdx="24" name="Tuve Centrum (Göteborg kn)" id="740059661" extId="740059661" lon="11.928389" lat="57.754246"/>
            <Stop arrDate="2020-06-02" arrTime="11:50:00" routeIdx="25" name="Norumsgärde (Göteborg kn)" id="740059471" extId="740059471" lon="11.924488" lat="57.758048"/>
            <Stop arrDate="2020-06-02" arrTime="11:51:00" routeIdx="26" name="Norumshöjd (Göteborg kn)" id="740059472" extId="740059472" lon="11.919804" lat="57.756385"/>
            <Stop arrDate="2020-06-02" arrTime="11:53:00" routeIdx="27" name="Hinnebäcksgatan (Göteborg kn)" id="740059298" extId="740059298" lon="11.917314" lat="57.752142"/>
        </Stops>
    </Departure>
    <Departure direction="Mölnlycke Häggvägen (Härryda kn)" name="Länstrafik - Buss Grön X" transportNumber="Grön X" transportCategory="BLT" type="S" stopid="740015585" stopExtId="740015585" stop="Göteborg Nordstan" date="2020-06-02" time="11:31:00">
        <Product catCode="7" catOutL="Länstrafik - Buss" catOutS="BLT" name="Länstrafik - Buss Grön X" num="Grön X" operator="Västtrafik" operatorCode="279" operatorUrl="http://www.vasttrafik.se/"/>
        <Stops>
            <Stop depDate="2020-06-02" depTime="11:31:00" routeIdx="7" name="Göteborg Nordstan" id="740015585" extId="740015585" lon="11.970791" lat="57.709246"/>
            <Stop arrDate="2020-06-02" arrTime="11:36:00" routeIdx="8" name="Göteborg Heden" id="740015568" extId="740015568" lon="11.975169" lat="57.702567"/>
            <Stop arrDate="2020-06-02" arrTime="11:38:00" routeIdx="9" name="Göteborg Berzeliigatan" id="740025610" extId="740025610" lon="11.981884" lat="57.698504"/>
            <Stop arrDate="2020-06-02" arrTime="11:41:00" routeIdx="10" name="Göteborg Korsvägen" id="740015578" extId="740015578" lon="11.986909" lat="57.696625"/>
            <Stop arrDate="2020-06-02" arrTime="11:44:00" routeIdx="11" name="Delsjömotet (Göteborg kn)" id="740022706" extId="740022706" lon="12.025706" lat="57.676786"/>
            <Stop arrDate="2020-06-02" arrTime="11:48:00" routeIdx="12" name="Mölnlyckemotet (Härryda kn)" id="740072738" extId="740072738" lon="12.090806" lat="57.670134"/>
            <Stop arrDate="2020-06-02" arrTime="11:50:00" routeIdx="13" name="Mölnlycke Råda Portar (Härryda kn)" id="740015970" extId="740015970" lon="12.097269" lat="57.668327"/>
            <Stop arrDate="2020-06-02" arrTime="11:51:00" routeIdx="14" name="Platåvägen (Härryda kn)" id="740061201" extId="740061201" lon="12.104793" lat="57.6675"/>
            <Stop arrDate="2020-06-02" arrTime="11:53:00" routeIdx="15" name="Solsten (Härryda kn)" id="740061202" extId="740061202" lon="12.113827" lat="57.666961"/>
            <Stop arrDate="2020-06-02" arrTime="11:54:00" routeIdx="16" name="Kyrkvägen (Härryda kn)" id="740061188" extId="740061188" lon="12.115023" lat="57.662106"/>
            <Stop arrDate="2020-06-02" arrTime="11:56:00" routeIdx="17" name="Hulebäcksgymnasiet (Härryda kn)" id="740061189" extId="740061189" lon="12.117792" lat="57.659257"/>
            <Stop arrDate="2020-06-02" arrTime="11:58:00" routeIdx="18" name="Mölnlycke station (Härryda kn)" id="740000205" extId="740000205" lon="12.117369" lat="57.656695"/>
            <Stop arrDate="2020-06-02" arrTime="12:01:00" routeIdx="19" name="Råda stock (Härryda kn)" id="740061190" extId="740061190" lon="12.109315" lat="57.657252"/>
            <Stop arrDate="2020-06-02" arrTime="12:02:00" routeIdx="20" name="Hönekullavägen (Härryda kn)" id="740061205" extId="740061205" lon="12.107975" lat="57.653549"/>
            <Stop arrDate="2020-06-02" arrTime="12:03:00" routeIdx="21" name="Gitarrvägen (Härryda kn)" id="740061207" extId="740061207" lon="12.110376" lat="57.651256"/>
            <Stop arrDate="2020-06-02" arrTime="12:03:00" routeIdx="22" name="Violinvägen (Härryda kn)" id="740061210" extId="740061210" lon="12.112515" lat="57.649378"/>
            <Stop arrDate="2020-06-02" arrTime="12:03:00" routeIdx="23" name="Fagottvägen (Härryda kn)" id="740061209" extId="740061209" lon="12.116839" lat="57.648641"/>
            <Stop arrDate="2020-06-02" arrTime="12:05:00" routeIdx="24" name="Råstensvägen (Härryda kn)" id="740061211" extId="740061211" lon="12.12216" lat="57.647742"/>
            <Stop arrDate="2020-06-02" arrTime="12:07:00" routeIdx="25" name="Rullstensvägen (Härryda kn)" id="740061212" extId="740061212" lon="12.128525" lat="57.651616"/>
            <Stop arrDate="2020-06-02" arrTime="12:08:00" routeIdx="26" name="Stenbrottet (Härryda kn)" id="740072932" extId="740072932" lon="12.12857" lat="57.653522"/>
            <Stop arrDate="2020-06-02" arrTime="12:09:00" routeIdx="27" name="Sommarhemsvägen (Härryda kn)" id="740061214" extId="740061214" lon="12.135186" lat="57.653711"/>
            <Stop arrDate="2020-06-02" arrTime="12:13:00" routeIdx="28" name="Mölnlycke Häggvägen (Härryda kn)" id="740015972" extId="740015972" lon="12.138134" lat="57.657756"/>
        </Stops>
    </Departure>
</DepartureBoard>
```

{{% /tab %}} {{% /tabs %}}

#### Response data fields

{{% info %}}
The structure for departure and arrival boards is nearly identical. We list the most commonly used fields for both 
endpoints in this table. When we write departure/arrival, apply the one that matches the endpoint you're using.
{{% /info %}}

| **Name**          | **Data type**             | **Description**                                                                                                                                                                                                                                                                                                                                                   |
| ----------------- | ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| DepartureBoard or ArrivalBoard    | Departure[] or Arrival[] | List of departures or arrivals.                                                                                                                                                                                                                                                                                                          |
| Departure or Arrival         | Object                  |                                                                                                                                                                                                                                                                                                                                                                   |
| time              | String                  | Scheduled departure/arrival time, formatted as HH:MM:SS.                                                                                                                                                                                                                                                                                                                                            |
| date              | Datum                   | Scheduled departure/arrival date, formatted as YYYY-MM-DD.                                                                                                                                                                                                                                                                                                                                          |
| rtTime            | String                  | Realtime departure/arrival time, formatted as HH:MM:SS.                                                                                                                                                                                                                                                                                                                                       |
| rtDate            | Datum                   | Realtime departure/arrival date, formatted as YYYY-MM-DD.                                                                                                                                                                                                                                                                                                                                           |
| rtTrack           | String                  | Realtime track |
| rtDepTrack        | String                  | Realtime departure track, in case arrival and departure track aren't identical                                                                                                                                                                                                                                                                                                           |
| stop              | String                  | Stop name                                                                                                                                                                                                                                                                                                                                                   |
| stopId            | String                  | Internal id, do not use |
| stopExtId         | String                  | Stop id |
| transportNumber   | String                  | Line number. Example:"19"                                                                                                                                                                                                                                                                                                                             |
| transportCategory | String                  | Transport type code.<br>Examples: <br>"BLT" (Buss Länstrafik) <br>”BXB” (Buss Express) <br>"ULT" (Tunnelbana Länstrafik) <br>"JAX" (Järnväg Arlanda Express) <br>"JLT" Järnväg Länstrafik), <br>"JRE" (Järnväg Regionaltrafik) <br>"JIC" (Järnväg InterCity), <br>”JPT” (Järnväg PågaTåg) <br>”JEX” (Järnväg Express) <br>”SLT” (Spårvagn Länstrafik) <br>”FLT” (Färja Länstrafik) <br>”FUT” (Färja Utrikes)                                                                                                                                                                                                                                                                                                                                       |
| name              | String                  | TransportCategory + transportNumber <br>Example: ”ULT 19” (Tunnelbana linje 19)                                                                                                                                                                                                                                                                 |
| direction         | String                  | Name of the last stop on the vehicle's trip                                                                                                                                                                                                                              |
| Product.name              | String                  | See name.                                                                                                                                                                                                                                                                                                                                       |
| Product.operator          | String                  | Operator name. For example: “SL”, ”Skånetrafiken”.                                                                                                                                                                                                                                                                                                                      | |
| Product.catOutS           | String                  | Short category code, see transport type code|
| Product.catOutL           | String                  | Category name <br>Example: "Buss", "Tåg", "Intercity", "Tunnelbana", "Arlanda Express","Regional","InterCity", ”PågaTåg”                                                                                                                                                                                                                                              |
| Product.catOutCode        | Integer                 | Category code <br>Example: <br>1="SnabbTåg", ”Express”, "Arlanda Express" <br>2="Regional", "InterCity" <br>3=”Expressbuss”, ”Flygbussar” <br>4="Tåg", ”PågaTåg”, ”Öresundståg” <br>5="Tunnelbana" <br>6=”Spårvagn” <br>7="Buss", <br>8=”Färja”, ”Utrikes Färja” <br>9="Taxi"                                                                                                                   |
| Stops         | Stop[]                   | List of upcoming stops for the vehicle at this at this departure/arrival. Enabled/disabled through the `passlist` parameter                                                                                                                                                                                                                                                                                                                                       | |
| Stop.name              | String                  | Name of the stop                                                                                                                                                                                                                                                                                                                                  |
| Stop.arrTime           | String                  | Arrival time at this stop, formatted as HH:MM                                                                                                                                                                                                                                                                                                                                   |
| Stop.arrDate           | Date                    | Arrival time at this stop, formatted as YYYY-MM-DD                                   
| Stop.lat               | String                  | Stop latitude (WGS84, decimal degree), ex 59.293611                   
| Stop.lon               | String                  | Stop longitude (WGS84, decimal degree), ex 18.083056                  
| Stop.id                | String                  | Internal id, do not use                                                                                                                                                                                                 |
| Stop.extId             | String                  | Stop id
| Stop.routeIdx          | Integer                 | Zero-based index 