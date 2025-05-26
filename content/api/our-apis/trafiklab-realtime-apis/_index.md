---
title: Trafiklab realtime APIs
layout: "single"
weight: 1
date: 2025-05-01
image: '/media/2024/09/banner_phone.jpg'
badge: beta
cascade:
  - image: '/media/2024/09/banner_phone.jpg'
---

Trafiklab realtime APIs is a collection of APIs which provide information for public transport in entire Sweden. They are developed internally based on our
own GTFS
Sweden 3 data, offering the same data in a way that is more suited for direct consumption. They make realtime data more accessible compared to GTFS and
NeTEx/SIRI, meaning you can use them for applications which can't handle complex GTFS or NeTEx datasets. Examples are mobile apps or digital signage.

{{% note %}}
**Trafiklab APIs vs Resrobot**

These APIs are a direct replacement for Resrobot 2.1 timetables and stop lookup. Compared to Resrobot, they
contain more detailed data, such as platforms and realtime data. They offer significantly better performance as well, which translates into higher quota for end
users while reducing the costs for Trafiklab.

**Note that these APIs are licensed as CC-BY**, allowing you to do whatever you want as long as you include a little "data from Trafiklab.se" attribution on
screens and website widgets. Read more about this in the license text on the bottom of this page.
{{% /note %}}

## Usage

Trafiklabs realtime APIs can be used for
- looking up departures and arrivals, using the [Trafiklab Timetables endpoint](timetables). 
- looking up the ids of stops, using the [Trafiklab Stop Lookup endpoint](stop-lookup).

For route planning, you can use the [Resrobot APIs](../resrobot-v21).

## Use cases

Trafiklabs APIs answers to specific questions, such as "when are the next departures from stop X". The response
is quick and easy to use, and can be used directly without having to process it first. This makes it a good fit for for
example smartphone applications where travellers need an answer on their queries, and for digital displays without much processing power.
It is however a poor choice for analytics where a lot of data from a lot of vehicles is needed, since a lot of API calls would be required to transfer large
amounts of data.

| Well suited for                                 | Less suited for                               |
|:------------------------------------------------|:----------------------------------------------|
| Quickly getting the next departures from a stop | Analysing public transport information        |
| Digital signage                                 | Applications requiring a certain uptime (SLA) |
| Onboard signage                                 | Data visualisation                            |
| Mobile applications                             |                                               |
| Websites and widgets                            |                                               |

### API key levels

There is only one API key required to access all features in Trafiklab APIs, the different key levels are specified in the table below. If you don´t have a key yet,
read [here](/docs/using-trafiklab/getting-api-keys) on how to get one.

| Level    | Maximum calls per minute | Maximum calls per month | Example usage                                                            |
|:---------|:------------------------:|:-----------------------:|:-------------------------------------------------------------------------|
| Bronze   |            25            |         100.000         | Departure boards for 2 stops                                             |
| Bronze + |            25            |         500.000         | Departure boards for 10 stops                                            |
| Silver   |           150            |        5.000.000        | Departure boards for 100 stops, mobile apps                              |
| Gold     |          1.200           |       50.000.000        | Departure boards for 2.000 stops updated every other minute, mobile apps |
| Platinum |          3.000           |       125.000.000       | Departure boards for 5.000 stops updated every other minute, mobile apps |

{{% warning %}} If you want to analyze data, if your service will have more than a million active users, or if you have strict requirements regarding uptime
we recommend using GTFS and hosting your own API based on that data. One GTFS file contains all information you possibly can get out of this API, meaning it's
easier to download this file if you need large amounts of data for analysis. {{% /warning %}}

{{% page-ref "/api/gtfs-datasets/gtfs-regional/" "/api/gtfs-datasets/gtfs-sverige-2" %}}

## License

These Trafiklab APIs are available under the CC-BY 4.0 license. You should mention the data is provided by Trafiklab.se, for example through the use of a little
footnote text on public displays or website widgets. Contact us for exemptions if you're implementing solutions for public transport operators, such as onboard
displays.

You are free to:

- Share — copy and redistribute the material in any medium or format for any purpose, even commercially.
- Adapt — remix, transform, and build upon the material for any purpose, even commercially.
- The licensor cannot revoke these freedoms as long as you follow the license terms.

Under the following terms:

- Attribution — You must give appropriate credit , provide a link to the license, and indicate if changes were made . You may do so in any reasonable manner,
  but not in any way that suggests the licensor endorses you or your use.
- No additional restrictions — You may not apply legal terms or technological measures that legally restrict others from doing anything the license permits.

Notices:

You do not have to comply with the license for elements of the material in the public domain or where your use is permitted by an applicable exception or
limitation .

No warranties are given. The license may not give you all of the permissions necessary for your intended use. For example, other rights such as publicity,
privacy, or moral rights may limit how you use the material.

https://creativecommons.org/licenses/by/4.0/legalcode.txt