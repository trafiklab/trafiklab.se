---
title: "Trafiklab launches Trafiklab Realtime APIs"
date: "2025-05-01"
---

Trafiklab has introduced the new [Trafiklab Realtime APIs](/api/our-apis/trafiklab-realtime-apis/), designed to deliver enhanced public transport data for Sweden in a format optimized for modern applications.
These APIs are based on [GTFS Sweden 3](/api/gtfs-datasets/gtfs-sweden/) data and provide live and scheduled transit information in an accessible structure suited for direct use, removing the
complexity of GTFS and NeTEx datasets. The Realtime APIs replace the outdated [Resrobot Timetables 2.1](/api/our-apis/resrobot-v21/timetables/) and Stop Lookup services, offering more detailed data and
significantly improved performance.

The launch represents a step forward in providing developers with an efficient and flexible toolset to create applications for real-time journey information.
The APIs cover departure and arrival data for stops through the Timetables endpoint and allow developers to fetch stop metadata using the Stop Lookup endpoint.
They are structured to support lightweight, fast use cases such as mobile apps, digital signage, and travel widgets, facilitating the integration of live
transport updates with minimal processing requirements.

The [Trafiklab Realtime APIs](/api/our-apis/trafiklab-realtime-apis/) respond exclusively in JSON format, ensuring streamlined integration and ease of use across platforms. Data is updated continuously for
real-time operations, while static schedules are refreshed regularly. Developers accessing these APIs can do so with a single API key system, which includes
varying quota levels tailored for different scenarios, ranging from small-scale deployments to extensive enterprise-level solutions capable of handling
thousands of stops.

This new system eliminates previous limitations of Resrobot by providing detailed, real-time data about public transport operations, including platforms and
vehicle movements. Furthermore, features such as support for meta-stops and rikshållplatser simplify the coordination of multi-modal transport stops, making it
easier for developers to create seamless user experiences for travellers.

Applications that depend on the Resrobot services are encouraged to migrate to the new Trafiklab Realtime APIs to benefit from the increased efficiency and
expanded functionality. The detailed documentation provides developers with all necessary information to begin integration and take full advantage of the
updated capabilities. This transition ensures that applications remain reliable and up-to-date as they improve journey planning services across Sweden.
