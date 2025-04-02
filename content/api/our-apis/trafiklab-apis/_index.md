---
title: Trafiklab APIs
layout: "single"
weight: 1
date: 2025-04-01
image: '/media/2024/09/banner_phone.jpg'
badge: beta
cascade:
  - image: '/media/2024/09/banner_phone.jpg'
---

Trafiklabs APIs are a collection of APIs which provide information for public transport in entire Sweden. They are developed internally based on our own GTFS
Sweden 3 data, offering the same data in a way which is more suited for direct consumption.

{{% note %}}
**Trafiklabs APIs vs Resrobot**

These APIs are a direct replacement for Resrobot 2.1, except for trip planning, which will remain available in its current form. Compared to Resrobot, they
contain more detailed data, such as platforms and realtime data. They offer significantly better performance as well, which translates into higher quota for end
users while reducing the costs for Trafiklab.
{{% /note %}}

## Usage

At this time, the APIs can be used for [looking up departures and arrivals](timetables). In order to find stop ids, or for route planning, use
the [Resrobot APIs](../resrobot-v21).

## Use cases

Trafiklabs APIs answers to specific questions, such as "when are the next departures from stop X". The response
is quick and easy to use, and can be used directly without having to process it first. This makes it a good fit for for
example smartphone applications where travellers need an answer on their queries, and for digital displays without much processing power.
It is however a poor choice for analytics where a lot of data from a lot of vehicles is needed, since a lot of API calls would be required to transfer large
amounts of data.

| Well suited for                                 | Less suited for                               |
|:------------------------------------------------|:----------------------------------------------|
| Quickly getting the next departures from a stop | Analysing public transport information        |
| Digital signage                                 | Applications requiring a certain uptime (SLA) |
| Onboard signage                                 | Data visualisation                            |
| Mobile applications                             |                                               |
| Websites and widgets                            |                                               |

### API key levels

There is only one API key required to access all features in ResRobot, the different key levels are specified in the table below. If you don´t have a key yet,
read [here](/docs/using-trafiklab/getting-api-keys) on how to get one.

| Level    | Maximum calls per minute | Maximum calls per month | Example usage                                  |
|:---------|:------------------------:|:-----------------------:|:-----------------------------------------------|
| Bronze   |            25            |         100.000         | Departure boards for 2 stops                   |
| Bronze + |            25            |         500.000         | Departure boards for 10 stops                  |
| Silver   |           150            |        5.000.000        | Departure boards for 100 stops, mobile apps    |
| Gold     |          1.200           |       50.000.000        | Departure boards for 1.000 stops, mobile apps  |
| Platinum |          6.000           |       250.000.000       | Departure boards for 5.000 stops , mobile apps |

{{% warning %}} If you want to analyze data, if your service will have more than a million active users, or if you have strict requirements regarding uptime
we recommend using GTFS and hosting your own API based on that data. One GTFS file contains all information you possibly can get out of this API, meaning it's
easier to download this file if you need large amounts of data for analysis. {{% /warning %}}

{{% page-ref "/api/gtfs-datasets/gtfs-regional/" "/api/gtfs-datasets/gtfs-sverige-2" %}}
