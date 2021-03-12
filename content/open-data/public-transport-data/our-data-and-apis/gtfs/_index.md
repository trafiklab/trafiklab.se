# GTFS

## What is GTFS?

The **General Transit Format Specification** is a file format which originally was developed by Google in 2006. It
combines all the data in one compact file. This means you can download a single file to get timetable information for
the entirety of Sweden.

### How does GTFS Work?

A GTFS file is a zip archive that contains several \*.txt files. You can compare this archive file with a database. The
files inside the archive contain Comma Separated Values \(CSV\) data, meaning they are easy to read, both for computers
and humans. Each file contains all the instances of a certain type, just like a database table. For example, one file
contains all the routes, another file contains all the stops. The files are linked together through ids, similar to how
foreign keys work in a database. The image below gives an idea of the structure.

![The structure of a GTFS dataset](../../../.gitbook/assets/image%20%2815%29.png)

### When should I use GTFS?

A dataset like GTFS is the opposite of an API like ResRobot. Each has its own benefits and drawbacks. When you want to
create a simple app, or let users search for the next departure from your website, an API is easier to use. However,
when you want to analyze data, an API would need millions of requests compared to a single GTFS file that has all the
data.

| Well suited for | Not so suited for |
| :--- | :--- |
| Analysing \(real-time\) transport data | Quickly getting the next departures from a stop |
| Building your own route-planner or API | Quickly calculating a route from A to B |
| Getting a list of all public transport stop-areas for an operator or a country | Projects where large files \(&gt;25MB\) can't be used |
| Getting the live position of all public transport vehicles |  |

{% hint style="info" %} There are hundreds of libraries, examples and demos for GTFS. You can find some
at [https://github.com/andredarcie/awesome-gtfs](https://github.com/andredarcie/awesome-gtfs)
and [https://github.com/CUTR-at-USF/awesome-transit](https://github.com/CUTR-at-USF/awesome-transit). {% endhint %}

## GTFS at Trafiklab

At Trafiklab, we offer two GTFS feeds. The first is [GTFS Sverige 2](https://www.trafiklab.se/api/gtfs-sverige-2), which
includes information for entire Sweden. We also offer[ GTFS Regional](https://www.trafiklab.se/api/gtfs-regional-beta),
which consists of multiple GTFS feeds, each of which covers an operator in Sweden. You can see the difference between
those two feeds below.

|  | GTFS Sverige 2  | GTFS Regional |
| :--- | :--- | :--- |
| Geographical coverage | 100% | 50% |
| Transit coverage | 100% | 92% |
| Data quality | Average quality | Highest quality |
| Real-time data | Only static data | Static + Real-time + GPS positions |
| Historical data \(static\) | Since 2012 | Not available |

## Read more

{% page-ref page="gtfs-sverige-2-static/" %}

{% page-ref page="gtfs-regional/" %}

