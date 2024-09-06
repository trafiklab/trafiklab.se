---
title: The right data for your project
layout: "single"
---


### Creating a map with travel times

When creating a map with travel times from one stop to different places, also known as an isochrone map, you need to
make hundreds till even tens of thousands of API calls. Using APIs for this is slow, and causes a huge load on the
server. A much better alternative is to fetch the GTFS files, and calculate everything locally. This way there is no
limit on the number of API calls, meaning you can create a high quality map after a few minutes of route-planning.

{{% info %}} You do not need to write your own route-planning algorithm. There are a lot of existing projects, such as
OpenTripPlanner, which allow you to load a GTFS file and to make API calls against a local API. {{% /info %}}

{{% info %}} There are over 50.000 stop locations in Sweden. It would take 25 million API calls to create an isochrone
map from every stop to every stop.This is equal to all ResRobot API traffic for 2 months. {{% /info %}}

### Making apps or voice assistants

If you're interested in voice assistants, you will only need data when a user asks a question. APIs are a perfect use
case for this scenario, as you want quick answers on relatively few route-planning questions.

Make sure you check out our [voice assistant tutorial with ResRobot](/docs/example-solutions/voice-assistant) if you
want to get started with a digital assistant.

### Showing the next departures on a smart mirror

Thanks to Raspberry Pi's, and technology in general becoming cheaper and thus more accessible, smart mirrors have become
more popular. Many use them to display departures from nearby stops, so you know when you need to run when leaving the
door. For this case, you can either use APIs or GTFS data.

The risk with APIs is the fact that you'll be making requests, evenif noone is looking in the mirror. Therefore, you
should adjust the update frequency based on how likely it is you will be looking at the departures table at a given
time. When you usualy sleep, the frequency can be decreased to once every fifteen minutes, while you could update the
mirror as often as every minute around the time you leave for work. Note that even without updates, you can update the
user-interface by counting down on the remaining time every minute.

{{% info %}}
**Did you know** there are multiple existing modules to use Trafiklab APIs with the most commonly used magic mirror
software?

[MMM-ResRobot](https://github.com/Alvinger/MMM-ResRobot) will show you departures using ResRobot departures API.

[MMM-SL](https://github.com/teppos/MMM-SL)
and [MMM-SL-PublicTransport](https://github.com/boghammar/MMM-SL-PublicTransport) will show you departures using SLs
APIs.

{{% /info %}}

An alternative would be using GTFS and GTFS-RT. While this allows for more frequent updates within the bronze level, it
does become more complicated. If you're up for a challenge, this will be a great learning experience.

{{% page-ref "departure-boards.md" "obtaining-stop-ids.md" "route-planning.md" %}}