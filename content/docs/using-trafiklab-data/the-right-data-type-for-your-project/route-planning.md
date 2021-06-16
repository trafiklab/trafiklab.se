---
title: Route-planning
description: We'll discuss which data-sources you need for route-planner applications
---

Route-planning can be intimidating. A route-planner needs a lot of data and processing time in order to come up with the
best results. This is why it is typically performed on a powerful server, which then exposes the functionality through
an API. In most cases, this API fulfils the need of developers. In cases where

### Showing users how to get from A to B using an API

When creating a simple app or website where users can search a route from A to B, you can use the ResRobot API. This way
you don't need to worry about servers or algorithms. Your app can make requests directly to the ResRobot APIs, with the
possibility to specify the origin and destination, transport modes, time of departure/arrival, ... . You typically make
no more than one API call every few seconds.

{{% info %}} If you're building an application specifically for Stockholms Länstrafik, you can use SLs APIs
instead of ResRobot. They have the same features, and might offer slightly more detailed data. {{% /info %}}

#### Searching for routes

You can search for routes by calling the routeplanner endpoint. This endpoint will take a number of parameters and
return a number of journeys. Each journey consists of one or more legs, for example, if you take a train and a bus, or
two trains, your journey contains two legs. Walking parts between different stops also count as legs.

When it comes to specifying the origin, destination, and possible vias, there are two possibilities. You can opt to use
the station ids, or you can use coordinates. While using coordinates has the benefit of seeing the walk to and from the
first and last stop, these queries tend to be a bit slower.

{{% warning %}} Coordinates are personal data, and you should obtain permission from users before sending
their position to an API. The use of this data should be described in your app or websites privacy policy, in accordance
to the GDPR. {{% /warning %}}

#### Searching for stations

If you want to specify the origin and destination station, you will need to find their ids. Follow the link below to
read about the different methods to obtain an id for the ResRobot routeplanning.

{{% page-ref page="obtaining-stop-ids" %}}

### When you need more API calls: hosting your own OpenTripPlanner instance

If you need more than one API call every few seconds, for example when you're creating statistics or an isochrome map,
you will need to run your own API. This has the advantage that you can make as much requests as you want. In order to
run your own API, you can (for example)
use [the open-source OpenTripPlanner](https://github.com/opentripplanner/OpenTripPlanner/) in combination with
our [GTFS Sverige 2](../../public-transport-data/our-data-and-apis/gtfs/gtfs-sverige-2-static/)
or [GTFS Regional](../../public-transport-data/our-data-and-apis/gtfs/gtfs-regional/) datasets.

### Creating your own route-planning API

If an existing project such as  [the open-source OpenTripPlanner](https://github.com/opentripplanner/OpenTripPlanner/)
doesn't fulfill your needs, you can create your own route-planning API. Note that this is for experienced programmers
with lots of time only. You will need to implement your own route-planning algorithm and write your own API, but you can
do anything you want. Use
our [GTFS Sverige 2](../../public-transport-data/our-data-and-apis/gtfs/gtfs-sverige-2-static/)
or [GTFS Regional](../../public-transport-data/our-data-and-apis/gtfs/gtfs-regional/) datasets as a datasource.

### Client-side route-planning

If you need client-side route-planning, you can use
our [GTFS Sverige 2](../../public-transport-data/our-data-and-apis/gtfs/gtfs-sverige-2-static/)
or [GTFS Regional](../../public-transport-data/our-data-and-apis/gtfs/gtfs-regional/) datasets as a datasource and
convert them into [Linked Connections](https://linkedconnections.org/). This way you get small data blocks which you can
process directly in route-planning algorithms on mobile devices.
