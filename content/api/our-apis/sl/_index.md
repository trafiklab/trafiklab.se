---
title: SL's APIs
layout: "single"
weight: 80
image: '/media/2024/09/banner_pendeltag.jpg'
image_position: 'bottom'
cascade:
  - image: '/media/2024/09/banner_pendeltag.jpg'
  - image_position: 'bottom'
---

SL's APIs is a collection of 3 APIs which provide information about planned and realtime traffic.

{{% info %}}
SL has updated their API's. 7 API's have become 3:
<ul>
<li>SL Transport (new: has replaced Departures v4 & Stops and lines v2) 
<li>SL Deviations (new: has replaced Service Alerts & Traffic Status)
<li>SL Journeyplanner (new: has replaced Route-planner and Stop lookup)</li>
</ul>
{{% /info %}}

| Well suited for                                 | Not so suited for                                |
|:------------------------------------------------|:-------------------------------------------------|
| Quickly getting the next departures from a stop | Analysing public transport information           |
| Quickly calculating a route from A to B         | Applications requiring huge amounts of API calls |
| Digital Signage                                 | Data visualisation                               |
| Mobile applications                             | Building your own route-planner algorithm        |
| Websites                                        |                                                  |

{{% info %}} SL's APIs only offer data for SL's traffic. [ResRobot](/api/our-apis/resrobot-v21/) offers the same data for
entire Sweden. {{% /info %}}

{{% info %}} If you want to do analytics, or if your service will have more than a million active users, we
recommend using GTFS data directly, or hosting your own API based on GTFS data. {{% /info %}}

{{% page-ref "/api/our-apis/resrobot-v21/" "/api/gtfs-datasets/gtfs-regional/" %}}
