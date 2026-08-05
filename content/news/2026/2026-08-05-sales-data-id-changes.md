---
title: "GTFS Sweden 2, Resrobot and Samtrafiken sales data ID changes"
date: "2026-08-05"
image: '/media/2024/09/banner_switch.jpg'
---

Around the middle of September 2026, we will be replacing one of the software solutions used to create our GTFS Sverige
2 and Samtrafiken Sales data. This will result in changes to the IDs of `ServiceJourney` elements in our
Samtrafiken Sales NeTEx feed, as well as changes to the IDs in our GTFS Sverige 2 feed and Resrobot APIs. This
change is needed so we can continue improving our data quality in these feeds.

Users of the Samtrafiken sales data must load the complete file once this change takes place and not rely on
`changes.csv` or `changeslines.csv` for incremental updates. We recommend that you remove any previously loaded traffic data
before importing the new file.

We will return with the exact date closer to the release.

The full documentation for our Samtrafiken Sales API is
available [on Trafiklab](https://www.trafiklab.se/api/netex-datasets/samtrafiken-sales-data/). If you have any
questions, please reach out to us [through our support forum](https://support.trafiklab.se).  