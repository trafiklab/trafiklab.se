---
title: SL's APIs
layout: "single"
weight: 80
---
SL's APIs is a collection of 7 APIs which provide information about planned and realtime traffic.

{{% info %}}
SL has updated their API's. 7 API's has become 5:
<ul>
<li>SL Transport (new: has replaced Departures v4 & Stops and lines v2) 
<li>SL Deviations (new: has replaced Service Alerts & Traffic Status)
<li>SL Route-planner v3.1 (updated: new url) 
<li>SL Stop lookup (updated: new url)
<li>SL Nearby stops 2 (updated: new url)
</ul>
{{% /warning %}}

| Well suited for | Not so suited for |
| :--- | :--- |
| Quickly getting the next departures from a stop | Analysing public transport information |
| Quickly calculating a route from A to B | Applications requiring huge amounts of API calls |
| Digital Signage | Data visualisation |
| Mobile applications | Building your own route-planner algorithm |
| Websites |  |

{{% info %}} SL's APIs only offer data for SL's traffic. [ResRobot](/api/trafiklab-apis/resrobot-v21/) offers the same data for
entire Sweden. {{% /info %}}

{{% info %}} If you want to do analytics, or if your service will have more than a million active users, we
recommend using GTFS data directly, or hosting your own API based on GTFS data. {{% /info %}}

{{% page-ref "/api/trafiklab-apis/resrobot-v21/" "/api/trafiklab-apis/gtfs-regional/" %}}
