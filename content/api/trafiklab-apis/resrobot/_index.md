---
title: ResRobot v2
layout: "single"
weight: 40
url: "api/resrobot"
aliases: 
  - /api/resrobot-reseplanerare
  - /api/resrobot-stolptidtabeller-2
---

### What is ResRobot?

ResRobot is an API which provides information for public transport in entire Sweden. It consists of three endpoints. The
first endpoint, Stop lookup, allows you to search for stops and to obtain their ID. The second endpoint, Timetables,
allows you to find departures and arrivals for those stations. The last endpoint, the route planner, allows you to find
ways to travel from A to B.

### When should I use ResRobot?

ResRobot is an API which answers to specific questions, such as "when does the next bus leave from stop X". The response
is quick and easy to use, and can be used directly without having to process it first. This makes it a good fit for for
example smartphone applications where travellers need an answer on their queries, but a poor choice for analytics where
a lot of data from a lot of vehicles is needed.

| Well suited for | Not so suited for |
| :--- | :--- |
| Quickly getting the next departures from a stop | Analysing public transport information |
| Quickly calculating a route from A to B | Applications requiring huge amounts of API calls |
| Digital Signage | Data visualisation |
| Mobile applications | Building your own route-planner algorithm |
| Websites and widgets |  |

{{% warning %}} If you want to do analytics, or if your service will have more than a million active users,
we recommend using GTFS and hosting your own API based on that data. One GTFS file can transfer more information than a
million API calls. {{% /warning %}}

{{% page-ref "/api/trafiklab-apis/gtfs-regional/" "/api/trafiklab-apis/gtfs-sverige-2/" %}}
