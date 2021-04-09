---
title: "Changes to the GTFS Regional API"
date: "2020-02-20"
layout: info
---

# Changes in the GTFS Regional URLs

The Regional APIs will soon be stable. However, before we can release them as stable, we need to make a last change to
the URL structure. This change means that you, as a data consumer, need to make a small change to your client in order
to keep using our data.

## Why we are doing this

In order to guarantee that the URLs can be permanent, we need to ensure they are future-proof. By adding the data type
to every url (gtfs, gtfs-rt, netex) we ensure that all URLs are consistent, readable, and allow for flexibility on the
server implementation. This way we can keep improving our APIs later on without making changes to the URLs.

## Which changes are needed in clients

When making requests to retrieve static GTFS files (zip files), you need to change the base URL from
opendata.samtrafiken.se to opendata.samtrafiken.se/gtfs. For example,
https://opendata.samtrafiken.se/ul/ul.zip becomes https://opendata.samtrafiken.se/gtfs/ul/ul.zip

When making requests to retrieve realtime GTFS files (protobuf files), you need to change the base URL from
opendata.samtrafiken.se to opendata.samtrafiken.se/gtfs-rt. For example,
https://opendata.samtrafiken.se/ul/TripUpdates.pb becomes https://opendata.samtrafiken.se/gtfs-rt/ul/TripUpdates.pb.

The documentation on Trafiklab has been update to show these updated URLs, so you can find all information there as
well.

## Migration period for the new URLs

We will automatically redirect all requests using an old address to the new address until March 31st 2020. After March
31st the old URLs will cease to function.

Questions Do not hesistate to contact us in case you have any questions. You can always reach us at info@trafiklab.se. 
 



