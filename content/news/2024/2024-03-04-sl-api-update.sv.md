---
title: "SL Transport API replaces Departures v4"
date: "2024-03-04"
image: /media/2024/03/sl-network-map.jpg
image_credit: Joakim Honkasalo, Unsplash
generated_fallback_page: true
---

After almost eight years, SL replaces the **Stops and Lines v2** and **Departure v4** APIs with 1 new API which combines the features of these two.
The SL Transport API is built from the ground up on new back-end systems, which should improve system stability and simplify the old architecture which
consisted
of 7 APIs.

<!--more--> 

The new API does not require API keys, and can be used without a Trafiklab account. While there are no quota, you should still not make more requests than
required and aim for efficient solutions.

Users of _SL Departures v4_, as well as users of _Stops and Lines v2_ need to switch to the new API before **March 31st 2024**. We regret the short migration
period, which is caused by the large changes behind the scenes in SL's data flows. For users of _SL Departures v4_, the new endpoint to look for is _Departures
from site_.

This new API is released shortly after the _SL Deviations_ API. Using this API, you can get information regarding deviations on SLs transport network. _SL
Deviations_ replaces the older _Service Alerts_ and _Traffic Status_ APIs. Keep
in mind that even other SL APIs have received updated URLs. [A list of all changes to SL APIs can be found here](/api/trafiklab-apis/sl/_index.md).

[The new documentation can be found here](/api/trafiklab-apis/sl/transport.md). For suggestions and feedback, feel free to contact us through Kundo
at [support.trafiklab.se](https://support.trafiklab.se).

