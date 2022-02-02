---
title: ResRobot v2
layout: "single"
weight: 40
aliases: 
  - /api/trafiklab-apis/resrobot-reseplanerare
  - /node/14049
  - /api/trafiklab-apis/resrobot-stolptidtabeller-2
  - /node/14075
  - /api/resrobot
---

### What is ResRobot?

ResRobot is a collection of APIs which provide information for public transport in entire Sweden. It consists of four
endpoints.

- ResRobot Timetables allows you to find departures and arrivals for those stations
- ResRobot Routeplanner allows you to find ways to travel from A to B
- ResRobot Stop lookup allows you to search for stops and to obtain their ID
- ResRobot Nearby stops allows you to search for nearby stops based on coordinates.

{{% warning %}}
**New version available**

A new version of ResRobot is available. Existing apps should migrate to the new version, and it is no longer possible to
build new apps on version 2.0. 

**Version 2.0, which you are currently looking at, will be discontinued at June 30th, 2022.**   
{{% /warning %}}

### When should I use ResRobot?

ResRobot is an API which answers to specific questions, such as "when does the next bus leave from stop X". The response
is quick and easy to use, and can be used directly without having to process it first. This makes it a good fit for
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
