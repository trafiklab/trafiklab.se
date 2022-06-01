---
title: GTFS Sweden
layout: "single"
weight: 10
aliases:
  - /api/gtfs-sweden-static-data
  - /api/gtfs-sweden-realtime
---

GTFS Sweden is a high quality GTFS feed containing most of the public transport data of Sweden. 

### What does this dataset contain?

This dataset contains high quality detailed data, both static and real-time, in the GTFS format.  
This dataset is an aggregated dataset of all the different datasets in the [GTFS Regional API](/api/trafiklab-apis/gtfs-regional/).
There is a single GTFS feed for static data. The realtime feeds are split up by specific regions or operators (for performance reasons). 

At the moment this dataset does not contain all of the public transport data of Sweden. 
If that is what you are looking for we recommend [GTFS Sverige 2](/api/trafiklab-apis/gtfs-sverige-2/), which is less detailed but does contain all of the public transport data of Sweden.

### Data format

The data is in the GTFS format, and makes use of the GTFS Extensions. Realtime data follows the GTFS-Realtime
(GTFS-RT) standard, and is stored in the protobuf format.

This data is also available in the NeTEx format. For the NeTEx format, see the 
[NeTEx Sweden API](/api/trafiklab-apis/netex-sweden/).

### How often is this dataset updated?

The static data in this dataset is updated on a daily basis. The real-time data receives multiple updates per minute,
see [realtime data](realtime) for more information.

### Which operators are covered by this dataset?

As this dataset is an aggregated format of the regional datasets you can see which operators are included in the documentation for the [Regional API](/api/trafiklab-apis/gtfs-regional/#which-operators-are-covered-by-this-dataset)

### How often does the data format changes? Do breaking changes happen?

Both the static and realtime datafeeds are stable. While we add new data all the time, we don't make breaking 
changes. Should we need to make a breaking change, we'll inform users first, and you'll have around 6 months time to 
make the necessary adjustments to your code.
