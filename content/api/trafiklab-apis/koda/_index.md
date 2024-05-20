---
title: KoDa 
layout: "single"
weight: 50 
date: 2021-12-14
---

KoDA, short for Kollektivtrafikens Datalabb is a dataset and API created by RISE and Vinnova in cooperation with
Trafiklab. It aims to provide historic data about public transport, along with tools to learn how to use this data in
combination with machine learning.

## About KoDa

Kollektivtrafikens Datalabb (KoDa) aims to collect, store, and provide a historical open data record of the real time
and static data that is provided by in the Trafiklab.se open data service. The GTFS static and GTFS realtime data from
many Swedish public transportation authorities’ (PTAs) that currently delivered such are stored in a common database and
becomes an open, annotated, dataset for both local and nationwide applications related to public transport.

The KoDa dataset is envisioned to be the base for application areas within the public transport sector, but it can also
be used in other sectors where other actors can create value by analysing public transport data. A platform for
interacting with the dataset has been developed to enable users to work with data analysis and AI development using the
KoDa public transport dataset as the base.

Public transport is not only an independent business that has its challenges,it can also be seen as a sensor in traffic.
The KoDa data can be used by external actors to get information on the current and historical traffic flows of a city
and thereby be able to monitor effects of changes made to the traffic environment. Accessibility and mobility are a
challenge area where more actors need more and better tools to support the transition to a more mobile & sustainable
society. The KoDa data- and toolset can be a used for the development of applications in that field.

More information about KoDa can be found at [the RiSE projekt page (in Swedish)](https://www.ri.se/sv/vad-vi-gor/projekt/koda).

## What does this dataset contains?

This dataset contains historic versions of our high quality and detailed GTFS data, both static and real-time, going
back to February 5th, 2020.

{{% info %}} **Looking for older data?**

GTFS Sverige 2 contains historical data dating back to 2012.
{{% /info %}}

{{% warning %}} Some data was not available from the start for all operators, therefore there are some feeds that start
at a later date:

- SL VehiclePositions are available from December 1st, 2020. {{% /warning %}}

### Historical data

The KoDA API provides raw GTFS and GTFS-RT data downloads, which are organized per operator, feed, and date.

## Data format

The data is in the GTFS format, and makes use of the GTFS Extensions. Realtime data follows the GTFS-Realtime
(GTFS-RT) standard, and is stored in the protobuf format.

## How often is this dataset updated?

Data is being stored as soon as it becomes public, and is accessible from the next day.

## Which operators are covered by this dataset?

All operators covered by the GTFS Regional dataset are covered by KoDA.

## How often does the data format changes? Do breaking changes happen?

The data in this feed will change according to any changes in the GTFS static or GTFS realtime data.
