---
title: Realtime data
weight: 3
layout: "single"
sidebar: true
aliases:
  - /docs/using-trafiklab-data/using-gtfs-files/realtime-gtfs-files/
---

Realtime data refers to elements defined in the [static data](#static-gtfs-files). You therefore need to download both 
the static dataset and the realtime files if you want to make use of Realtime GTFS.  

{{% info %}} We will only discuss the general working and contents of GTFS Realtime feeds. You can find the
complete technical specification
at [https://developers.google.com/transit/gtfs-realtime/](https://developers.google.com/transit/gtfs-realtime/).
{{% /info %}}

{{% warning %}} GTFS Realtime communicates deviations from the data in the static GTFS file. You need both in
order to create realtime timetables. {{% /warning %}}

The GTFS Realtime standard uses
the [protobuf format](/docs/using-trafiklab-data/the-protobuf-file-format) to transfer compact messages
which describe deviations between the
real world and the schedules for a public transport network. There are 3 different feeds, each of which provides their
own type of information.

### ServiceAlerts

ServiceAlerts provide information about incidents, planned maintenance, ... which affect more than one or a couple of
trips. They can describe a closed station, incidents like electricity failures or defect trains, extra services for
certain events, ... . They typically contain similar information as the messages shown on digital signs in stations.
Usually a header, description and link are provided, along with a cause and an effect (provided as an enum). Service
alerts can be limited in time or to certain agencies, trips, stops, transport types, ...

### TripUpdates

TripUpdates provide information about deviations between the scheduled timetable of a trip and the real world. This can
be a delay, a vehicle running early, a partial cancellation, a platform change, ... . Each TripUpdates file contains
multiple TripDescriptors, each of which describes deviations in a trip. If a scheduled trip isn't present in a
TripUpdates file, this can both mean that there are no delays, or that no information is available.

### VehicleUpdates

VehicleUpdates contain realtime GPS positions of public transport vehicles. These allow you to see where a vehicle is
located, along with its speed and bearing. These can be used to show vehicles on a map, to analyze traffic congestion,
...

### Continue reading

{{% page-ref page="/docs/using-trafiklab-data/the-protobuf-file-format" %}}

<br>
