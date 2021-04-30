---
title: The right data for your project
layout: "single"
---

### Making a voice assistant tell you about public transport

### Showing the next departures on a smart mirror

### Creating a map with travel times

When creating a map with travel times from one stop to different places, also known as an isochrone map, you need to
make hundreds till even tens of thousands of API calls. Using APIs for this is slow, and causes a huge load on the
server. A much better alternative is to fetch the GTFS files, and calculate everything locally. This way there is no
limit on the number of API calls, meaning you can create a high quality map after a few minutes of route-planning.

{{% info %}} You do not need to write your own route-planning algorithm. There are a lot of existing projects,
such as OpenTripPlanner, which allow you to load a GTFS file and to make API calls against a local API. {{% /info %}}

{{% info %}} There are over 50.000 stop locations in Sweden. It would take 25 million API calls to create an
isochrone map from every stop to every stop.This is equal to all ResRobot API traffic for 2 months. {{% /info %}}

### Creating your own routeplanner algorithm

### Tracking delays

### Showing the actual position of a bus, train, ...
