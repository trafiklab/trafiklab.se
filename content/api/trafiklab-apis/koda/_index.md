---
title: KoDA 
layout: "single"
weight: 50
date: 2021-07-29
draft: true
cascade:
    draft
---

KoDA, short for Kollektivtrafikens Datalabb is a dataset and API created by RISE, Vinnova and Trafiklab. It aims to
provide historic data about public transport, along with tools to learn how to use this data in combination with machine
learning.

### About Koda

Kollektivtrafikens Datalabb (KoDa) aims to collect, store, and provide a historical open data record of the real time
and static data that is provided by in the Trafiklab.se open data service. The GTFS static and GTFS realtime data from
many Swedish public transportation authorities’ (PTAs) that currently delivered such are stored in a common database and
becomes an open, annotated, dataset for both local and nationwide applications related to public transport. The KoDa
dataset is envisioned to be the base for application areas within the public transport sector, but it can also be used
in other sectors where other actors can create value by analysing public transport data. A platform for interacting with
the dataset has been developed to enable users to work with data analysis and AI development using the KoDa public
transport dataset as the base. Public transport is not only an independent business that has its challenges, it can also
be seen as a sensor in traffic. The KoDa data can be used by external actors to get information on the current and
historical traffic flows of a city and thereby be able to monitor effects of changes made to the traffic environment.
Accessibility and mobility are a challenge area where more actors need more and better tools to support the transition
to a more mobile & sustainable society. The KoDa data- and toolset can be a used for the development of applications in
that field.

### What does this dataset contains?

This dataset contains historic versions of our high quality and detailed GTFS data, both static and real-time, going
back to December 2019.

#### KoDa API

To access the KoDa data the user has to interact via the [KoDa API](https://api.koda.trafiklab.se/KoDa/api/v2/swagger/).
The KoDa API allows the user to access the raw static and real time GTFS data via special API calls.

#### KoDa Database

The raw GTFS and GTFS-rt data has been downloaded from [trafiklab.se](https://www.trafiklab.se/) and stored in its raw
original GTFS format but the data has also been imported into a [Cassandra](https://cassandra.apache.org/) database.

To access the structured database a user has to get an account for the KoDa JupyterHub server. To request an account
please contact 'koda(at)ri.se'.

### Data format

The data is in the GTFS format, and makes use of the GTFS Extensions. Realtime data follows the GTFS-Realtime
(GTFS-RT) standard, and is stored in the protobuf format.

### How often is this dataset updated?

### Which operators are covered by this dataset?

All operators covered by the GTFS Regional dataset are covered by KoDA.

### How often does the data format changes? Do breaking changes happen?

# Example of usage

In order to help users how the KoDa database and services can be used we have prepared a number
of [examples](koda-api/examples.md) that illustrate some features of the KoDa system.

