---
title: SL's APIs
layout: "single"
weight: 80
---
SL's APIs is a collection of 7 APIs which provide information about planned and realtime traffic.

| Well suited for | Not so suited for |
| :--- | :--- |
| Quickly getting the next departures from a stop | Analysing public transport information |
| Quickly calculating a route from A to B | Applications requiring huge amounts of API calls |
| Digital Signage | Data visualisation |
| Mobile applications | Building your own route-planner algorithm |
| Websites |  |

{{% info %}} SL's APIs only offer data for SL's traffic. [ResRobot](../resrobot/) offers the same data for
entire Sweden. {{% /info %}}

{{% info %}} If you want to do analytics, or if your service will have more than a million active users, we
recommend using GTFS data directly, or hosting your own API based on GTFS data. {{% /info %}}

{{% page-ref "/api/trafiklab-apis/resrobot-v2/" "/api/trafiklab-apis/gtfs-regional/" %}}
