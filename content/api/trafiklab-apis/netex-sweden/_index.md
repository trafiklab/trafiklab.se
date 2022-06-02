---
title: NeTEx Sweden (beta)
layout: "single"
weight: 35
date: 2022-06-01
draft: true
---

NeTEx Sweden is a NeTEx feed of high quality. The feed contains all data present in GTFS Sweden, as 
well as additional data which can't be represented in GTFS.

At the moment this dataset does not contain all of the public transport data of Sweden. 
If that is what you are looking for we recommend GTFS Sverige 2, which is much less detailed but does contain all of the public transport data of Sweden.

### What does this dataset contain?

This dataset contains high quality detailed data, both static and real-time, in the NeTEx format.
This dataset is an aggregated dataset of all the different datasets in the [Netex Regional API](/api/trafiklab-apis/netex-regional/).

### Data format

The data is in the NeTEx (**Ne**twork and **T**imetable **Ex**change) format. This is a format in which all European
operators have to publish their data. The data is aimed at both operator-to-traveller communication and internal
communication between different organizations.

### How often is this dataset updated?

The static data in this dataset is updated on a daily basis, typically between 10:00 and 13:00.

### Which operators are covered by this dataset?

See the documentation in the [Netex Regional API](/api/trafiklab-apis/netex-regional/#which-operators-are-covered-by-this-dataset).

### How often does the data format changes? Do breaking changes happen?

This dataset has the **stable** status. This means that the fields can be added without prior warning, but when changes
to existing fields are made, you will get three months to update your implementations.
