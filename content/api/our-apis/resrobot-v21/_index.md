---
title: ResRobot v2.1
layout: "single"
weight: 41
aliases: 
  - /api/resrobot2
  - /api/resrobot21
  - /api/trafiklab-apis/resrobot-reseplanerare
  - /node/14049
  - /api/trafiklab-apis/resrobot-stolptidtabeller-2
  - /node/14075
  - /api/resrobot
date: 2022-02-07
image: '/media/2024/09/banner_phone.jpg'
cascade:
  - image: '/media/2024/09/banner_phone.jpg'
---

### What is ResRobot?

ResRobot is a collection of APIs which provide information for public transport in entire Sweden. It consists of four 
endpoints. 
- ResRobot Timetables allows you to find departures and arrivals for those stations
- ResRobot Routeplanner allows you to find ways to travel from A to B 
- ResRobot Stop lookup allows you to search for stops and to obtain their ID
- ResRobot Nearby stops allows you to search for nearby stops based on coordinates.

### When should I use ResRobot?

ResRobot is an API which answers to specific questions, such as "when does the next bus leave from stop X". The response
is quick and easy to use, and can be used directly without having to process it first. This makes it a good fit for for
example smartphone applications where travellers need an answer on their queries, but a poor choice for analytics where
a lot of data from a lot of vehicles is needed.

{{% info %}}
Want to build departure or arrival boards for digital signage, smart mirrors, home automation, ... etc? Take a look at
our [Trafiklab realtime APIs](/api/our-apis/trafiklab-realtime-apis/_index.md) which contain more details and realtime data,
while being easier to use.
{{% /info %}}

| Well suited for                         | Not so suited for                                |
|:----------------------------------------|:-------------------------------------------------|
| Websites and widgets                    | Analysing public transport information           |
| Quickly calculating a route from A to B | Applications requiring huge amounts of API calls |
| Mobile applications                     | Data visualisation                               |
|                                         | Building your own route-planner algorithm        |

### API key levels
There is only one API key required to access all features in ResRobot, the different key levels are specified in the table below. If you don´t have a key yet, 
read [here](/docs/using-trafiklab/getting-api-keys) on how to get one.

| Level    | Maximum calls per minute | Maximum calls per month |
|:---------|:------------------------:|:-----------------------:|
| Bronze   |            45            |         30 000          |
| Silver   |            60            |         200 000         |
| Gold     |           200            |        1 000 000        |

{{% warning %}} Upgrade requests for Resrobot API keys using the departure boards will not be approved when our
[Trafiklab realtime APIs](/api/our-apis/trafiklab-realtime-apis/_index.md) are a better fit. Please check if the 
realtime APIs are better for your use case before starting development. You can always ask us at [our support forum](https://support.trafiklab.se).{{% /warning %}}

{{% warning %}} If you want to do analytics, or if your service will have more than a million active users,
we recommend using GTFS and hosting your own API based on that data. One GTFS file can transfer more information than a
million API calls. {{% /warning %}}

{{% page-ref "/api/gtfs-datasets/gtfs-regional/" "/api/gtfs-datasets/gtfs-sverige-2" %}}
