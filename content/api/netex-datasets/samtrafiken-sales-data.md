---
title: Samtrafiken Sales data
layout: "single"
weight: 35
date: 2025-01-10
aliases:
  - /api/trafiklab-apis/samtrafiken-sales-data/
---

Samtrafiken Sales data is a NeTEx feed with sellable data.
This API differ from the NeTEx Sweden API. More details about additional, removed or changed fields can be found through the following url:
[Samtrafiken sales export](https://samtrafiken.atlassian.net/wiki/spaces/SamA/pages/3448668185/NeTEx+format+adjustments+-+Samtrafiken+sales+export)

## What does this dataset contain?

This API contains data intended for those selling public transport tickets through the Samtrafiken Access platform. 
It contains only traffic present in the Samtrafiken Access platform, including additional attributes which may be of interest for ticket resellers. 
Note that the Samtrafiken Sales data API only contains traffic data, to actually sell tickets you need to use the Samtrafiken Access platform.

Are you looking for an unfiltered dataset including quays and platforms we recommend the [NeTEx Sweden](https://trafiklab.se/api/netex-datasets/netex-sweden/) or [NeTEx Regional](https://trafiklab.se/api/netex-datasets/netex-regional/) API.


### Data format

The data is in the NeTEx (**Ne**twork and **T**imetable **Ex**change) format. This is a format in which all European
operators have to publish their data. The data is aimed at both operator-to-traveller communication and internal
communication between different organizations.

### Updates

The static data in this dataset is updated monday to friday, usually between 22.00 and 00.00.

## Latest

{{% note %}}
**Where to download**

You can access the latest dataset through the following URL:
[https://opendata.samtrafiken.se/netex-access/samtrafiken_access_netex_latest.zip?key={apikey}]()

Replace `{apikey}` with your own API key. If you don´t have a key yet, read [here](/docs/using-trafiklab/getting-api-keys) on how to get one.
{{% /note %}}

## Historical data

{{% note %}}
**Where to download**
You can also access historical data for specific dates by following this URL:
[https://opendata.samtrafiken.se/netex-access/samtrafiken_access_netex_{date}.zip?key={apikey}]()

Replace `{date}` with a specified date in the format YYYYMMDD.

Replace `{apikey}` with your own API key. If you don´t have a key yet, read [here](/docs/using-trafiklab/getting-api-keys) on how to get one.

The earliest available historical data is from 2025-01-01.
{{% /note %}}

<div style="max-width: 270px">

#### API key levels

| Level  | Maximum calls per minute | Maximum calls per month |
|:-------|:------------------------:|:-----------------------:|
| Bronze |            10            |           50            |
| Silver |            10            |           180           |

</div>

For more information about Samtrafiken NeTEx exports, see [Samtrafiken NeTEx export](https://samtrafiken.atlassian.net/wiki/spaces/SamtrafikenOpenData/pages/989233182/Samtrafiken+NeTEx+export)

## Licence

Data from the Samtrafiken Sales data API is available under the CC0 1.0 Universal (CC0 1.0) Public Domain Dedication license.

#### Summary

The person who associated a work with this deed has dedicated the work to the public domain by waiving all of his or her
rights to the work worldwide under copyright law, including all related and neighboring rights, to the extent allowed by
law.

#### Other Information

In no way are the patent or trademark rights of any person affected by CC0, nor are the rights that other persons may
have in the work or in how the work is used, such as publicity or privacy rights.

Unless expressly stated otherwise, the person who associated a work with this deed makes no warranties about the work,
and disclaims liability for all uses of the work, to the fullest extent permitted by applicable law.

When using or citing the work, you should not imply endorsement by the author or the affirmer.

{{% info %}}
More information, as well as the complete license text, can be found at
[the creative commons website](https://creativecommons.org/publicdomain/zero/1.0/deed.en).
{{% /info %}} 