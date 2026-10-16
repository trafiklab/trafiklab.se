---
title: "Improvements in GTFS Sweden 2"
date: 2018-05-31
draft: true
image: "/media/2018/05/2018-05-31-forbattringar-i-gtfs-sverige-2-1.png"
---

## Hi all Trafiklab users!

From 18 June 2018, there will be some changes in GTFS Sweden 2. It will include two new extra files, trips_technical.txt and routes_technical.txt. We will also introduce changes to trip_id and route_id. Our new IDs are longer than before, and we want to inform you before we deploy this so that you have time to adapt your applications if needed.

In short, this is what will happen:

![](/media/2018/05/2018-05-31-forbattringar-i-gtfs-sverige-2-1.png)

## What is Trips_technical.txt?

The idea behind trips_technical.txt is that it lets you get the technical trip number (technical_trip_number) for a given trip_id from GTFS. One example use case is taking the technical_trip_number for trains and using it to look up announced information for trains in Trafikverket's APIs. Trips_technical.txt is a comma-separated file with two fields as shown below:

![](/media/2018/05/2018-05-31-forbattringar-i-gtfs-sverige-2-2.jpg)

One example of an improvement is the naming of commuter trains in trips_short_name and trips_long_name, which will be more in line with [GTFS best practice](http://gtfs.org/best-practices/). In concrete terms, this change means that the commuter trains' train numbers will be removed from trip_short_name. During a transition period, they will be present in both trip_short_name and technical_trip_number. After the transition period, we will put the commuter trains' line numbers in route_long_name instead, e.g. Pendeltåg 40 instead of just Pendeltåg as it is today.

## What is Routes_technical.txt?

The technical line number (technical_route_number) can be very helpful when you want to filter out certain services from the full GTFS dataset, e.g. only buses belonging to Malmö city bus services. Routes_technical.txt is a comma-separated file with two fields as shown below:

![](/media/2018/05/2018-05-31-forbattringar-i-gtfs-sverige-2-3.jpg)

## Changes to trip_id and route_id

Below you can see examples of what trip_id and route_id may look like after the change.

Important: We strongly recommend **not** trying to extract data from the different parts, e.g. the technical trip number from pos 9-14 in trip_id, but to treat them as random numbers. To get the technical trip number, for example, you have to go to trips_technical.txt. The structure of the IDs may change without prior notice. Instead, you should retrieve the fields where they are located, i.e. agency.agency_id, trips_technical.technical_trip_id and routes_technical.technical_route_id. This is in line with GTFS best practice.

Example of trip_id: 23334444666666

- Pos 1-1 (2) = Class ID for trip id is 2. (Class ID for route id is 1).
- Pos 2-4 (333) = Transport authority number
- Pos 5-8 (4444) = Technical line number
- Pos 9-14 (666666) = Technical trip number or a running number if needed to make the trip unique

Example of route_id: 1333444455555

- Pos 1-1 (1) = Class ID for route id is 1. (Class ID for trip id is 2).
- Pos 2-4 (333) = Transport authority number
- Pos 5-8 (4444) = Technical line number
- Pos 9-13 (55555) = Running number to make it unique with regards to short name, long name and means-of-transport

If you have any questions about this, you are welcome to contact us [here](http://kundo.se/org/trafiklabse/)
