---
title: ResRobot Deep Links 
weight: 200
date: 2022-02-07
aliases: /api/resrobot-reseplanerare/djuplankning-0
---

## What does this API provide?

ResRobot deep links allow you to create links that point directly to specific results in the ResRobot web application.

### Data format

You will get a redirect to the page with results.

### Updates

The static data behind the ResRobot web application is updated when changes are made, at most once per day.

### Operators covered by this API

All operators which operate in Sweden are covered by the ResRobot web application.

### Breaking changes

This API has the **stable** status. When breaking changes are made, we strive to have a 6 months transition period for
users to update their implementations. Examples of breaking changes are the changes to existing fields or query
parameters, or in case new query parameters are required to keep the results the same. The addition of new fields isn't
considered a breaking change, and can happen without warning.

## Using ResRobot Deep links

In order to use deep links into ResRobot results, you construct the request URL based on the parameters you want to show
results for, and redirect the user who needs to see the results to this URL. This allows you to show users
route-plannings directly from your website or app, without any need to implement your own user-interface. 

## Request and response

### Requests

{{% info %}} 
**No key required** 

This API does not require an API key. 
{{% /info %}}

Example 1: Route between specific stops

[https://reseplanerare.resrobot.se/bin/query.exe/sn?&S=740000044&Z=740000001&start=1](https://reseplanerare.resrobot.se/bin/query.exe/sn?&S=740000044&Z=740000001&start=1)

Example 2: Between coordinates

[https://reseplanerare.resrobot.se/bin/query.exe/sn?&SID=A=16@X=17703271@Y=59869065@O=Uppsala&Z=740000001&time=12:00&amp;timesel=arrive&start=1](https://reseplanerare.resrobot.se/bin/query.exe/sn?&SID=A=16@X=17703271@Y=59869065@O=Uppsala&Z=740000001&time=12:00&timesel=arrive&start=1)

#### Request parameters

| Parameter | Required                              | Description                                                                                                                                                                                                                                                                                                                                                                                                                  | Example                                     |
| --------- | ------------------------------------- |------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| ------------------------------------------- |
| S         | Either `S` or `SID` are required      | _extId_ for the origin stop. This id can be obtained through [the stop lookup API](/api/trafiklab-apis/resrobot-v21/resrobot-stop-lookup/) or [the nearby stops API](/api/trafiklab-apis/resrobot-v21/resrobot-nearby-stops/). Can not be used in combination with the `SID` parameter.                                                                                                                                      | 740000044 (for Helsingborgs Centralstation) |
| SID       | Either `S` or `SID` are required      | A so-called “triple id” containing the name and coordinates for the place of departure. Syntax: `[A=16@X=<X-coordinate>@Y=<Y-coordinate>@O=<name>`.<br>Coordinates must be in [WGS84 format](https://en.wikipedia.org/wiki/World_Geodetic_System_1984), with 6 digits precision but without comma. Name is the name shown to the user and does not affect the search. Can not be used in combination with the `S` parameter. | A=16@X=17703271@Y=59869065@O=Uppsala        |
| Z         | Either `Z` or `ZID` are required      | _extId_ for the origin stop. This id can be obtained through [the stop lookup API](/api/trafiklab-apis/resrobot-v21/resrobot-stop-lookup/) or [the nearby stops API](/api/trafiklab-apis/resrobot-v21/resrobot-nearby-stops/). Can not be used in combination with the `SID` parameter.                                                                                                                                      | 740000001 (for Stockholm Centralstation)    |
| ZID       | Either `Z` or `ZID` are required      | A so-called “triple id” containing the name and coordinates for the place of arrival. Syntax: `[A=16@X=<X-coordinate>@Y=<Y-coordinate>@O=<name>`.<br>Coordinates must be in [WGS84 format](https://en.wikipedia.org/wiki/World_Geodetic_System_1984), with 6 digits precision but without comma. Name is the name shown to the user and does not affect the search. Can not be used in combination with the `S` parameter.   | A=16@X=18048505@Y=59340682@O=Home           |
| timesel   | No, default depart                    | Indicates if the specified time and date are the departure or arrival date/time. Can be `arrive` or `depart`.                                                                                                                                                                                                                                                                                                                | depart                                      |
| date      | No, default today                     | Date of departure or arrival, in the YYYY-MM-DD format                                                                                                                                                                                                                                                                                                                                                                       | 2020-12-31                                  |
| time      | No, default now                       | Time of departure or arrival, in the YYYY-MM-DD format                                                                                                                                                                                                                                                                                                                                                                       | 15:23                                       |
| start     | Yes                                   | Must be set to `1`                                                                                                                                                                                                                                                                                                                                                                                                           | 1                                           |

### Response

You will receive a meta-redirect to the route-planning page.

```html
<html>
<head>
    <meta http-equiv="Refresh"
          content="0; url=https://reseplanerare.resrobot.se/index.html#!P|TP!SID|A%3D16%40O%3DUppsala%40X%3D17703271%40Y%3D59869065%40!S|Uppsala!ZID|A%3D1%40O%3DStockholm%20Centralstation%40X%3D18058151%40Y%3D59330136%40U%3D1%40L%3D740000001%40B%3D1%40V%3D74.9,%40p%3D1633491748%40!Z|Stockholm%20Centralstation!date|07.10.2021!time|12:00!start|1"/>
    <script>location.replace('https://reseplanerare.resrobot.se/index.html#!P|TP!SID|A%3D16%40O%3DUppsala%40X%3D17703271%40Y%3D59869065%40!S|Uppsala!ZID|A%3D1%40O%3DStockholm%20Centralstation%40X%3D18058151%40Y%3D59330136%40U%3D1%40L%3D740000001%40B%3D1%40V%3D74.9,%40p%3D1633491748%40!Z|Stockholm%20Centralstation!date|07.10.2021!time|12:00!start|1');</script>
</head>
<body>
The journey planner moved to a new url.<br>
<a href="https://reseplanerare.resrobot.se/index.html#!P|TP!SID|A%3D16%40O%3DUppsala%40X%3D17703271%40Y%3D59869065%40!S|Uppsala!ZID|A%3D1%40O%3DStockholm%20Centralstation%40X%3D18058151%40Y%3D59330136%40U%3D1%40L%3D740000001%40B%3D1%40V%3D74.9,%40p%3D1633491748%40!Z|Stockholm%20Centralstation!date|07.10.2021!time|12:00!start|1">Click
    here to start the journey planner</a>
</body>
</html>
```