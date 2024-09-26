---
title: Overview
weight: 1
layout: "single"
sidebar: true
aliases:
  - /docs/using-trafiklab-data/using-gtfs-files/
  - /docs/using-trafiklab-data/using-gtfs-files/static-gtfs-files/
  - /docs/using-trafiklab-data/using-gtfs-files/realtime-gtfs-files/
---

## GTFS at Trafiklab

At Trafiklab, we offer three GTFS feeds.

[GTFS Sverige 2](/api/gtfs-datasets/gtfs-sverige-2) which includes information for entire Sweden

[GTFS Regional](/api/gtfs-datasets/gtfs-regional) which consists of multiple GTFS feeds, each of which covers an
operator in Sweden

[GTFS Sweden 3](/api/gtfs-datasets/gtfs-sweden) which is an aggregated dataset of all the different datasets
  in GTFS Regional. It gives a single GTFS feed for static data while the realtime feeds are, for performance
  reasons, split up by specific regions or operators

#### What is the difference?
It can be hard to understand the differences between all GTFS feeds but here is a short description. GTFS Sverige 2 is
the only feed with complete coverage of operators in Sweden and only contains static data. GTFS Regional is per
region/operator and perfect if you are interested in for example only SL or only Skånetrafiken. GTFS Regional also
contains
more details like for example shapes or stop points (instead of only stop areas) which is missing in GTFS Sverige.
GTFS Sweden 3 is an aggregated dataset of all GTFS Regional so the level of detail is the same. The goal is to replace
GTFS Sverige with this dataset but that requires a 100% coverage of operators which is not the case at the moment

You can see the general difference between GTFS Sverige 2 and GTFS Regional data below.
<div class="wide">

|                          | GTFS Sverige 2   | GTFS Regional/ GTFS Sweden 3                   |
|:-------------------------|:-----------------|:-----------------------------------------------|
| Coverage                 | 100%             | 92%                                            |
| Data quality             | Average quality  | High quality, based on higher level of details |
| Real-time data           | Only static data | Static + Real-time + GPS positions             |
| Historical data (static) | Since 2012       | Partly available in Koda                       |

{{% info %}} You can find the complete GTFS reference
at [https://developers.google.com/transit/gtfs/reference/](https://developers.google.com/transit/gtfs/reference/).

You can find the complete GTFS-RT reference
at [https://developers.google.com/transit/gtfs-realtime/reference](https://developers.google.com/transit/gtfs-realtime/reference)
{{% /info %}}

{{% note %}} If you want to learn about what GTFS is and how it works, read further [down](./_index.md#gtfs-basics)
on this page.
{{% /note %}}


## GTFS basics

### What is GTFS?

The **General Transit Feed Specification** is a file format which originally was developed by Google in 2006. It
combines all the data in one compact file. This means you can download a single file to get timetable information for
the entirety of Sweden. The GTFS standard defines files which must be present in the dataset, and files which are
optional. In this guide we will only discuss the files which are present in the Trafiklab datasets.

The GTFS Standard consists of 2 parts: static and real-time data. In the following sections, we will help you to get
started with both.

### How does GTFS Work?

A GTFS file is a zip archive that contains several \*.txt files. You can compare this archive file with a database. The
files inside the archive contain Comma Separated Values (CSV) data, meaning they are easy to read, both for computers
and humans. Each file contains all the instances of a certain type, just like a database table. For example, one file
contains all the routes, another file contains all the stops. The files are linked together through ids, similar to how
foreign keys work in a database. The image below gives an idea of the structure.
{{% warning %}} GTFS Sverige 2 does not contain a shapes.txt file {{% /warning %}}

![The GTFS model, as used by Trafiklab. Fields which are always present are marked in bold.](/media/2020/05/gtfs-model.png)
The GTFS model contains multiple files, which can be required or optional. The fields in these files can be always
present, present for certain feed (e.g. only in GTFS Regional) or optional. The diagram above shows which fields are
used by Trafiklab. The fields which are always present in a file are marked in bold. The tables marked in green are
required by the GTFS standard, the blue ones are optional files used in the Trafiklab data.

{{% info %}} A GTFS archive forms a database-like structure with every file as one table, and you can import
these CSV files directly into a new database to run queries on them. One example is
the [csv2db](https://csv2db.github.io/) tool, but there are many other ways to achieve this. {{% /info %}}

### How it is linked together

Before diving deeper into what each field means, it's important to understand how transport data is described in the 7
required files.

A certain "path" on which public transport vehicles travel, is called a **route** and defined in routes.txt. A **route**
is provided by a public transport **agency** (defined in agencies.txt), and can be serviced one or more times in a
day. Every **trip** on a route is defined in the trips.txt file.

**Example**: Let's say there is a route "Stockholm - Skövde - Göteborg". There is a train leaving stockholm at 10:00,
12:00, and 16:00. In this case, we have one route with three trips on that route.

{{% warning %}} Different trips on the same route might make use of different stops. {{% /warning %}}

The stops which are made during a trip are defined as **stop times** in stop\_times.txt. A **stop time** does not
contain information about the stop itself: it only links a **trip** to a **stop**, and includes some additional
information such as the time of arrival and departure. Stops itself are defined in the stops.txt file, including
information such as their name, location and entrances.

**Example**: Let's say there is a trip on the route "Stockholm - Skövde - Göteborg" leaving at 10:00. The GTFS file
would contain the trip, 3 stops, and 3 stop\_times to link the stops to the trip.

### When should I use GTFS?

A dataset like GTFS is the opposite of an API like ResRobot. Each has its own benefits and drawbacks. When you want to
create a simple app, or let users search for the next departure from your website, an API is easier to use. However,
when you want to analyze data, an API would need millions of requests compared to a single GTFS file that has all the
data.

| Well suited for                                                                | Not so suited for                                   |
|:-------------------------------------------------------------------------------|:----------------------------------------------------|
| Analysing (real-time) transport data                                           | Quickly getting the next departures from a stop     |
| Building your own route-planner or API                                         | Quickly calculating a route from A to B             |
| Getting a list of all public transport stop-areas for an operator or a country | Projects where large files (&gt;25MB) can't be used |
| Getting the live position of all public transport vehicles                     |                                                     |

{{% info %}} There are hundreds of libraries, examples and demos for GTFS. You can find some
at [https://github.com/andredarcie/awesome-gtfs](https://github.com/andredarcie/awesome-gtfs)
and [https://github.com/CUTR-at-USF/awesome-transit](https://github.com/CUTR-at-USF/awesome-transit). {{% /info %}}