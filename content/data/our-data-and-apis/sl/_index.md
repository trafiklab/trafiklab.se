---
title: SL
layout: "single"
---

ResRobot is an API which provides information for public transport in entire Sweden.

| Well suited for | Not so suited for |
| :--- | :--- |
| Quickly getting the next departures from a stop | Analysing public transport information |
| Quickly calculating a route from A to B | Applications requiring huge amounts of API calls |
| Digital Signage | Data visualisation |
| Mobile applications | Building your own route-planner algorithm |
| Websites |  |

{{% warning %}} SL's APIs only offer data for SL's traffic. [ResRobot ](../resrobot/)offers the same data for
entire Sweden. {{% /warning %}}

{% page-ref page="../resrobot/" %}

{{% info %}} If you want to do analytics, or if your service will have more than a million active users, we
recommend using GTFS and hosting your own API based on that data. {{% /info %}}

{% page-ref page="../gtfs/gtfs-regional/" %}
