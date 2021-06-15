---
title: Historical data
---

{{% info %}} For technical details about HTTP headers, URLs, and response structures, please use the OpenAPI
Specification available on our developer portal. {{% /info %}}

Historical GTFS data can be found
at  [**https://data.samtrafiken.se/trafiklab/gtfs-sverige-2/**](https://data.samtrafiken.se/trafiklab/gtfs-sverige-2/)**
.** This archive is updated every time a new GTFS feed is published. The latest version is not available in this
archive, only through the 'usual' API endpoint.

### Differences between historical systems

Keep in mind that the GTFS Sverige 2 feed has been updated a few times in the time period covered by the archive. This
might affect your data processing when you want to handle data over a timespan of multiple years. There have been
migrations between databases, systems and service providers, for example in 2016. There might be small changes in naming
and data quality between the feeds created by different systems which your analytics need to handle.

### Example differences

* Up till 2016 stop ids used 7 digits. This was changed to 9 digits by replacing the '74' prefix with '7400'.
* Up till 2016 all trains where grouped in one route per type, this was changed to one route per trip.
* Up till 2016 trains used their type as route name, for example "SJ Intercity". This was changed to the train number,
  for example 7689
